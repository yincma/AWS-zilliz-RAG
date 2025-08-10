"""
API栈 - 清理后的Lambda函数和API Gateway实现
使用代码文件方式部署，避免层大小限制
"""

from aws_cdk import (
    Stack,
    Duration,
    CfnParameter,
    CfnOutput,
    aws_lambda as lambda_,
    aws_apigateway as apigateway,
    aws_iam as iam,
    aws_logs as logs,
    aws_s3 as s3,
)
from constructs import Construct
import os


class ApiStack(Stack):
    """API服务栈 - 清理版本"""
    
    def __init__(self, scope: Construct, construct_id: str, 
                 data_bucket: s3.Bucket, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        # 定义参数
        bedrock_model_param = CfnParameter(
            self, "BedrockModelId",
            type="String",
            default="amazon.nova-lite-v1:0",
            description="Bedrock model ID"
        )
        
        embedding_model_param = CfnParameter(
            self, "EmbeddingModelId",
            type="String",
            default="amazon.titan-embed-text-v2:0",
            description="Embedding model ID"
        )
        
        zilliz_endpoint_param = CfnParameter(
            self, "ZillizEndpoint",
            type="String",
            description="Zilliz endpoint URL"
        )
        
        zilliz_token_param = CfnParameter(
            self, "ZillizToken",
            type="String",
            no_echo=True,
            description="Zilliz API token"
        )
        
        # Lambda执行角色
        # 检查是否有预创建的角色
        existing_role_arn = os.environ.get("LAMBDA_EXECUTION_ROLE_ARN")
        
        if existing_role_arn:
            # 使用现有角色
            lambda_role = iam.Role.from_role_arn(
                self,
                "LambdaExecutionRole",
                existing_role_arn
            )
        else:
            # 创建新角色
            lambda_role = iam.Role(
                self,
                "LambdaExecutionRole",
                assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
                managed_policies=[
                    iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AWSLambdaBasicExecutionRole")
                ]
            )
            
            # 添加Bedrock权限
            lambda_role.add_to_policy(
                iam.PolicyStatement(
                    effect=iam.Effect.ALLOW,
                    actions=[
                        "bedrock:InvokeModel",
                        "bedrock:InvokeModelWithResponseStream"
                    ],
                    resources=["*"]
                )
            )
            
            # 添加S3权限
            data_bucket.grant_read_write(lambda_role)
        
        # 环境变量
        environment = {
            "S3_BUCKET": data_bucket.bucket_name,
            "BEDROCK_MODEL_ID": bedrock_model_param.value_as_string,
            "EMBEDDING_MODEL_ID": embedding_model_param.value_as_string,
            "ZILLIZ_ENDPOINT": zilliz_endpoint_param.value_as_string,
            "ZILLIZ_TOKEN": zilliz_token_param.value_as_string,
            "ZILLIZ_COLLECTION": os.environ.get("ZILLIZ_COLLECTION", "rag_collection"),
            "PYTHONPATH": "/var/task"
        }
        
        # 查询Lambda函数
        query_function = lambda_.Function(
            self,
            "QueryFunction",
            runtime=lambda_.Runtime.PYTHON_3_9,
            code=lambda_.Code.from_asset("lambda_functions"),
            handler="query_handler.handler",
            role=lambda_role,
            environment=environment,
            timeout=Duration.seconds(30),
            memory_size=1024,
            log_retention=logs.RetentionDays.ONE_WEEK,
            description="RAG查询处理函数"
        )
        
        # 文档摄入Lambda函数
        ingest_function = lambda_.Function(
            self,
            "IngestFunction",
            runtime=lambda_.Runtime.PYTHON_3_9,
            code=lambda_.Code.from_asset("lambda_functions"),
            handler="ingest_handler.handler",
            role=lambda_role,
            environment=environment,
            timeout=Duration.minutes(5),
            memory_size=2048,
            log_retention=logs.RetentionDays.ONE_WEEK,
            description="文档摄入处理函数"
        )
        
        # 健康检查Lambda函数
        health_function = lambda_.Function(
            self,
            "HealthFunction",
            runtime=lambda_.Runtime.PYTHON_3_9,
            code=lambda_.Code.from_inline("""
def handler(event, context):
    return {
        'statusCode': 200,
        'body': '{"status": "healthy"}'
    }
            """),
            handler="index.handler",
            timeout=Duration.seconds(5),
            memory_size=128,
            log_retention=logs.RetentionDays.ONE_WEEK,
            description="健康检查函数"
        )
        
        # API Gateway
        self.api = apigateway.RestApi(
            self,
            "RagApi",
            rest_api_name=f"rag-api-{self.node.try_get_context('stage')}",
            description="RAG应用API",
            deploy_options=apigateway.StageOptions(
                stage_name=self.node.try_get_context('stage') or 'prod',  # 统一默认使用prod
                logging_level=apigateway.MethodLoggingLevel.INFO,
                data_trace_enabled=True,
                metrics_enabled=True,
                throttling_rate_limit=100,
                throttling_burst_limit=200
            ),
            default_cors_preflight_options=apigateway.CorsOptions(
                allow_origins=apigateway.Cors.ALL_ORIGINS,
                allow_methods=apigateway.Cors.ALL_METHODS,
                allow_headers=["*"],
                allow_credentials=False
            )
        )
        
        # 暴露API URL为栈属性
        self.api_url = self.api.url
        
        # 健康检查端点
        health = self.api.root.add_resource("health")
        health.add_method(
            "GET",
            apigateway.LambdaIntegration(health_function)
        )
        
        # 查询端点
        query = self.api.root.add_resource("query")
        
        # 添加POST方法，包含CORS响应头
        query.add_method(
            "POST",
            apigateway.LambdaIntegration(
                query_function,
                timeout=Duration.seconds(29),
                # 确保Lambda代理集成传递所有请求信息
                proxy=True,
                integration_responses=[
                    apigateway.IntegrationResponse(
                        status_code="200",
                        response_parameters={
                            "method.response.header.Access-Control-Allow-Origin": "'*'"
                        }
                    )
                ]
            ),
            authorization_type=apigateway.AuthorizationType.NONE,
            method_responses=[
                apigateway.MethodResponse(
                    status_code="200",
                    response_parameters={
                        "method.response.header.Access-Control-Allow-Origin": True
                    }
                )
            ]
        )
        
        
        # 文档端点
        documents = self.api.root.add_resource("documents")
        
        # 添加POST方法，包含CORS响应头
        documents.add_method(
            "POST",
            apigateway.LambdaIntegration(
                ingest_function,
                timeout=Duration.seconds(29),
                proxy=True,
                integration_responses=[
                    apigateway.IntegrationResponse(
                        status_code="200",
                        response_parameters={
                            "method.response.header.Access-Control-Allow-Origin": "'*'"
                        }
                    )
                ]
            ),
            authorization_type=apigateway.AuthorizationType.NONE,
            method_responses=[
                apigateway.MethodResponse(
                    status_code="200",
                    response_parameters={
                        "method.response.header.Access-Control-Allow-Origin": True
                    }
                )
            ]
        )
        
        
        # 输出
        CfnOutput(
            self,
            "ApiUrl",
            value=self.api.url,
            description="API Gateway URL"
        )
        
        CfnOutput(
            self,
            "QueryFunctionArn",
            value=query_function.function_arn,
            description="Query Lambda Function ARN"
        )
        
        CfnOutput(
            self,
            "IngestFunctionArn",
            value=ingest_function.function_arn,
            description="Ingest Lambda Function ARN"
        )