"""
测试更新后的Lambda RAG功能
"""

import json
import requests
import time

# API端点
API_URL = "https://abbrw64qve.execute-api.us-east-1.amazonaws.com/prod"


def test_health_check():
    """测试健康检查端点"""
    print("测试健康检查端点...")
    
    response = requests.get(f"{API_URL}/health")
    
    if response.status_code == 200:
        print("✅ 健康检查通过")
        return True
    else:
        print(f"❌ 健康检查失败: {response.status_code}")
        return False


def test_query_endpoint(query, use_rag=True):
    """测试查询端点"""
    print("\n测试查询端点...")
    print(f"查询: {query}")
    print(f"使用RAG: {use_rag}")
    
    payload = {
        "query": query,
        "use_rag": use_rag,
        "top_k": 5
    }
    
    headers = {
        "Content-Type": "application/json"
    }
    
    start_time = time.time()
    
    try:
        response = requests.post(
            f"{API_URL}/query",
            json=payload,
            headers=headers,
            timeout=30
        )
        
        elapsed_time = time.time() - start_time
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ 查询成功 (耗时: {elapsed_time:.2f}秒)")
            print(f"\n回答:")
            print(data.get('answer', 'No answer'))
            
            if data.get('sources'):
                print(f"\n相关文档:")
                for i, source in enumerate(data['sources'][:3], 1):
                    print(f"{i}. {source.get('content', '')[:100]}...")
                    print(f"   分数: {source.get('score', 0):.2f}")
            
            print(f"\n模式: {data.get('mode', 'unknown')}")
            return True
        else:
            print(f"❌ 查询失败: {response.status_code}")
            print(f"响应: {response.text}")
            return False
            
    except requests.Timeout:
        print("❌ 请求超时")
        return False
    except Exception as e:
        print(f"❌ 错误: {str(e)}")
        return False


def run_all_tests():
    """运行所有测试"""
    print("="*60)
    print("开始RAG Lambda功能测试")
    print("="*60)
    
    results = []
    
    # 1. 健康检查
    results.append(("健康检查", test_health_check()))
    
    # 2. 测试RAG查询
    test_queries = [
        ("What is RAG?", True),
        ("How does RAG work with vector databases?", True),
        ("What is the capital of France?", False),  # 测试非RAG模式
    ]
    
    for query, use_rag in test_queries:
        mode = "RAG" if use_rag else "Direct"
        results.append((f"查询测试 ({mode}): {query[:30]}...", 
                       test_query_endpoint(query, use_rag)))
    
    # 打印测试总结
    print("\n" + "="*60)
    print("测试总结")
    print("="*60)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✅ 通过" if result else "❌ 失败"
        print(f"{test_name}: {status}")
    
    print(f"\n总计: {passed}/{total} 测试通过")
    
    if passed == total:
        print("🎉 所有测试通过！")
    else:
        print("⚠️ 部分测试失败")
    
    return passed == total


if __name__ == "__main__":
    success = run_all_tests()
    exit(0 if success else 1)