"""
测试前端移动端响应式设计
"""

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def test_mobile_responsive():
    """测试移动端响应式设计"""
    
    # 配置Chrome选项
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    
    # 移动设备尺寸
    mobile_sizes = [
        {"name": "iPhone SE", "width": 375, "height": 667},
        {"name": "iPhone XR", "width": 414, "height": 896},
        {"name": "Pixel 5", "width": 393, "height": 851},
        {"name": "Samsung Galaxy S8+", "width": 360, "height": 740},
    ]
    
    print("="*60)
    print("测试移动端响应式设计")
    print("="*60)
    
    for device in mobile_sizes:
        print(f"\n测试设备: {device['name']} ({device['width']}x{device['height']})")
        
        # 创建driver
        driver = webdriver.Chrome(options=chrome_options)
        
        try:
            # 设置窗口大小
            driver.set_window_size(device['width'], device['height'])
            
            # 访问网站
            driver.get("https://dfg648088lloi.cloudfront.net")
            
            # 等待页面加载
            time.sleep(3)
            
            # 检查页面元素
            viewport_width = driver.execute_script("return window.innerWidth")
            viewport_height = driver.execute_script("return window.innerHeight")
            
            print(f"  视口大小: {viewport_width}x{viewport_height}")
            
            # 检查响应式元素
            # 检查是否有水平滚动条
            has_horizontal_scroll = driver.execute_script(
                "return document.documentElement.scrollWidth > document.documentElement.clientWidth"
            )
            
            if has_horizontal_scroll:
                print(f"  ❌ 存在水平滚动条（响应式问题）")
            else:
                print(f"  ✅ 没有水平滚动条")
            
            # 检查特定元素的响应式
            try:
                # 检查容器宽度
                container_width = driver.execute_script(
                    "return document.querySelector('.container, .main, [class*=container]')?.offsetWidth || 0"
                )
                
                if container_width > 0:
                    if container_width > viewport_width:
                        print(f"  ❌ 容器宽度({container_width}px)超出视口")
                    else:
                        print(f"  ✅ 容器宽度适配({container_width}px)")
                        
            except Exception as e:
                print(f"  ⚠️ 无法检查容器宽度: {e}")
            
            # 截图
            screenshot_name = f"mobile_{device['name'].replace(' ', '_')}.png"
            driver.save_screenshot(screenshot_name)
            print(f"  📸 截图已保存: {screenshot_name}")
            
        except Exception as e:
            print(f"  ❌ 测试失败: {e}")
            
        finally:
            driver.quit()
    
    print("\n" + "="*60)
    print("测试完成")
    print("="*60)


if __name__ == "__main__":
    # 注意：需要安装selenium和chrome driver
    # pip install selenium
    # 并下载对应的chromedriver
    
    print("注意：此测试需要安装selenium和Chrome driver")
    print("如果没有安装，请运行：")
    print("pip install selenium")
    print("并从 https://chromedriver.chromium.org/ 下载chromedriver")
    
    # 简单的HTTP请求测试作为替代
    import urllib.request
    
    print("\n进行简单的HTTP响应测试...")
    
    try:
        response = urllib.request.urlopen("https://dfg648088lloi.cloudfront.net")
        html = response.read().decode('utf-8')
        
        # 检查是否有viewport meta标签
        if 'viewport' in html:
            print("✅ 找到viewport meta标签（移动端优化）")
        else:
            print("❌ 未找到viewport meta标签")
        
        # 检查是否有响应式CSS
        if 'media' in html or '@media' in html:
            print("✅ 找到媒体查询（响应式CSS）")
        else:
            print("⚠️ 未找到明显的媒体查询")
            
        # 保存HTML用于分析
        with open('frontend.html', 'w', encoding='utf-8') as f:
            f.write(html)
        print("📄 HTML已保存到frontend.html")
        
    except Exception as e:
        print(f"❌ 无法访问网站: {e}")