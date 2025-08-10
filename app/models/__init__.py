"""
Model层 - 数据和业务逻辑
处理所有数据相关操作、业务逻辑、与外部服务交互
"""

# 延迟导入，避免在Lambda中导入不需要的依赖
__all__ = [
    "DocumentModel",
    "EmbeddingModel", 
    "VectorStoreModel",
    "LLMModel",
    "RAGChainModel"
]

def __getattr__(name):
    """延迟导入机制"""
    if name == "DocumentModel":
        from .document import DocumentModel
        return DocumentModel
    elif name == "EmbeddingModel":
        from .embedding import EmbeddingModel
        return EmbeddingModel
    elif name == "VectorStoreModel":
        from .vector_store import VectorStoreModel
        return VectorStoreModel
    elif name == "LLMModel":
        from .llm import LLMModel
        return LLMModel
    elif name == "RAGChainModel":
        from .rag_chain import RAGChainModel
        return RAGChainModel
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")