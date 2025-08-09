"""
RAG Controller - RAG主控制器
协调RAG流程的请求处理
"""

from typing import Dict, Any, List, Optional
import logging
from fastapi import HTTPException

from app.models.rag_chain import RAGChainModel, RAGResponse
from app.views.api.responses import ResponseFormatter
from app.views.api.serializers import (
    QueryRequest,
    QueryResponse,
    IngestRequest,
    IngestResponse
)

logger = logging.getLogger(__name__)


class RAGController:
    """
    RAG控制器类
    处理RAG相关的HTTP请求
    """
    
    def __init__(self):
        """初始化控制器"""
        self.rag_model = RAGChainModel()
        self.formatter = ResponseFormatter()
        logger.info("RAG控制器初始化完成")
    
    async def query(self, request: QueryRequest) -> QueryResponse:
        """
        处理查询请求
        
        Args:
            request: 查询请求对象
            
        Returns:
            查询响应对象
        """
        try:
            # 验证请求
            if not request.query:
                raise HTTPException(status_code=400, detail="查询不能为空")
            
            # 调用Model层处理
            rag_response = self.rag_model.query(
                query=request.query,
                top_k=request.top_k,
                filter_expr=request.filter_expr
            )
            
            # 格式化响应
            response = QueryResponse(
                answer=rag_response.answer,
                sources=rag_response.sources,
                query=rag_response.query,
                confidence=rag_response.confidence
            )
            
            logger.info(f"查询处理成功: {request.query[:50]}...")
            return response
            
        except HTTPException:
            raise
        except Exception as e:
            logger.error(f"查询处理失败: {e}")
            raise HTTPException(status_code=500, detail=str(e))
    
    async def ingest_documents(self, request: IngestRequest) -> IngestResponse:
        """
        处理文档摄入请求
        
        Args:
            request: 摄入请求对象
            
        Returns:
            摄入响应对象
        """
        try:
            # 验证请求
            if not request.file_paths:
                raise HTTPException(status_code=400, detail="文件路径列表不能为空")
            
            # 调用Model层处理
            result = self.rag_model.ingest_documents(request.file_paths)
            
            if result["status"] == "error":
                raise HTTPException(status_code=500, detail=result.get("message"))
            
            # 格式化响应
            response = IngestResponse(
                status=result["status"],
                files_processed=result.get("files_processed", 0),
                chunks_created=result.get("chunks_created", 0),
                vectors_stored=result.get("vectors_stored", 0),
                document_ids=result.get("document_ids", [])
            )
            
            logger.info(f"文档摄入成功: {response.files_processed} 个文件")
            return response
            
        except HTTPException:
            raise
        except Exception as e:
            logger.error(f"文档摄入失败: {e}")
            raise HTTPException(status_code=500, detail=str(e))
    
    async def get_status(self) -> Dict[str, Any]:
        """
        获取系统状态
        
        Returns:
            系统状态信息
        """
        try:
            # 获取统计信息
            stats = self.rag_model.get_stats()
            
            # 测试系统连接
            test_results = self.rag_model.test_system()
            
            # 组合响应
            status = {
                "status": "healthy" if all(test_results.values()) else "degraded",
                "components": test_results,
                "statistics": stats
            }
            
            return self.formatter.format_success(status)
            
        except Exception as e:
            logger.error(f"获取状态失败: {e}")
            return self.formatter.format_error(str(e))
    
    async def delete_documents(self, doc_ids: List[int]) -> Dict[str, Any]:
        """
        删除文档
        
        Args:
            doc_ids: 文档ID列表
            
        Returns:
            删除结果
        """
        try:
            if not doc_ids:
                raise HTTPException(status_code=400, detail="文档ID列表不能为空")
            
            # 调用Model层处理
            success = self.rag_model.delete_document(doc_ids)
            
            if success:
                return self.formatter.format_success({
                    "deleted": len(doc_ids),
                    "document_ids": doc_ids
                })
            else:
                raise HTTPException(status_code=500, detail="删除文档失败")
                
        except HTTPException:
            raise
        except Exception as e:
            logger.error(f"删除文档失败: {e}")
            raise HTTPException(status_code=500, detail=str(e))
    
    async def stream_query(self, query: str):
        """
        流式查询（SSE）
        
        Args:
            query: 查询文本
            
        Yields:
            流式响应
        """
        try:
            # 这里可以实现流式响应逻辑
            # 目前简化处理，直接返回完整响应
            response = await self.query(QueryRequest(query=query))
            
            # 模拟流式输出
            words = response.answer.split()
            for word in words:
                yield f"data: {word} \n\n"
            
            yield "data: [DONE]\n\n"
            
        except Exception as e:
            logger.error(f"流式查询失败: {e}")
            yield f"data: ERROR: {str(e)}\n\n"