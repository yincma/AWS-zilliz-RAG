"""
Vector Store Model - 向量存储模型
使用Zilliz Cloud进行向量存储和检索
"""

from typing import List, Dict, Any, Optional, Tuple
import logging
from pymilvus import (
    connections,
    Collection,
    CollectionSchema,
    FieldSchema,
    DataType,
    utility
)

from config.settings import settings

logger = logging.getLogger(__name__)


class VectorStoreModel:
    """
    向量存储模型类
    使用Zilliz Cloud存储和检索向量
    """
    
    def __init__(self, collection_name: Optional[str] = None):
        """
        初始化向量存储模型
        
        Args:
            collection_name: 集合名称，默认使用配置中的值
        """
        self.collection_name = collection_name or settings.zilliz.collection
        self.dimension = settings.zilliz.dimension
        self.collection = None
        
        # 连接到Zilliz
        self._connect()
        
        # 初始化或加载集合
        self._init_collection()
    
    def _connect(self):
        """连接到Zilliz Cloud"""
        try:
            connections.connect(
                alias="default",
                uri=settings.zilliz.endpoint,
                token=settings.zilliz.token
            )
            logger.info("成功连接到Zilliz Cloud")
        except Exception as e:
            logger.error(f"连接Zilliz失败: {e}")
            raise
    
    def _init_collection(self):
        """初始化或加载集合"""
        try:
            if utility.has_collection(self.collection_name):
                self.collection = Collection(self.collection_name)
                logger.info(f"加载已存在的集合: {self.collection_name}")
            else:
                self._create_collection()
                logger.info(f"创建新集合: {self.collection_name}")
            
            # 加载集合到内存
            self.collection.load()
            
        except Exception as e:
            logger.error(f"初始化集合失败: {e}")
            raise
    
    def _create_collection(self):
        """创建新的集合"""
        # 定义字段
        fields = [
            FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=True),
            FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=self.dimension),
            FieldSchema(name="text", dtype=DataType.VARCHAR, max_length=65535),
            FieldSchema(name="metadata", dtype=DataType.JSON)
        ]
        
        # 创建schema
        schema = CollectionSchema(
            fields=fields,
            description="RAG文档向量集合"
        )
        
        # 创建集合
        self.collection = Collection(
            name=self.collection_name,
            schema=schema
        )
        
        # 创建索引
        index_params = {
            "metric_type": settings.zilliz.metric_type,
            "index_type": settings.zilliz.index_type,
            "params": {"nlist": settings.zilliz.nlist}
        }
        
        self.collection.create_index(
            field_name="embedding",
            index_params=index_params
        )
    
    def insert_documents(self, texts: List[str], embeddings: List[List[float]], 
                        metadatas: Optional[List[Dict[str, Any]]] = None) -> List[int]:
        """
        插入文档到向量存储
        
        Args:
            texts: 文本列表
            embeddings: 向量列表
            metadatas: 元数据列表
            
        Returns:
            插入的文档ID列表
        """
        if not metadatas:
            metadatas = [{}] * len(texts)
        
        # 准备插入数据
        # Milvus需要列表格式，每个列表对应一个字段
        data = [
            embeddings,  # embedding字段
            texts,       # text字段
            metadatas    # metadata字段
        ]
        
        try:
            # 插入数据
            result = self.collection.insert(data)
            
            # 刷新以确保数据持久化
            self.collection.flush()
            
            logger.info(f"成功插入 {len(texts)} 个文档")
            return result.primary_keys
            
        except Exception as e:
            logger.error(f"插入文档失败: {e}")
            raise
    
    def search(self, query_embedding: List[float], top_k: int = 5,
              filter_expr: Optional[str] = None) -> List[Tuple[str, float, Dict]]:
        """
        搜索相似文档
        
        Args:
            query_embedding: 查询向量
            top_k: 返回的文档数量
            filter_expr: 过滤表达式
            
        Returns:
            [(文本, 分数, 元数据), ...]
        """
        # 搜索参数
        search_params = {
            "metric_type": settings.zilliz.metric_type,
            "params": {"nprobe": 10}
        }
        
        try:
            # 执行搜索
            results = self.collection.search(
                data=[query_embedding],
                anns_field="embedding",
                param=search_params,
                limit=top_k,
                expr=filter_expr,
                output_fields=["text", "metadata"]
            )
            
            # 处理结果
            documents = []
            for hits in results:
                for hit in hits:
                    # Milvus返回的entity可能是dict或object
                    text = hit.entity.get("text") if isinstance(hit.entity, dict) else getattr(hit.entity, "text", "")
                    metadata = hit.entity.get("metadata", {}) if isinstance(hit.entity, dict) else getattr(hit.entity, "metadata", {})
                    documents.append((text, hit.score, metadata))
            
            logger.info(f"搜索返回 {len(documents)} 个结果")
            return documents
            
        except Exception as e:
            logger.error(f"搜索失败: {e}")
            raise
    
    def delete_documents(self, doc_ids: List[int]) -> bool:
        """
        删除文档
        
        Args:
            doc_ids: 文档ID列表
            
        Returns:
            是否成功
        """
        try:
            expr = f"id in {doc_ids}"
            self.collection.delete(expr)
            logger.info(f"删除 {len(doc_ids)} 个文档")
            return True
        except Exception as e:
            logger.error(f"删除文档失败: {e}")
            return False
    
    def get_collection_stats(self) -> Dict[str, Any]:
        """
        获取集合统计信息
        
        Returns:
            统计信息字典
        """
        try:
            stats = {
                "name": self.collection_name,
                "num_entities": self.collection.num_entities,
                "dimension": self.dimension,
                "index_type": settings.zilliz.index_type,
                "metric_type": settings.zilliz.metric_type
            }
            return stats
        except Exception as e:
            logger.error(f"获取统计信息失败: {e}")
            return {}
    
    def clear_collection(self):
        """清空集合"""
        try:
            self.collection.release()
            utility.drop_collection(self.collection_name)
            logger.info(f"已清空集合: {self.collection_name}")
            
            # 重新初始化集合
            self._init_collection()
            
        except Exception as e:
            logger.error(f"清空集合失败: {e}")
            raise
    
    def disconnect(self):
        """断开连接"""
        try:
            connections.disconnect("default")
            logger.info("已断开Zilliz连接")
        except Exception as e:
            logger.error(f"断开连接失败: {e}")