"""
RAG Chain Model - RAG链模型
整合文档处理、向量化、存储、检索和生成的完整RAG流程
"""

from typing import List, Dict, Any, Optional, Tuple
import logging
from dataclasses import dataclass

from app.models.document import DocumentModel
from app.models.embedding import EmbeddingModel
from app.models.vector_store import VectorStoreModel
from app.models.llm import LLMModel

logger = logging.getLogger(__name__)


@dataclass
class RAGResponse:
    """RAG响应数据类"""
    answer: str
    sources: List[Dict[str, Any]]
    query: str
    confidence: float = 0.0


class RAGChainModel:
    """
    RAG链模型类
    整合完整的RAG流程
    """
    
    def __init__(self, collection_name: Optional[str] = None, s3_bucket: Optional[str] = None):
        """初始化RAG链
        
        Args:
            collection_name: Zilliz集合名称
            s3_bucket: S3存储桶名称
        """
        from config.settings import settings
        
        self.s3_bucket = s3_bucket or settings.aws.s3_bucket
        self.document_model = DocumentModel(s3_bucket=self.s3_bucket)
        self.embedding_model = EmbeddingModel()
        self.vector_store = VectorStoreModel(collection_name=collection_name)
        self.llm_model = LLMModel()
        
        logger.info("RAG链初始化完成")
    
    def ingest_documents(self, file_paths: List[str]) -> Dict[str, Any]:
        """
        摄入文档：加载、分割、向量化、存储
        
        Args:
            file_paths: 文档路径列表
            
        Returns:
            摄入结果统计
        """
        try:
            # 1. 处理文档（加载和分割）
            logger.info("开始处理文档...")
            chunks = self.document_model.process_documents(file_paths)
            
            if not chunks:
                return {
                    "status": "error",
                    "message": "没有可处理的文档"
                }
            
            # 2. 提取文本和元数据
            texts = [chunk.page_content for chunk in chunks]
            metadatas = [chunk.metadata for chunk in chunks]
            
            # 3. 生成向量
            logger.info(f"开始向量化 {len(texts)} 个文本块...")
            embeddings = self.embedding_model.embed_texts(texts)
            
            # 4. 存储到向量数据库
            logger.info("存储向量到Zilliz...")
            doc_ids = self.vector_store.insert_documents(
                texts=texts,
                embeddings=embeddings,
                metadatas=metadatas
            )
            
            # 5. 返回统计信息
            result = {
                "status": "success",
                "files_processed": len(file_paths),
                "chunks_created": len(chunks),
                "vectors_stored": len(doc_ids),
                "document_ids": doc_ids
            }
            
            logger.info(f"文档摄入完成: {result}")
            return result
            
        except Exception as e:
            logger.error(f"文档摄入失败: {e}")
            return {
                "status": "error",
                "message": str(e)
            }
    
    def query(self, query: str, top_k: int = 5, 
             filter_expr: Optional[str] = None) -> RAGResponse:
        """
        执行RAG查询
        
        Args:
            query: 用户查询
            top_k: 返回的文档数量
            filter_expr: 过滤表达式
            
        Returns:
            RAG响应
        """
        try:
            # 1. 向量化查询
            logger.info(f"处理查询: {query}")
            query_embedding = self.embedding_model.embed_query(query)
            
            # 2. 检索相关文档
            logger.info("检索相关文档...")
            search_results = self.vector_store.search(
                query_embedding=query_embedding,
                top_k=top_k,
                filter_expr=filter_expr
            )
            
            if not search_results:
                return RAGResponse(
                    answer="抱歉，没有找到相关信息。",
                    sources=[],
                    query=query,
                    confidence=0.0
                )
            
            # 3. 构建上下文
            context_parts = []
            sources = []
            
            for text, score, metadata in search_results:
                context_parts.append(text)
                sources.append({
                    "text": text[:200] + "..." if len(text) > 200 else text,
                    "score": float(score),
                    "metadata": metadata
                })
            
            context = "\n\n".join(context_parts)
            
            # 4. 生成答案
            logger.info("生成答案...")
            answer = self.llm_model.generate_with_context(
                query=query,
                context=context
            )
            
            # 5. 计算置信度（基于检索分数）
            avg_score = sum(s[1] for s in search_results) / len(search_results)
            confidence = min(avg_score / 100, 1.0)  # 归一化到0-1
            
            return RAGResponse(
                answer=answer,
                sources=sources,
                query=query,
                confidence=confidence
            )
            
        except Exception as e:
            logger.error(f"查询处理失败: {e}")
            return RAGResponse(
                answer=f"处理查询时发生错误: {str(e)}",
                sources=[],
                query=query,
                confidence=0.0
            )
    
    def update_document(self, file_path: str) -> Dict[str, Any]:
        """
        更新单个文档
        
        Args:
            file_path: 文档路径
            
        Returns:
            更新结果
        """
        # 这里可以实现删除旧版本并添加新版本的逻辑
        return self.ingest_documents([file_path])
    
    def delete_document(self, doc_ids: List[int]) -> bool:
        """
        删除文档
        
        Args:
            doc_ids: 文档ID列表
            
        Returns:
            是否成功
        """
        return self.vector_store.delete_documents(doc_ids)
    
    def get_stats(self) -> Dict[str, Any]:
        """
        获取RAG系统统计信息
        
        Returns:
            统计信息
        """
        stats = {
            "vector_store": self.vector_store.get_collection_stats(),
            "embedding_model": self.embedding_model.model_id,
            "llm_model": self.llm_model.model_id,
            "chunk_size": self.document_model.chunk_size,
            "chunk_overlap": self.document_model.chunk_overlap
        }
        return stats
    
    def test_system(self) -> Dict[str, bool]:
        """
        测试系统各组件连接
        
        Returns:
            各组件测试结果
        """
        results = {
            "embedding_model": False,
            "llm_model": False,
            "vector_store": False
        }
        
        try:
            results["embedding_model"] = self.embedding_model.test_connection()
        except Exception as e:
            logger.error(f"Embedding模型测试失败: {e}")
        
        try:
            results["llm_model"] = self.llm_model.test_connection()
        except Exception as e:
            logger.error(f"LLM模型测试失败: {e}")
        
        try:
            results["vector_store"] = bool(self.vector_store.get_collection_stats())
        except Exception as e:
            logger.error(f"向量存储测试失败: {e}")
        
        return results
    
    def ingest_s3_documents(self, s3_keys: List[str]) -> Dict[str, Any]:
        """
        从S3摄入文档
        
        Args:
            s3_keys: S3对象键列表
            
        Returns:
            摄入结果统计
        """
        try:
            # 1. 处理S3文档
            logger.info(f"开始处理S3文档: {s3_keys}")
            chunks = self.document_model.process_s3_documents(s3_keys)
            
            if not chunks:
                return {
                    "status": "error",
                    "message": "没有可处理的文档"
                }
            
            # 2. 提取文本和元数据
            texts = [chunk.page_content for chunk in chunks]
            metadatas = [chunk.metadata for chunk in chunks]
            
            # 3. 生成向量
            logger.info(f"开始向量化 {len(texts)} 个文本块...")
            embeddings = self.embedding_model.embed_texts(texts)
            
            # 4. 存储到向量数据库
            logger.info("存储向量到Zilliz...")
            doc_ids = self.vector_store.insert_documents(
                texts=texts,
                embeddings=embeddings,
                metadatas=metadatas
            )
            
            # 5. 返回统计信息
            result = {
                "status": "success",
                "s3_keys_processed": len(s3_keys),
                "chunks_created": len(chunks),
                "vectors_stored": len(doc_ids),
                "document_ids": doc_ids
            }
            
            logger.info(f"S3文档摄入完成: {result}")
            return result
            
        except Exception as e:
            logger.error(f"S3文档摄入失败: {e}")
            return {
                "status": "error",
                "message": str(e)
            }