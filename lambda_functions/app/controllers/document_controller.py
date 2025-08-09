"""
Document Controller - 文档管理控制器
处理文档的上传、删除、更新等操作
"""

from typing import List, Dict, Any, Optional
import logging
from pathlib import Path
from fastapi import HTTPException, UploadFile, File

from app.models.document import DocumentModel
from app.views.api.responses import ResponseFormatter

logger = logging.getLogger(__name__)


class DocumentController:
    """
    文档管理控制器类
    """
    
    def __init__(self):
        """初始化控制器"""
        self.document_model = DocumentModel()
        self.formatter = ResponseFormatter()
        self.upload_dir = Path("uploads")
        self.upload_dir.mkdir(exist_ok=True)
        logger.info("文档控制器初始化完成")
    
    async def upload_document(self, file: UploadFile = File(...)) -> Dict[str, Any]:
        """
        处理文档上传
        
        Args:
            file: 上传的文件
            
        Returns:
            上传结果
        """
        try:
            # 验证文件类型
            allowed_types = ['.pdf', '.txt', '.md']
            file_ext = Path(file.filename).suffix.lower()
            
            if file_ext not in allowed_types:
                raise HTTPException(
                    status_code=400,
                    detail=f"不支持的文件类型: {file_ext}。支持的类型: {allowed_types}"
                )
            
            # 保存文件
            file_path = self.upload_dir / file.filename
            content = await file.read()
            file_path.write_bytes(content)
            
            # 处理文档
            document = self.document_model.load_document(str(file_path))
            
            # 返回结果
            result = {
                "filename": file.filename,
                "file_path": str(file_path),
                "content_length": len(document.content),
                "metadata": document.metadata
            }
            
            logger.info(f"文档上传成功: {file.filename}")
            return self.formatter.format_success(result)
            
        except HTTPException:
            raise
        except Exception as e:
            logger.error(f"文档上传失败: {e}")
            raise HTTPException(status_code=500, detail=str(e))
    
    async def process_document(self, file_path: str) -> Dict[str, Any]:
        """
        处理单个文档
        
        Args:
            file_path: 文档路径
            
        Returns:
            处理结果
        """
        try:
            # 加载文档
            document = self.document_model.load_document(file_path)
            
            # 分割文档
            chunks = self.document_model.split_document(document)
            
            # 返回结果
            result = {
                "file_path": file_path,
                "total_chunks": len(chunks),
                "chunk_size": self.document_model.chunk_size,
                "chunk_overlap": self.document_model.chunk_overlap,
                "metadata": document.metadata
            }
            
            logger.info(f"文档处理成功: {file_path}")
            return self.formatter.format_success(result)
            
        except Exception as e:
            logger.error(f"文档处理失败: {e}")
            raise HTTPException(status_code=500, detail=str(e))
    
    async def list_documents(self) -> Dict[str, Any]:
        """
        列出所有已上传的文档
        
        Returns:
            文档列表
        """
        try:
            documents = []
            
            for file_path in self.upload_dir.glob("*"):
                if file_path.is_file():
                    documents.append({
                        "filename": file_path.name,
                        "file_path": str(file_path),
                        "size": file_path.stat().st_size,
                        "modified": file_path.stat().st_mtime
                    })
            
            result = {
                "total": len(documents),
                "documents": documents
            }
            
            return self.formatter.format_success(result)
            
        except Exception as e:
            logger.error(f"列出文档失败: {e}")
            raise HTTPException(status_code=500, detail=str(e))
    
    async def delete_document(self, filename: str) -> Dict[str, Any]:
        """
        删除文档
        
        Args:
            filename: 文件名
            
        Returns:
            删除结果
        """
        try:
            file_path = self.upload_dir / filename
            
            if not file_path.exists():
                raise HTTPException(status_code=404, detail=f"文档不存在: {filename}")
            
            # 删除文件
            file_path.unlink()
            
            result = {
                "deleted": filename,
                "message": "文档删除成功"
            }
            
            logger.info(f"文档删除成功: {filename}")
            return self.formatter.format_success(result)
            
        except HTTPException:
            raise
        except Exception as e:
            logger.error(f"文档删除失败: {e}")
            raise HTTPException(status_code=500, detail=str(e))
    
    async def get_document_info(self, filename: str) -> Dict[str, Any]:
        """
        获取文档信息
        
        Args:
            filename: 文件名
            
        Returns:
            文档信息
        """
        try:
            file_path = self.upload_dir / filename
            
            if not file_path.exists():
                raise HTTPException(status_code=404, detail=f"文档不存在: {filename}")
            
            # 加载文档获取详细信息
            document = self.document_model.load_document(str(file_path))
            
            # 分割文档获取块信息
            chunks = self.document_model.split_document(document)
            
            result = {
                "filename": filename,
                "file_path": str(file_path),
                "size": file_path.stat().st_size,
                "content_length": len(document.content),
                "total_chunks": len(chunks),
                "metadata": document.metadata,
                "preview": document.content[:500] + "..." if len(document.content) > 500 else document.content
            }
            
            return self.formatter.format_success(result)
            
        except HTTPException:
            raise
        except Exception as e:
            logger.error(f"获取文档信息失败: {e}")
            raise HTTPException(status_code=500, detail=str(e))