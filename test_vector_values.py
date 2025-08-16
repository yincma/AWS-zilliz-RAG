#!/usr/bin/env python3
"""
检查存储在Zilliz中的实际向量值
"""
import os
import logging
from pymilvus import connections, Collection
import numpy as np

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def check_stored_vectors():
    """检查存储的向量值"""
    
    endpoint = 'https://in03-a9b3b5529895a3d.serverless.aws-eu-central-1.cloud.zilliz.com'
    token = '88c6ee3f3abf448278a1e30d5b951517645207f1fa94daeec7fc7b7e4b47fbaeb2bc953e5d1ccb2e94749f8f3992955310026115'
    
    try:
        if endpoint.startswith('https://'):
            endpoint = endpoint.replace('https://', '')
        
        connections.connect(
            alias="default",
            uri=f"https://{endpoint}",
            token=token,
            secure=True
        )
        logger.info("✅ 连接Zilliz成功")
        
        collection = Collection('rag_collection')
        collection.load()
        
        # 查询所有文档的向量
        results = collection.query(
            expr="doc_id != ''",
            output_fields=["doc_id", "content", "embedding"],
            limit=10
        )
        
        logger.info(f"找到 {len(results)} 个文档")
        
        for i, doc in enumerate(results):
            logger.info(f"\n--- 文档 {i+1} ---")
            logger.info(f"doc_id: {doc['doc_id']}")
            logger.info(f"content前50字符: {doc['content'][:50]}")
            
            embedding = doc.get('embedding', [])
            if embedding:
                # 转换为numpy数组进行分析
                vec = np.array(embedding)
                
                logger.info(f"向量维度: {len(embedding)}")
                logger.info(f"向量前10个值: {embedding[:10]}")
                logger.info(f"向量L2范数: {np.linalg.norm(vec):.4f}")
                logger.info(f"向量最大值: {np.max(vec):.4f}")
                logger.info(f"向量最小值: {np.min(vec):.4f}")
                logger.info(f"向量平均值: {np.mean(vec):.4f}")
                logger.info(f"向量标准差: {np.std(vec):.4f}")
                
                # 检查是否有异常值
                zero_count = np.sum(vec == 0)
                logger.info(f"零值数量: {zero_count}")
                
                # 检查向量是否全是相同的值
                unique_values = len(np.unique(vec))
                logger.info(f"唯一值数量: {unique_values}")
                
                # 如果向量看起来异常，打印更多信息
                if np.linalg.norm(vec) > 50 or unique_values < 100:
                    logger.warning("⚠️ 向量可能有异常！")
                    logger.info(f"向量前50个值: {embedding[:50]}")
            else:
                logger.warning("❌ 没有找到embedding字段")
        
    except Exception as e:
        logger.error(f"错误: {str(e)}")
        import traceback
        logger.error(traceback.format_exc())
    finally:
        connections.disconnect("default")

if __name__ == "__main__":
    check_stored_vectors()