"""
Document Model - 文档处理模型
负责文档的加载、解析、分割等操作
支持PDF、TXT、Markdown格式，支持S3存储
"""

from typing import List, Dict, Any, Optional
from pathlib import Path
from dataclasses import dataclass
import logging
import hashlib
import tempfile
import boto3
from botocore.exceptions import ClientError

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader, TextLoader, UnstructuredMarkdownLoader
from langchain.schema import Document as LangchainDocument

logger = logging.getLogger(__name__)


@dataclass
class Document:
    """文档数据类"""
    content: str
    metadata: Dict[str, Any]
    doc_id: Optional[str] = None
    chunks: Optional[List[str]] = None


class DocumentModel:
    """
    文档模型类
    处理文档的加载、解析、分割等业务逻辑
    """
    
    def __init__(self, chunk_size: int = 1000, chunk_overlap: int = 200, s3_bucket: Optional[str] = None):
        """
        初始化文档模型
        
        Args:
            chunk_size: 文本块大小
            chunk_overlap: 文本块重叠大小
            s3_bucket: S3存储桶名称
        """
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.s3_bucket = s3_bucket
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            length_function=len,
            separators=["\n\n", "\n", "。", "！", "？", "；", "，", " ", ""]
        )
        
        # 初始化S3客户端
        if s3_bucket:
            self.s3_client = boto3.client('s3')
        else:
            self.s3_client = None
    
    def load_document(self, file_path: str) -> Document:
        """
        加载单个文档
        
        Args:
            file_path: 文档路径
            
        Returns:
            Document对象
        """
        path = Path(file_path)
        if not path.exists():
            raise FileNotFoundError(f"文档不存在: {file_path}")
        
        # 根据文件类型选择加载器
        if path.suffix.lower() == '.pdf':
            loader = PyPDFLoader(str(path))
        elif path.suffix.lower() in ['.txt', '.text']:
            loader = TextLoader(str(path), encoding='utf-8')
        elif path.suffix.lower() in ['.md', '.markdown']:
            loader = UnstructuredMarkdownLoader(str(path))
        else:
            raise ValueError(f"不支持的文件类型: {path.suffix}")
        
        # 加载文档
        documents = loader.load()
        
        # 合并所有页面内容
        content = "\n".join([doc.page_content for doc in documents])
        
        # 构建元数据
        metadata = {
            "source": str(path),
            "file_name": path.name,
            "file_type": path.suffix,
            "total_pages": len(documents)
        }
        
        # 如果有额外的元数据，合并进来
        if documents and documents[0].metadata:
            metadata.update(documents[0].metadata)
        
        return Document(
            content=content,
            metadata=metadata
        )
    
    def load_documents(self, file_paths: List[str]) -> List[Document]:
        """
        批量加载文档
        
        Args:
            file_paths: 文档路径列表
            
        Returns:
            Document对象列表
        """
        documents = []
        for file_path in file_paths:
            try:
                doc = self.load_document(file_path)
                documents.append(doc)
                logger.info(f"成功加载文档: {file_path}")
            except Exception as e:
                logger.error(f"加载文档失败 {file_path}: {e}")
        
        return documents
    
    def split_document(self, document: Document) -> List[LangchainDocument]:
        """
        将文档分割成文本块
        
        Args:
            document: Document对象
            
        Returns:
            LangChain Document对象列表
        """
        # 使用文本分割器分割内容
        texts = self.text_splitter.split_text(document.content)
        
        # 创建LangChain文档对象
        chunks = []
        for i, text in enumerate(texts):
            chunk_metadata = document.metadata.copy()
            chunk_metadata["chunk_id"] = self.generate_chunk_id(document.metadata.get('source', ''), i)
            chunk_metadata["chunk_index"] = i
            chunk_metadata["chunk_total"] = len(texts)
            
            chunks.append(LangchainDocument(
                page_content=text,
                metadata=chunk_metadata
            ))
        
        # 更新原始文档的chunks
        document.chunks = texts
        
        return chunks
    
    def process_documents(self, file_paths: List[str]) -> List[LangchainDocument]:
        """
        处理文档的完整流程：加载并分割
        
        Args:
            file_paths: 文档路径列表
            
        Returns:
            所有文档的文本块列表
        """
        all_chunks = []
        documents = self.load_documents(file_paths)
        
        for doc in documents:
            chunks = self.split_document(doc)
            all_chunks.extend(chunks)
            logger.info(f"文档 {doc.metadata['file_name']} 被分割成 {len(chunks)} 个文本块")
        
        return all_chunks
    
    def load_from_s3(self, s3_key: str) -> Document:
        """
        从S3加载文档
        
        Args:
            s3_key: S3对象键
            
        Returns:
            Document对象
        """
        if not self.s3_client or not self.s3_bucket:
            raise ValueError("S3 client not configured")
        
        try:
            # 下载文件到临时目录
            with tempfile.NamedTemporaryFile(suffix=Path(s3_key).suffix, delete=False) as tmp_file:
                self.s3_client.download_fileobj(
                    self.s3_bucket,
                    s3_key,
                    tmp_file
                )
                tmp_path = tmp_file.name
            
            # 加载文档
            document = self.load_document(tmp_path)
            
            # 添加S3元数据
            document.metadata['s3_key'] = s3_key
            document.metadata['s3_bucket'] = self.s3_bucket
            
            # 清理临时文件
            Path(tmp_path).unlink()
            
            return document
            
        except ClientError as e:
            logger.error(f"Failed to load document from S3: {e}")
            raise
    
    def process_s3_documents(self, s3_keys: List[str]) -> List[LangchainDocument]:
        """
        处理S3中的文档
        
        Args:
            s3_keys: S3对象键列表
            
        Returns:
            所有文档的文本块列表
        """
        all_chunks = []
        
        for s3_key in s3_keys:
            try:
                doc = self.load_from_s3(s3_key)
                chunks = self.split_document(doc)
                all_chunks.extend(chunks)
                logger.info(f"S3文档 {s3_key} 被分割成 {len(chunks)} 个文本块")
            except Exception as e:
                logger.error(f"处理S3文档失败 {s3_key}: {e}")
        
        return all_chunks
    
    def generate_chunk_id(self, source: str, chunk_index: int) -> str:
        """
        生成唯一的文本块ID
        
        Args:
            source: 文档来源
            chunk_index: 块索引
            
        Returns:
            唯一ID
        """
        content = f"{source}:{chunk_index}"
        return hashlib.md5(content.encode()).hexdigest()[:16]