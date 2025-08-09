"""
测试前端与API Gateway的连接
"""

import time
import json
import urllib.request
import urllib.error

# 前端和API端点
FRONTEND_URL = "https://dfg648088lloi.cloudfront.net"
API_URL = "https://abbrw64qve.execute-api.us-east-1.amazonaws.com/prod"

def test_frontend_loading():
    """测试前端加载"""
    print("="*60)
    print("测试前端加载")
    print("="*60)
    
    try:
        response = urllib.request.urlopen(FRONTEND_URL)
        html = response.read().decode('utf-8')
        
        # 检查关键元素
        checks = [
            ('API配置文件', '/js/config.js' in html or 'config.js' in html),
            ('API客户端', '/js/api.js' in html or 'api.js' in html),
            ('聊天功能', '/js/chat.js' in html or 'chat.js' in html),
            ('主应用', '/js/app.js' in html or 'app.js' in html)
        ]
        
        for name, result in checks:
            status = "✅" if result else "❌"
            print(f"{status} {name}")
        
        return all(result for _, result in checks)
        
    except Exception as e:
        print(f"❌ 前端加载失败: {e}")
        return False


def test_config_file():
    """测试配置文件"""
    print("\n" + "="*60)
    print("测试配置文件")
    print("="*60)
    
    try:
        # 尝试不同的路径
        paths = [
            f"{FRONTEND_URL}/js/config.js",
            f"{FRONTEND_URL}/static/js/config.js",
            f"{FRONTEND_URL}/config.js"
        ]
        
        config_found = False
        for path in paths:
            try:
                response = urllib.request.urlopen(path)
                content = response.read().decode('utf-8')
                
                if 'API_URL' in content and 'abbrw64qve.execute-api.us-east-1.amazonaws.com' in content:
                    print(f"✅ 配置文件找到: {path}")
                    print(f"✅ API URL配置正确")
                    config_found = True
                    break
            except:
                continue
        
        if not config_found:
            print("❌ 配置文件未找到或配置错误")
        
        return config_found
        
    except Exception as e:
        print(f"❌ 测试配置文件失败: {e}")
        return False


def test_api_health():
    """测试API健康检查"""
    print("\n" + "="*60)
    print("测试API健康检查")
    print("="*60)
    
    try:
        response = urllib.request.urlopen(f"{API_URL}/health", timeout=10)
        data = json.loads(response.read().decode('utf-8'))
        
        if data.get('status') == 'healthy':
            print("✅ API健康检查通过")
            return True
        else:
            print(f"❌ API状态异常: {data}")
            return False
            
    except Exception as e:
        print(f"❌ API健康检查失败: {e}")
        return False


def test_api_query():
    """测试API查询功能"""
    print("\n" + "="*60)
    print("测试API查询功能")
    print("="*60)
    
    try:
        # 准备请求
        data = json.dumps({
            "query": "What is RAG?",
            "top_k": 3,
            "use_rag": True
        }).encode('utf-8')
        
        req = urllib.request.Request(
            f"{API_URL}/query",
            data=data,
            headers={
                'Content-Type': 'application/json'
            },
            method='POST'
        )
        
        # 发送请求
        start_time = time.time()
        response = urllib.request.urlopen(req, timeout=30)
        elapsed = time.time() - start_time
        
        # 解析响应
        result = json.loads(response.read().decode('utf-8'))
        
        if result.get('answer'):
            print(f"✅ 查询成功 (耗时: {elapsed:.2f}秒)")
            print(f"回答预览: {result['answer'][:100]}...")
            
            if result.get('sources'):
                print(f"✅ 找到 {len(result['sources'])} 个相关文档")
            
            return True
        else:
            print(f"❌ 查询返回空结果")
            return False
            
    except Exception as e:
        print(f"❌ API查询失败: {e}")
        return False


def wait_for_cloudfront():
    """等待CloudFront缓存清除"""
    print("\n" + "="*60)
    print("等待CloudFront缓存更新")
    print("="*60)
    
    print("CloudFront缓存正在更新，这可能需要几分钟...")
    print("建议等待2-3分钟后再测试前端")
    
    # 简单的进度条
    for i in range(30):
        print(".", end="", flush=True)
        time.sleep(2)
    print("\n缓存应该已更新")


def run_all_tests():
    """运行所有测试"""
    print("🚀 开始测试前端与API连接")
    print("="*60)
    
    results = []
    
    # 运行测试
    results.append(("前端加载", test_frontend_loading()))
    results.append(("配置文件", test_config_file()))
    results.append(("API健康检查", test_api_health()))
    results.append(("API查询功能", test_api_query()))
    
    # 总结
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
        print("\n🎉 所有测试通过！前端已成功连接到API Gateway")
        print(f"前端URL: {FRONTEND_URL}")
        print(f"API URL: {API_URL}")
    else:
        print("\n⚠️ 部分测试失败")
        print("\n建议：")
        print("1. 等待CloudFront缓存更新（2-3分钟）")
        print("2. 清除浏览器缓存")
        print("3. 使用隐身模式访问")
    
    return passed == total


if __name__ == "__main__":
    success = run_all_tests()
    
    if not success:
        print("\n是否要等待CloudFront缓存更新后重试？(y/n)")
        # 这里简化处理，直接提示用户
        print("如需等待并重试，请稍后手动运行此脚本")
    
    exit(0 if success else 1)