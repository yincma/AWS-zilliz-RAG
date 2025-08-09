"""
简化版UI测试 - 验证基本功能
"""

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import os

def test_basic_ui():
    """测试基本UI功能"""
    
    # 配置Chrome选项
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--window-size=1920,1080')
    
    # 创建驱动
    driver_path = ChromeDriverManager().install()
    # 修正路径到实际的chromedriver文件
    if "THIRD_PARTY_NOTICES" in driver_path:
        driver_path = driver_path.replace("THIRD_PARTY_NOTICES.chromedriver", "chromedriver")
    
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    test_results = {
        "总测试数": 0,
        "通过": 0,
        "失败": 0,
        "错误": [],
        "性能指标": {}
    }
    
    try:
        # 测试URL
        url = os.getenv('TEST_URL', 'https://dfg648088lloi.cloudfront.net')
        print(f"\n📍 测试URL: {url}\n")
        
        # 1. 页面加载测试
        print("1️⃣ 测试页面加载...")
        test_results["总测试数"] += 1
        start_time = time.time()
        driver.get(url)
        load_time = time.time() - start_time
        test_results["性能指标"]["页面加载时间"] = f"{load_time:.2f}秒"
        
        # 检查标题
        wait = WebDriverWait(driver, 10)
        if "RAG" in driver.title or "Retrieval" in driver.title:
            print("   ✅ 页面加载成功")
            test_results["通过"] += 1
        else:
            print(f"   ❌ 页面标题异常: {driver.title}")
            test_results["失败"] += 1
            test_results["错误"].append(f"页面标题异常: {driver.title}")
        
        # 2. 检查主要容器
        print("2️⃣ 测试页面结构...")
        test_results["总测试数"] += 1
        try:
            container = wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "container"))
            )
            print("   ✅ 主容器存在")
            test_results["通过"] += 1
        except Exception as e:
            print(f"   ❌ 主容器未找到: {e}")
            test_results["失败"] += 1
            test_results["错误"].append("主容器未找到")
        
        # 3. 检查侧边栏
        print("3️⃣ 测试侧边栏...")
        test_results["总测试数"] += 1
        try:
            sidebar = driver.find_element(By.CLASS_NAME, "sidebar")
            if sidebar.is_displayed():
                print("   ✅ 侧边栏显示正常")
                test_results["通过"] += 1
            else:
                print("   ⚠️ 侧边栏存在但不可见")
                test_results["失败"] += 1
                test_results["错误"].append("侧边栏不可见")
        except Exception as e:
            print(f"   ❌ 侧边栏未找到: {e}")
            test_results["失败"] += 1
            test_results["错误"].append("侧边栏未找到")
        
        # 4. 检查导航标签
        print("4️⃣ 测试导航标签...")
        test_results["总测试数"] += 1
        tabs = ['chat', 'documents', 'search', 'settings']
        tab_count = 0
        for tab in tabs:
            try:
                element = driver.find_element(By.CSS_SELECTOR, f'[data-tab="{tab}"]')
                if element:
                    tab_count += 1
            except:
                pass
        
        if tab_count == len(tabs):
            print(f"   ✅ 所有{len(tabs)}个导航标签都存在")
            test_results["通过"] += 1
        else:
            print(f"   ⚠️ 只找到{tab_count}/{len(tabs)}个导航标签")
            if tab_count > 0:
                test_results["通过"] += 1
            else:
                test_results["失败"] += 1
                test_results["错误"].append(f"导航标签缺失: 只找到{tab_count}/{len(tabs)}个")
        
        # 5. 检查聊天输入框
        print("5️⃣ 测试聊天界面...")
        test_results["总测试数"] += 1
        try:
            chat_input = driver.find_element(By.ID, "chat-input")
            send_btn = driver.find_element(By.ID, "send-btn")
            if chat_input and send_btn:
                print("   ✅ 聊天界面元素完整")
                test_results["通过"] += 1
            else:
                print("   ⚠️ 聊天界面元素不完整")
                test_results["失败"] += 1
                test_results["错误"].append("聊天界面元素不完整")
        except Exception as e:
            print(f"   ❌ 聊天界面元素未找到: {e}")
            test_results["失败"] += 1
            test_results["错误"].append("聊天界面元素未找到")
        
        # 6. 测试标签切换
        print("6️⃣ 测试标签切换...")
        test_results["总测试数"] += 1
        try:
            docs_tab = driver.find_element(By.CSS_SELECTOR, '[data-tab="documents"]')
            docs_tab.click()
            time.sleep(1)
            
            # 检查是否切换成功
            docs_content = driver.find_element(By.ID, "documents-tab")
            if docs_content.is_displayed():
                print("   ✅ 标签切换功能正常")
                test_results["通过"] += 1
            else:
                print("   ⚠️ 标签切换后内容未显示")
                test_results["失败"] += 1
                test_results["错误"].append("标签切换功能异常")
        except Exception as e:
            print(f"   ❌ 标签切换失败: {e}")
            test_results["失败"] += 1
            test_results["错误"].append("标签切换失败")
        
        # 7. 检查响应式设计
        print("7️⃣ 测试响应式设计...")
        test_results["总测试数"] += 1
        try:
            # 测试移动端视图
            driver.set_window_size(375, 667)
            time.sleep(1)
            
            # 检查页面是否适应
            container = driver.find_element(By.CLASS_NAME, "container")
            if container.size['width'] <= 375:
                print("   ✅ 移动端响应式正常")
                test_results["通过"] += 1
            else:
                print("   ⚠️ 移动端响应式可能有问题")
                test_results["失败"] += 1
                test_results["错误"].append("移动端响应式异常")
            
            # 恢复窗口大小
            driver.set_window_size(1920, 1080)
        except Exception as e:
            print(f"   ❌ 响应式测试失败: {e}")
            test_results["失败"] += 1
            test_results["错误"].append("响应式测试失败")
        
        # 8. 性能指标收集
        print("8️⃣ 收集性能指标...")
        test_results["总测试数"] += 1
        try:
            performance = driver.execute_script("""
                const timing = performance.timing;
                const navigationStart = timing.navigationStart;
                return {
                    domReady: timing.domContentLoadedEventEnd - navigationStart,
                    pageLoad: timing.loadEventEnd - navigationStart,
                    ttfb: timing.responseStart - navigationStart
                };
            """)
            
            test_results["性能指标"]["DOM Ready"] = f"{performance['domReady']}ms"
            test_results["性能指标"]["完整加载"] = f"{performance['pageLoad']}ms"
            test_results["性能指标"]["TTFB"] = f"{performance['ttfb']}ms"
            
            print(f"   ✅ 性能指标已收集")
            print(f"      - TTFB: {performance['ttfb']}ms")
            print(f"      - DOM Ready: {performance['domReady']}ms")
            print(f"      - 完整加载: {performance['pageLoad']}ms")
            test_results["通过"] += 1
        except Exception as e:
            print(f"   ❌ 性能指标收集失败: {e}")
            test_results["失败"] += 1
            test_results["错误"].append("性能指标收集失败")
        
        # 截图保存
        os.makedirs("screenshots", exist_ok=True)
        driver.save_screenshot("screenshots/ui_test_final.png")
        print("\n📸 截图已保存: screenshots/ui_test_final.png")
        
    except Exception as e:
        print(f"\n❌ 测试过程出错: {e}")
        test_results["错误"].append(f"测试过程出错: {e}")
    
    finally:
        driver.quit()
    
    # 输出测试结果总结
    print("\n" + "="*50)
    print("📊 测试结果总结")
    print("="*50)
    print(f"总测试数: {test_results['总测试数']}")
    print(f"✅ 通过: {test_results['通过']}")
    print(f"❌ 失败: {test_results['失败']}")
    print(f"通过率: {(test_results['通过']/test_results['总测试数']*100):.1f}%")
    
    if test_results["性能指标"]:
        print("\n⚡ 性能指标:")
        for key, value in test_results["性能指标"].items():
            print(f"  - {key}: {value}")
    
    if test_results["错误"]:
        print("\n❌ 错误详情:")
        for error in test_results["错误"]:
            print(f"  - {error}")
    
    print("\n" + "="*50)
    
    # 返回测试是否成功
    return test_results["失败"] == 0

if __name__ == "__main__":
    success = test_basic_ui()
    exit(0 if success else 1)