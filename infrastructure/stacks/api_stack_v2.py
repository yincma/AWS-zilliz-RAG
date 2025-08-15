"""
API栈 V2 - 使用容器镜像的Lambda函数和API Gateway实现
默认使用容器镜像部署，支持更大的依赖包
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
    aws_ecr as ecr,
)
from constructs import Construct
import os


class ApiStackV2(Stack):
    """API服务栈 V2 - 自动配置CORS和正确的路径"""
    
    def __init__(self, scope: Construct, construct_id: str, 
                 data_bucket: s3.Bucket, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        # 直接从环境变量读取配置（从.env文件加载）
        # 这样确保配置能正确传递给Lambda函数
        bedrock_model_id = os.environ.get("BEDROCK_MODEL_ID", "amazon.nova-pro-v1:0")
        embedding_model_id = os.environ.get("EMBEDDING_MODEL_ID", "amazon.titan-embed-image-v1")
        zilliz_endpoint = os.environ.get("ZILLIZ_ENDPOINT", "")
        zilliz_token = os.environ.get("ZILLIZ_TOKEN", "")
        zilliz_collection = os.environ.get("ZILLIZ_COLLECTION", "rag_collection")
        
        # 打印配置信息（隐藏敏感信息）
        print(f"📋 API栈配置:")
        print(f"  Bedrock Model: {bedrock_model_id}")
        print(f"  Embedding Model: {embedding_model_id}")
        print(f"  Zilliz Endpoint: {zilliz_endpoint if zilliz_endpoint else '未配置'}")
        print(f"  Zilliz Token: {'***已配置***' if zilliz_token else '未配置'}")
        print(f"  Zilliz Collection: {zilliz_collection}")
        
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
        
        # 环境变量 - 直接使用从.env文件读取的值
        environment = {
            "S3_BUCKET": data_bucket.bucket_name,
            "BEDROCK_MODEL_ID": bedrock_model_id,
            "EMBEDDING_MODEL_ID": embedding_model_id,
            "ZILLIZ_ENDPOINT": zilliz_endpoint,
            "ZILLIZ_TOKEN": zilliz_token,
            "ZILLIZ_COLLECTION": zilliz_collection,
            "PYTHONPATH": "/var/task",
            # CORS配置
            "CORS_ALLOW_ORIGINS": "*",
            "CORS_ALLOW_METHODS": "GET,POST,PUT,DELETE,OPTIONS",
            "CORS_ALLOW_HEADERS": "Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token"
        }
        
        # 获取项目根目录
        project_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        
        # 动态获取Lambda包路径（从项目根目录开始）- 即使在容器模式下也定义，避免后续引用错误
        lambda_package_dir = os.path.join(project_root, "lambda_build_temp")
        
        # 部署模式选择（通过环境变量控制）
        use_container = os.environ.get("USE_CONTAINER", "true").lower() == "true"
        
        if use_container:
            print(f"📋 使用容器镜像模式部署")
            
            # 获取账号ID和ECR镜像URI
            account_id = os.environ.get("ACCOUNT_ID", "375004070918")
            region = os.environ.get("AWS_REGION", "us-east-1")
            ecr_repo = os.environ.get("ECR_REPOSITORY_NAME", "rag-lambda-query")
            ecr_tag = os.environ.get("ECR_IMAGE_TAG", "latest")
            ecr_image_uri = f"{account_id}.dkr.ecr.{region}.amazonaws.com/{ecr_repo}:{ecr_tag}"
            
            print(f"  使用ECR镜像: {ecr_image_uri}")
            
            # 查询Lambda函数 - 使用ECR镜像部署
            query_function = lambda_.Function(
                self,
                "QueryFunction",
                code=lambda_.Code.from_ecr_image(
                    repository=ecr.Repository.from_repository_arn(
                        self,
                        "ECRRepoQuery",
                        repository_arn=f"arn:aws:ecr:{region}:{account_id}:repository/{ecr_repo}"
                    ),
                    tag=ecr_tag,
                    cmd=["query_handler.handler"]
                ),
                handler=lambda_.Handler.FROM_IMAGE,
                runtime=lambda_.Runtime.FROM_IMAGE,
                role=lambda_role,
                environment=environment,
                timeout=Duration.seconds(30),
                memory_size=1024,
                log_retention=logs.RetentionDays.ONE_WEEK,
                description="RAG查询处理函数（容器版）"
            )
            
            # 文档摄入Lambda函数 - 使用同一个ECR镜像
            ingest_function = lambda_.Function(
                self,
                "IngestFunction",
                code=lambda_.Code.from_ecr_image(
                    repository=ecr.Repository.from_repository_arn(
                        self,
                        "ECRRepoIngest",
                        repository_arn=f"arn:aws:ecr:{region}:{account_id}:repository/{ecr_repo}"
                    ),
                    tag=ecr_tag,
                    cmd=["ingest_handler.handler"]
                ),
                handler=lambda_.Handler.FROM_IMAGE,
                runtime=lambda_.Runtime.FROM_IMAGE,
                role=lambda_role,
                environment=environment,
                timeout=Duration.minutes(5),
                memory_size=2048,
                log_retention=logs.RetentionDays.ONE_WEEK,
                description="文档摄入处理函数（容器版）"
            )
        else:
            print(f"📋 使用传统ZIP包模式部署")
            
            # 查询Lambda函数 - 使用ZIP包部署（传统方式）
            query_package = os.path.join(lambda_package_dir, "query_lambda.zip")
            query_function = lambda_.Function(
                self,
                "QueryFunction",
                runtime=lambda_.Runtime.PYTHON_3_9,
                code=lambda_.Code.from_asset(query_package),
                handler="query_handler.handler",
                role=lambda_role,
                environment=environment,
                timeout=Duration.seconds(30),
                memory_size=1024,
                log_retention=logs.RetentionDays.ONE_WEEK,
                description="RAG查询处理函数"
            )
            
            # 文档摄入Lambda函数 - 使用ZIP包部署（传统方式）
            ingest_package = os.path.join(lambda_package_dir, "ingest_lambda.zip")
            ingest_function = lambda_.Function(
                self,
                "IngestFunction",
                runtime=lambda_.Runtime.PYTHON_3_9,
                code=lambda_.Code.from_asset(ingest_package),
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
        
        # 添加documents/{proxy+}来处理带路径参数的请求（如DELETE /documents/xxx）
        document_item = documents.add_resource("{proxy+}")
        
        # DELETE方法 - 删除单个文档（支持Zilliz）
        # 使用ZIP包模式部署删除函数
        delete_package = os.path.join(lambda_package_dir, "delete_lambda.zip")
        if os.path.exists(delete_package):
            delete_function = lambda_.Function(
                self,
                "DeleteDocFunction",
                runtime=lambda_.Runtime.PYTHON_3_9,
                code=lambda_.Code.from_asset(delete_package),
                handler="delete_handler.handler",
                role=lambda_role,
                environment=environment,
                timeout=Duration.seconds(30),
                memory_size=512,
                log_retention=logs.RetentionDays.ONE_WEEK,
                description="删除文档函数(支持Zilliz)"
            )
        else:
            # 如果删除包不存在，使用简单的内联代码作为后备
            delete_function = lambda_.Function(
                self,
                "DeleteDocFunction",
                runtime=lambda_.Runtime.PYTHON_3_9,
                code=lambda_.Code.from_inline("""
import json
import boto3
import os

def handler(event, context):
    # 获取CORS配置
    allow_origins = os.environ.get('CORS_ALLOW_ORIGINS', '*')
    allow_methods = os.environ.get('CORS_ALLOW_METHODS', 'GET,POST,PUT,DELETE,OPTIONS')
    allow_headers = os.environ.get('CORS_ALLOW_HEADERS', 'Content-Type')
    
    cors_headers = {
        'Access-Control-Allow-Origin': allow_origins,
        'Access-Control-Allow-Methods': allow_methods,
        'Access-Control-Allow-Headers': allow_headers
    }
    
    try:
        path_params = event.get('pathParameters', {})
        doc_path = path_params.get('proxy', '')
        
        if not doc_path:
            return {
                'statusCode': 400,
                'headers': {**cors_headers, 'Content-Type': 'application/json'},
                'body': json.dumps({'error': 'Document path is required'})
            }
        
        s3 = boto3.client('s3')
        bucket = os.environ.get('S3_BUCKET', '')
        s3_key = f"documents/{doc_path}" if not doc_path.startswith('documents/') else doc_path
        
        s3.delete_object(Bucket=bucket, Key=s3_key)
        
        # Try to delete embeddings
        try:
            embeddings_key = s3_key.replace('documents/', 'embeddings/') + '.json'
            s3.delete_object(Bucket=bucket, Key=embeddings_key)
        except:
            pass
        
        return {
            'statusCode': 200,
            'headers': {**cors_headers, 'Content-Type': 'application/json'},
            'body': json.dumps({
                'status': 'success',
                'message': 'Document deleted successfully',
                'document': doc_path,
                'zilliz_deleted': False  # Not supported in fallback mode
            })
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {**cors_headers, 'Content-Type': 'application/json'},
            'body': json.dumps({
                'status': 'error',
                'error': str(e),
                'message': 'Failed to delete document'
            })
        }
                """),
                handler="index.handler",
                role=lambda_role,
                environment=environment,
                timeout=Duration.seconds(10),
                memory_size=256,
                log_retention=logs.RetentionDays.ONE_WEEK,
                description="删除文档函数(基础版本)"
            )
        
        # 添加DELETE方法
        document_item.add_method(
            "DELETE",
            apigateway.LambdaIntegration(delete_function),
            authorization_type=apigateway.AuthorizationType.NONE
        )
        
        # OPTIONS方法由全局CORS配置自动处理，不需要手动添加
        
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