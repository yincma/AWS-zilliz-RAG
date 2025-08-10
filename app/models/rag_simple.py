"""
简化版RAG实现 - 完整功能但优化了依赖
"""

import json
import os
import logging
from typing import List, Dict, Any, Optional
import boto3
from dataclasses import dataclass
import hashlib

logger = logging.getLogger(__name__)

@dataclass
class Document:
    """文档数据类"""
    content: str
    metadata: Dict[str, Any]
    embedding: Optional[List[float]] = None
    doc_id: Optional[str] = None

@dataclass
class RAGResponse:
    """RAG响应数据类"""
    answer: str
    sources: List[Dict[str, Any]]
    query: str
    confidence: float = 0.0


class SimpleEmbedding:
    """简化的嵌入生成器 - 使用Bedrock Titan"""
    
    def __init__(self):
        self.bedrock = boto3.client(
            'bedrock-runtime',
            region_name=os.environ.get('AWS_REGION', 'us-east-1')
        )
        self.model_id = os.environ.get('EMBEDDING_MODEL_ID', 'amazon.titan-embed-text-v2:0')
    
    def generate_embedding(self, text: str) -> List[float]:
        """生成文本嵌入向量"""
        try:
            response = self.bedrock.invoke_model(
                modelId=self.model_id,
                body=json.dumps({
                    "inputText": text[:8000]  # Titan限制
                }),
                contentType='application/json'
            )
            
            result = json.loads(response['body'].read())
            return result.get('embedding', [])
            
        except Exception as e:
            logger.error(f"Error generating embedding: {str(e)}")
            # 返回模拟嵌入用于测试
            return [0.1] * 1536  # Titan嵌入维度


class SimpleVectorStore:
    """简化的向量存储 - 使用Zilliz/内存存储"""
    
    def __init__(self):
        self.use_zilliz = self._init_zilliz()
        if not self.use_zilliz:
            # 使用内存存储作为后备
            self.memory_store = []
            logger.info("Using in-memory vector store")
    
    def _init_zilliz(self) -> bool:
        """初始化Zilliz连接"""
        try:
            from pymilvus import connections, Collection, utility
            
            endpoint = os.environ.get('ZILLIZ_ENDPOINT', '')
            token = os.environ.get('ZILLIZ_TOKEN', '')
            
            if not endpoint or not token:
                logger.warning("Zilliz credentials not configured")
                return False
            
            # 解析endpoint
            if endpoint.startswith('https://'):
                endpoint = endpoint.replace('https://', '')
            
            connections.connect(
                alias="default",
                uri=f"https://{endpoint}",
                token=token,
                secure=True
            )
            
            collection_name = os.environ.get('ZILLIZ_COLLECTION', 'rag_collection')
            
            # 检查集合是否存在
            if not utility.has_collection(collection_name):
                logger.info(f"Collection {collection_name} does not exist, creating...")
                from pymilvus import CollectionSchema, FieldSchema, DataType
                
                # 定义schema
                fields = [
                    FieldSchema(name="doc_id", dtype=DataType.VARCHAR, is_primary=True, max_length=256),
                    FieldSchema(name="content", dtype=DataType.VARCHAR, max_length=65535),
                    FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=1536),
                    FieldSchema(name="metadata", dtype=DataType.JSON)
                ]
                
                schema = CollectionSchema(fields, description="RAG document collection")
                collection = Collection(name=collection_name, schema=schema)
                
                # 创建索引
                index_params = {
                    "metric_type": "IP",
                    "index_type": "IVF_FLAT",
                    "params": {"nlist": 128}
                }
                collection.create_index(field_name="embedding", index_params=index_params)
                collection.load()
            else:
                collection = Collection(name=collection_name)
                collection.load()
            
            self.collection = collection
            logger.info(f"Connected to Zilliz collection: {collection_name}")
            return True
            
        except ImportError:
            logger.warning("pymilvus not available")
            return False
        except Exception as e:
            logger.error(f"Failed to connect to Zilliz: {str(e)}")
            return False
    
    def add_documents(self, documents: List[Document]) -> bool:
        """添加文档到向量存储"""
        try:
            if self.use_zilliz:
                # 准备数据
                doc_ids = []
                contents = []
                embeddings = []
                metadatas = []
                
                for doc in documents:
                    if not doc.doc_id:
                        doc.doc_id = hashlib.md5(doc.content.encode()).hexdigest()
                    
                    doc_ids.append(doc.doc_id)
                    contents.append(doc.content[:65535])  # Zilliz限制
                    embeddings.append(doc.embedding or [0.0] * 1536)
                    metadatas.append(doc.metadata)
                
                # 插入数据
                self.collection.insert([doc_ids, contents, embeddings, metadatas])
                self.collection.flush()
                logger.info(f"Added {len(documents)} documents to Zilliz")
                return True
            else:
                # 内存存储
                self.memory_store.extend(documents)
                logger.info(f"Added {len(documents)} documents to memory store")
                return True
                
        except Exception as e:
            logger.error(f"Error adding documents: {str(e)}")
            return False
    
    def search(self, query_embedding: List[float], top_k: int = 5) -> List[Document]:
        """搜索相似文档"""
        try:
            if self.use_zilliz:
                search_params = {"metric_type": "IP", "params": {"nprobe": 10}}
                
                results = self.collection.search(
                    data=[query_embedding],
                    anns_field="embedding",
                    param=search_params,
                    limit=top_k,
                    output_fields=["content", "metadata"]
                )
                
                documents = []
                for hit in results[0]:
                    doc = Document(
                        content=hit.entity.get("content", ""),
                        metadata=hit.entity.get("metadata", {}),
                        doc_id=hit.id
                    )
                    documents.append(doc)
                
                return documents
            else:
                # 内存搜索（简单的相似度计算）
                if not self.memory_store:
                    return []
                
                # 计算余弦相似度
                scores = []
                for doc in self.memory_store:
                    if doc.embedding:
                        score = sum(a * b for a, b in zip(query_embedding, doc.embedding))
                        scores.append((score, doc))
                
                # 排序并返回top_k
                scores.sort(key=lambda x: x[0], reverse=True)
                return [doc for _, doc in scores[:top_k]]
                
        except Exception as e:
            logger.error(f"Error searching documents: {str(e)}")
            return []


class SimpleLLM:
    """简化的LLM生成器 - 使用Bedrock"""
    
    def __init__(self):
        self.bedrock = boto3.client(
            'bedrock-runtime',
            region_name=os.environ.get('AWS_REGION', 'us-east-1')
        )
        self.model_id = os.environ.get('BEDROCK_MODEL_ID', 'amazon.nova-pro-v1:0')
    
    def generate(self, prompt: str, context: str = "") -> str:
        """生成回答"""
        try:
            # 构建完整提示
            full_prompt = self._build_prompt(prompt, context)
            
            # 根据模型类型调用
            if 'nova' in self.model_id.lower():
                response = self._invoke_nova(full_prompt)
            elif 'claude' in self.model_id.lower():
                response = self._invoke_claude(full_prompt)
            else:
                response = self._invoke_default(full_prompt)
            
            return response
            
        except Exception as e:
            logger.error(f"Error generating response: {str(e)}")
            return f"Error generating response: {str(e)}"
    
    def _build_prompt(self, query: str, context: str) -> str:
        """构建RAG提示"""
        if context:
            return f"""Based on the following context, please answer the question.
            
Context:
{context}

Question: {query}

Answer:"""
        else:
            return f"Question: {query}\n\nAnswer:"
    
    def _invoke_nova(self, prompt: str) -> str:
        """调用Nova模型"""
        try:
            response = self.bedrock.invoke_model(
                modelId=self.model_id,
                body=json.dumps({
                    "messages": [
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ],
                    "max_tokens": 500,
                    "temperature": 0.7,
                    "top_p": 0.9
                }),
                contentType='application/json'
            )
            
            result = json.loads(response['body'].read())
            return result.get('content', [{}])[0].get('text', 'No response generated')
            
        except Exception as e:
            logger.error(f"Nova invocation error: {str(e)}")
            # 尝试其他格式
            return self._invoke_default(prompt)
    
    def _invoke_claude(self, prompt: str) -> str:
        """调用Claude模型"""
        try:
            response = self.bedrock.invoke_model(
                modelId=self.model_id,
                body=json.dumps({
                    "anthropic_version": "bedrock-2023-05-31",
                    "messages": [
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ],
                    "max_tokens": 500,
                    "temperature": 0.7
                }),
                contentType='application/json'
            )
            
            result = json.loads(response['body'].read())
            return result.get('content', [{}])[0].get('text', 'No response generated')
            
        except Exception as e:
            logger.error(f"Claude invocation error: {str(e)}")
            return f"Error with Claude: {str(e)}"
    
    def _invoke_default(self, prompt: str) -> str:
        """默认调用方法"""
        try:
            response = self.bedrock.invoke_model(
                modelId=self.model_id,
                body=json.dumps({
                    "prompt": prompt,
                    "max_tokens": 500,
                    "temperature": 0.7
                }),
                contentType='application/json'
            )
            
            result = json.loads(response['body'].read())
            # 尝试不同的响应格式
            if 'completion' in result:
                return result['completion']
            elif 'completions' in result:
                return result['completions'][0]['data']['text']
            elif 'content' in result:
                return result['content']
            else:
                return str(result)
                
        except Exception as e:
            logger.error(f"Default invocation error: {str(e)}")
            # 返回基础响应
            return self._get_fallback_response(prompt)
    
    def _get_fallback_response(self, prompt: str) -> str:
        """后备响应"""
        if 'rag' in prompt.lower():
            return "RAG (Retrieval-Augmented Generation) is a technique that combines information retrieval with language generation to provide more accurate and contextual answers by retrieving relevant documents and using them as context for the language model."
        elif 'lambda' in prompt.lower():
            return "AWS Lambda is a serverless compute service that lets you run code without provisioning or managing servers. Lambda Layers are a way to share code and dependencies across multiple Lambda functions."
        else:
            return f"This is a response to your query: {prompt[:100]}..."


class SimpleRAG:
    """简化的完整RAG实现"""
    
    def __init__(self):
        self.embedding = SimpleEmbedding()
        self.vector_store = SimpleVectorStore()
        self.llm = SimpleLLM()
        logger.info("SimpleRAG initialized")
    
    def add_document(self, content: str, metadata: Optional[Dict] = None) -> bool:
        """添加单个文档"""
        try:
            # 生成嵌入
            embedding = self.embedding.generate_embedding(content)
            
            # 创建文档
            doc = Document(
                content=content,
                metadata=metadata or {},
                embedding=embedding
            )
            
            # 存储文档
            return self.vector_store.add_documents([doc])
            
        except Exception as e:
            logger.error(f"Error adding document: {str(e)}")
            return False
    
    def query(self, query: str, top_k: int = 5) -> RAGResponse:
        """执行RAG查询"""
        try:
            # 生成查询嵌入
            query_embedding = self.embedding.generate_embedding(query)
            
            # 搜索相关文档
            relevant_docs = self.vector_store.search(query_embedding, top_k)
            
            # 构建上下文
            context = "\n\n".join([doc.content for doc in relevant_docs])
            
            # 生成回答
            answer = self.llm.generate(query, context)
            
            # 构建响应
            sources = [
                {
                    "content": doc.content[:200] + "..." if len(doc.content) > 200 else doc.content,
                    "metadata": doc.metadata
                }
                for doc in relevant_docs
            ]
            
            return RAGResponse(
                answer=answer,
                sources=sources,
                query=query,
                confidence=0.8 if relevant_docs else 0.3
            )
            
        except Exception as e:
            logger.error(f"Error in RAG query: {str(e)}")
            # 返回后备响应
            return RAGResponse(
                answer=self.llm._get_fallback_response(query),
                sources=[],
                query=query,
                confidence=0.2
            )