#!/usr/bin/env python3
"""MVC Architecture Layer Diagram"""

from diagrams import Diagram, Cluster, Edge
from diagrams.aws.compute import Lambda
from diagrams.aws.storage import S3
from diagrams.aws.network import CloudFront, APIGateway
from diagrams.aws.ml import Bedrock
from diagrams.custom import Custom
from diagrams.generic.compute import Rack
from diagrams.programming.framework import React
from diagrams.onprem.client import Users
from diagrams.programming.framework import Django  # Use Django to represent LangChain framework

with Diagram("MVC Architecture Layers", filename="../images/mvc_architecture", show=False, direction="TB"):
    users = Users("Users")
    
    with Cluster("View Layer (Presentation Layer)"):
        with Cluster("Web Frontend"):
            templates = React("HTML Templates")
            static_assets = S3("Static Assets")
            cloudfront_view = CloudFront("CloudFront Distribution")
            s3_static = S3("S3 Static Hosting")
        
        with Cluster("API Views"):
            api_responses = APIGateway("API Response Formatting")
            # Data serialization also runs in Lambda
            serializers = Lambda("Data Serializers")
    
    with Cluster("Controller Layer (Control Layer)"):
        rag_controller = Lambda("RAG Controller")
        doc_controller = Lambda("Document Controller") 
        search_controller = Lambda("Search Controller")
        lambda_handlers = Lambda("Lambda Handlers")
    
    with Cluster("Model Layer (Data Layer)"):
        with Cluster("Business Models"):
            # Document model also runs in Lambda
            document_model = Lambda("Document Model")
            embedding_model = Bedrock("Embedding Model")
            # 使用自定义Zilliz图标
            vector_store_model = Custom("Zilliz Vector Store", "../images/Zilliz.jpeg")
            llm_model = Bedrock("LLM Model")
            rag_chain_model = Django("LangChain RAG链")
    
    # MVC interaction relationships
    users >> Edge(label="Request") >> cloudfront_view
    cloudfront_view >> s3_static
    
    users >> Edge(label="API Calls") >> api_responses
    api_responses >> rag_controller
    
    rag_controller >> Edge(label="Business Logic") >> [document_model, embedding_model, llm_model]
    doc_controller >> Edge(label="Document Processing") >> document_model
    search_controller >> Edge(label="Vector Retrieval") >> vector_store_model
    
    lambda_handlers >> Edge(label="Routing") >> [rag_controller, doc_controller, search_controller]