"""
Web栈 - S3静态网站托管和CloudFront CDN (修复版)
"""

from aws_cdk import (
    Stack,
    RemovalPolicy,
    Duration,
    CfnOutput,
    Size,
    aws_s3 as s3,
    aws_s3_deployment as s3_deployment,
    aws_cloudfront as cloudfront,
    aws_cloudfront_origins as origins,
    aws_iam as iam,
)
from constructs import Construct
import os


class WebStack(Stack):
    """Web前端栈 - 修复403错误版本"""
    
    def __init__(self, scope: Construct, construct_id: str, 
                 api_url: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        # 创建S3存储桶 - 完全私有，只允许CloudFront访问
        web_bucket = s3.Bucket(
            self,
            "WebBucket",
            bucket_name=f"rag-web-{self.account}-{self.region}",
            # 移除website配置，因为我们通过CloudFront访问
            public_read_access=False,
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,  # 完全阻止公共访问
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
        
        # 创建CloudFront Origin Access Identity
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
        
        # 创建CloudFront响应头策略
        response_headers_policy = cloudfront.ResponseHeadersPolicy(
            self,
            "ResponseHeadersPolicy",
            response_headers_policy_name=f"rag-web-headers-{self.stack_name}",
            comment="Response headers for RAG Web Application",
            cors_behavior=cloudfront.ResponseHeadersCorsBehavior(
                access_control_allow_origins=["*"],
                access_control_allow_headers=["*"],
                access_control_allow_methods=["GET", "HEAD", "OPTIONS"],
                access_control_allow_credentials=False,
                origin_override=True
            ),
            security_headers_behavior=cloudfront.ResponseSecurityHeadersBehavior(
                content_type_options=cloudfront.ResponseHeadersContentTypeOptions(
                    override=True
                ),
                frame_options=cloudfront.ResponseHeadersFrameOptions(
                    frame_option=cloudfront.HeadersFrameOption.DENY,
                    override=True
                ),
                referrer_policy=cloudfront.ResponseHeadersReferrerPolicy(
                    referrer_policy=cloudfront.HeadersReferrerPolicy.STRICT_ORIGIN_WHEN_CROSS_ORIGIN,
                    override=True
                ),
                xss_protection=cloudfront.ResponseHeadersXSSProtection(
                    protection=True,
                    mode_block=True,
                    override=True
                ),
                strict_transport_security=cloudfront.ResponseHeadersStrictTransportSecurity(
                    access_control_max_age=Duration.seconds(63072000),
                    include_subdomains=True,
                    override=True
                )
            )
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
            
            # 默认行为
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
                cache_policy=cloudfront.CachePolicy(
                    self,
                    "CachePolicy",
                    cache_policy_name=f"rag-web-cache-{self.stack_name}",
                    comment="Cache policy for RAG Web Application",
                    default_ttl=Duration.hours(24),
                    max_ttl=Duration.days(365),
                    min_ttl=Duration.seconds(0),
                    enable_accept_encoding_gzip=True,
                    enable_accept_encoding_brotli=True,
                    query_string_behavior=cloudfront.CacheQueryStringBehavior.all(),
                    header_behavior=cloudfront.CacheHeaderBehavior.none(),
                    cookie_behavior=cloudfront.CacheCookieBehavior.none()
                )
            ),
            
            # 错误页面配置
            error_responses=[
                # 404错误 - 返回index.html用于SPA路由
                cloudfront.ErrorResponse(
                    http_status=404,
                    response_page_path="/index.html",
                    response_http_status=200,
                    ttl=Duration.seconds(10)
                ),
                # 403错误 - 返回index.html
                cloudfront.ErrorResponse(
                    http_status=403,
                    response_page_path="/index.html",
                    response_http_status=200,
                    ttl=Duration.seconds(10)
                )
            ]
        )
        
        # 为API调用添加额外的行为（如果提供了有效的API URL）
        if api_url and api_url != "https://api.example.com":
            # 提取域名部分
            api_domain = api_url.replace("https://", "").replace("http://", "").split("/")[0]
            if api_domain and "." in api_domain:  # 确保是有效域名
                distribution.add_behavior(
                    "/api/*",
                    origins.HttpOrigin(api_domain),
                    viewer_protocol_policy=cloudfront.ViewerProtocolPolicy.HTTPS_ONLY,
                    allowed_methods=cloudfront.AllowedMethods.ALLOW_ALL,
                    cache_policy=cloudfront.CachePolicy.CACHING_DISABLED,
                    origin_request_policy=cloudfront.OriginRequestPolicy.ALL_VIEWER
                )
        
        # 准备前端文件路径
        web_assets_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
            "app", "views", "web"
        )
        
        # 创建动态配置文件内容
        config_content = f"""// 自动生成的配置文件
const API_CONFIG = {{
    // API端点 - 支持本地和远程
    API_URL: window.location.hostname === 'localhost' 
        ? 'http://localhost:8000' 
        : '{api_url}',
    
    // CloudFront分发域名
    CLOUDFRONT_URL: window.location.origin,
    
    // 默认设置
    DEFAULT_TOP_K: 5,
    DEFAULT_USE_RAG: true,
    DEFAULT_TEMPERATURE: 0.7,
    DEFAULT_MAX_TOKENS: 1000,
    
    // 请求超时设置（毫秒）
    REQUEST_TIMEOUT: 30000,
    
    // 健康检查间隔（毫秒）
    HEALTH_CHECK_INTERVAL: 30000,
    
    // 重试设置
    MAX_RETRIES: 3,
    RETRY_DELAY: 1000
}};

// 环境检测
const ENV = {{
    isProduction: window.location.hostname !== 'localhost',
    isDevelopment: window.location.hostname === 'localhost',
    isCloudFront: window.location.hostname.includes('cloudfront.net'),
    stage: '{self.node.try_get_context('stage') or 'prod'}'
}};

// 导出配置
window.RAG_CONFIG = {{
    ...API_CONFIG,
    ENV,
    // 兼容旧配置
    API_BASE_URL: API_CONFIG.API_URL,
    MAX_QUERY_LENGTH: 500,
    TIMEOUT: API_CONFIG.REQUEST_TIMEOUT
}};
"""
        
        # 部署静态文件到S3
        deployment = s3_deployment.BucketDeployment(
            self,
            "WebDeployment",
            sources=[
                s3_deployment.Source.asset(web_assets_path),
                s3_deployment.Source.data("static/js/rag-config.js", config_content)
            ],
            destination_bucket=web_bucket,
            distribution=distribution,
            distribution_paths=["/*"],
            retain_on_delete=False,
            prune=True,  # 删除目标中不存在于源中的文件
            memory_limit=512,  # 增加Lambda内存以提高部署速度
            ephemeral_storage_size=Size.mebibytes(1024)  # 增加临时存储
        )
        
        # 输出URL
        self.distribution_url = f"https://{distribution.distribution_domain_name}"
        self.distribution_id = distribution.distribution_id
        
        # CloudFormation输出
        CfnOutput(
            self,
            "CloudFrontURL",
            value=self.distribution_url,
            description="CloudFront Distribution URL"
        )
        
        CfnOutput(
            self,
            "CloudFrontDistributionId",
            value=self.distribution_id,
            description="CloudFront Distribution ID"
        )
        
        CfnOutput(
            self,
            "S3BucketName",
            value=web_bucket.bucket_name,
            description="S3 Bucket Name"
        )
        
        CfnOutput(
            self,
            "OAIId",
            value=oai.cloud_front_origin_access_identity_s3_canonical_user_id,
            description="CloudFront OAI ID"
        )