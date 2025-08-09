"""
应用配置管理
使用pydantic-settings进行环境变量验证和管理
"""

from typing import Optional
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class AWSSettings(BaseSettings):
    """AWS相关配置"""
    region: str = Field(default="us-east-1", alias="AWS_REGION")
    access_key_id: Optional[str] = Field(default=None, alias="AWS_ACCESS_KEY_ID")
    secret_access_key: Optional[str] = Field(default=None, alias="AWS_SECRET_ACCESS_KEY")
    
    # Bedrock配置
    bedrock_model_id: str = Field(
        default="amazon.nova-lite-v1:0",
        alias="BEDROCK_MODEL_ID"
    )
    embedding_model_id: str = Field(
        default="amazon.titan-embed-text-v2:0",
        alias="EMBEDDING_MODEL_ID"
    )
    
    # S3配置
    s3_bucket: Optional[str] = Field(default=None, alias="S3_BUCKET")
    s3_prefix: str = Field(default="documents/", alias="S3_PREFIX")

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore"  # 忽略额外的环境变量
    )


class ZillizSettings(BaseSettings):
    """Zilliz向量数据库配置"""
    endpoint: str = Field(..., alias="ZILLIZ_ENDPOINT")
    token: str = Field(..., alias="ZILLIZ_TOKEN")
    collection: str = Field(default="rag_collection", alias="ZILLIZ_COLLECTION")
    
    # 向量维度（Titan Embedding v2的维度）
    dimension: int = Field(default=1024)
    
    # 索引参数
    index_type: str = Field(default="IVF_FLAT")
    metric_type: str = Field(default="L2")
    nlist: int = Field(default=1024)

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore"
    )


class RAGSettings(BaseSettings):
    """RAG相关配置"""
    # 文档处理
    chunk_size: int = Field(default=1000)
    chunk_overlap: int = Field(default=200)
    
    # 检索配置
    top_k: int = Field(default=5)
    score_threshold: float = Field(default=0.5)
    
    # 生成配置
    max_tokens: int = Field(default=2048)
    temperature: float = Field(default=0.7)
    
    # Prompt模板
    system_prompt: str = Field(
        default="你是一个专业的AI助手，基于提供的上下文信息回答用户问题。"
    )

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore"
    )


class APISettings(BaseSettings):
    """API服务配置"""
    host: str = Field(default="0.0.0.0", alias="API_HOST")
    port: int = Field(default=8000, alias="API_PORT")
    env: str = Field(default="development", alias="API_ENV")
    
    # CORS配置
    cors_origins: list[str] = Field(
        default=["http://localhost:3000", "http://localhost:8080"]
    )
    
    # 限流配置
    rate_limit_per_minute: int = Field(default=60)

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore"
    )


class TestSettings(BaseSettings):
    """测试环境配置"""
    test_env: bool = Field(default=False, alias="TEST_ENV")
    test_collection: str = Field(default="test_collection", alias="TEST_COLLECTION")
    
    # Mock配置
    use_mocks: bool = Field(default=True)
    mock_embeddings: bool = Field(default=True)
    mock_llm: bool = Field(default=True)

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore"
    )


class Settings:
    """统一配置管理器"""
    
    def __init__(self):
        self.aws = AWSSettings()
        self.zilliz = ZillizSettings()
        self.rag = RAGSettings()
        self.api = APISettings()
        self.test = TestSettings()
    
    @property
    def is_production(self) -> bool:
        """判断是否为生产环境"""
        return self.api.env == "production"
    
    @property
    def is_test(self) -> bool:
        """判断是否为测试环境"""
        return self.test.test_env


# 全局配置实例
settings = Settings()