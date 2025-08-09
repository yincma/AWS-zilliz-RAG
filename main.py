"""
Main Application Entry Point
FastAPI应用主入口
"""

import logging
import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
import time
from pathlib import Path

from config.settings import settings
from app.controllers import RAGController, DocumentController, SearchController
from app.views.api.serializers import (
    QueryRequest,
    IngestRequest,
    SearchRequest
)

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# 创建FastAPI应用
app = FastAPI(
    title="AWS Zilliz RAG API",
    description="基于AWS和Zilliz的RAG应用API",
    version="0.1.0"
)

# 配置CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.api.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 初始化控制器
rag_controller = RAGController()
document_controller = DocumentController()
search_controller = SearchController()

# 记录启动时间
start_time = time.time()

# 获取静态文件路径
BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR / "app" / "views" / "web" / "static"
HTML_FILE = BASE_DIR / "app" / "views" / "web" / "index.html"

# 挂载静态文件
app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")


# ============ 健康检查 ============

@app.get("/")
async def root():
    """根路径 - 返回Web界面"""
    return FileResponse(str(HTML_FILE))

@app.get("/api")
async def api_info():
    """API信息"""
    return {
        "message": "AWS Zilliz RAG API",
        "version": "0.1.0",
        "docs": "/docs"
    }


@app.get("/health")
async def health_check():
    """健康检查"""
    uptime = time.time() - start_time
    return {
        "status": "healthy",
        "version": "0.1.0",
        "uptime": uptime,
        "environment": settings.api.env
    }


@app.get("/status")
async def system_status():
    """系统状态"""
    return await rag_controller.get_status()


# ============ RAG接口 ============

@app.post("/api/v1/query")
async def query(request: QueryRequest):
    """
    执行RAG查询
    """
    return await rag_controller.query(request)


@app.post("/api/v1/ingest")
async def ingest_documents(request: IngestRequest):
    """
    摄入文档
    """
    return await rag_controller.ingest_documents(request)


# ============ 文档管理接口 ============

@app.get("/api/v1/documents")
async def list_documents():
    """
    列出所有文档
    """
    return await document_controller.list_documents()


@app.get("/api/v1/documents/{filename}")
async def get_document_info(filename: str):
    """
    获取文档信息
    """
    return await document_controller.get_document_info(filename)


@app.delete("/api/v1/documents/{filename}")
async def delete_document(filename: str):
    """
    删除文档
    """
    return await document_controller.delete_document(filename)


# ============ 搜索接口 ============

@app.post("/api/v1/search")
async def search(request: SearchRequest):
    """
    向量搜索
    """
    if request.query:
        return await search_controller.search_similar(
            query=request.query,
            top_k=request.top_k,
            filter_expr=request.filter_expr
        )
    else:
        raise HTTPException(status_code=400, detail="查询文本不能为空")


@app.get("/api/v1/collection/stats")
async def get_collection_stats():
    """
    获取集合统计信息
    """
    return await search_controller.get_collection_stats()


@app.delete("/api/v1/collection/clear")
async def clear_collection():
    """
    清空集合
    """
    return await search_controller.clear_collection()


# ============ 错误处理 ============

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    """HTTP异常处理"""
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "status": "error",
            "message": exc.detail,
            "error": {
                "code": exc.status_code,
                "message": exc.detail
            }
        }
    )


@app.exception_handler(Exception)
async def general_exception_handler(request, exc):
    """通用异常处理"""
    logger.error(f"未处理的异常: {exc}")
    return JSONResponse(
        status_code=500,
        content={
            "status": "error",
            "message": "内部服务器错误",
            "error": {
                "code": 500,
                "message": str(exc)
            }
        }
    )


# ============ 启动函数 ============

def main():
    """主函数"""
    logger.info(f"启动 RAG API 服务器...")
    logger.info(f"环境: {settings.api.env}")
    logger.info(f"监听地址: {settings.api.host}:{settings.api.port}")
    
    uvicorn.run(
        "main:app",
        host=settings.api.host,
        port=settings.api.port,
        reload=(settings.api.env == "development")
    )


if __name__ == "__main__":
    main()