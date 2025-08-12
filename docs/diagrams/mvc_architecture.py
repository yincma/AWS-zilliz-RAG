#!/usr/bin/env python3
"""MVC架构层次图"""

from diagrams import Diagram, Cluster, Edge
from diagrams.aws.compute import Lambda
from diagrams.aws.storage import S3
from diagrams.aws.network import CloudFront, APIGateway
from diagrams.aws.ml import Bedrock
from diagrams.custom import Custom
from diagrams.generic.compute import Rack
from diagrams.programming.framework import React
from diagrams.onprem.client import Users
from diagrams.programming.framework import Django  # 用Django代表LangChain框架

with Diagram("MVC架构层次", filename="../images/mvc_architecture", show=False, direction="TB"):
    users = Users("用户")
    
    with Cluster("View层 (视图层)"):
        with Cluster("Web前端"):
            templates = React("HTML模板")
            static_assets = S3("静态资源")
            cloudfront_view = CloudFront("CloudFront分发")
            s3_static = S3("S3静态托管")
        
        with Cluster("API视图"):
            api_responses = APIGateway("API响应格式化")
            # 数据序列化也在Lambda中运行
            serializers = Lambda("数据序列化器")
    
    with Cluster("Controller层 (控制器层)"):
        rag_controller = Lambda("RAG控制器")
        doc_controller = Lambda("文档控制器") 
        search_controller = Lambda("搜索控制器")
        lambda_handlers = Lambda("Lambda处理器")
    
    with Cluster("Model层 (模型层)"):
        with Cluster("业务模型"):
            # 文档模型也在Lambda中运行
            document_model = Lambda("文档模型")
            embedding_model = Bedrock("嵌入模型")
            # 使用自定义Zilliz图标
            vector_store_model = Custom("Zilliz向量存储", "../images/Zilliz.jpeg")
            llm_model = Bedrock("LLM模型")
            rag_chain_model = Django("LangChain RAG链")
    
    # MVC交互关系
    users >> Edge(label="请求") >> cloudfront_view
    cloudfront_view >> s3_static
    
    users >> Edge(label="API调用") >> api_responses
    api_responses >> rag_controller
    
    rag_controller >> Edge(label="业务逻辑") >> [document_model, embedding_model, llm_model]
    doc_controller >> Edge(label="文档处理") >> document_model
    search_controller >> Edge(label="向量检索") >> vector_store_model
    
    lambda_handlers >> Edge(label="路由") >> [rag_controller, doc_controller, search_controller]