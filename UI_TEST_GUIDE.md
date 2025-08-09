# UI测试指南

## 🎯 测试套件概览

为RAG系统创建了完整的UI测试套件，包括：

### 1. **Selenium测试** (`test_ui_comprehensive.py`)
- 传统Web自动化测试
- 支持Chrome、Firefox、Safari
- 详细的页面交互测试

### 2. **Playwright测试** (`test_ui_playwright.py`)
- 现代化测试框架
- 支持多浏览器并发测试
- 更好的性能和稳定性

### 3. **测试类别**

#### 📱 功能测试
- 页面加载测试
- 导航测试
- 表单交互测试
- API集成测试

#### 🎨 视觉测试
- 响应式设计测试（桌面/平板/移动）
- 截图对比
- 视觉回归测试

#### ⚡ 性能测试
- 页面加载时间
- TTFB (Time to First Byte)
- 资源加载时间
- Core Web Vitals

#### ♿ 可访问性测试
- WCAG合规性检查
- 键盘导航测试
- 屏幕阅读器兼容性
- 颜色对比度检查

## 🚀 快速开始

### 安装依赖

```bash
# 安装测试依赖
pip install -r tests/requirements-test.txt

# 安装Playwright浏览器
playwright install
```

### 运行测试

#### 方式1：使用测试脚本（推荐）

```bash
# 运行交互式测试菜单
./tests/run_ui_tests.sh
```

选项：
1. 快速测试 - 只运行关键测试
2. 标准测试 - 运行所有功能测试  
3. 完整测试 - 包含性能和可访问性测试
4. 单个测试 - 运行特定测试
5. 生成HTML报告

#### 方式2：直接使用pytest

```bash
# 运行所有UI测试
pytest tests/test_ui_comprehensive.py -v

# 运行特定测试
pytest tests/test_ui_comprehensive.py::TestRAGUI::test_page_load -v

# 生成HTML报告
pytest tests/test_ui_comprehensive.py --html=test-reports/report.html --self-contained-html

# 运行Playwright测试
pytest tests/test_ui_playwright.py -v

# 多浏览器测试
pytest tests/test_ui_playwright.py --browser chromium --browser firefox --browser webkit
```

## 📊 测试覆盖范围

### 页面元素测试
✅ 侧边栏导航
✅ 聊天界面
✅ 文档管理
✅ 向量搜索
✅ 系统设置

### 交互测试
✅ 表单输入验证
✅ 按钮点击响应
✅ Tab切换
✅ 快速操作按钮
✅ 拖拽上传

### API测试
✅ 健康检查
✅ 查询请求
✅ 文档上传
✅ 统计信息

### 浏览器兼容性
✅ Chrome/Chromium
✅ Firefox
✅ Safari/WebKit
✅ Edge

## 📸 截图功能

测试会自动生成截图：
- 每个主要页面的截图
- 不同视口尺寸的截图
- 测试失败时的截图
- 性能指标可视化

截图保存位置：`screenshots/`

## 📈 性能基准

### 目标指标
- 页面加载时间: < 3秒
- TTFB: < 1秒
- DOM Ready: < 2秒
- 首次渲染: < 1.5秒

### 测试命令
```bash
# 只运行性能测试
pytest tests/test_ui_comprehensive.py::TestRAGUI::test_page_load_performance -v

# Playwright性能测试
pytest tests/test_ui_playwright.py::TestRAGUIPlaywright::test_performance_metrics -v
```

## ♿ 可访问性测试

### 检查项目
- 语义HTML
- ARIA标签
- 键盘导航
- 颜色对比度
- 焦点管理

### 运行可访问性审计
```bash
pytest tests/test_ui_playwright.py::TestRAGUIPlaywright::test_accessibility_audit -v
```

## 🐛 调试技巧

### 1. 有头模式运行（可见浏览器）
```python
# 在测试代码中注释掉无头模式
# chrome_options.add_argument('--headless')
```

### 2. 增加等待时间
```python
# 修改WebDriverWait超时
self.wait = WebDriverWait(self.driver, 30)  # 增加到30秒
```

### 3. 保存页面源码
```python
# 在测试中添加
with open("page_source.html", "w") as f:
    f.write(self.driver.page_source)
```

### 4. 控制台日志
```python
# 获取浏览器控制台日志
logs = self.driver.get_log('browser')
for log in logs:
    print(log)
```

## 📝 测试报告

### HTML报告
```bash
# 生成详细的HTML测试报告
pytest tests/test_ui_comprehensive.py \
  --html=test-reports/ui-test-report.html \
  --self-contained-html \
  --cov=app \
  --cov-report=html:test-reports/coverage
```

报告位置：
- 测试报告: `test-reports/ui-test-report.html`
- 覆盖率报告: `test-reports/coverage/index.html`

### Allure报告（可选）
```bash
# 安装Allure
brew install allure  # macOS

# 运行测试并生成Allure数据
pytest tests/test_ui_comprehensive.py --alluredir=test-reports/allure-results

# 查看报告
allure serve test-reports/allure-results
```

## 🔄 CI/CD集成

### GitHub Actions示例
```yaml
name: UI Tests

on: [push, pull_request]

jobs:
  ui-tests:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v2
    
    - name: Setup Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.9'
    
    - name: Install dependencies
      run: |
        pip install -r tests/requirements-test.txt
        playwright install
    
    - name: Run UI tests
      run: |
        pytest tests/test_ui_comprehensive.py \
          --html=test-reports/report.html \
          --self-contained-html
    
    - name: Upload test results
      uses: actions/upload-artifact@v2
      with:
        name: test-results
        path: test-reports/
```

## 🎯 测试最佳实践

1. **页面对象模式**: 将页面元素封装为对象
2. **数据驱动测试**: 使用参数化测试不同场景
3. **等待策略**: 使用显式等待而非sleep
4. **截图对比**: 定期更新基准截图
5. **并行执行**: 使用pytest-xdist加速测试

## 🚨 常见问题

### Chrome驱动版本不匹配
```bash
# 使用webdriver-manager自动管理
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
```

### 元素找不到
- 增加等待时间
- 检查iframe
- 验证选择器正确性

### 测试不稳定
- 使用重试机制
- 改进等待策略
- 检查网络延迟

## 📚 扩展阅读

- [Selenium文档](https://www.selenium.dev/documentation/)
- [Playwright文档](https://playwright.dev/python/)
- [Pytest文档](https://docs.pytest.org/)
- [Web可访问性指南](https://www.w3.org/WAI/WCAG21/quickref/)

## 💡 提示

- 定期运行测试确保UI变更不破坏功能
- 在PR合并前运行UI测试
- 保持测试代码简洁可维护
- 及时更新测试用例覆盖新功能