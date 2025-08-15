"""
Embedding Model - 向量化模型
使用Amazon Titan Embeddings处理文本向量化
"""

from typing import List, Optional
import json
import logging
import boto3
from botocore.exceptions import ClientError

from config.settings import settings

logger = logging.getLogger(__name__)


class EmbeddingModel:
    """
    Embedding模型类
    使用Amazon Bedrock的Titan Embeddings模型
    """
    
    def __init__(self, model_id: Optional[str] = None):
        """
        初始化Embedding模型
        
        Args:
            model_id: Bedrock模型ID，默认使用配置中的值
        """
        self.model_id = model_id or settings.aws.embedding_model_id
        self.dimension = 1024  # Titan Embedding v2的维度
        
        # 初始化Bedrock客户端
        self.bedrock_client = boto3.client(
            'bedrock-runtime',
            region_name=settings.aws.region,
            aws_access_key_id=settings.aws.access_key_id,
            aws_secret_access_key=settings.aws.secret_access_key
        )
        
        logger.info(f"初始化Embedding模型: {self.model_id}")
    
    def embed_text(self, text: str) -> List[float]:
        """
        将单个文本转换为向量
        
        Args:
            text: 输入文本
            
        Returns:
            向量列表
        """
        try:
            # 准备请求体
            request_body = {
                "inputText": text
            }
            
            # 调用Bedrock API
            response = self.bedrock_client.invoke_model(
                modelId=self.model_id,
                body=json.dumps(request_body),
                contentType='application/json',
                accept='application/json'
            )
            
            # 解析响应
            response_body = json.loads(response['body'].read())
            embedding = response_body.get('embedding', [])
            
            if not embedding:
                raise ValueError("Embedding响应为空")
            
            return embedding
            
        except ClientError as e:
            logger.error(f"Bedrock API调用失败: {e}")
            raise
        except Exception as e:
            logger.error(f"生成embedding失败: {e}")
            raise
    
    def embed_texts(self, texts: List[str], batch_size: int = 10) -> List[List[float]]:
        """
        批量将文本转换为向量
        
        Args:
            texts: 文本列表
            batch_size: 批处理大小（Titan可能有限制）
            
        Returns:
            向量列表
        """
        embeddings = []
        total = len(texts)
        
        for i in range(0, total, batch_size):
            batch = texts[i:i + batch_size]
            batch_embeddings = []
            
            for text in batch:
                try:
                    embedding = self.embed_text(text)
                    batch_embeddings.append(embedding)
                except Exception as e:
                    logger.error(f"处理文本失败: {text[:50]}... 错误: {e}")
                    # 使用零向量作为失败的后备
                    batch_embeddings.append([0.0] * self.dimension)
            
            embeddings.extend(batch_embeddings)
            logger.info(f"已处理 {min(i + batch_size, total)}/{total} 个文本")
        
        return embeddings
    
    def embed_documents(self, documents: List[str]) -> List[List[float]]:
        """
        将文档列表转换为向量（LangChain兼容接口）
        
        Args:
            documents: 文档文本列表
            
        Returns:
            向量列表
        """
        return self.embed_texts(documents)
    
    def embed_query(self, query: str) -> List[float]:
        """
        将查询文本转换为向量（LangChain兼容接口）
        
        Args:
            query: 查询文本
            
        Returns:
            向量
        """
        return self.embed_text(query)
    
    def get_dimension(self) -> int:
        """
        获取向量维度
        
        Returns:
            向量维度
        """
        return self.dimension
    
    def test_connection(self) -> bool:
        """
        测试与Bedrock的连接
        
        Returns:
            连接是否成功
        """
        try:
            test_text = "Test connection"
            embedding = self.embed_text(test_text)
            return len(embedding) == self.dimension
        except Exception as e:
            logger.error(f"连接测试失败: {e}")
            return False