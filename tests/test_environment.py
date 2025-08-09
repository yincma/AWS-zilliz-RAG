"""
环境配置测试
验证项目环境和依赖是否正确配置
"""

import pytest
import sys
from pathlib import Path


class TestEnvironment:
    """环境配置测试类"""
    
    def test_python_version(self):
        """测试Python版本"""
        assert sys.version_info >= (3, 9), "需要Python 3.9或更高版本"
    
    def test_project_structure(self):
        """测试项目目录结构"""
        root = Path(__file__).parent.parent
        
        # 检查主要目录
        assert (root / "app").exists(), "app目录不存在"
        assert (root / "app" / "models").exists(), "models目录不存在"
        assert (root / "app" / "views").exists(), "views目录不存在"
        assert (root / "app" / "controllers").exists(), "controllers目录不存在"
        
        # 检查配置目录
        assert (root / "config").exists(), "config目录不存在"
        assert (root / "config" / "settings.py").exists(), "settings.py不存在"
        
        # 检查测试目录
        assert (root / "tests").exists(), "tests目录不存在"
        assert (root / "tests" / "unit").exists(), "unit测试目录不存在"
        assert (root / "tests" / "integration").exists(), "integration测试目录不存在"
        assert (root / "tests" / "e2e").exists(), "e2e测试目录不存在"
    
    def test_dependencies_import(self):
        """测试关键依赖包导入"""
        try:
            import boto3
            import langchain
            import pymilvus
            import fastapi
            import pytest
            import pydantic
        except ImportError as e:
            pytest.fail(f"依赖包导入失败: {e}")
    
    def test_config_loading(self):
        """测试配置加载"""
        from config.settings import settings
        
        # 测试AWS配置
        assert settings.aws.region is not None
        assert settings.aws.bedrock_model_id is not None
        assert settings.aws.embedding_model_id is not None
        
        # 测试Zilliz配置
        assert settings.zilliz.endpoint is not None
        assert settings.zilliz.token is not None
        assert settings.zilliz.collection is not None
        
        # 测试RAG配置
        assert settings.rag.chunk_size > 0
        assert settings.rag.chunk_overlap >= 0
        assert settings.rag.top_k > 0
        
        # 测试API配置
        assert settings.api.host is not None
        assert settings.api.port > 0
    
    def test_test_mode(self):
        """测试是否处于测试模式"""
        import os
        assert os.getenv("TEST_ENV") == "true", "未设置测试环境变量"
        
        from config.settings import settings
        assert settings.test.test_env is True, "测试模式未激活"


@pytest.mark.unit
class TestMockSetup:
    """Mock配置测试"""
    
    def test_aws_mock(self, mock_aws_credentials):
        """测试AWS Mock配置"""
        import os
        assert os.getenv("AWS_ACCESS_KEY_ID") == "test-key"
        assert os.getenv("AWS_SECRET_ACCESS_KEY") == "test-secret"
    
    def test_bedrock_mock(self, mock_bedrock_client):
        """测试Bedrock Mock配置"""
        response = mock_bedrock_client.invoke_model()
        assert "body" in response
        assert response["body"].read() == b'{"completion": "test response"}'
    
    def test_zilliz_mock(self, mock_zilliz_connection):
        """测试Zilliz Mock配置"""
        mock_zilliz_connection.assert_not_called()  # 初始状态未调用
    
    def test_sample_data(self, sample_documents, sample_embeddings):
        """测试示例数据fixture"""
        assert len(sample_documents) == 2
        assert "content" in sample_documents[0]
        assert "metadata" in sample_documents[0]
        
        assert len(sample_embeddings) == 2
        assert len(sample_embeddings[0]) == 1024  # Titan Embedding维度