"""
测试前端显示是否正常
"""

import urllib.request
import time

FRONTEND_URL = "https://dfg648088lloi.cloudfront.net"

def test_static_resources():
    """测试静态资源加载"""
    print("="*60)
    print("测试静态资源加载")
    print("="*60)
    
    resources = [
        ("/static/css/style.css", "CSS样式文件"),
        ("/static/js/config.js", "配置文件"),
        ("/static/js/api.js", "API客户端"),
        ("/static/js/chat.js", "聊天功能"),
        ("/static/js/app.js", "主应用"),
        ("/static/js/documents.js", "文档管理"),
        ("/static/js/search.js", "搜索功能")
    ]
    
    all_loaded = True
    
    for path, name in resources:
        url = f"{FRONTEND_URL}{path}"
        try:
            response = urllib.request.urlopen(url, timeout=10)
            status = response.getcode()
            
            if status == 200:
                # 获取文件大小
                content_length = response.headers.get('Content-Length', 'Unknown')
                print(f"✅ {name}: {status} (大小: {content_length} bytes)")
            else:
                print(f"❌ {name}: {status}")
                all_loaded = False
                
        except Exception as e:
            print(f"❌ {name}: 加载失败 - {str(e)[:50]}")
            all_loaded = False
    
    return all_loaded


def test_html_structure():
    """测试HTML结构"""
    print("\n" + "="*60)
    print("测试HTML结构")
    print("="*60)
    
    try:
        response = urllib.request.urlopen(FRONTEND_URL, timeout=10)
        html = response.read().decode('utf-8')
        
        # 检查关键HTML元素
        checks = [
            ('侧边栏', '<aside class="sidebar">' in html),
            ('主内容区', '<main class="main-content">' in html),
            ('聊天容器', 'id="chat-container"' in html),
            ('输入框', 'id="chat-input"' in html),
            ('发送按钮', 'id="send-btn"' in html),
            ('状态指示器', 'id="status-indicator"' in html)
        ]
        
        all_present = True
        for name, present in checks:
            if present:
                print(f"✅ {name}: 存在")
            else:
                print(f"❌ {name}: 缺失")
                all_present = False
        
        # 检查资源路径是否正确
        print("\n资源路径检查:")
        correct_paths = [
            '/static/css/style.css',
            '/static/js/config.js',
            '/static/js/api.js',
            '/static/js/chat.js',
            '/static/js/app.js'
        ]
        
        for path in correct_paths:
            if path in html:
                print(f"✅ 正确路径: {path}")
            else:
                print(f"❌ 缺失路径: {path}")
                all_present = False
        
        return all_present
        
    except Exception as e:
        print(f"❌ 无法加载HTML: {e}")
        return False


def test_api_config():
    """测试API配置"""
    print("\n" + "="*60)
    print("测试API配置")
    print("="*60)
    
    try:
        config_url = f"{FRONTEND_URL}/static/js/config.js"
        response = urllib.request.urlopen(config_url, timeout=10)
        content = response.read().decode('utf-8')
        
        # 检查API URL配置
        if 'abbrw64qve.execute-api.us-east-1.amazonaws.com' in content:
            print("✅ API URL配置正确")
            
            # 检查其他配置
            configs = [
                ('CloudFront URL', 'dfg648088lloi.cloudfront.net'),
                ('默认Top K', 'DEFAULT_TOP_K'),
                ('默认使用RAG', 'DEFAULT_USE_RAG'),
                ('请求超时设置', 'REQUEST_TIMEOUT')
            ]
            
            for name, key in configs:
                if key in content:
                    print(f"✅ {name}: 已配置")
                else:
                    print(f"⚠️ {name}: 未找到")
            
            return True
        else:
            print("❌ API URL配置错误或缺失")
            return False
            
    except Exception as e:
        print(f"❌ 无法加载配置文件: {e}")
        return False


def run_all_tests():
    """运行所有测试"""
    print("🔍 开始测试前端显示")
    print("="*60)
    print(f"前端URL: {FRONTEND_URL}")
    print("="*60)
    
    # 运行测试
    results = []
    results.append(("静态资源加载", test_static_resources()))
    results.append(("HTML结构", test_html_structure()))
    results.append(("API配置", test_api_config()))
    
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
        print("\n🎉 所有测试通过！前端显示应该正常")
        print("\n建议操作：")
        print("1. 清除浏览器缓存")
        print("2. 使用隐身模式访问")
        print("3. 按F12检查控制台是否有错误")
    else:
        print("\n⚠️ 部分测试失败")
        print("\n可能的问题：")
        print("1. CloudFront缓存未完全更新（等待2-3分钟）")
        print("2. 浏览器缓存问题")
        print("3. 静态资源路径配置错误")
        
        if not results[0][1]:  # 如果静态资源加载失败
            print("\n紧急修复建议：")
            print("等待CloudFront缓存更新后重试")
    
    return passed == total


if __name__ == "__main__":
    print("注意：CloudFront缓存更新可能需要2-3分钟")
    print("如果测试失败，请稍后重试\n")
    
    success = run_all_tests()
    
    print("\n" + "="*60)
    print(f"访问前端: {FRONTEND_URL}")
    print("="*60)
    
    exit(0 if success else 1)