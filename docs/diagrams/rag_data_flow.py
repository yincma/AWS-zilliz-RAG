#!/usr/bin/env python3
"""RAG Query Processing Data Flow Diagram"""

from diagrams import Diagram, Cluster, Edge
from diagrams.aws.compute import Lambda
from diagrams.aws.ml import Bedrock
from diagrams.aws.network import APIGateway
from diagrams.custom import Custom
from diagrams.onprem.client import User
from diagrams.programming.flowchart import Decision
from diagrams.generic.compute import Rack

with Diagram("RAG Query Processing Flow", filename="../images/rag_data_flow", show=False, direction="LR"):
    user = User("User")
    
    with Cluster("Request Processing"):
        api = APIGateway("API Gateway")
        lambda_handler = Lambda("Query Handler")
    
    with Cluster("Query Processing"):
        # Query preprocessing runs in Lambda
        preprocess = Lambda("Query Preprocessing")
        vectorize = Bedrock("Query Vectorization\n(Titan)")
    
    with Cluster("Retrieval Stage"):
        # Use custom Zilliz icon
        vector_search = Custom("Vector Retrieval\n(Zilliz)", "../images/Zilliz.jpeg")
        # Result reranking runs in Lambda
        rerank = Lambda("Result Reranking")
    
    with Cluster("Generation Stage"):
        # Context building runs in Lambda
        context_build = Lambda("Context Building")
        llm_generate = Bedrock("Answer Generation\n(Nova Pro)")
        # Response formatting runs in Lambda
        format_response = Lambda("Response Formatting")
    
    # Data flow
    user >> Edge(label="Query") >> api >> lambda_handler
    lambda_handler >> preprocess >> vectorize
    vectorize >> vector_search >> rerank
    rerank >> context_build >> llm_generate
    llm_generate >> format_response >> Edge(label="Answer") >> user