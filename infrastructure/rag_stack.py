"""
CDK Stack for RAG System with Lambda and API Gateway
"""

from aws_cdk import (
    Stack,
    Duration,
    RemovalPolicy,
    aws_lambda as lambda_,
    aws_apigateway as apigateway,
    aws_iam as iam,
    aws_s3 as s3,
    aws_logs as logs,
)
from constructs import Construct
import os
from pathlib import Path


class RAGStack(Stack):
    """RAG系统的CDK栈"""
    
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        # 获取环境变量
        env_vars = {
            "AWS_REGION": os.environ.get("AWS_REGION", "us-east-1"),
            "BEDROCK_MODEL_ID": os.environ.get("BEDROCK_MODEL_ID", "amazon.nova-pro-v1:0"),
            "EMBEDDING_MODEL_ID": os.environ.get("EMBEDDING_MODEL_ID", "amazon.titan-embed-image-v1"),
            "ZILLIZ_ENDPOINT": os.environ.get("ZILLIZ_ENDPOINT", ""),
            "ZILLIZ_TOKEN": os.environ.get("ZILLIZ_TOKEN", ""),
            "ZILLIZ_COLLECTION": os.environ.get("ZILLIZ_COLLECTION", "rag_collection"),
            "S3_BUCKET": os.environ.get("S3_BUCKET", "AWS_zilliz_RAG"),
            "S3_PREFIX": os.environ.get("S3_PREFIX", "documents/"),
        }
        
        # 创建S3存储桶（如果不存在）
        document_bucket = s3.Bucket(
            self, "DocumentBucket",
            bucket_name=env_vars["S3_BUCKET"],
            versioned=True,
            removal_policy=RemovalPolicy.RETAIN,
            cors=[
                s3.CorsRule(
                    allowed_headers=["*"],
                    allowed_methods=[
                        s3.HttpMethods.GET,
                        s3.HttpMethods.PUT,
                        s3.HttpMethods.POST,
                        s3.HttpMethods.DELETE,
                    ],
                    allowed_origins=["*"],
                    max_age=3000,
                )
            ],
        )
        
        # 创建Lambda执行角色
        lambda_role = iam.Role(
            self, "LambdaExecutionRole",
            assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AWSLambdaBasicExecutionRole")
            ],
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
        lambda_role.add_to_policy(
            iam.PolicyStatement(
                effect=iam.Effect.ALLOW,
                actions=[
                    "s3:GetObject",
                    "s3:PutObject",
                    "s3:DeleteObject",
                    "s3:ListBucket"
                ],
                resources=[
                    document_bucket.bucket_arn,
                    f"{document_bucket.bucket_arn}/*"
                ]
            )
        )
        
        # Lambda层（用于共享依赖）
        lambda_layer = lambda_.LayerVersion(
            self, "RAGDependencies",
            code=lambda_.Code.from_asset(
                str(Path(__file__).parent.parent / "app" / "controllers" / "lambda_handlers" / "layer.zip")
            ) if (Path(__file__).parent.parent / "app" / "controllers" / "lambda_handlers" / "layer.zip").exists() else lambda_.Code.from_inline("# placeholder"),
            compatible_runtimes=[lambda_.Runtime.PYTHON_3_9],
            description="RAG system dependencies",
        )
        
        # 健康检查Lambda函数
        health_lambda = lambda_.Function(
            self, "HealthCheckFunction",
            runtime=lambda_.Runtime.PYTHON_3_9,
            code=lambda_.Code.from_asset(
                str(Path(__file__).parent.parent / "app" / "controllers" / "lambda_handlers"),
                exclude=["*.pyc", "__pycache__", "requirements.txt", "layer.zip"]
            ),
            handler="health_handler.lambda_handler",
            environment=env_vars,
            timeout=Duration.seconds(30),
            memory_size=256,
            role=lambda_role,
            log_retention=logs.RetentionDays.ONE_WEEK,
        )
        
        # 查询Lambda函数
        query_lambda = lambda_.Function(
            self, "QueryFunction",
            runtime=lambda_.Runtime.PYTHON_3_9,
            code=lambda_.Code.from_asset(
                str(Path(__file__).parent.parent / "app" / "controllers" / "lambda_handlers"),
                exclude=["*.pyc", "__pycache__", "requirements.txt", "layer.zip"]
            ),
            handler="query_handler.lambda_handler",
            environment=env_vars,
            timeout=Duration.seconds(60),
            memory_size=3008,
            role=lambda_role,
            layers=[lambda_layer] if lambda_layer else [],
            log_retention=logs.RetentionDays.ONE_WEEK,
        )
        
        # 上传Lambda函数
        upload_lambda = lambda_.Function(
            self, "UploadFunction",
            runtime=lambda_.Runtime.PYTHON_3_9,
            code=lambda_.Code.from_asset(
                str(Path(__file__).parent.parent / "app" / "controllers" / "lambda_handlers"),
                exclude=["*.pyc", "__pycache__", "requirements.txt", "layer.zip"]
            ),
            handler="upload_handler.lambda_handler",
            environment=env_vars,
            timeout=Duration.seconds(120),
            memory_size=3008,
            role=lambda_role,
            layers=[lambda_layer] if lambda_layer else [],
            log_retention=logs.RetentionDays.ONE_WEEK,
        )
        
        # 创建API Gateway
        api = apigateway.RestApi(
            self, "RAGApi",
            rest_api_name="RAG System API",
            description="API for RAG system",
            default_cors_preflight_options={
                "allow_origins": ["*"],
                "allow_methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
                "allow_headers": ["*"],
                "max_age": Duration.seconds(300),
            },
            deploy_options={
                "stage_name": "prod",
                "throttling_rate_limit": 100,
                "throttling_burst_limit": 200,
                "logging_level": apigateway.MethodLoggingLevel.INFO,
                "data_trace_enabled": True,
                "metrics_enabled": True,
            },
        )
        
        # 添加健康检查端点
        health_resource = api.root.add_resource("health")
        health_resource.add_method(
            "GET",
            apigateway.LambdaIntegration(health_lambda),
            method_responses=[
                {
                    "status_code": "200",
                    "response_parameters": {
                        "method.response.header.Access-Control-Allow-Origin": True,
                    },
                }
            ],
        )
        
        # 添加查询端点
        query_resource = api.root.add_resource("query")
        query_resource.add_method(
            "POST",
            apigateway.LambdaIntegration(query_lambda),
            method_responses=[
                {
                    "status_code": "200",
                    "response_parameters": {
                        "method.response.header.Access-Control-Allow-Origin": True,
                    },
                }
            ],
        )
        
        # 添加上传端点
        upload_resource = api.root.add_resource("upload")
        upload_resource.add_method(
            "POST",
            apigateway.LambdaIntegration(upload_lambda),
            method_responses=[
                {
                    "status_code": "200",
                    "response_parameters": {
                        "method.response.header.Access-Control-Allow-Origin": True,
                    },
                }
            ],
        )
        
        # 输出
        self.api_url = api.url
        self.health_url = f"{api.url}health"
        self.query_url = f"{api.url}query"
        self.upload_url = f"{api.url}upload"
        
        # 打印输出
        print(f"\n{'='*60}")
        print("🚀 RAG System Deployment Outputs:")
        print(f"{'='*60}")
        print(f"API Gateway URL: {self.api_url}")
        print(f"Health Check: {self.health_url}")
        print(f"Query Endpoint: {self.query_url}")
        print(f"Upload Endpoint: {self.upload_url}")
        print(f"S3 Bucket: {document_bucket.bucket_name}")
        print(f"{'='*60}\n")