"""
端到端RAG测试
测试完整的RAG流程：文档摄入 -> 查询 -> 生成答案
"""

import logging
from pathlib import Path
from app.models.rag_chain import RAGChainModel

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def test_rag_e2e():
    """测试完整的RAG流程"""
    
    print("=" * 50)
    print("RAG 端到端测试")
    print("=" * 50)
    
    # 1. 初始化RAG链
    print("\n1. 初始化RAG系统...")
    rag = RAGChainModel()
    
    # 2. 测试系统连接
    print("\n2. 测试系统组件...")
    test_results = rag.test_system()
    for component, status in test_results.items():
        status_icon = "✅" if status else "❌"
        print(f"   {status_icon} {component}: {'正常' if status else '失败'}")
    
    if not all(test_results.values()):
        print("\n⚠️ 警告：部分组件未正常工作，测试可能失败")
    
    # 3. 摄入示例文档
    print("\n3. 摄入示例文档...")
    sample_doc_path = "sample_docs/rag_intro.txt"
    
    if not Path(sample_doc_path).exists():
        print(f"   ❌ 示例文档不存在: {sample_doc_path}")
        print("   请先创建示例文档")
        return
    
    result = rag.ingest_documents([sample_doc_path])
    
    if result["status"] == "success":
        print(f"   ✅ 文档摄入成功:")
        print(f"      - 处理文件数: {result['files_processed']}")
        print(f"      - 创建文本块: {result['chunks_created']}")
        print(f"      - 存储向量数: {result['vectors_stored']}")
    else:
        print(f"   ❌ 文档摄入失败: {result.get('message')}")
        return
    
    # 4. 测试查询
    print("\n4. 测试RAG查询...")
    
    test_queries = [
        "什么是RAG？",
        "RAG有哪些优势？",
        "RAG的工作原理是什么？",
        "RAG可以应用在哪些场景？"
    ]
    
    for query in test_queries:
        print(f"\n   查询: {query}")
        response = rag.query(query, top_k=3)
        
        if response.answer:
            print(f"   答案: {response.answer[:200]}...")
            print(f"   置信度: {response.confidence:.2f}")
            print(f"   引用源: {len(response.sources)} 个文档块")
        else:
            print(f"   ❌ 无法生成答案")
    
    # 5. 获取系统统计
    print("\n5. 系统统计信息...")
    stats = rag.get_stats()
    print(f"   向量存储:")
    print(f"      - 集合名称: {stats['vector_store']['name']}")
    print(f"      - 实体数量: {stats['vector_store']['num_entities']}")
    print(f"      - 向量维度: {stats['vector_store']['dimension']}")
    print(f"   模型配置:")
    print(f"      - Embedding: {stats['embedding_model']}")
    print(f"      - LLM: {stats['llm_model']}")
    
    print("\n" + "=" * 50)
    print("测试完成!")
    print("=" * 50)


def cleanup_collection():
    """清理测试数据"""
    print("\n清理测试数据...")
    rag = RAGChainModel()
    rag.vector_store.clear_collection()
    print("✅ 集合已清空")


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "cleanup":
        cleanup_collection()
    else:
        test_rag_e2e()
        
        # 询问是否清理
        response = input("\n是否清理测试数据？(y/n): ")
        if response.lower() == 'y':
            cleanup_collection()