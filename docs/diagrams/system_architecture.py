#!/usr/bin/env python3
"""AWS-Zilliz-RAG系统整体架构图"""

from diagrams import Diagram, Cluster, Edge
from diagrams.aws.compute import Lambda
from diagrams.aws.storage import S3
from diagrams.aws.network import CloudFront, APIGateway
from diagrams.aws.ml import Bedrock
from diagrams.custom import Custom
from diagrams.onprem.client import Users

with Diagram("AWS-Zilliz-RAG系统架构", filename="../images/system_architecture", show=False, direction="TB"):
    users = Users("用户")
    
    with Cluster("AWS前端层"):
        cloudfront = CloudFront("CloudFront CDN")
        s3_web = S3("S3静态托管")
    
    with Cluster("AWS API层"):
        api_gateway = APIGateway("API Gateway")
        
    with Cluster("AWS计算层"):
        lambda_query = Lambda("查询处理Lambda")
        lambda_ingest = Lambda("文档摄入Lambda")
        lambda_search = Lambda("搜索Lambda")
        
    with Cluster("AWS AI服务层"):
        bedrock_llm = Bedrock("Bedrock LLM\n(Nova Pro)")
        bedrock_emb = Bedrock("Bedrock Embeddings\n(Titan)")
        
    with Cluster("存储层"):
        s3_docs = S3("S3文档存储")
        # 使用自定义Zilliz图标
        zilliz = Custom("Zilliz向量数据库", "../images/Zilliz.jpeg")
    
    # 用户访问流程
    users >> Edge(label="Web访问") >> cloudfront >> s3_web
    users >> Edge(label="API调用") >> api_gateway
    
    # API路由
    api_gateway >> Edge(label="查询请求") >> lambda_query
    api_gateway >> Edge(label="文档上传") >> lambda_ingest
    api_gateway >> Edge(label="搜索请求") >> lambda_search
    
    # Lambda业务逻辑
    lambda_query >> Edge(label="生成回答") >> bedrock_llm
    lambda_query >> Edge(label="向量检索") >> zilliz
    
    lambda_ingest >> Edge(label="向量化") >> bedrock_emb
    lambda_ingest >> Edge(label="存储文档") >> s3_docs
    lambda_ingest >> Edge(label="存储向量") >> zilliz
    
    lambda_search >> Edge(label="向量搜索") >> zilliz