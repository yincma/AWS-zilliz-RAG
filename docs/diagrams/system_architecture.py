#!/usr/bin/env python3
"""AWS-Zilliz-RAG System Overall Architecture Diagram"""

from diagrams import Diagram, Cluster, Edge
from diagrams.aws.compute import Lambda
from diagrams.aws.storage import S3
from diagrams.aws.network import CloudFront, APIGateway
from diagrams.aws.ml import Bedrock
from diagrams.custom import Custom
from diagrams.onprem.client import Users

with Diagram("AWS-Zilliz-RAG System Architecture", filename="../images/system_architecture", show=False, direction="TB"):
    users = Users("Users")
    
    with Cluster("AWS Frontend Layer"):
        cloudfront = CloudFront("CloudFront CDN")
        s3_web = S3("S3 Static Hosting")
    
    with Cluster("AWS API Layer"):
        api_gateway = APIGateway("API Gateway")
        
    with Cluster("AWS Compute Layer"):
        lambda_query = Lambda("Query Processing Lambda")
        lambda_ingest = Lambda("Document Ingestion Lambda")
        lambda_search = Lambda("Search Lambda")
        
    with Cluster("AWS AI Services Layer"):
        bedrock_llm = Bedrock("Bedrock LLM\n(Nova Pro)")
        bedrock_emb = Bedrock("Bedrock Embeddings\n(Titan)")
        
    with Cluster("Storage Layer"):
        s3_docs = S3("S3 Document Storage")
        # Use custom Zilliz icon
        zilliz = Custom("Zilliz Vector Database", "../images/Zilliz.jpeg")
    
    # User access flow
    users >> Edge(label="Web Access") >> cloudfront >> s3_web
    users >> Edge(label="API Calls") >> api_gateway
    
    # API routing
    api_gateway >> Edge(label="Query Request") >> lambda_query
    api_gateway >> Edge(label="Document Upload") >> lambda_ingest
    api_gateway >> Edge(label="Search Request") >> lambda_search
    
    # Lambda business logic
    lambda_query >> Edge(label="Generate Answer") >> bedrock_llm
    lambda_query >> Edge(label="Vector Retrieval") >> zilliz
    
    lambda_ingest >> Edge(label="Vectorization") >> bedrock_emb
    lambda_ingest >> Edge(label="Store Documents") >> s3_docs
    lambda_ingest >> Edge(label="Store Vectors") >> zilliz
    
    lambda_search >> Edge(label="Vector Search") >> zilliz