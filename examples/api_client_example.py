"""
RAG API客户端示例
展示如何使用Python调用RAG API
"""

import httpx
import asyncio
from pathlib import Path


class RAGClient:
    """RAG API客户端"""
    
    def __init__(self, base_url="http://localhost:8000"):
        self.base_url = base_url
        self.client = httpx.AsyncClient(timeout=30.0)
    
    async def health_check(self):
        """健康检查"""
        response = await self.client.get(f"{self.base_url}/health")
        return response.json()
    
    async def ingest_documents(self, file_paths):
        """摄入文档"""
        response = await self.client.post(
            f"{self.base_url}/api/v1/ingest",
            json={"file_paths": file_paths}
        )
        return response.json()
    
    async def query(self, question, top_k=5):
        """查询问题"""
        response = await self.client.post(
            f"{self.base_url}/api/v1/query",
            json={"query": question, "top_k": top_k}
        )
        return response.json()
    
    async def search(self, query, top_k=5):
        """向量搜索"""
        response = await self.client.post(
            f"{self.base_url}/api/v1/search",
            json={"query": query, "top_k": top_k}
        )
        return response.json()
    
    async def get_stats(self):
        """获取统计信息"""
        response = await self.client.get(
            f"{self.base_url}/api/v1/collection/stats"
        )
        return response.json()
    
    async def close(self):
        """关闭客户端"""
        await self.client.aclose()


async def example_usage():
    """示例用法"""
    
    # 创建客户端
    client = RAGClient()
    
    try:
        # 1. 健康检查
        print("1. 健康检查")
        health = await client.health_check()
        print(f"   状态: {health['status']}")
        print(f"   版本: {health['version']}")
        print()
        
        # 2. 摄入文档
        print("2. 摄入文档")
        # 确保sample_docs目录存在
        sample_dir = Path("sample_docs")
        if sample_dir.exists():
            files = [str(f) for f in sample_dir.glob("*.txt")]
            if files:
                result = await client.ingest_documents(files)
                print(f"   状态: {result.get('status', 'unknown')}")
                print(f"   处理文件数: {result.get('files_processed', 0)}")
                print(f"   创建文本块: {result.get('chunks_created', 0)}")
            else:
                print("   没有找到文档文件")
        print()
        
        # 3. 查询问题
        print("3. 查询问题")
        questions = [
            "什么是RAG？",
            "RAG有哪些优势？",
            "RAG的工作原理是什么？"
        ]
        
        for question in questions:
            print(f"\n   问题: {question}")
            result = await client.query(question, top_k=3)
            
            if 'answer' in result:
                answer = result['answer']
                if len(answer) > 200:
                    answer = answer[:200] + "..."
                print(f"   答案: {answer}")
                
                if 'confidence' in result:
                    print(f"   置信度: {result['confidence']:.2%}")
                
                if 'sources' in result:
                    print(f"   引用源: {len(result['sources'])} 个")
        
        print()
        
        # 4. 向量搜索
        print("4. 向量搜索")
        search_result = await client.search("RAG技术", top_k=3)
        
        if 'data' in search_result and 'results' in search_result['data']:
            results = search_result['data']['results']
            print(f"   找到 {len(results)} 个相关文档")
            for i, doc in enumerate(results[:3], 1):
                content = doc.get('content', '')[:50]
                score = doc.get('score', 0.0)
                print(f"   {i}. {content}... (相似度: {score:.4f})")
        
        print()
        
        # 5. 获取统计信息
        print("5. 系统统计")
        stats = await client.get_stats()
        
        if 'data' in stats:
            data = stats['data']
            print(f"   集合名称: {data.get('name', 'unknown')}")
            print(f"   文档数量: {data.get('num_entities', 0)}")
            print(f"   向量维度: {data.get('dimension', 0)}")
        
    finally:
        # 关闭客户端
        await client.close()


async def interactive_mode():
    """交互式模式"""
    
    client = RAGClient()
    
    print("=" * 50)
    print("RAG API 交互式客户端")
    print("=" * 50)
    print("输入 'quit' 退出")
    print("输入 'help' 查看帮助")
    print()
    
    try:
        while True:
            question = input("请输入问题: ").strip()
            
            if question.lower() == 'quit':
                break
            
            if question.lower() == 'help':
                print("\n可用命令:")
                print("  quit - 退出程序")
                print("  help - 显示帮助")
                print("  stats - 显示统计信息")
                print("  其他输入将作为问题进行查询\n")
                continue
            
            if question.lower() == 'stats':
                stats = await client.get_stats()
                if 'data' in stats:
                    data = stats['data']
                    print(f"\n系统统计:")
                    print(f"  集合: {data.get('name', 'unknown')}")
                    print(f"  文档数: {data.get('num_entities', 0)}")
                    print(f"  维度: {data.get('dimension', 0)}\n")
                continue
            
            if question:
                print("\n查询中...")
                result = await client.query(question)
                
                if 'answer' in result:
                    print(f"\n答案: {result['answer']}")
                    
                    if 'confidence' in result:
                        print(f"置信度: {result['confidence']:.2%}")
                    
                    if 'sources' in result and result['sources']:
                        print(f"\n引用源 ({len(result['sources'])} 个):")
                        for i, source in enumerate(result['sources'][:3], 1):
                            text = source.get('text', '')[:100]
                            score = source.get('score', 0.0)
                            print(f"  {i}. {text}... (相似度: {score:.4f})")
                else:
                    print("无法生成答案")
                
                print()
    
    finally:
        await client.close()
        print("\n再见！")


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "interactive":
        # 交互式模式
        asyncio.run(interactive_mode())
    else:
        # 示例模式
        asyncio.run(example_usage())