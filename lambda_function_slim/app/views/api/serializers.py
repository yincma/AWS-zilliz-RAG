"""
API Serializers - 数据序列化器
使用Pydantic进行请求和响应的数据验证和序列化
"""

from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field, validator
from datetime import datetime


# ============ 查询相关 ============

class QueryRequest(BaseModel):
    """查询请求模型"""
    query: str = Field(..., min_length=1, max_length=1000, description="查询文本")
    top_k: int = Field(default=5, ge=1, le=50, description="返回的文档数量")
    filter_expr: Optional[str] = Field(default=None, description="过滤表达式")
    
    @validator('query')
    def validate_query(cls, v):
        """验证查询文本"""
        v = v.strip()
        if not v:
            raise ValueError("查询文本不能为空")
        return v


class QueryResponse(BaseModel):
    """查询响应模型"""
    answer: str = Field(..., description="生成的答案")
    sources: List[Dict[str, Any]] = Field(default_factory=list, description="引用的源文档")
    query: str = Field(..., description="原始查询")
    confidence: float = Field(default=0.0, ge=0.0, le=1.0, description="置信度分数")
    
    class Config:
        schema_extra = {
            "example": {
                "answer": "根据文档内容，答案是...",
                "sources": [
                    {
                        "text": "相关文本片段",
                        "score": 0.95,
                        "metadata": {"source": "document.pdf", "page": 1}
                    }
                ],
                "query": "什么是RAG？",
                "confidence": 0.85
            }
        }


# ============ 文档摄入相关 ============

class IngestRequest(BaseModel):
    """文档摄入请求模型"""
    file_paths: List[str] = Field(..., min_items=1, description="文档路径列表")
    chunk_size: Optional[int] = Field(default=1000, ge=100, le=5000, description="文本块大小")
    chunk_overlap: Optional[int] = Field(default=200, ge=0, le=1000, description="文本块重叠")
    
    @validator('file_paths')
    def validate_paths(cls, v):
        """验证文件路径"""
        if not v:
            raise ValueError("文件路径列表不能为空")
        return v


class IngestResponse(BaseModel):
    """文档摄入响应模型"""
    status: str = Field(..., description="状态")
    files_processed: int = Field(..., ge=0, description="处理的文件数")
    chunks_created: int = Field(..., ge=0, description="创建的文本块数")
    vectors_stored: int = Field(..., ge=0, description="存储的向量数")
    document_ids: List[int] = Field(default_factory=list, description="文档ID列表")


# ============ 文档管理相关 ============

class DocumentInfo(BaseModel):
    """文档信息模型"""
    filename: str = Field(..., description="文件名")
    file_path: str = Field(..., description="文件路径")
    size: int = Field(..., ge=0, description="文件大小（字节）")
    content_length: int = Field(..., ge=0, description="内容长度")
    total_chunks: int = Field(..., ge=0, description="文本块总数")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="元数据")
    created_at: Optional[datetime] = Field(default=None, description="创建时间")
    updated_at: Optional[datetime] = Field(default=None, description="更新时间")


class DocumentListResponse(BaseModel):
    """文档列表响应模型"""
    total: int = Field(..., ge=0, description="文档总数")
    documents: List[DocumentInfo] = Field(default_factory=list, description="文档列表")


# ============ 搜索相关 ============

class SearchRequest(BaseModel):
    """搜索请求模型"""
    query: Optional[str] = Field(default=None, description="查询文本")
    embedding: Optional[List[float]] = Field(default=None, description="查询向量")
    top_k: int = Field(default=5, ge=1, le=100, description="返回结果数")
    filter_expr: Optional[str] = Field(default=None, description="过滤表达式")
    
    @validator('query')
    def validate_search_input(cls, v, values):
        """验证搜索输入"""
        if not v and not values.get('embedding'):
            raise ValueError("必须提供查询文本或查询向量")
        return v


class SearchResult(BaseModel):
    """搜索结果模型"""
    text: str = Field(..., description="文本内容")
    score: float = Field(..., description="相似度分数")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="元数据")


class SearchResponse(BaseModel):
    """搜索响应模型"""
    query: Optional[str] = Field(default=None, description="查询文本")
    total_results: int = Field(..., ge=0, description="结果总数")
    results: List[SearchResult] = Field(default_factory=list, description="搜索结果")


# ============ 系统状态相关 ============

class SystemStatus(BaseModel):
    """系统状态模型"""
    status: str = Field(..., description="系统状态")
    components: Dict[str, bool] = Field(default_factory=dict, description="组件状态")
    statistics: Dict[str, Any] = Field(default_factory=dict, description="统计信息")
    timestamp: datetime = Field(default_factory=datetime.utcnow, description="时间戳")


class HealthCheckResponse(BaseModel):
    """健康检查响应模型"""
    status: str = Field(..., description="健康状态")
    version: str = Field(..., description="版本号")
    uptime: float = Field(..., ge=0, description="运行时间（秒）")
    checks: Dict[str, bool] = Field(default_factory=dict, description="检查项")


# ============ 错误响应 ============

class ErrorDetail(BaseModel):
    """错误详情模型"""
    code: int = Field(..., description="错误代码")
    message: str = Field(..., description="错误消息")
    details: Optional[Dict[str, Any]] = Field(default=None, description="详细信息")


class ErrorResponse(BaseModel):
    """错误响应模型"""
    status: str = Field(default="error", description="状态")
    message: str = Field(..., description="错误消息")
    error: ErrorDetail = Field(..., description="错误详情")
    timestamp: datetime = Field(default_factory=datetime.utcnow, description="时间戳")