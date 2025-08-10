"""
优化版API栈 - 使用Lambda层解决包大小问题
"""

from aws_cdk import (
    Stack,
    Duration,
    RemovalPolicy,
    aws_lambda as _lambda,
    aws_apigateway as apigateway,
    aws_iam as iam,
    aws_logs as logs,
    aws_s3 as s3,
    CfnOutput
)
from constructs import Construct
import os


class OptimizedApiStack(Stack):
    """优化版API栈，使用Lambda层"""
    
    def __init__(self, scope: Construct, construct_id: str, data_stack, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        # 获取环境变量
        env_vars = self._get_env_vars(data_stack)
        
        # 创建Lambda层（大型依赖）
        dependencies_layer = self._create_dependencies_layer()
        
        # 创建Lambda函数（精简版）
        query_function = self._create_query_function(dependencies_layer, env_vars)
        ingest_function = self._create_ingest_function(dependencies_layer, env_vars, data_stack)
        
        # 创建API Gateway
        api = self._create_api_gateway(query_function, ingest_function)
        
        # 输出
        self._create_outputs(api, query_function, ingest_function)
    
    def _create_dependencies_layer(self) -> _lambda.LayerVersion:
        """创建依赖层"""
        
        # 方案1：从预构建的zip文件创建层
        dependencies_layer = _lambda.LayerVersion(
            self, "DependenciesLayer",
            code=_lambda.Code.from_asset("layers/dependencies_layer.zip"),
            compatible_runtimes=[_lambda.Runtime.PYTHON_3_9],
            description="Core dependencies for RAG application",
            layer_version_name=f"rag-dependencies-{self.stack_name}"
        )
        
        # 方案2：使用Docker构建层（更可靠）
        # dependencies_layer = _lambda.LayerVersion(
        #     self, "DependenciesLayer",
        #     code=_lambda.Code.from_docker_build(
        #         "layers",
        #         file="Dockerfile.layer",
        #         build_args={
        #             "PYTHON_VERSION": "3.9"
        #         }
        #     ),
        #     compatible_runtimes=[_lambda.Runtime.PYTHON_3_9],
        #     description="Core dependencies for RAG application"
        # )
        
        return dependencies_layer
    
    def _create_query_function(self, layer: _lambda.LayerVersion, env_vars: dict) -> _lambda.Function:
        """创建查询Lambda函数（精简版）"""
        
        # 方案1：使用精简的代码包
        query_function = _lambda.Function(
            self, "QueryFunction",
            runtime=_lambda.Runtime.PYTHON_3_9,
            code=_lambda.Code.from_asset("lambda_function_slim"),  # 只包含应用代码
            handler="query_handler.handler",
            layers=[layer],  # 使用层提供依赖
            environment=env_vars,
            memory_size=1024,
            timeout=Duration.minutes(5),
            reserved_concurrent_executions=10,  # 预留并发
            tracing=_lambda.Tracing.ACTIVE,
            log_retention=logs.RetentionDays.ONE_WEEK
        )
        
        # 方案2：使用容器镜像（支持最大10GB）
        # query_function = _lambda.DockerImageFunction(
        #     self, "QueryFunction",
        #     code=_lambda.DockerImageCode.from_image_asset(
        #         ".",
        #         file="Dockerfile",
        #         cmd=["query_handler.handler"]
        #     ),
        #     environment=env_vars,
        #     memory_size=2048,
        #     timeout=Duration.minutes(5),
        #     reserved_concurrent_executions=10
        # )
        
        # 添加权限
        self._add_function_permissions(query_function)
        
        return query_function
    
    def _create_ingest_function(self, layer: _lambda.LayerVersion, env_vars: dict, data_stack) -> _lambda.Function:
        """创建文档摄入Lambda函数"""
        
        ingest_function = _lambda.Function(
            self, "IngestFunction",
            runtime=_lambda.Runtime.PYTHON_3_9,
            code=_lambda.Code.from_asset("lambda_function_slim"),
            handler="ingest_handler.handler",
            layers=[layer],
            environment={
                **env_vars,
                "S3_BUCKET": data_stack.document_bucket.bucket_name
            },
            memory_size=2048,  # 文档处理需要更多内存
            timeout=Duration.minutes(15),  # 文档处理需要更长时间
            reserved_concurrent_executions=5,
            tracing=_lambda.Tracing.ACTIVE,
            log_retention=logs.RetentionDays.ONE_WEEK
        )
        
        # 添加S3权限
        data_stack.document_bucket.grant_read(ingest_function)
        
        # 添加其他权限
        self._add_function_permissions(ingest_function)
        
        # 配置S3事件触发（可选）
        # from aws_cdk.aws_s3_notifications import LambdaDestination
        # data_stack.document_bucket.add_event_notification(
        #     s3.EventType.OBJECT_CREATED,
        #     LambdaDestination(ingest_function),
        #     s3.NotificationKeyFilter(prefix="documents/", suffix=".pdf")
        # )
        
        return ingest_function
    
    def _add_function_permissions(self, function: _lambda.Function):
        """添加Lambda函数权限"""
        
        # Bedrock权限
        function.add_to_role_policy(iam.PolicyStatement(
            effect=iam.Effect.ALLOW,
            actions=[
                "bedrock:InvokeModel",
                "bedrock:InvokeModelWithResponseStream",
                "bedrock:ListFoundationModels",
                "bedrock:GetFoundationModel"
            ],
            resources=["*"]
        ))
        
        # CloudWatch权限（已默认包含）
        
        # 可选：Secrets Manager权限（用于管理API密钥）
        # function.add_to_role_policy(iam.PolicyStatement(
        #     effect=iam.Effect.ALLOW,
        #     actions=[
        #         "secretsmanager:GetSecretValue"
        #     ],
        #     resources=["arn:aws:secretsmanager:*:*:secret:rag/*"]
        # ))
    
    def _create_api_gateway(self, query_function: _lambda.Function, 
                           ingest_function: _lambda.Function) -> apigateway.RestApi:
        """创建API Gateway"""
        
        api = apigateway.RestApi(
            self, "RagApi",
            rest_api_name=f"RAG-API-{self.stack_name}",
            description="RAG Application API",
            deploy_options=apigateway.StageOptions(
                stage_name=os.environ.get("STAGE", "prod"),
                metrics_enabled=True,
                logging_level=apigateway.MethodLoggingLevel.INFO,
                data_trace_enabled=True,
                throttling_rate_limit=100,
                throttling_burst_limit=200,
                caching_enabled=True,
                cache_ttl=Duration.minutes(5)
            ),
            default_cors_preflight_options=apigateway.CorsOptions(
                allow_origins=apigateway.Cors.ALL_ORIGINS,
                allow_methods=apigateway.Cors.ALL_METHODS,
                allow_headers=["Content-Type", "Authorization"]
            )
        )
        
        # 健康检查端点
        health = api.root.add_resource("health")
        health.add_method("GET", apigateway.LambdaIntegration(query_function))
        
        # 查询端点
        query = api.root.add_resource("query")
        query.add_method("POST", apigateway.LambdaIntegration(
            query_function,
            request_templates={
                "application/json": '{"statusCode": 200}'
            }
        ))
        
        # 文档端点
        documents = api.root.add_resource("documents")
        documents.add_method("POST", apigateway.LambdaIntegration(ingest_function))
        
        return api
    
    def _get_env_vars(self, data_stack) -> dict:
        """获取环境变量"""
        
        from dotenv import load_dotenv
        load_dotenv()
        
        return {
            "BEDROCK_MODEL_ID": os.environ.get("BEDROCK_MODEL_ID", "amazon.nova-pro-v1:0"),
            "EMBEDDING_MODEL_ID": os.environ.get("EMBEDDING_MODEL_ID", "amazon.titan-embed-text-v2:0"),
            "ZILLIZ_ENDPOINT": os.environ.get("ZILLIZ_ENDPOINT", ""),
            "ZILLIZ_TOKEN": os.environ.get("ZILLIZ_TOKEN", ""),
            "ZILLIZ_COLLECTION": os.environ.get("ZILLIZ_COLLECTION", "rag_collection"),
            "AWS_REGION": os.environ.get("AWS_REGION", "us-east-1"),
            "LOG_LEVEL": os.environ.get("LOG_LEVEL", "INFO")
        }
    
    def _create_outputs(self, api: apigateway.RestApi, 
                       query_function: _lambda.Function,
                       ingest_function: _lambda.Function):
        """创建输出"""
        
        CfnOutput(
            self, "ApiUrl",
            value=api.url,
            description="API Gateway URL"
        )
        
        CfnOutput(
            self, "QueryFunctionArn",
            value=query_function.function_arn,
            description="Query Lambda Function ARN"
        )
        
        CfnOutput(
            self, "IngestFunctionArn",
            value=ingest_function.function_arn,
            description="Ingest Lambda Function ARN"
        )