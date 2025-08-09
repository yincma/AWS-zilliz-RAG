#!/usr/bin/env python3
"""
本地API服务器 - 模拟AWS API Gateway和Lambda函数
用于测试和开发
"""

from fastapi import FastAPI, HTTPException, Request, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional, List, Dict, Any
import json
import os
import boto3
import uuid
from datetime import datetime
import logging
import uvicorn

# 设置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 创建FastAPI应用
app = FastAPI(title="RAG API Local Server")

# 配置CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 在生产环境中应该限制具体的域名
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# AWS客户端
try:
    s3_client = boto3.client('s3')
    bedrock_runtime = boto3.client('bedrock-runtime', region_name='us-east-1')
except Exception as e:
    logger.warning(f"AWS clients initialization failed: {e}")
    s3_client = None
    bedrock_runtime = None

# 配置
S3_BUCKET = 'rag-documents-375004070918-us-east-1'
S3_PREFIX = 'documents/'

# 模拟数据存储
mock_documents = []
mock_stats = {
    'name': 'rag_collection',
    'num_entities': 0,
    'num_documents': 0,
    'dimension': 1024,
    'index_type': 'IVF_FLAT',
    'metric_type': 'L2'
}

# 请求模型
class QueryRequest(BaseModel):
    query: str
    top_k: int = 5
    use_rag: bool = True

class DocumentRequest(BaseModel):
    operation: Optional[str] = 'list'
    file_paths: Optional[List[str]] = []

class UploadRequest(BaseModel):
    filename: str
    content: str
    content_type: str = 'text/plain'
    size: Optional[int] = None


@app.get("/health")
async def health_check():
    """健康检查"""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "service": "RAG API Local Server"
    }


@app.post("/query")
async def query(request: QueryRequest):
    """处理查询请求"""
    try:
        # 模拟RAG查询
        if request.use_rag:
            # 模拟向量搜索结果
            sources = [
                {
                    "content": f"Sample content related to: {request.query[:50]}",
                    "score": 0.85 + i * 0.02,
                    "metadata": {"source": f"document_{i+1}.txt"}
                }
                for i in range(min(request.top_k, 5))
            ]
            
            answer = f"基于文档的回答：{request.query}\n\n这是一个RAG系统的示例回答。"
        else:
            # 直接LLM回答
            sources = []
            answer = f"直接回答：{request.query}\n\n这是一个不使用RAG的示例回答。"
        
        return {
            "answer": answer,
            "sources": sources,
            "model": "nova-pro-v1",
            "timestamp": datetime.now().isoformat()
        }
    except Exception as e:
        logger.error(f"Query error: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/documents")
async def list_documents():
    """列出文档"""
    try:
        if s3_client:
            # 从S3获取真实文档列表
            response = s3_client.list_objects_v2(
                Bucket=S3_BUCKET,
                Prefix=S3_PREFIX,
                MaxKeys=100
            )
            
            documents = []
            if 'Contents' in response:
                for obj in response['Contents']:
                    if not obj['Key'].endswith('/'):
                        documents.append({
                            'name': obj['Key'].replace(S3_PREFIX, ''),
                            'size': obj['Size'],
                            'last_modified': obj['LastModified'].isoformat()
                        })
        else:
            # 使用模拟数据
            documents = mock_documents
        
        return {
            "status": "success",
            "data": documents,
            "count": len(documents)
        }
    except Exception as e:
        logger.error(f"List documents error: {e}")
        # 返回模拟数据而不是错误
        return {
            "status": "success",
            "data": mock_documents,
            "count": len(mock_documents)
        }


@app.post("/documents")
async def document_operations(request: DocumentRequest):
    """文档操作"""
    try:
        if request.operation == 'stats':
            # 返回统计信息
            if s3_client:
                try:
                    response = s3_client.list_objects_v2(
                        Bucket=S3_BUCKET,
                        Prefix=S3_PREFIX
                    )
                    doc_count = len(response.get('Contents', []))
                    mock_stats['num_documents'] = doc_count
                    mock_stats['num_entities'] = doc_count * 10
                except:
                    pass
            
            return {
                "status": "success",
                "data": mock_stats
            }
        
        elif request.operation == 'ingest':
            # 摄入文档
            return {
                "status": "success",
                "message": f"Ingested {len(request.file_paths)} documents",
                "documents": request.file_paths
            }
        
        else:
            # 默认返回文档列表
            return await list_documents()
            
    except Exception as e:
        logger.error(f"Document operation error: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/documents/upload")
async def upload_document(request: UploadRequest):
    """上传文档"""
    try:
        # 添加到模拟文档列表
        doc = {
            "name": request.filename,
            "size": request.size or len(request.content),
            "last_modified": datetime.now().isoformat(),
            "content_type": request.content_type
        }
        mock_documents.append(doc)
        
        # 更新统计
        mock_stats['num_documents'] += 1
        mock_stats['num_entities'] += 10
        
        # 如果有S3客户端，尝试上传到S3
        s3_key = None
        if s3_client and request.content:
            try:
                s3_key = f"{S3_PREFIX}{datetime.now().strftime('%Y/%m/%d')}/{request.filename}"
                s3_client.put_object(
                    Bucket=S3_BUCKET,
                    Key=s3_key,
                    Body=request.content.encode('utf-8'),
                    ContentType=request.content_type,
                    Metadata={
                        'upload_time': datetime.now().isoformat(),
                        'source': 'local_api'
                    }
                )
            except Exception as e:
                logger.warning(f"S3 upload failed: {e}")
        
        return {
            "status": "success",
            "message": "Document uploaded successfully",
            "filename": request.filename,
            "s3_key": s3_key,
            "timestamp": datetime.now().isoformat()
        }
    except Exception as e:
        logger.error(f"Upload error: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.delete("/documents/{filename}")
async def delete_document(filename: str):
    """删除文档"""
    try:
        # 从模拟列表中删除
        global mock_documents
        original_count = len(mock_documents)
        mock_documents = [d for d in mock_documents if d['name'] != filename]
        
        if len(mock_documents) == original_count:
            raise HTTPException(status_code=404, detail=f"Document not found: {filename}")
        
        # 更新统计
        mock_stats['num_documents'] -= 1
        mock_stats['num_entities'] -= 10
        
        return {
            "status": "success",
            "message": f"Document deleted: {filename}"
        }
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Delete error: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.delete("/documents")
async def clear_collection(request: Request):
    """清空集合"""
    try:
        body = await request.json()
        if body.get('operation') == 'clear':
            # 清空模拟数据
            global mock_documents
            deleted_count = len(mock_documents)
            mock_documents = []
            mock_stats['num_documents'] = 0
            mock_stats['num_entities'] = 0
            
            return {
                "status": "success",
                "message": "Collection cleared",
                "deleted_count": deleted_count
            }
        else:
            raise HTTPException(status_code=400, detail="Invalid operation")
    except Exception as e:
        logger.error(f"Clear collection error: {e}")
        raise HTTPException(status_code=500, detail=str(e))


# 添加一些初始模拟数据
mock_documents = [
    {
        "name": "rag_introduction.txt",
        "size": 2048,
        "last_modified": datetime.now().isoformat(),
        "content_type": "text/plain"
    },
    {
        "name": "llm_basics.md",
        "size": 4096,
        "last_modified": datetime.now().isoformat(),
        "content_type": "text/markdown"
    }
]
mock_stats['num_documents'] = len(mock_documents)
mock_stats['num_entities'] = len(mock_documents) * 10


if __name__ == "__main__":
    print("Starting RAG API Local Server...")
    print("Server will run on: http://localhost:8000")
    print("API Documentation: http://localhost:8000/docs")
    print("\nPress Ctrl+C to stop the server")
    
    # 运行服务器
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        log_level="info"
    )