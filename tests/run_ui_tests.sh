#!/bin/bash

# UI测试运行脚本
echo "🧪 开始RAG系统UI测试..."

# 设置颜色
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# 检查Python环境
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}❌ Python3未安装${NC}"
    exit 1
fi

# 创建虚拟环境（如果不存在）
if [ ! -d "venv" ]; then
    echo -e "${YELLOW}📦 创建虚拟环境...${NC}"
    python3 -m venv venv
fi

# 激活虚拟环境
source venv/bin/activate

# 安装测试依赖
echo -e "${YELLOW}📦 安装测试依赖...${NC}"
pip install -q -r tests/requirements-test.txt

# 安装Chrome驱动
echo -e "${YELLOW}🌐 配置Chrome驱动...${NC}"
python3 -c "
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os

# 自动下载并安装Chrome驱动
driver_path = ChromeDriverManager().install()
print(f'Chrome驱动已安装: {driver_path}')
"

# 创建截图目录
mkdir -p screenshots
mkdir -p test-reports

# 设置测试URL
if [ -z "$TEST_URL" ]; then
    export TEST_URL="https://dfg648088lloi.cloudfront.net"
    echo -e "${YELLOW}使用默认测试URL: $TEST_URL${NC}"
fi

# 运行测试选项
echo -e "\n${GREEN}选择测试模式:${NC}"
echo "1) 快速测试 - 只运行关键测试"
echo "2) 标准测试 - 运行所有功能测试"
echo "3) 完整测试 - 包含性能和可访问性测试"
echo "4) 单个测试 - 运行特定测试"
echo "5) 生成HTML报告"

read -p "请选择 (1-5): " choice

case $choice in
    1)
        echo -e "\n${GREEN}🚀 运行快速测试...${NC}"
        pytest tests/test_ui_comprehensive.py::TestRAGUI::test_page_load \
               tests/test_ui_comprehensive.py::TestRAGUI::test_sidebar_navigation \
               tests/test_ui_comprehensive.py::TestRAGUI::test_chat_interface \
               -v --tb=short
        ;;
    2)
        echo -e "\n${GREEN}🧪 运行标准测试...${NC}"
        pytest tests/test_ui_comprehensive.py::TestRAGUI -v --tb=short
        ;;
    3)
        echo -e "\n${GREEN}🔍 运行完整测试...${NC}"
        pytest tests/test_ui_comprehensive.py -v --tb=short \
               --html=test-reports/ui-test-report.html \
               --self-contained-html
        ;;
    4)
        echo -e "\n${GREEN}请输入测试名称 (例如: test_page_load):${NC}"
        read test_name
        pytest tests/test_ui_comprehensive.py::TestRAGUI::$test_name -v -s
        ;;
    5)
        echo -e "\n${GREEN}📊 生成HTML测试报告...${NC}"
        pytest tests/test_ui_comprehensive.py \
               --html=test-reports/ui-test-report.html \
               --self-contained-html \
               --cov=app \
               --cov-report=html:test-reports/coverage
        echo -e "${GREEN}✅ 报告已生成: test-reports/ui-test-report.html${NC}"
        ;;
    *)
        echo -e "${RED}❌ 无效选择${NC}"
        exit 1
        ;;
esac

# 测试结果
if [ $? -eq 0 ]; then
    echo -e "\n${GREEN}✅ UI测试完成！${NC}"
    
    # 显示截图
    if [ -d "screenshots" ] && [ "$(ls -A screenshots)" ]; then
        echo -e "${GREEN}📸 截图已保存到 screenshots/ 目录${NC}"
        ls -la screenshots/
    fi
    
    # 播放完成音
    afplay /System/Library/Sounds/Glass.aiff 2>/dev/null || true
else
    echo -e "\n${RED}❌ 测试失败${NC}"
    afplay /System/Library/Sounds/Basso.aiff 2>/dev/null || true
    exit 1
fi