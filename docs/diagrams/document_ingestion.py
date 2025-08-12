#!/usr/bin/env python3
"""文档摄入处理流程图"""

from diagrams import Diagram, Cluster, Edge
from diagrams.aws.compute import Lambda
from diagrams.aws.storage import S3
from diagrams.aws.ml import Bedrock
from diagrams.custom import Custom
from diagrams.onprem.client import User
from diagrams.generic.storage import Storage
from diagrams.onprem.compute import Server

with Diagram("文档摄入流程", filename="../images/document_ingestion", show=False, direction="TB"):
    user = User("用户")
    
    with Cluster("文档上传"):
        upload = Storage("文档上传")
        s3_storage = S3("S3存储")
        trigger = Lambda("摄入触发器")
    
    with Cluster("文档处理"):
        # 文档处理都在Lambda中运行
        parse = Lambda("文档解析")
        chunk = Lambda("文本分块")
        clean = Lambda("文本清洗")
    
    with Cluster("向量化处理"):
        batch_embed = Bedrock("批量向量化\n(Titan)")
        # 向量优化在Lambda中运行
        optimize = Lambda("向量优化")
    
    with Cluster("存储更新"):
        # 使用自定义Zilliz图标
        store_vectors = Custom("存储向量\n(Zilliz)", "../images/Zilliz.jpeg")
        cache_s3 = S3("缓存到S3")
        # 更新元数据在Lambda中运行
        update_meta = Lambda("更新元数据")
    
    complete = Server("完成通知")
    
    # 处理流程
    user >> upload >> s3_storage >> trigger
    trigger >> parse >> chunk >> clean
    clean >> batch_embed >> optimize
    optimize >> [store_vectors, cache_s3]
    store_vectors >> update_meta >> complete
    cache_s3 >> update_meta