"""
全面的UI测试套件
使用Selenium进行端到端UI测试
"""

import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
import os
from datetime import datetime

class TestRAGUI:
    """RAG系统UI自动化测试"""
    
    @classmethod
    def setup_class(cls):
        """测试类初始化"""
        # 配置Chrome选项
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        # chrome_options.add_argument('--headless')  # 无头模式，可选
        
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.maximize_window()
        cls.wait = WebDriverWait(cls.driver, 10)
        
        # 测试URL配置
        cls.base_url = os.getenv('TEST_URL', 'https://dfg648088lloi.cloudfront.net')
        cls.local_url = 'http://localhost:8000'
        
    @classmethod
    def teardown_class(cls):
        """测试类清理"""
        cls.driver.quit()
    
    def setup_method(self):
        """每个测试方法前的准备"""
        self.driver.get(self.base_url)
        time.sleep(2)  # 等待页面加载
    
    def take_screenshot(self, name):
        """截图功能"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"screenshots/{name}_{timestamp}.png"
        os.makedirs("screenshots", exist_ok=True)
        self.driver.save_screenshot(filename)
        print(f"Screenshot saved: {filename}")
    
    # ========== 页面加载测试 ==========
    
    def test_page_load(self):
        """测试页面基本加载"""
        assert "RAG" in self.driver.title
        
        # 检查主要容器
        container = self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "container"))
        )
        assert container is not None
        
        # 检查侧边栏
        sidebar = self.driver.find_element(By.CLASS_NAME, "sidebar")
        assert sidebar.is_displayed()
        
        # 检查主内容区
        main_content = self.driver.find_element(By.CLASS_NAME, "main-content")
        assert main_content.is_displayed()
        
        self.take_screenshot("page_load")
    
    def test_responsive_design(self):
        """测试响应式设计"""
        # 桌面视图
        self.driver.set_window_size(1920, 1080)
        time.sleep(1)
        self.take_screenshot("desktop_view")
        
        # 平板视图
        self.driver.set_window_size(768, 1024)
        time.sleep(1)
        self.take_screenshot("tablet_view")
        
        # 移动视图
        self.driver.set_window_size(375, 667)
        time.sleep(1)
        self.take_screenshot("mobile_view")
        
        # 恢复桌面视图
        self.driver.maximize_window()
    
    # ========== 导航测试 ==========
    
    def test_sidebar_navigation(self):
        """测试侧边栏导航"""
        nav_items = self.driver.find_elements(By.CLASS_NAME, "nav-item")
        assert len(nav_items) == 4  # 应该有4个导航项
        
        # 测试每个导航项
        tabs = ["chat", "documents", "search", "settings"]
        for tab in tabs:
            nav_item = self.driver.find_element(By.CSS_SELECTOR, f'[data-tab="{tab}"]')
            nav_item.click()
            time.sleep(0.5)
            
            # 验证对应的内容区显示
            content = self.driver.find_element(By.ID, f"{tab}-tab")
            assert "active" in content.get_attribute("class")
            
            self.take_screenshot(f"tab_{tab}")
    
    # ========== 聊天功能测试 ==========
    
    def test_chat_interface(self):
        """测试聊天界面"""
        # 确保在聊天标签
        chat_tab = self.driver.find_element(By.CSS_SELECTOR, '[data-tab="chat"]')
        chat_tab.click()
        time.sleep(1)
        
        # 检查聊天输入框
        chat_input = self.driver.find_element(By.ID, "chat-input")
        assert chat_input.is_displayed()
        
        # 检查发送按钮（初始应该禁用）
        send_btn = self.driver.find_element(By.ID, "send-btn")
        assert send_btn.get_attribute("disabled") == "true"
        
        # 输入文本
        chat_input.send_keys("什么是RAG？")
        time.sleep(0.5)
        
        # 发送按钮应该启用
        assert send_btn.get_attribute("disabled") is None
        
        self.take_screenshot("chat_with_input")
    
    def test_quick_actions(self):
        """测试快速操作按钮"""
        quick_actions = self.driver.find_elements(By.CLASS_NAME, "quick-action")
        assert len(quick_actions) > 0
        
        # 点击第一个快速操作
        first_action = quick_actions[0]
        question = first_action.get_attribute("data-question")
        first_action.click()
        time.sleep(0.5)
        
        # 验证问题被填入输入框
        chat_input = self.driver.find_element(By.ID, "chat-input")
        assert chat_input.get_attribute("value") == question
        
        self.take_screenshot("quick_action_clicked")
    
    def test_chat_options(self):
        """测试聊天选项"""
        # Top K 设置
        top_k_input = self.driver.find_element(By.ID, "top-k")
        assert top_k_input.get_attribute("value") == "5"
        
        # 修改Top K
        top_k_input.clear()
        top_k_input.send_keys("10")
        assert top_k_input.get_attribute("value") == "10"
        
        # 显示引用源复选框
        show_sources = self.driver.find_element(By.ID, "show-sources")
        assert show_sources.is_selected()
        
        show_sources.click()
        assert not show_sources.is_selected()
    
    # ========== 文档管理测试 ==========
    
    def test_document_upload_area(self):
        """测试文档上传区域"""
        # 切换到文档标签
        doc_tab = self.driver.find_element(By.CSS_SELECTOR, '[data-tab="documents"]')
        doc_tab.click()
        time.sleep(1)
        
        # 检查上传区域
        upload_area = self.driver.find_element(By.ID, "upload-area")
        assert upload_area.is_displayed()
        
        # 检查上传按钮
        upload_btn = self.driver.find_element(By.ID, "upload-btn")
        assert upload_btn.is_displayed()
        
        # 检查文件输入（隐藏）
        file_input = self.driver.find_element(By.ID, "file-input")
        assert not file_input.is_displayed()
        
        self.take_screenshot("document_upload_area")
    
    def test_document_stats(self):
        """测试文档统计显示"""
        # 切换到文档标签
        doc_tab = self.driver.find_element(By.CSS_SELECTOR, '[data-tab="documents"]')
        doc_tab.click()
        time.sleep(1)
        
        # 检查统计面板
        stats_grid = self.driver.find_element(By.ID, "stats-grid")
        assert stats_grid.is_displayed()
        
        # 检查统计项
        stat_items = self.driver.find_elements(By.CLASS_NAME, "stat-item")
        assert len(stat_items) == 4  # 应该有4个统计项
        
        self.take_screenshot("document_stats")
    
    # ========== 向量搜索测试 ==========
    
    def test_vector_search(self):
        """测试向量搜索功能"""
        # 切换到搜索标签
        search_tab = self.driver.find_element(By.CSS_SELECTOR, '[data-tab="search"]')
        search_tab.click()
        time.sleep(1)
        
        # 检查搜索输入框
        search_input = self.driver.find_element(By.ID, "search-input")
        assert search_input.is_displayed()
        
        # 检查搜索按钮
        search_btn = self.driver.find_element(By.ID, "search-btn")
        assert search_btn.is_displayed()
        
        # 检查Top K设置
        search_top_k = self.driver.find_element(By.ID, "search-top-k")
        assert search_top_k.get_attribute("value") == "10"
        
        # 输入搜索内容
        search_input.send_keys("RAG技术")
        search_btn.click()
        time.sleep(1)
        
        self.take_screenshot("vector_search")
    
    # ========== 设置测试 ==========
    
    def test_settings_page(self):
        """测试设置页面"""
        # 切换到设置标签
        settings_tab = self.driver.find_element(By.CSS_SELECTOR, '[data-tab="settings"]')
        settings_tab.click()
        time.sleep(1)
        
        # 检查API URL输入
        api_url = self.driver.find_element(By.ID, "api-url")
        assert api_url.is_displayed()
        
        # 检查温度设置
        temperature = self.driver.find_element(By.ID, "temperature")
        assert temperature.get_attribute("value") == "0.7"
        
        # 检查最大令牌数
        max_tokens = self.driver.find_element(By.ID, "max-tokens")
        assert max_tokens.get_attribute("value") == "1000"
        
        # 检查深色模式
        dark_mode = self.driver.find_element(By.ID, "dark-mode")
        assert not dark_mode.is_selected()
        
        # 检查保存按钮
        save_btn = self.driver.find_element(By.ID, "save-settings")
        assert save_btn.is_displayed()
        
        self.take_screenshot("settings_page")
    
    def test_dark_mode_toggle(self):
        """测试深色模式切换"""
        # 切换到设置
        settings_tab = self.driver.find_element(By.CSS_SELECTOR, '[data-tab="settings"]')
        settings_tab.click()
        time.sleep(1)
        
        # 启用深色模式
        dark_mode = self.driver.find_element(By.ID, "dark-mode")
        dark_mode.click()
        time.sleep(1)
        
        # 验证body类变化
        body = self.driver.find_element(By.TAG_NAME, "body")
        assert "dark-mode" in body.get_attribute("class")
        
        self.take_screenshot("dark_mode_enabled")
        
        # 禁用深色模式
        dark_mode.click()
        time.sleep(1)
        assert "dark-mode" not in body.get_attribute("class")
    
    # ========== 交互测试 ==========
    
    def test_loading_overlay(self):
        """测试加载遮罩"""
        loading_overlay = self.driver.find_element(By.ID, "loading-overlay")
        # 初始应该隐藏
        assert not loading_overlay.is_displayed()
    
    def test_keyboard_shortcuts(self):
        """测试键盘快捷键"""
        chat_input = self.driver.find_element(By.ID, "chat-input")
        chat_input.send_keys("测试消息")
        
        # 测试Enter发送（需要Shift+Enter换行）
        chat_input.send_keys(Keys.ENTER)
        time.sleep(0.5)
        
        self.take_screenshot("keyboard_test")
    
    # ========== 性能测试 ==========
    
    def test_page_load_performance(self):
        """测试页面加载性能"""
        # 使用Navigation Timing API
        performance = self.driver.execute_script("""
            var timing = window.performance.timing;
            return {
                loadTime: timing.loadEventEnd - timing.navigationStart,
                domReady: timing.domContentLoadedEventEnd - timing.navigationStart,
                firstPaint: timing.responseEnd - timing.navigationStart
            };
        """)
        
        print(f"页面加载性能：")
        print(f"  总加载时间: {performance['loadTime']}ms")
        print(f"  DOM准备时间: {performance['domReady']}ms")
        print(f"  首次渲染时间: {performance['firstPaint']}ms")
        
        # 验证性能指标
        assert performance['loadTime'] < 5000  # 5秒内加载完成
        assert performance['domReady'] < 3000  # 3秒内DOM准备完成
    
    # ========== 错误处理测试 ==========
    
    def test_error_handling(self):
        """测试错误处理"""
        # 测试空查询
        chat_input = self.driver.find_element(By.ID, "chat-input")
        send_btn = self.driver.find_element(By.ID, "send-btn")
        
        # 空输入时发送按钮应该禁用
        chat_input.clear()
        time.sleep(0.5)
        assert send_btn.get_attribute("disabled") == "true"
        
        self.take_screenshot("error_handling")
    
    # ========== 跨浏览器测试 ==========
    
    def test_font_awesome_icons(self):
        """测试Font Awesome图标加载"""
        # 检查图标是否正确显示
        robot_icon = self.driver.find_element(By.CSS_SELECTOR, ".fa-robot")
        assert robot_icon.is_displayed()
        
        # 验证图标字体加载
        icon_font = self.driver.execute_script("""
            var icon = document.querySelector('.fa-robot');
            var style = window.getComputedStyle(icon, ':before');
            return style.fontFamily;
        """)
        assert "Font Awesome" in icon_font
    
    # ========== 可访问性测试 ==========
    
    def test_accessibility_basics(self):
        """基本可访问性测试"""
        # 检查语言属性
        html = self.driver.find_element(By.TAG_NAME, "html")
        assert html.get_attribute("lang") == "zh-CN"
        
        # 检查viewport meta标签
        viewport = self.driver.find_element(By.CSS_SELECTOR, 'meta[name="viewport"]')
        assert viewport is not None
        
        # 检查标题
        title = self.driver.title
        assert len(title) > 0
        
        # 检查表单标签
        labels = self.driver.find_elements(By.TAG_NAME, "label")
        assert len(labels) > 0


class TestAPIIntegration:
    """API集成测试"""
    
    @classmethod
    def setup_class(cls):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.maximize_window()
        cls.wait = WebDriverWait(cls.driver, 10)
        cls.base_url = os.getenv('TEST_URL', 'https://dfg648088lloi.cloudfront.net')
    
    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
    
    def test_api_connection_status(self):
        """测试API连接状态"""
        self.driver.get(self.base_url)
        time.sleep(3)
        
        # 检查连接状态指示器
        status_indicator = self.driver.find_element(By.ID, "status-indicator")
        status_text = self.driver.find_element(By.ID, "status-text")
        
        # 等待连接状态更新
        time.sleep(2)
        
        # 验证状态文本
        status = status_text.text
        print(f"API连接状态: {status}")
        
        # 截图
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        os.makedirs("screenshots", exist_ok=True)
        self.driver.save_screenshot(f"screenshots/api_status_{timestamp}.png")


if __name__ == "__main__":
    # 运行测试
    pytest.main([__file__, "-v", "--tb=short", "--capture=no"])