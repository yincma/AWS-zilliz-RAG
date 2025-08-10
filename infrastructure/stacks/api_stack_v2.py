"""
API栈 V2 - 包含完整CORS配置和正确的路径结构
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


class ApiStackV2(Stack):
    """API服务栈 V2 - 自动配置CORS和正确的路径"""
    
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
            default="",
            description="Zilliz endpoint URL (optional)"
        )
        
        zilliz_token_param = CfnParameter(
            self, "ZillizToken",
            type="String",
            default="",
            no_echo=True,
            description="Zilliz API token (optional)"
        )
        
        # Lambda执行角色
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
            "PYTHONPATH": "/var/task",
            # CORS配置
            "CORS_ALLOW_ORIGINS": "*",
            "CORS_ALLOW_METHODS": "GET,POST,PUT,DELETE,OPTIONS",
            "CORS_ALLOW_HEADERS": "Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token"
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
import json
import os

def handler(event, context):
    # 获取CORS配置
    allow_origins = os.environ.get('CORS_ALLOW_ORIGINS', '*')
    allow_methods = os.environ.get('CORS_ALLOW_METHODS', 'GET,OPTIONS')
    allow_headers = os.environ.get('CORS_ALLOW_HEADERS', 'Content-Type')
    
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': allow_origins,
            'Access-Control-Allow-Methods': allow_methods,
            'Access-Control-Allow-Headers': allow_headers
        },
        'body': json.dumps({
            'status': 'healthy',
            'service': 'rag-api',
            'timestamp': context.aws_request_id
        })
    }
            """),
            handler="index.handler",
            role=lambda_role,
            environment=environment,
            timeout=Duration.seconds(5),
            memory_size=128,
            log_retention=logs.RetentionDays.ONE_WEEK,
            description="健康检查函数"
        )
        
        # API Gateway - 带完整CORS配置
        self.api = apigateway.RestApi(
            self,
            "RagApi",
            rest_api_name=f"rag-api-{self.node.try_get_context('stage') or 'prod'}",
            description="RAG应用API V2",
            deploy_options=apigateway.StageOptions(
                stage_name=self.node.try_get_context('stage') or 'prod',
                logging_level=apigateway.MethodLoggingLevel.INFO,
                data_trace_enabled=True,
                metrics_enabled=True,
                throttling_rate_limit=100,
                throttling_burst_limit=200
            ),
            # 全局CORS配置
            default_cors_preflight_options=apigateway.CorsOptions(
                allow_origins=["*"],
                allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
                allow_headers=[
                    "Content-Type",
                    "X-Amz-Date",
                    "Authorization",
                    "X-Api-Key",
                    "X-Amz-Security-Token",
                    "X-Amz-User-Agent"
                ],
                allow_credentials=False,
                max_age=Duration.hours(1)
            )
        )
        
        # 暴露API URL为栈属性
        self.api_url = self.api.url
        
        # 健康检查端点 - /health
        health = self.api.root.add_resource("health")
        health.add_method(
            "GET",
            apigateway.LambdaIntegration(health_function),
            authorization_type=apigateway.AuthorizationType.NONE
        )
        
        # 查询端点 - /query
        query = self.api.root.add_resource("query")
        query.add_method(
            "POST",
            apigateway.LambdaIntegration(
                query_function,
                timeout=Duration.seconds(29)
            ),
            authorization_type=apigateway.AuthorizationType.NONE
        )
        
        # 文档端点 - /documents
        documents = self.api.root.add_resource("documents")
        documents.add_method(
            "POST",
            apigateway.LambdaIntegration(
                ingest_function,
                timeout=Duration.seconds(29)
            ),
            authorization_type=apigateway.AuthorizationType.NONE
        )
        documents.add_method(
            "GET",
            apigateway.LambdaIntegration(
                lambda_.Function(
                    self,
                    "ListDocsFunction",
                    runtime=lambda_.Runtime.PYTHON_3_9,
                    code=lambda_.Code.from_inline("""
import json
import boto3
import os

def handler(event, context):
    try:
        s3 = boto3.client('s3')
        bucket = os.environ.get('S3_BUCKET', '')
        
        # 列出文档
        response = s3.list_objects_v2(
            Bucket=bucket,
            Prefix='documents/',
            MaxKeys=100
        )
        
        files = []
        if 'Contents' in response:
            files = [
                {
                    'name': obj['Key'].replace('documents/', ''),
                    'size': obj['Size'],
                    'modified': obj['LastModified'].isoformat()
                }
                for obj in response['Contents']
            ]
        
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': os.environ.get('CORS_ALLOW_ORIGINS', '*'),
                'Access-Control-Allow-Methods': os.environ.get('CORS_ALLOW_METHODS', 'GET,OPTIONS'),
                'Access-Control-Allow-Headers': os.environ.get('CORS_ALLOW_HEADERS', 'Content-Type')
            },
            'body': json.dumps({'documents': files})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({'error': str(e)})
        }
                    """),
                    handler="index.handler",
                    role=lambda_role,
                    environment=environment,
                    timeout=Duration.seconds(10),
                    memory_size=256
                )
            ),
            authorization_type=apigateway.AuthorizationType.NONE
        )
        
        # 搜索端点 - /search (可选)
        search = self.api.root.add_resource("search")
        search.add_method(
            "POST",
            apigateway.LambdaIntegration(query_function),
            authorization_type=apigateway.AuthorizationType.NONE
        )
        
        # 统计端点 - /stats (可选)
        stats = self.api.root.add_resource("stats")
        stats.add_method(
            "GET",
            apigateway.LambdaIntegration(
                lambda_.Function(
                    self,
                    "StatsFunction",
                    runtime=lambda_.Runtime.PYTHON_3_9,
                    code=lambda_.Code.from_inline("""
import json
import os

def handler(event, context):
    # 返回默认统计信息
    stats = {
        'documents': 0,
        'vectors': 0,
        'dimension': 1536,
        'collection': os.environ.get('ZILLIZ_COLLECTION', 'rag_collection'),
        'status': 'operational'
    }
    
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': os.environ.get('CORS_ALLOW_ORIGINS', '*'),
            'Access-Control-Allow-Methods': os.environ.get('CORS_ALLOW_METHODS', 'GET,OPTIONS'),
            'Access-Control-Allow-Headers': os.environ.get('CORS_ALLOW_HEADERS', 'Content-Type')
        },
        'body': json.dumps(stats)
    }
                    """),
                    handler="index.handler",
                    role=lambda_role,
                    environment=environment,
                    timeout=Duration.seconds(5),
                    memory_size=128
                )
            ),
            authorization_type=apigateway.AuthorizationType.NONE
        )
        
        # 输出
        CfnOutput(
            self,
            "ApiUrl",
            value=self.api.url,
            description="API Gateway URL",
            export_name=f"{self.stack_name}-ApiUrl"
        )
        
        CfnOutput(
            self,
            "ApiId",
            value=self.api.rest_api_id,
            description="API Gateway ID",
            export_name=f"{self.stack_name}-ApiId"
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