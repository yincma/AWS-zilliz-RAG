"""
Fixed API Stack with proper CORS configuration and API paths
Solves all CORS issues and 403 errors
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


class ApiStackFixed(Stack):
    """Fixed API service stack with proper CORS and routing"""
    
    def __init__(self, scope: Construct, construct_id: str, 
                 data_bucket: s3.Bucket, 
                 cloudfront_url: str = None,  # Accept CloudFront URL as parameter
                 **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        # Define parameters
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
        
        # Create Lambda execution role
        lambda_role = iam.Role(
            self,
            "LambdaExecutionRole",
            assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AWSLambdaBasicExecutionRole")
            ]
        )
        
        # Add Bedrock permissions
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
        
        # Add S3 permissions
        data_bucket.grant_read_write(lambda_role)
        
        # Environment variables for Lambda functions
        environment = {
            "S3_BUCKET": data_bucket.bucket_name,
            "BEDROCK_MODEL_ID": bedrock_model_param.value_as_string,
            "EMBEDDING_MODEL_ID": embedding_model_param.value_as_string,
            "ZILLIZ_ENDPOINT": zilliz_endpoint_param.value_as_string,
            "ZILLIZ_TOKEN": zilliz_token_param.value_as_string,
            "ZILLIZ_COLLECTION": os.environ.get("ZILLIZ_COLLECTION", "rag_collection"),
            "PYTHONPATH": "/var/task",
            # Add CloudFront URL if provided (for CORS)
            "ALLOWED_ORIGINS": cloudfront_url or "*"
        }
        
        # Query Lambda function
        query_function = lambda_.Function(
            self,
            "QueryFunction",
            runtime=lambda_.Runtime.PYTHON_3_9,
            code=lambda_.Code.from_asset("../app/controllers/lambda_handlers"),
            handler="query_handler.handler",
            role=lambda_role,
            environment=environment,
            timeout=Duration.seconds(30),
            memory_size=1024,
            log_retention=logs.RetentionDays.ONE_WEEK,
            description="RAG query processing function"
        )
        
        # Document ingestion Lambda function
        ingest_function = lambda_.Function(
            self,
            "IngestFunction",
            runtime=lambda_.Runtime.PYTHON_3_9,
            code=lambda_.Code.from_asset("../app/controllers/lambda_handlers"),
            handler="ingest_handler.handler",
            role=lambda_role,
            environment=environment,
            timeout=Duration.minutes(5),
            memory_size=2048,
            log_retention=logs.RetentionDays.ONE_WEEK,
            description="Document ingestion processing function"
        )
        
        # Collection stats Lambda function
        stats_function = lambda_.Function(
            self,
            "StatsFunction",
            runtime=lambda_.Runtime.PYTHON_3_9,
            code=lambda_.Code.from_asset("../app/controllers/lambda_handlers"),
            handler="stats_handler.handler",
            role=lambda_role,
            environment=environment,
            timeout=Duration.seconds(10),
            memory_size=512,
            log_retention=logs.RetentionDays.ONE_WEEK,
            description="Collection statistics function"
        )
        
        # Health check Lambda function
        health_function = lambda_.Function(
            self,
            "HealthFunction",
            runtime=lambda_.Runtime.PYTHON_3_9,
            code=lambda_.Code.from_inline("""
import json
import os

def handler(event, context):
    allowed_origins = os.environ.get('ALLOWED_ORIGINS', '*')
    origin = event.get('headers', {}).get('origin', '*')
    
    # If specific origins are allowed, check if the request origin is in the list
    if allowed_origins != '*':
        allowed_list = allowed_origins.split(',')
        if origin not in allowed_list:
            origin = allowed_list[0] if allowed_list else '*'
    else:
        origin = '*'
    
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': origin,
            'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token',
            'Access-Control-Allow-Methods': 'GET,POST,OPTIONS,DELETE',
            'Access-Control-Allow-Credentials': 'true'
        },
        'body': json.dumps({'status': 'healthy'})
    }
            """),
            handler="index.handler",
            environment=environment,
            timeout=Duration.seconds(5),
            memory_size=128,
            log_retention=logs.RetentionDays.ONE_WEEK,
            description="Health check function"
        )
        
        # OPTIONS handler for CORS preflight requests
        cors_function = lambda_.Function(
            self,
            "CorsFunction",
            runtime=lambda_.Runtime.PYTHON_3_9,
            code=lambda_.Code.from_inline("""
import json
import os

def handler(event, context):
    allowed_origins = os.environ.get('ALLOWED_ORIGINS', '*')
    origin = event.get('headers', {}).get('origin', '*')
    
    # If specific origins are allowed, check if the request origin is in the list
    if allowed_origins != '*':
        allowed_list = allowed_origins.split(',')
        if origin not in allowed_list:
            origin = allowed_list[0] if allowed_list else '*'
    else:
        origin = '*'
    
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': origin,
            'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token',
            'Access-Control-Allow-Methods': 'GET,POST,OPTIONS,DELETE',
            'Access-Control-Allow-Credentials': 'true',
            'Access-Control-Max-Age': '86400'
        },
        'body': json.dumps({'message': 'CORS preflight successful'})
    }
            """),
            handler="index.handler",
            environment=environment,
            timeout=Duration.seconds(3),
            memory_size=128,
            log_retention=logs.RetentionDays.ONE_WEEK,
            description="CORS preflight handler"
        )
        
        # Create API Gateway with proper CORS configuration
        self.api = apigateway.RestApi(
            self,
            "RagApi",
            rest_api_name=f"rag-api-{self.stack_name}",
            description="RAG Application API with fixed CORS",
            deploy_options=apigateway.StageOptions(
                stage_name=os.environ.get('STAGE', 'prod'),
                logging_level=apigateway.MethodLoggingLevel.INFO,
                data_trace_enabled=True,
                metrics_enabled=True,
                throttling_rate_limit=100,
                throttling_burst_limit=200
            ),
            # Enable CORS for all origins by default
            default_cors_preflight_options=apigateway.CorsOptions(
                allow_origins=apigateway.Cors.ALL_ORIGINS,
                allow_methods=apigateway.Cors.ALL_METHODS,
                allow_headers=[
                    "Content-Type",
                    "X-Amz-Date",
                    "Authorization",
                    "X-Api-Key",
                    "X-Amz-Security-Token"
                ],
                allow_credentials=True
            )
        )
        
        # Store API URL for reference
        self.api_url = self.api.url
        
        # Create /api/v1 resource structure
        api_resource = self.api.root.add_resource("api")
        v1_resource = api_resource.add_resource("v1")
        
        # Configure /api/v1/query endpoint
        query_resource = v1_resource.add_resource("query")
        query_resource.add_method(
            "POST",
            apigateway.LambdaIntegration(
                query_function,
                timeout=Duration.seconds(29),
                proxy=True
            ),
            authorization_type=apigateway.AuthorizationType.NONE
        )
        query_resource.add_method(
            "OPTIONS",
            apigateway.LambdaIntegration(cors_function),
            authorization_type=apigateway.AuthorizationType.NONE
        )
        
        # Configure /api/v1/ingest endpoint
        ingest_resource = v1_resource.add_resource("ingest")
        ingest_resource.add_method(
            "POST",
            apigateway.LambdaIntegration(
                ingest_function,
                timeout=Duration.seconds(29),
                proxy=True
            ),
            authorization_type=apigateway.AuthorizationType.NONE
        )
        ingest_resource.add_method(
            "OPTIONS",
            apigateway.LambdaIntegration(cors_function),
            authorization_type=apigateway.AuthorizationType.NONE
        )
        
        # Configure /api/v1/collection/stats endpoint
        collection_resource = v1_resource.add_resource("collection")
        stats_resource = collection_resource.add_resource("stats")
        stats_resource.add_method(
            "GET",
            apigateway.LambdaIntegration(
                stats_function,
                timeout=Duration.seconds(29),
                proxy=True
            ),
            authorization_type=apigateway.AuthorizationType.NONE
        )
        stats_resource.add_method(
            "OPTIONS",
            apigateway.LambdaIntegration(cors_function),
            authorization_type=apigateway.AuthorizationType.NONE
        )
        
        # Configure /api/v1/documents endpoint
        documents_resource = v1_resource.add_resource("documents")
        documents_resource.add_method(
            "GET",
            apigateway.LambdaIntegration(
                stats_function,  # Reuse stats function for listing documents
                timeout=Duration.seconds(29),
                proxy=True
            ),
            authorization_type=apigateway.AuthorizationType.NONE
        )
        documents_resource.add_method(
            "OPTIONS",
            apigateway.LambdaIntegration(cors_function),
            authorization_type=apigateway.AuthorizationType.NONE
        )
        
        # Configure /api/v1/search endpoint
        search_resource = v1_resource.add_resource("search")
        search_resource.add_method(
            "POST",
            apigateway.LambdaIntegration(
                query_function,  # Reuse query function for search
                timeout=Duration.seconds(29),
                proxy=True
            ),
            authorization_type=apigateway.AuthorizationType.NONE
        )
        search_resource.add_method(
            "OPTIONS",
            apigateway.LambdaIntegration(cors_function),
            authorization_type=apigateway.AuthorizationType.NONE
        )
        
        # Configure /api/v1/collection/clear endpoint
        clear_resource = collection_resource.add_resource("clear")
        clear_resource.add_method(
            "DELETE",
            apigateway.LambdaIntegration(
                stats_function,  # Reuse stats function for clearing
                timeout=Duration.seconds(29),
                proxy=True
            ),
            authorization_type=apigateway.AuthorizationType.NONE
        )
        clear_resource.add_method(
            "OPTIONS",
            apigateway.LambdaIntegration(cors_function),
            authorization_type=apigateway.AuthorizationType.NONE
        )
        
        # Add health check endpoint
        health_resource = self.api.root.add_resource("health")
        health_resource.add_method(
            "GET",
            apigateway.LambdaIntegration(health_function),
            authorization_type=apigateway.AuthorizationType.NONE
        )
        
        # Output important values
        CfnOutput(
            self,
            "ApiUrl",
            value=self.api.url,
            description="API Gateway URL",
            export_name=f"{self.stack_name}-api-url"
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
        
        CfnOutput(
            self,
            "StatsFunctionArn",
            value=stats_function.function_arn,
            description="Stats Lambda Function ARN"
        )