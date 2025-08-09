"""
Search Controller - 搜索控制器
处理向量搜索相关的请求
"""

from typing import List, Dict, Any, Optional
import logging
from fastapi import HTTPException

from app.models.embedding import EmbeddingModel
from app.models.vector_store import VectorStoreModel
from app.views.api.responses import ResponseFormatter

logger = logging.getLogger(__name__)


class SearchController:
    """
    搜索控制器类
    处理向量搜索和相似度查询
    """
    
    def __init__(self):
        """初始化控制器"""
        self.embedding_model = EmbeddingModel()
        self.vector_store = VectorStoreModel()
        self.formatter = ResponseFormatter()
        logger.info("搜索控制器初始化完成")
    
    async def search_similar(self, query: str, top_k: int = 5,
                            filter_expr: Optional[str] = None) -> Dict[str, Any]:
        """
        搜索相似文档
        
        Args:
            query: 查询文本
            top_k: 返回的结果数量
            filter_expr: 过滤表达式
            
        Returns:
            搜索结果
        """
        try:
            # 验证参数
            if not query:
                raise HTTPException(status_code=400, detail="查询文本不能为空")
            
            if top_k < 1 or top_k > 100:
                raise HTTPException(status_code=400, detail="top_k必须在1-100之间")
            
            # 向量化查询
            query_embedding = self.embedding_model.embed_query(query)
            
            # 执行搜索
            results = self.vector_store.search(
                query_embedding=query_embedding,
                top_k=top_k,
                filter_expr=filter_expr
            )
            
            # 格式化结果
            formatted_results = []
            for text, score, metadata in results:
                formatted_results.append({
                    "text": text,
                    "score": float(score),
                    "metadata": metadata
                })
            
            response = {
                "query": query,
                "total_results": len(formatted_results),
                "results": formatted_results
            }
            
            logger.info(f"搜索完成: {query[:50]}... 返回 {len(formatted_results)} 个结果")
            return self.formatter.format_success(response)
            
        except HTTPException:
            raise
        except Exception as e:
            logger.error(f"搜索失败: {e}")
            raise HTTPException(status_code=500, detail=str(e))
    
    async def search_by_metadata(self, metadata_filter: Dict[str, Any],
                                top_k: int = 5) -> Dict[str, Any]:
        """
        按元数据搜索
        
        Args:
            metadata_filter: 元数据过滤条件
            top_k: 返回的结果数量
            
        Returns:
            搜索结果
        """
        try:
            # 构建过滤表达式
            filter_parts = []
            for key, value in metadata_filter.items():
                if isinstance(value, str):
                    filter_parts.append(f'metadata["{key}"] == "{value}"')
                else:
                    filter_parts.append(f'metadata["{key}"] == {value}')
            
            filter_expr = " and ".join(filter_parts) if filter_parts else None
            
            # 执行搜索（使用一个随机向量，因为我们主要依赖过滤）
            import numpy as np
            random_embedding = np.random.rand(self.embedding_model.dimension).tolist()
            
            results = self.vector_store.search(
                query_embedding=random_embedding,
                top_k=top_k,
                filter_expr=filter_expr
            )
            
            # 格式化结果
            formatted_results = []
            for text, score, metadata in results:
                formatted_results.append({
                    "text": text,
                    "metadata": metadata
                })
            
            response = {
                "filter": metadata_filter,
                "total_results": len(formatted_results),
                "results": formatted_results
            }
            
            logger.info(f"元数据搜索完成: 返回 {len(formatted_results)} 个结果")
            return self.formatter.format_success(response)
            
        except Exception as e:
            logger.error(f"元数据搜索失败: {e}")
            raise HTTPException(status_code=500, detail=str(e))
    
    async def get_collection_stats(self) -> Dict[str, Any]:
        """
        获取集合统计信息
        
        Returns:
            统计信息
        """
        try:
            stats = self.vector_store.get_collection_stats()
            
            logger.info("获取集合统计信息成功")
            return self.formatter.format_success(stats)
            
        except Exception as e:
            logger.error(f"获取统计信息失败: {e}")
            raise HTTPException(status_code=500, detail=str(e))
    
    async def clear_collection(self) -> Dict[str, Any]:
        """
        清空集合
        
        Returns:
            操作结果
        """
        try:
            self.vector_store.clear_collection()
            
            result = {
                "message": "集合已清空",
                "collection": self.vector_store.collection_name
            }
            
            logger.info(f"集合已清空: {self.vector_store.collection_name}")
            return self.formatter.format_success(result)
            
        except Exception as e:
            logger.error(f"清空集合失败: {e}")
            raise HTTPException(status_code=500, detail=str(e))
    
    async def test_embedding(self, text: str) -> Dict[str, Any]:
        """
        测试向量化功能
        
        Args:
            text: 测试文本
            
        Returns:
            向量化结果
        """
        try:
            # 生成向量
            embedding = self.embedding_model.embed_text(text)
            
            result = {
                "text": text,
                "dimension": len(embedding),
                "embedding_preview": embedding[:10],  # 只显示前10个值
                "model": self.embedding_model.model_id
            }
            
            logger.info(f"向量化测试成功: {text[:50]}...")
            return self.formatter.format_success(result)
            
        except Exception as e:
            logger.error(f"向量化测试失败: {e}")
            raise HTTPException(status_code=500, detail=str(e))