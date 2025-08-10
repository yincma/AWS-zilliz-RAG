"""
改进的Web栈 - 支持动态API配置和CloudFront反向代理
"""

from aws_cdk import (
    Stack,
    RemovalPolicy,
    Duration,
    CfnOutput,
    aws_s3 as s3,
    aws_s3_deployment as s3_deployment,
    aws_cloudfront as cloudfront,
    aws_cloudfront_origins as origins,
    aws_iam as iam,
    aws_apigateway as apigateway,
)
from constructs import Construct
import os
import json


class ImprovedWebStack(Stack):
    """改进的Web前端栈 - 支持动态配置和反向代理"""
    
    def __init__(self, scope: Construct, construct_id: str, 
                 api_gateway: apigateway.RestApi = None, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        # 创建S3存储桶
        web_bucket = s3.Bucket(
            self,
            "WebBucket",
            bucket_name=f"rag-web-{self.account}-{self.region}",
            public_read_access=False,
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
            removal_policy=RemovalPolicy.DESTROY,
            auto_delete_objects=True,
            encryption=s3.BucketEncryption.S3_MANAGED,
            versioned=False,
            cors=[
                s3.CorsRule(
                    allowed_methods=[
                        s3.HttpMethods.GET,
                        s3.HttpMethods.HEAD
                    ],
                    allowed_origins=["*"],
                    allowed_headers=["*"],
                    exposed_headers=[],
                    max_age=3000
                )
            ]
        )
        
        # 创建CloudFront OAI
        oai = cloudfront.OriginAccessIdentity(
            self,
            "WebOAI",
            comment=f"OAI for RAG Web Application {self.stack_name}"
        )
        
        # 授予CloudFront OAI读取S3的权限
        web_bucket.add_to_resource_policy(
            iam.PolicyStatement(
                sid="AllowCloudFrontOAIRead",
                effect=iam.Effect.ALLOW,
                principals=[oai.grant_principal],
                actions=[
                    "s3:GetObject",
                    "s3:GetObjectVersion",
                    "s3:ListBucket"
                ],
                resources=[
                    web_bucket.bucket_arn,
                    f"{web_bucket.bucket_arn}/*"
                ]
            )
        )
        
        # 创建响应头策略
        response_headers_policy = cloudfront.ResponseHeadersPolicy(
            self,
            "ResponseHeadersPolicy",
            response_headers_policy_name=f"rag-web-headers-{self.stack_name}",
            comment="Response headers for RAG Web Application",
            cors_behavior=cloudfront.ResponseHeadersCorsBehavior(
                access_control_allow_origins=["*"],
                access_control_allow_headers=["*"],
                access_control_allow_methods=["GET", "HEAD", "OPTIONS", "POST", "PUT", "DELETE"],
                access_control_allow_credentials=False,
                origin_override=True
            )
        )
        
        # 创建缓存策略 - 禁用API调用的缓存
        api_cache_policy = cloudfront.CachePolicy(
            self,
            "ApiCachePolicy",
            cache_policy_name=f"rag-api-cache-{self.stack_name}",
            comment="No cache for API calls",
            default_ttl=Duration.seconds(0),
            max_ttl=Duration.seconds(0),
            min_ttl=Duration.seconds(0),
            enable_accept_encoding_gzip=True,
            enable_accept_encoding_brotli=True
        )
        
        # 创建源请求策略 - 转发所有headers
        api_origin_request_policy = cloudfront.OriginRequestPolicy(
            self,
            "ApiOriginRequestPolicy",
            origin_request_policy_name=f"rag-api-origin-{self.stack_name}",
            comment="Forward all for API",
            header_behavior=cloudfront.OriginRequestHeaderBehavior.all_viewer(),
            query_string_behavior=cloudfront.OriginRequestQueryStringBehavior.all(),
            cookie_behavior=cloudfront.OriginRequestCookieBehavior.all()
        )
        
        # 准备分发行为配置
        additional_behaviors = {}
        
        # 如果提供了API Gateway，添加反向代理行为
        if api_gateway:
            # 获取API Gateway的域名
            api_domain = f"{api_gateway.rest_api_id}.execute-api.{self.region}.amazonaws.com"
            api_stage = "prod"  # 或从context获取
            
            # 添加API行为
            additional_behaviors["/api/*"] = cloudfront.BehaviorOptions(
                origin=origins.HttpOrigin(
                    api_domain,
                    origin_path=f"/{api_stage}",
                    protocol_policy=cloudfront.OriginProtocolPolicy.HTTPS_ONLY
                ),
                viewer_protocol_policy=cloudfront.ViewerProtocolPolicy.HTTPS_ONLY,
                allowed_methods=cloudfront.AllowedMethods.ALLOW_ALL,
                cache_policy=api_cache_policy,
                origin_request_policy=api_origin_request_policy,
                response_headers_policy=response_headers_policy
            )
        
        # CloudFront分发配置
        distribution = cloudfront.Distribution(
            self,
            "WebDistribution",
            default_root_object="index.html",
            price_class=cloudfront.PriceClass.PRICE_CLASS_100,
            enabled=True,
            http_version=cloudfront.HttpVersion.HTTP2_AND_3,
            comment=f"RAG Web Application Distribution - {self.stack_name}",
            
            # 默认行为 - 静态文件
            default_behavior=cloudfront.BehaviorOptions(
                origin=origins.S3Origin(
                    web_bucket,
                    origin_access_identity=oai
                ),
                viewer_protocol_policy=cloudfront.ViewerProtocolPolicy.REDIRECT_TO_HTTPS,
                allowed_methods=cloudfront.AllowedMethods.ALLOW_GET_HEAD_OPTIONS,
                cached_methods=cloudfront.CachedMethods.CACHE_GET_HEAD_OPTIONS,
                compress=True,
                response_headers_policy=response_headers_policy,
                cache_policy=cloudfront.CachePolicy.CACHING_OPTIMIZED
            ),
            
            # 额外的行为（API反向代理）
            additional_behaviors=additional_behaviors,
            
            # 错误页面配置
            error_responses=[
                cloudfront.ErrorResponse(
                    http_status=404,
                    response_page_path="/index.html",
                    response_http_status=200,
                    ttl=Duration.seconds(10)
                ),
                cloudfront.ErrorResponse(
                    http_status=403,
                    response_page_path="/index.html",
                    response_http_status=200,
                    ttl=Duration.seconds(10)
                )
            ]
        )
        
        # 创建运行时配置文件
        runtime_config = {
            "apiUrl": "",  # 使用相对路径，通过CloudFront代理
            "cloudFrontUrl": distribution.distribution_domain_name,
            "environment": self.node.try_get_context('stage') or 'prod',
            "features": {
                "useProxy": True,  # 使用CloudFront反向代理
                "apiPath": "/api",  # API路径前缀
                "debug": False
            }
        }
        
        # 准备前端文件路径
        web_assets_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
            "app", "views", "web"
        )
        
        # 部署静态文件到S3
        deployment = s3_deployment.BucketDeployment(
            self,
            "WebDeployment",
            sources=[
                s3_deployment.Source.asset(web_assets_path),
                s3_deployment.Source.data(
                    "static/js/runtime-config.json", 
                    json.dumps(runtime_config, indent=2)
                )
            ],
            destination_bucket=web_bucket,
            distribution=distribution,
            distribution_paths=["/*"],
            memory_limit=256,
            retain_on_delete=False
        )
        
        # 输出
        CfnOutput(
            self,
            "CloudFrontURL",
            value=f"https://{distribution.distribution_domain_name}",
            description="CloudFront distribution URL"
        )
        
        CfnOutput(
            self,
            "CloudFrontDistributionId",
            value=distribution.distribution_id,
            description="CloudFront distribution ID"
        )
        
        CfnOutput(
            self,
            "S3BucketName",
            value=web_bucket.bucket_name,
            description="S3 bucket name for web assets"
        )
        
        CfnOutput(
            self,
            "OAIId",
            value=oai.cloud_front_origin_access_identity_s3_canonical_user_id,
            description="CloudFront OAI ID"
        )
        
        # 如果有API Gateway，输出代理配置信息
        if api_gateway:
            CfnOutput(
                self,
                "ApiProxyPath",
                value="/api/*",
                description="API proxy path in CloudFront"
            )
            
            CfnOutput(
                self,
                "ApiGatewayOrigin",
                value=f"https://{api_domain}/{api_stage}",
                description="API Gateway origin URL"
            )