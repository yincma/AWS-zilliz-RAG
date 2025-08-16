#!/usr/bin/env python3
"""
计算存储向量之间的实际L2距离，并与查询结果对比
"""
import os
import logging
from pymilvus import connections, Collection
import numpy as np

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def test_vector_distance():
    """测试向量距离计算"""
    
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
        
        # 获取所有文档的向量
        results = collection.query(
            expr="doc_id != ''",
            output_fields=["doc_id", "content", "embedding"],
            limit=10
        )
        
        if len(results) >= 2:
            # 提取两个向量
            vec1 = np.array(results[0]['embedding'])
            vec2 = np.array(results[1]['embedding'])
            
            logger.info("=== 向量分析 ===")
            logger.info(f"向量1 L2范数: {np.linalg.norm(vec1):.4f}")
            logger.info(f"向量2 L2范数: {np.linalg.norm(vec2):.4f}")
            
            # 计算L2距离
            l2_distance = np.linalg.norm(vec1 - vec2)
            logger.info(f"两个向量之间的L2距离: {l2_distance:.4f}")
            
            # 计算余弦相似度
            cos_sim = np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))
            logger.info(f"余弦相似度: {cos_sim:.4f}")
            
            # 现在用第一个向量作为查询向量进行搜索
            logger.info("\n=== 使用向量1进行搜索 ===")
            search_params = {"metric_type": "L2", "params": {"nprobe": 10}}
            
            search_results = collection.search(
                data=[vec1.tolist()],
                anns_field="embedding",
                param=search_params,
                limit=3,
                output_fields=["content"]
            )
            
            for i, hit in enumerate(search_results[0]):
                logger.info(f"结果{i+1}: L2距离={hit.distance:.4f}, 内容前30字符={getattr(hit.entity, 'content', '')[:30]}")
            
            # 用零向量搜索
            logger.info("\n=== 使用零向量搜索 ===")
            zero_vec = np.zeros(1536)
            search_results = collection.search(
                data=[zero_vec.tolist()],
                anns_field="embedding",
                param=search_params,
                limit=2,
                output_fields=["content"]
            )
            
            for i, hit in enumerate(search_results[0]):
                logger.info(f"结果{i+1}: L2距离={hit.distance:.4f}")
            
            # 理论计算：零向量到存储向量的L2距离应该等于存储向量的L2范数
            logger.info("\n=== 理论 vs 实际 ===")
            logger.info(f"向量1的L2范数（理论距离）: {np.linalg.norm(vec1):.4f}")
            logger.info(f"零向量到向量1的实际搜索距离: {search_results[0][1].distance if len(search_results[0]) > 1 else 'N/A'}")
            
        else:
            logger.warning("文档数量不足，无法进行距离计算")
        
    except Exception as e:
        logger.error(f"错误: {str(e)}")
        import traceback
        logger.error(traceback.format_exc())
    finally:
        connections.disconnect("default")

if __name__ == "__main__":
    test_vector_distance()