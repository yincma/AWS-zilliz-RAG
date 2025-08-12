#!/usr/bin/env python3
"""RAG查询处理数据流程图"""

from diagrams import Diagram, Cluster, Edge
from diagrams.aws.compute import Lambda
from diagrams.aws.ml import Bedrock
from diagrams.aws.network import APIGateway
from diagrams.custom import Custom
from diagrams.onprem.client import User
from diagrams.programming.flowchart import Decision
from diagrams.generic.compute import Rack

with Diagram("RAG查询处理流程", filename="../images/rag_data_flow", show=False, direction="LR"):
    user = User("用户")
    
    with Cluster("请求处理"):
        api = APIGateway("API Gateway")
        lambda_handler = Lambda("Query Handler")
    
    with Cluster("查询处理"):
        # 查询预处理在Lambda中运行
        preprocess = Lambda("查询预处理")
        vectorize = Bedrock("查询向量化\n(Titan)")
    
    with Cluster("检索阶段"):
        # 使用自定义Zilliz图标
        vector_search = Custom("向量检索\n(Zilliz)", "../images/Zilliz.jpeg")
        # 结果重排序在Lambda中运行
        rerank = Lambda("结果重排序")
    
    with Cluster("生成阶段"):
        # 上下文构建在Lambda中运行
        context_build = Lambda("上下文构建")
        llm_generate = Bedrock("答案生成\n(Nova Pro)")
        # 响应格式化在Lambda中运行
        format_response = Lambda("响应格式化")
    
    # 数据流向
    user >> Edge(label="查询") >> api >> lambda_handler
    lambda_handler >> preprocess >> vectorize
    vectorize >> vector_search >> rerank
    rerank >> context_build >> llm_generate
    llm_generate >> format_response >> Edge(label="答案") >> user