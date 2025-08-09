"""
Web栈 - S3静态网站托管和CloudFront CDN
"""

from aws_cdk import (
    Stack,
    RemovalPolicy,
    Duration,
    aws_s3 as s3,
    aws_s3_deployment as s3_deployment,
    aws_cloudfront as cloudfront,
    aws_cloudfront_origins as origins,
    aws_iam as iam,
)
from constructs import Construct


class WebStack(Stack):
    """Web前端栈"""
    
    def __init__(self, scope: Construct, construct_id: str, 
                 api_url: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        # 静态网站S3存储桶
        web_bucket = s3.Bucket(
            self,
            "WebBucket",
            bucket_name=f"rag-web-{self.account}-{self.region}",
            website_index_document="index.html",
            website_error_document="error.html",
            public_read_access=False,
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
            removal_policy=RemovalPolicy.DESTROY,
            auto_delete_objects=True,
            cors=[
                s3.CorsRule(
                    allowed_methods=[s3.HttpMethods.GET],
                    allowed_origins=["*"],
                    allowed_headers=["*"],
                    max_age=3000
                )
            ]
        )
        
        # CloudFront Origin Access Identity
        oai = cloudfront.OriginAccessIdentity(
            self,
            "OAI",
            comment="OAI for RAG Web Application"
        )
        
        # 授予CloudFront访问S3的权限
        web_bucket.grant_read(oai)
        
        # CloudFront分发
        distribution = cloudfront.Distribution(
            self,
            "WebDistribution",
            default_root_object="index.html",
            default_behavior=cloudfront.BehaviorOptions(
                origin=origins.S3Origin(
                    web_bucket,
                    origin_access_identity=oai
                ),
                viewer_protocol_policy=cloudfront.ViewerProtocolPolicy.REDIRECT_TO_HTTPS,
                cache_policy=cloudfront.CachePolicy.CACHING_OPTIMIZED,
                allowed_methods=cloudfront.AllowedMethods.ALLOW_GET_HEAD,
                compress=True
            ),
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
            ],
            price_class=cloudfront.PriceClass.PRICE_CLASS_100,
            enabled=True,
            http_version=cloudfront.HttpVersion.HTTP2,
            comment="RAG Web Application Distribution"
        )
        
        # 创建配置文件，包含API URL
        config_content = f"""
window.RAG_CONFIG = {{
    apiUrl: "{api_url}",
    version: "0.1.0",
    environment: "{self.node.try_get_context('stage') or 'dev'}"
}};
        """
        
        # 部署静态文件到S3
        s3_deployment.BucketDeployment(
            self,
            "WebDeployment",
            sources=[
                s3_deployment.Source.asset("../app/views/web"),
                s3_deployment.Source.data("config.js", config_content)
            ],
            destination_bucket=web_bucket,
            distribution=distribution,
            distribution_paths=["/*"],
            retain_on_delete=False
        )
        
        # 输出CloudFront URL
        self.distribution_url = f"https://{distribution.distribution_domain_name}"