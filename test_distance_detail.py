#!/usr/bin/env python3
"""
深入测试：验证L2距离和向量维度问题
"""
import os
import logging
from pymilvus import connections, Collection, utility
import numpy as np

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def test_distance_calculation():
    """测试距离计算问题"""
    
    # 连接配置
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
        
        # 获取collection信息
        logger.info(f"Collection entities: {collection.num_entities}")
        
        # 先查询获取一个实际的向量
        sample_results = collection.query(
            expr="doc_id != ''",
            output_fields=["doc_id", "content"],
            limit=1
        )
        
        if sample_results:
            logger.info(f"找到样本文档: {sample_results[0]['doc_id']}")
            logger.info(f"文档内容前100字符: {sample_results[0]['content'][:100]}")
            
            # 用一个实际文档ID来查询
            doc_id = sample_results[0]['doc_id']
            
            # 创建不同类型的测试向量
            test_vectors = {
                "零向量": np.zeros(1536).tolist(),
                "随机向量": np.random.rand(1536).tolist(),
                "归一化随机向量": (np.random.rand(1536) / np.linalg.norm(np.random.rand(1536))).tolist(),
                "小随机向量": (np.random.rand(1536) * 0.01).tolist()
            }
            
            for vector_type, query_vector in test_vectors.items():
                logger.info(f"\n--- 测试 {vector_type} ---")
                
                # 计算向量的L2范数
                vector_norm = np.linalg.norm(query_vector)
                logger.info(f"查询向量L2范数: {vector_norm:.4f}")
                
                search_params = {"metric_type": "L2", "params": {"nprobe": 10}}
                
                results = collection.search(
                    data=[query_vector],
                    anns_field="embedding",
                    param=search_params,
                    limit=2,
                    output_fields=["content", "metadata"]
                )
                
                for i, hit in enumerate(results[0]):
                    distance = hit.distance
                    # 按照代码中的公式计算score
                    calculated_score = max(0, min(100, 100 - distance * 10))
                    
                    logger.info(f"  结果{i+1}:")
                    logger.info(f"    L2距离: {distance:.4f}")
                    logger.info(f"    计算的score: {calculated_score:.2f}")
                    # 处理entity的访问方式
                    content = ""
                    if isinstance(hit.entity, dict):
                        content = hit.entity.get('content', '')
                    else:
                        content = getattr(hit.entity, 'content', '')
                    logger.info(f"    文档前50字符: {content[:50] if content else 'N/A'}")
        
        # 检查向量维度是否匹配
        logger.info("\n--- 检查Collection Schema ---")
        schema = collection.schema
        for field in schema.fields:
            if field.dtype.name == "FLOAT_VECTOR":
                logger.info(f"向量字段: {field.name}, 维度: {field.params.get('dim')}")
        
    except Exception as e:
        logger.error(f"错误: {str(e)}")
        import traceback
        logger.error(traceback.format_exc())
    finally:
        connections.disconnect("default")

if __name__ == "__main__":
    test_distance_calculation()