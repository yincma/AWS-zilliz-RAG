"""
API Response Formatter - API响应格式化器
统一的API响应格式
"""

from typing import Any, Dict, Optional, List
from datetime import datetime
import json


class ResponseFormatter:
    """
    响应格式化器类
    提供统一的API响应格式
    """
    
    @staticmethod
    def format_success(data: Any, message: str = "Success") -> Dict[str, Any]:
        """
        格式化成功响应
        
        Args:
            data: 响应数据
            message: 成功消息
            
        Returns:
            格式化的响应字典
        """
        return {
            "status": "success",
            "message": message,
            "data": data,
            "timestamp": datetime.utcnow().isoformat(),
            "error": None
        }
    
    @staticmethod
    def format_error(error: str, status_code: int = 500,
                    details: Optional[Dict] = None) -> Dict[str, Any]:
        """
        格式化错误响应
        
        Args:
            error: 错误消息
            status_code: HTTP状态码
            details: 额外的错误详情
            
        Returns:
            格式化的错误响应
        """
        return {
            "status": "error",
            "message": error,
            "data": None,
            "timestamp": datetime.utcnow().isoformat(),
            "error": {
                "code": status_code,
                "message": error,
                "details": details
            }
        }
    
    @staticmethod
    def format_paginated(data: List[Any], page: int, page_size: int,
                        total: int) -> Dict[str, Any]:
        """
        格式化分页响应
        
        Args:
            data: 数据列表
            page: 当前页码
            page_size: 每页大小
            total: 总数
            
        Returns:
            格式化的分页响应
        """
        total_pages = (total + page_size - 1) // page_size
        
        return {
            "status": "success",
            "data": data,
            "pagination": {
                "page": page,
                "page_size": page_size,
                "total": total,
                "total_pages": total_pages,
                "has_next": page < total_pages,
                "has_prev": page > 1
            },
            "timestamp": datetime.utcnow().isoformat()
        }
    
    @staticmethod
    def format_rag_response(answer: str, sources: List[Dict],
                           confidence: float) -> Dict[str, Any]:
        """
        格式化RAG响应
        
        Args:
            answer: 生成的答案
            sources: 引用的源文档
            confidence: 置信度分数
            
        Returns:
            格式化的RAG响应
        """
        return {
            "status": "success",
            "data": {
                "answer": answer,
                "sources": sources,
                "confidence": confidence,
                "sources_count": len(sources)
            },
            "metadata": {
                "model": "Amazon Bedrock Nova",
                "retrieval_method": "vector_similarity",
                "timestamp": datetime.utcnow().isoformat()
            }
        }
    
    @staticmethod
    def format_stream_chunk(content: str, is_final: bool = False) -> str:
        """
        格式化流式响应块
        
        Args:
            content: 内容块
            is_final: 是否是最后一个块
            
        Returns:
            SSE格式的字符串
        """
        if is_final:
            return "data: [DONE]\n\n"
        
        chunk = {
            "content": content,
            "timestamp": datetime.utcnow().isoformat()
        }
        return f"data: {json.dumps(chunk)}\n\n"
    
    @staticmethod
    def format_validation_error(errors: Dict[str, List[str]]) -> Dict[str, Any]:
        """
        格式化验证错误
        
        Args:
            errors: 字段错误字典
            
        Returns:
            格式化的验证错误响应
        """
        return {
            "status": "error",
            "message": "Validation failed",
            "data": None,
            "timestamp": datetime.utcnow().isoformat(),
            "error": {
                "code": 400,
                "message": "Validation failed",
                "validation_errors": errors
            }
        }