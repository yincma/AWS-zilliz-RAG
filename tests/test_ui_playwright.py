"""
使用Playwright进行高级UI测试
支持多浏览器测试和更好的性能
"""

import pytest
from playwright.sync_api import Page, expect
import os
from datetime import datetime

class TestRAGUIPlaywright:
    """使用Playwright的RAG UI测试"""
    
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, page: Page):
        """每个测试前的设置"""
        self.page = page
        self.base_url = os.getenv('TEST_URL', 'https://dfg648088lloi.cloudfront.net')
        self.page.goto(self.base_url)
        self.page.wait_for_load_state("networkidle")
    
    def test_visual_regression(self, page: Page):
        """视觉回归测试"""
        # 截取完整页面
        page.screenshot(path="screenshots/full-page.png", full_page=True)
        
        # 截取特定元素
        sidebar = page.locator(".sidebar")
        sidebar.screenshot(path="screenshots/sidebar.png")
        
        # 验证元素可见性
        expect(sidebar).to_be_visible()
    
    def test_network_requests(self, page: Page):
        """测试网络请求"""
        # 监听API请求
        api_requests = []
        
        def handle_request(request):
            if "api" in request.url:
                api_requests.append({
                    "url": request.url,
                    "method": request.method,
                    "headers": request.headers
                })
        
        page.on("request", handle_request)
        
        # 触发API调用
        page.fill("#chat-input", "测试问题")
        page.click("#send-btn")
        
        # 等待请求完成
        page.wait_for_timeout(2000)
        
        # 验证API请求
        assert len(api_requests) > 0, "应该有API请求"
    
    def test_multi_browser(self, browser_name: str):
        """多浏览器测试"""
        # Playwright自动处理不同浏览器
        # 在pytest.ini中配置：
        # --browser chromium
        # --browser firefox
        # --browser webkit
        
        # 测试在不同浏览器中的表现
        assert self.page.title() != ""
        
        # 检查关键元素
        expect(self.page.locator(".container")).to_be_visible()
        expect(self.page.locator(".sidebar")).to_be_visible()
        expect(self.page.locator(".main-content")).to_be_visible()
    
    def test_performance_metrics(self, page: Page):
        """性能指标测试"""
        # 获取性能指标
        metrics = page.evaluate("""() => {
            const timing = performance.timing;
            const navigationStart = timing.navigationStart;
            
            return {
                // 页面加载时间
                loadTime: timing.loadEventEnd - navigationStart,
                // DOM解析时间
                domParsingTime: timing.domInteractive - timing.domLoading,
                // 资源加载时间
                resourceLoadTime: timing.loadEventEnd - timing.responseEnd,
                // TTFB (Time to First Byte)
                ttfb: timing.responseStart - navigationStart,
                // DOM Ready时间
                domReady: timing.domContentLoadedEventEnd - navigationStart
            };
        }""")
        
        print(f"性能指标:")
        print(f"  页面加载时间: {metrics['loadTime']}ms")
        print(f"  DOM解析时间: {metrics['domParsingTime']}ms")
        print(f"  资源加载时间: {metrics['resourceLoadTime']}ms")
        print(f"  TTFB: {metrics['ttfb']}ms")
        print(f"  DOM Ready: {metrics['domReady']}ms")
        
        # 断言性能标准
        assert metrics['loadTime'] < 5000, "页面加载应在5秒内完成"
        assert metrics['ttfb'] < 1000, "TTFB应小于1秒"
    
    def test_accessibility_audit(self, page: Page):
        """可访问性审计"""
        # 注入axe-core进行可访问性测试
        page.add_script_tag(url="https://cdnjs.cloudflare.com/ajax/libs/axe-core/4.8.2/axe.min.js")
        
        # 运行可访问性测试
        results = page.evaluate("""async () => {
            return await axe.run();
        }""")
        
        violations = results.get('violations', [])
        
        # 报告违规项
        if violations:
            print(f"发现 {len(violations)} 个可访问性问题:")
            for violation in violations:
                print(f"  - {violation['description']}")
                print(f"    影响: {violation['impact']}")
                print(f"    元素: {len(violation['nodes'])} 个")
        
        # 断言没有严重的可访问性问题
        serious_violations = [v for v in violations if v['impact'] in ['serious', 'critical']]
        assert len(serious_violations) == 0, f"发现严重的可访问性问题: {serious_violations}"
    
    def test_mobile_gestures(self, page: Page):
        """移动端手势测试"""
        # 设置移动视口
        page.set_viewport_size({"width": 375, "height": 667})
        
        # 测试触摸滑动
        sidebar = page.locator(".sidebar")
        
        # 模拟滑动手势
        sidebar.scroll_into_view_if_needed()
        
        # 测试点击
        page.tap('[data-tab="documents"]')
        
        # 验证响应
        expect(page.locator("#documents-tab")).to_have_class(/active/)
    
    def test_console_errors(self, page: Page):
        """控制台错误检测"""
        console_messages = []
        
        # 监听控制台消息
        page.on("console", lambda msg: console_messages.append({
            "type": msg.type,
            "text": msg.text
        }))
        
        # 执行一些操作
        page.click('[data-tab="chat"]')
        page.click('[data-tab="documents"]')
        page.click('[data-tab="search"]')
        page.click('[data-tab="settings"]')
        
        # 检查错误
        errors = [msg for msg in console_messages if msg['type'] == 'error']
        warnings = [msg for msg in console_messages if msg['type'] == 'warning']
        
        print(f"控制台消息统计:")
        print(f"  错误: {len(errors)}")
        print(f"  警告: {len(warnings)}")
        
        # 打印错误详情
        for error in errors:
            print(f"  错误: {error['text']}")
        
        # 断言没有错误
        assert len(errors) == 0, f"发现控制台错误: {errors}"
    
    def test_form_validation(self, page: Page):
        """表单验证测试"""
        # 切换到设置页
        page.click('[data-tab="settings"]')
        
        # 测试无效输入
        temp_input = page.locator("#temperature")
        temp_input.fill("2")  # 超出范围
        
        # 验证值被限制
        value = temp_input.input_value()
        assert float(value) <= 1, "Temperature应该被限制在0-1之间"
        
        # 测试必填字段
        api_input = page.locator("#api-url")
        api_input.fill("")
        
        # 尝试保存
        page.click("#save-settings")
        
        # 应该有验证提示
        # 这里根据实际实现调整
    
    def test_data_persistence(self, page: Page):
        """数据持久化测试"""
        # 修改设置
        page.click('[data-tab="settings"]')
        
        # 更改温度值
        temp_input = page.locator("#temperature")
        temp_input.fill("0.8")
        
        # 保存设置
        page.click("#save-settings")
        
        # 刷新页面
        page.reload()
        page.wait_for_load_state("networkidle")
        
        # 返回设置页
        page.click('[data-tab="settings"]')
        
        # 验证值是否保持
        saved_value = page.locator("#temperature").input_value()
        assert saved_value == "0.8", "设置应该被保存"


@pytest.mark.parametrize("browser_name", ["chromium", "firefox", "webkit"])
class TestCrossBrowser:
    """跨浏览器测试套件"""
    
    def test_browser_compatibility(self, page: Page, browser_name: str):
        """测试浏览器兼容性"""
        base_url = os.getenv('TEST_URL', 'https://dfg648088lloi.cloudfront.net')
        page.goto(base_url)
        
        # 基本检查
        assert page.title() != ""
        
        # 检查关键功能
        expect(page.locator(".sidebar")).to_be_visible()
        expect(page.locator("#chat-input")).to_be_visible()
        
        # 截图对比
        page.screenshot(path=f"screenshots/{browser_name}-compatibility.png")
        
        print(f"✅ {browser_name} 浏览器测试通过")