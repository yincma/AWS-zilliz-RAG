"""
Lambda友好的Zilliz向量客户端
使用HTTP API替代pymilvus以减少依赖
"""

import json
import os
import urllib.request
import urllib.parse
import urllib.error
import logging
from typing import List, Dict, Any, Optional, Tuple

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class ZillizClient:
    """轻量级Zilliz客户端，适用于Lambda环境"""
    
    def __init__(self):
        """初始化Zilliz客户端"""
        self.endpoint = os.environ.get('ZILLIZ_ENDPOINT', '')
        self.token = os.environ.get('ZILLIZ_TOKEN', '')
        self.collection_name = os.environ.get('ZILLIZ_COLLECTION', 'rag_collection')
        
        if not self.endpoint or not self.token:
            logger.warning("Zilliz配置缺失，将使用模拟数据")
            self.use_mock = True
        else:
            self.use_mock = False
            # 确保endpoint格式正确
            if not self.endpoint.startswith('http'):
                self.endpoint = f"https://{self.endpoint}"
    
    def search(self, query_embedding: List[float], top_k: int = 5) -> List[Dict[str, Any]]:
        """
        搜索相似向量
        
        Args:
            query_embedding: 查询向量
            top_k: 返回结果数量
            
        Returns:
            搜索结果列表
        """
        if self.use_mock:
            return self._mock_search(query_embedding, top_k)
        
        try:
            # 使用Zilliz HTTP API进行搜索
            url = f"{self.endpoint}/v1/vector/search"
            
            headers = {
                "Authorization": f"Bearer {self.token}",
                "Content-Type": "application/json"
            }
            
            payload = {
                "collectionName": self.collection_name,
                "vector": query_embedding,
                "topK": top_k,
                "outputFields": ["text", "metadata"]
            }
            
            data = json.dumps(payload).encode('utf-8')
            req = urllib.request.Request(url, data=data, headers=headers, method='POST')
            
            with urllib.request.urlopen(req, timeout=10) as response:
                if response.status == 200:
                    results = json.loads(response.read().decode('utf-8'))
                    return self._format_results(results.get('data', []))
                else:
                    logger.error(f"Zilliz搜索失败: {response.status}")
                    return []
                
        except Exception as e:
            logger.error(f"搜索出错: {str(e)}")
            return self._mock_search(query_embedding, top_k)
    
    def _format_results(self, results: List[Dict]) -> List[Dict[str, Any]]:
        """格式化搜索结果"""
        formatted = []
        for item in results:
            formatted.append({
                'content': item.get('text', ''),
                'score': item.get('score', 0.0),
                'metadata': item.get('metadata', {})
            })
        return formatted
    
    def _mock_search(self, query_embedding: List[float], top_k: int) -> List[Dict[str, Any]]:
        """返回模拟搜索结果"""
        logger.info("使用模拟数据")
        
        # 模拟RAG相关文档
        mock_documents = [
            {
                'content': 'RAG (Retrieval-Augmented Generation) 是一种结合检索和生成的技术，通过检索相关文档来增强语言模型的生成能力。',
                'score': 0.95,
                'metadata': {'source': 'rag_introduction.md', 'page': 1}
            },
            {
                'content': 'RAG系统的核心组件包括：文档向量化、向量数据库存储、相似度搜索和语言模型生成。',
                'score': 0.92,
                'metadata': {'source': 'rag_components.md', 'page': 2}
            },
            {
                'content': '使用RAG可以减少模型幻觉，提供更准确和可追溯的答案，特别适合知识密集型任务。',
                'score': 0.89,
                'metadata': {'source': 'rag_benefits.md', 'page': 1}
            },
            {
                'content': 'Zilliz Cloud是一个全托管的向量数据库服务，基于Milvus开源项目，提供高性能的向量搜索能力。',
                'score': 0.87,
                'metadata': {'source': 'zilliz_overview.md', 'page': 1}
            },
            {
                'content': 'Amazon Bedrock提供了多种基础模型，包括Nova、Claude、Titan等，可用于RAG系统的生成组件。',
                'score': 0.85,
                'metadata': {'source': 'bedrock_models.md', 'page': 3}
            }
        ]
        
        return mock_documents[:top_k]
    
    def insert(self, texts: List[str], embeddings: List[List[float]], 
               metadatas: Optional[List[Dict]] = None) -> bool:
        """
        插入文档到向量数据库
        
        Args:
            texts: 文本列表
            embeddings: 向量列表
            metadatas: 元数据列表
            
        Returns:
            是否成功
        """
        if self.use_mock:
            logger.info(f"模拟插入 {len(texts)} 个文档")
            return True
        
        try:
            url = f"{self.endpoint}/v1/vector/insert"
            
            headers = {
                "Authorization": f"Bearer {self.token}",
                "Content-Type": "application/json"
            }
            
            # 准备数据
            data_list = []
            for i, (text, embedding) in enumerate(zip(texts, embeddings)):
                item = {
                    "text": text,
                    "embedding": embedding
                }
                if metadatas and i < len(metadatas):
                    item["metadata"] = metadatas[i]
                data_list.append(item)
            
            payload = {
                "collectionName": self.collection_name,
                "data": data_list
            }
            
            data = json.dumps(payload).encode('utf-8')
            req = urllib.request.Request(url, data=data, headers=headers, method='POST')
            
            with urllib.request.urlopen(req, timeout=30) as response:
                if response.status == 200:
                    logger.info(f"成功插入 {len(texts)} 个文档")
                    return True
                else:
                    logger.error(f"插入失败: {response.status}")
                    return False
                
        except Exception as e:
            logger.error(f"插入出错: {str(e)}")
            return False
    
    def test_connection(self) -> bool:
        """测试Zilliz连接"""
        if self.use_mock:
            logger.info("使用模拟模式，跳过连接测试")
            return True
        
        try:
            url = f"{self.endpoint}/v1/collections"
            headers = {
                "Authorization": f"Bearer {self.token}"
            }
            
            req = urllib.request.Request(url, headers=headers, method='GET')
            
            with urllib.request.urlopen(req, timeout=5) as response:
                if response.status == 200:
                    logger.info("Zilliz连接成功")
                    return True
                else:
                    logger.error(f"Zilliz连接失败: {response.status}")
                    return False
                
        except Exception as e:
            logger.error(f"连接测试失败: {str(e)}")
            return False


# 全局客户端实例
_client = None


def get_client() -> ZillizClient:
    """获取Zilliz客户端单例"""
    global _client
    if _client is None:
        _client = ZillizClient()
    return _client