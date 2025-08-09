"""
数据栈 - S3存储桶和数据库资源
"""

from aws_cdk import (
    Stack,
    RemovalPolicy,
    Duration,
    aws_s3 as s3,
    aws_dynamodb as dynamodb,
)
from constructs import Construct


class DataStack(Stack):
    """数据存储栈"""
    
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        # 文档存储桶
        self.document_bucket = s3.Bucket(
            self,
            "DocumentBucket",
            bucket_name=f"rag-documents-{self.account}-{self.region}",
            versioned=True,
            encryption=s3.BucketEncryption.S3_MANAGED,
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
            removal_policy=RemovalPolicy.RETAIN,
            lifecycle_rules=[
                s3.LifecycleRule(
                    id="DeleteOldVersions",
                    noncurrent_version_expiration=Duration.days(30),
                    enabled=True
                )
            ],
            cors=[
                s3.CorsRule(
                    allowed_methods=[
                        s3.HttpMethods.GET,
                        s3.HttpMethods.PUT,
                        s3.HttpMethods.POST,
                        s3.HttpMethods.DELETE
                    ],
                    allowed_origins=["*"],
                    allowed_headers=["*"],
                    max_age=3000
                )
            ]
        )
        
        # 会话存储表（可选）
        self.session_table = dynamodb.Table(
            self,
            "SessionTable",
            table_name=f"rag-sessions-{self.node.try_get_context('stage')}",
            partition_key=dynamodb.Attribute(
                name="session_id",
                type=dynamodb.AttributeType.STRING
            ),
            sort_key=dynamodb.Attribute(
                name="timestamp",
                type=dynamodb.AttributeType.NUMBER
            ),
            billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST,
            removal_policy=RemovalPolicy.DESTROY,
            time_to_live_attribute="ttl",
            point_in_time_recovery=True
        )
        
        # 文档元数据表
        self.document_metadata_table = dynamodb.Table(
            self,
            "DocumentMetadataTable",
            table_name=f"rag-document-metadata-{self.node.try_get_context('stage')}",
            partition_key=dynamodb.Attribute(
                name="document_id",
                type=dynamodb.AttributeType.STRING
            ),
            billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST,
            removal_policy=RemovalPolicy.DESTROY,
            stream=dynamodb.StreamViewType.NEW_AND_OLD_IMAGES
        )
        
        # 添加GSI用于按用户查询
        self.document_metadata_table.add_global_secondary_index(
            index_name="user-index",
            partition_key=dynamodb.Attribute(
                name="user_id",
                type=dynamodb.AttributeType.STRING
            ),
            sort_key=dynamodb.Attribute(
                name="upload_date",
                type=dynamodb.AttributeType.STRING
            )
        )