"""
Pytest配置和共享fixtures
"""

import os
import sys
from pathlib import Path
from typing import Generator
import pytest
from unittest.mock import Mock, patch
import asyncio
from datetime import datetime

# 添加项目根目录到Python路径
sys.path.insert(0, str(Path(__file__).parent.parent))

# 设置测试环境变量
os.environ["TEST_ENV"] = "true"
os.environ["ZILLIZ_ENDPOINT"] = "test-endpoint"
os.environ["ZILLIZ_TOKEN"] = "test-token"

def pytest_configure(config):
    """Pytest配置钩子"""
    # 创建必要的目录
    os.makedirs("screenshots", exist_ok=True)
    os.makedirs("test-reports", exist_ok=True)
    os.makedirs("test-reports/coverage", exist_ok=True)


@pytest.fixture(scope="session")
def event_loop():
    """创建事件循环fixture"""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture
def mock_aws_credentials():
    """Mock AWS凭证"""
    with patch.dict(os.environ, {
        "AWS_ACCESS_KEY_ID": "test-key",
        "AWS_SECRET_ACCESS_KEY": "test-secret",
        "AWS_REGION": "us-east-1"
    }):
        yield


@pytest.fixture
def mock_bedrock_client():
    """Mock Bedrock客户端"""
    with patch("boto3.client") as mock_client:
        client = Mock()
        mock_client.return_value = client
        
        # Mock invoke_model响应
        client.invoke_model.return_value = {
            "body": Mock(read=Mock(return_value=b'{"completion": "test response"}'))
        }
        
        yield client


@pytest.fixture
def mock_zilliz_connection():
    """Mock Zilliz连接"""
    with patch("pymilvus.connections.connect") as mock_connect:
        mock_connect.return_value = True
        yield mock_connect


@pytest.fixture
def sample_documents():
    """示例文档数据"""
    return [
        {
            "content": "这是第一个测试文档的内容。",
            "metadata": {"source": "test1.txt", "page": 1}
        },
        {
            "content": "这是第二个测试文档的内容。",
            "metadata": {"source": "test2.txt", "page": 1}
        }
    ]


@pytest.fixture
def sample_embeddings():
    """示例向量数据"""
    import numpy as np
    return [
        np.random.rand(1024).tolist(),  # Titan Embedding v2维度
        np.random.rand(1024).tolist()
    ]


@pytest.fixture
def mock_langchain_components():
    """Mock LangChain组件"""
    with patch("langchain.text_splitter.RecursiveCharacterTextSplitter") as mock_splitter, \
         patch("langchain.embeddings.BedrockEmbeddings") as mock_embeddings, \
         patch("langchain.vectorstores.Milvus") as mock_vectorstore:
        
        # 配置mock行为
        mock_splitter.return_value.split_text.return_value = ["chunk1", "chunk2"]
        mock_embeddings.return_value.embed_documents.return_value = [[0.1] * 1024]
        mock_vectorstore.return_value.similarity_search.return_value = []
        
        yield {
            "splitter": mock_splitter,
            "embeddings": mock_embeddings,
            "vectorstore": mock_vectorstore
        }


@pytest.fixture
def test_config():
    """测试配置"""
    from config.settings import Settings
    settings = Settings()
    settings.test.use_mocks = True
    return settings


@pytest.fixture(autouse=True)
def reset_singleton():
    """重置单例模式（如果有）"""
    yield
    # 在这里重置任何单例


@pytest.fixture
def temp_file(tmp_path):
    """创建临时文件"""
    def _create_file(filename: str, content: str) -> Path:
        file_path = tmp_path / filename
        file_path.write_text(content, encoding="utf-8")
        return file_path
    return _create_file


@pytest.fixture
def mock_api_client():
    """Mock API客户端"""
    from httpx import AsyncClient
    from unittest.mock import AsyncMock
    
    client = AsyncMock(spec=AsyncClient)
    client.get.return_value.json.return_value = {"status": "ok"}
    client.post.return_value.json.return_value = {"result": "success"}
    
    return client


# 测试数据目录
TEST_DATA_DIR = Path(__file__).parent / "test_data"
TEST_DATA_DIR.mkdir(exist_ok=True)


@pytest.fixture
def test_data_dir():
    """返回测试数据目录"""
    return TEST_DATA_DIR


# 跳过条件装饰器
skip_if_no_aws = pytest.mark.skipif(
    not os.getenv("AWS_ACCESS_KEY_ID"),
    reason="需要AWS凭证"
)

skip_if_no_zilliz = pytest.mark.skipif(
    not os.getenv("ZILLIZ_TOKEN"),
    reason="需要Zilliz凭证"
)

skip_in_ci = pytest.mark.skipif(
    os.getenv("CI", "false").lower() == "true",
    reason="CI环境中跳过"
)

# UI测试专用fixtures
@pytest.fixture(autouse=True)
def screenshot_on_failure(request):
    """失败时自动截图"""
    yield
    if hasattr(request.node, 'rep_call') and request.node.rep_call.failed:
        # 如果测试失败，截图
        if hasattr(request.node, 'driver'):
            driver = request.node.driver
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            test_name = request.node.name
            screenshot_path = f"screenshots/failure_{test_name}_{timestamp}.png"
            driver.save_screenshot(screenshot_path)
            print(f"失败截图已保存: {screenshot_path}")

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """添加测试结果到节点"""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

# Playwright配置
@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """Playwright浏览器上下文参数"""
    return {
        **browser_context_args,
        "viewport": {"width": 1920, "height": 1080},
        "ignore_https_errors": True,
        "locale": "zh-CN",
        "timezone_id": "Asia/Shanghai",
    }

# 性能测试标记
def pytest_collection_modifyitems(config, items):
    """添加自定义标记"""
    for item in items:
        # 添加标记
        if "performance" in item.nodeid:
            item.add_marker(pytest.mark.performance)
        if "accessibility" in item.nodeid:
            item.add_marker(pytest.mark.accessibility)
        if "visual" in item.nodeid:
            item.add_marker(pytest.mark.visual)