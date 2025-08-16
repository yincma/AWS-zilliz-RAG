#!/usr/bin/env python3
"""
测试脚本：验证Zilliz返回的hit对象是否包含distance属性
"""
import os
import logging
from pymilvus import connections, Collection
import numpy as np

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def test_zilliz_distance():
    """测试Zilliz返回的distance值"""
    
    # 连接配置
    endpoint = os.environ.get('ZILLIZ_ENDPOINT', 'in01-e5e8bb97fc4c1e8.serverless.gcp-us-west1.cloud.zilliz.com')
    token = os.environ.get('ZILLIZ_TOKEN', '')
    
    if not token:
        logger.error("请设置ZILLIZ_TOKEN环境变量")
        return
    
    # 连接Zilliz
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
        
        # 获取collection
        collection_name = 'rag_collection'
        collection = Collection(collection_name)
        collection.load()
        logger.info(f"✅ 加载collection: {collection_name}")
        
        # 创建一个随机向量进行搜索
        query_vector = np.random.rand(1536).tolist()
        
        # 搜索参数
        search_params = {"metric_type": "L2", "params": {"nprobe": 10}}
        
        # 执行搜索
        results = collection.search(
            data=[query_vector],
            anns_field="embedding",
            param=search_params,
            limit=3,
            output_fields=["content", "metadata"]
        )
        
        logger.info(f"搜索返回 {len(results[0])} 个结果")
        
        # 检查每个hit的属性
        for i, hit in enumerate(results[0]):
            logger.info(f"\n--- Hit {i+1} ---")
            logger.info(f"Hit类型: {type(hit)}")
            logger.info(f"Hit属性: {dir(hit)}")
            
            # 尝试获取distance
            if hasattr(hit, 'distance'):
                logger.info(f"✅ distance属性存在: {hit.distance}")
            else:
                logger.info(f"❌ distance属性不存在")
            
            # 尝试其他可能的属性名
            possible_attrs = ['distance', 'score', 'dist', '_distance', '_score']
            for attr in possible_attrs:
                if hasattr(hit, attr):
                    value = getattr(hit, attr)
                    logger.info(f"  {attr}: {value}")
            
            # 检查entity
            logger.info(f"Entity类型: {type(hit.entity)}")
            if isinstance(hit.entity, dict):
                logger.info(f"Entity keys: {hit.entity.keys()}")
            
            # 打印完整的hit对象
            logger.info(f"Hit对象字符串表示: {hit}")
            
    except Exception as e:
        logger.error(f"错误: {str(e)}")
        import traceback
        logger.error(traceback.format_exc())
    finally:
        connections.disconnect("default")

if __name__ == "__main__":
    test_zilliz_distance()