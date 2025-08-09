# AWS-Zilliz-RAG 系统架构设计文档

## 1. 系统概述

基于AWS和Zilliz构建的企业级RAG（Retrieval-Augmented Generation）系统，采用MVC架构模式，实现高性能、可扩展的文档检索增强生成服务。

## 2. 架构设计原则

### 2.1 核心原则
- **分层解耦**：严格遵循MVC模式，各层职责单一
- **无状态设计**：所有服务无状态，支持水平扩展
- **异步优先**：采用异步处理提高并发性能
- **容错设计**：实现优雅降级和故障恢复
- **配置外置**：敏感信息和配置外部化管理

### 2.2 技术选型依据
- **AWS Bedrock**：托管式LLM服务，无需维护模型基础设施
- **Zilliz Cloud**：托管式向量数据库，高性能向量检索
- **AWS Lambda**：无服务器计算，按需扩展
- **LangChain**：成熟的RAG框架，丰富的生态系统

## 3. MVC架构详细设计

### 3.1 Model层设计

#### 3.1.1 核心模型

```python
# Document Model - 文档实体和操作
class Document:
    - id: str
    - content: str  
    - metadata: Dict[str, Any]
    - embedding: Optional[List[float]]
    - chunks: List[DocumentChunk]
    
    + load_from_s3(bucket: str, key: str)
    + split_chunks(chunk_size: int, overlap: int)
    + generate_embedding()

# Embedding Model - 向量化处理
class EmbeddingModel:
    - model_id: str = "amazon.titan-embed-image-v1"
    - dimension: int = 1024
    
    + encode(text: str) -> List[float]
    + batch_encode(texts: List[str]) -> List[List[float]]
    + encode_multimodal(text: str, image: bytes) -> List[float]

# Vector Store Model - 向量存储
class VectorStore:
    - collection_name: str
    - index_type: str = "IVF_FLAT"
    - metric_type: str = "L2"
    
    + create_collection(schema: Schema)
    + insert(embeddings: List[float], metadata: Dict)
    + search(query_vector: List[float], top_k: int, filters: Dict)
    + delete(ids: List[str])
    + update(id: str, embedding: List[float], metadata: Dict)

# LLM Model - 语言模型
class LLMModel:
    - model_id: str = "nova-pro-v1:0"
    - temperature: float = 0.7
    - max_tokens: int = 2048
    
    + generate(prompt: str, context: str) -> str
    + stream_generate(prompt: str, context: str) -> Generator
    + batch_generate(prompts: List[str]) -> List[str]

# RAG Chain Model - RAG链
class RAGChain:
    - retriever: VectorStore
    - llm: LLMModel
    - prompt_template: PromptTemplate
    
    + process_query(query: str) -> RAGResponse
    + rerank_results(results: List[Document], query: str)
    + generate_answer(query: str, context: List[Document])
```

#### 3.1.2 数据流设计

```
输入文档 → 文档分割 → 向量化 → 存储到Zilliz
                ↓
            元数据处理 → 存储到S3

查询请求 → 向量化 → 向量检索 → 重排序 → 上下文构建 → LLM生成 → 响应
```

### 3.2 Controller层设计

#### 3.2.1 核心控制器

```python
# RAG主控制器
class RAGController:
    + process_query(request: QueryRequest) -> QueryResponse
    + handle_feedback(feedback: FeedbackRequest) -> FeedbackResponse
    
    工作流：
    1. 验证请求参数
    2. 调用Model层处理业务逻辑
    3. 错误处理和重试
    4. 调用View层格式化响应

# 文档管理控制器  
class DocumentController:
    + upload_document(file: UploadFile) -> DocumentResponse
    + delete_document(doc_id: str) -> DeleteResponse
    + update_document(doc_id: str, content: str) -> UpdateResponse
    + list_documents(filters: Dict) -> ListResponse
    
    工作流：
    1. 文件验证（格式、大小、安全）
    2. 存储到S3
    3. 触发异步处理流程
    4. 返回处理状态

# 搜索控制器
class SearchController:
    + search(query: str, filters: Dict) -> SearchResponse
    + advanced_search(request: AdvancedSearchRequest) -> SearchResponse
    + semantic_search(query: str, top_k: int) -> SemanticSearchResponse
    
    工作流：
    1. 查询预处理
    2. 多路检索（向量、关键词、混合）
    3. 结果融合和重排序
    4. 响应构建
```

#### 3.2.2 Lambda处理器

```python
# 查询处理Lambda
def query_handler(event, context):
    """
    处理API Gateway请求
    触发器：API Gateway (POST /api/query)
    """
    controller = RAGController()
    request = parse_request(event)
    response = controller.process_query(request)
    return format_api_response(response)

# 文档摄入Lambda
def ingest_handler(event, context):
    """
    处理S3上传事件
    触发器：S3 PUT Object
    """
    controller = DocumentController()
    s3_event = parse_s3_event(event)
    result = controller.process_document(s3_event)
    return result

# 批处理Lambda
def batch_handler(event, context):
    """
    处理批量文档处理
    触发器：EventBridge Schedule
    """
    controller = DocumentController()
    batch_request = parse_batch_request(event)
    results = controller.process_batch(batch_request)
    return results
```

### 3.3 View层设计

#### 3.3.1 API响应视图

```python
# 响应格式化器
class ResponseFormatter:
    + format_success(data: Any, meta: Dict) -> Dict
    + format_error(error: Exception, code: int) -> Dict
    + format_paginated(data: List, page: int, size: int) -> Dict
    
    响应格式：
    {
        "status": "success|error",
        "code": 200,
        "data": {...},
        "meta": {
            "timestamp": "2024-01-01T00:00:00Z",
            "request_id": "uuid",
            "version": "1.0"
        }
    }

# 数据序列化器
class Serializer:
    + serialize_document(doc: Document) -> Dict
    + serialize_search_result(result: SearchResult) -> Dict
    + serialize_rag_response(response: RAGResponse) -> Dict
    
    序列化规则：
    - 日期时间：ISO 8601格式
    - 浮点数：保留4位小数
    - 向量：Base64编码（可选）
    - 大文本：截断或分页
```

#### 3.3.2 Web前端视图

```html
<!-- 查询界面 -->
<div class="rag-interface">
    <SearchBox />
    <FilterPanel />
    <ResultsDisplay />
    <SourceViewer />
</div>

<!-- 组件规范 -->
- SearchBox: 支持自然语言输入、语音输入
- FilterPanel: 时间范围、文档类型、相关度阈值
- ResultsDisplay: 答案展示、来源引用、置信度
- SourceViewer: 原文预览、高亮显示
```

## 4. API接口设计

### 4.1 RESTful API规范

```yaml
# 查询接口
POST /api/v1/query
Request:
  {
    "query": "string",
    "top_k": 5,
    "filters": {
      "date_range": ["2024-01-01", "2024-12-31"],
      "document_type": ["pdf", "txt"]
    },
    "include_sources": true
  }
Response:
  {
    "answer": "string",
    "sources": [{
      "document_id": "string",
      "content": "string",
      "score": 0.95,
      "metadata": {}
    }],
    "confidence": 0.88
  }

# 文档管理接口
POST /api/v1/documents
  - 上传文档
  
GET /api/v1/documents/{id}
  - 获取文档详情
  
PUT /api/v1/documents/{id}
  - 更新文档
  
DELETE /api/v1/documents/{id}
  - 删除文档
  
GET /api/v1/documents
  - 列出文档（分页）

# 搜索接口
POST /api/v1/search
  - 语义搜索
  
POST /api/v1/search/advanced
  - 高级搜索（混合检索）

# 管理接口
GET /api/v1/health
  - 健康检查
  
GET /api/v1/metrics
  - 性能指标
  
POST /api/v1/feedback
  - 用户反馈
```

### 4.2 错误处理规范

```python
ERROR_CODES = {
    400: "Bad Request - 请求参数错误",
    401: "Unauthorized - 未授权访问",
    403: "Forbidden - 禁止访问",
    404: "Not Found - 资源不存在",
    429: "Too Many Requests - 请求频率过高",
    500: "Internal Server Error - 服务器内部错误",
    503: "Service Unavailable - 服务暂时不可用"
}

class APIException:
    - code: int
    - message: str
    - details: Dict
    - request_id: str
```

## 5. 数据模型设计

### 5.1 向量数据库Schema

```python
# Zilliz Collection Schema
COLLECTION_SCHEMA = {
    "name": "rag_documents",
    "fields": [
        {
            "name": "id",
            "type": DataType.VARCHAR,
            "max_length": 128,
            "is_primary": True
        },
        {
            "name": "embedding",
            "type": DataType.FLOAT_VECTOR,
            "dim": 1024
        },
        {
            "name": "content",
            "type": DataType.VARCHAR,
            "max_length": 65535
        },
        {
            "name": "metadata",
            "type": DataType.JSON
        },
        {
            "name": "created_at",
            "type": DataType.INT64
        }
    ],
    "indexes": [
        {
            "field": "embedding",
            "index_type": "IVF_FLAT",
            "metric_type": "L2",
            "params": {"nlist": 1024}
        }
    ]
}
```

### 5.2 S3存储结构

```
s3://rag-bucket/
├── documents/           # 原始文档
│   ├── pdf/
│   ├── txt/
│   └── html/
├── embeddings/          # 向量缓存
│   └── {doc_id}/
│       └── chunks.json
├── metadata/            # 元数据
│   └── {doc_id}.json
└── indexes/            # 索引文件
    └── inverted/
```

## 6. 性能优化设计

### 6.1 缓存策略

```python
# 多级缓存架构
CACHE_LAYERS = {
    "L1": {
        "type": "Memory",
        "ttl": 300,  # 5分钟
        "size": "100MB"
    },
    "L2": {
        "type": "Redis",
        "ttl": 3600,  # 1小时
        "size": "1GB"
    },
    "L3": {
        "type": "S3",
        "ttl": 86400,  # 1天
        "prefix": "cache/"
    }
}

# 缓存键设计
cache_key = f"query:{hash(query)}:top_k:{top_k}:filters:{hash(filters)}"
```

### 6.2 并发优化

```python
# 异步处理配置
ASYNC_CONFIG = {
    "max_workers": 10,
    "queue_size": 1000,
    "timeout": 30,
    "retry_count": 3,
    "retry_delay": [1, 2, 4]  # 指数退避
}

# 批处理配置
BATCH_CONFIG = {
    "batch_size": 100,
    "max_batch_wait": 1.0,  # 秒
    "parallel_batches": 5
}
```

### 6.3 向量检索优化

```python
# 索引优化参数
INDEX_PARAMS = {
    "index_type": "IVF_FLAT",
    "nlist": 1024,  # 聚类中心数
    "nprobe": 16,   # 搜索时访问的聚类数
    "cache_size": 1000,  # 缓存向量数
    "ef_construction": 200,  # HNSW构建参数
    "M": 16  # HNSW连接数
}

# 查询优化
QUERY_OPTIMIZATION = {
    "pre_filter": True,  # 预过滤
    "rerank": True,      # 重排序
    "hybrid_search": True,  # 混合检索
    "async_search": True  # 异步检索
}
```

## 7. 安全设计

### 7.1 认证授权

```python
# IAM角色配置
LAMBDA_ROLE = {
    "policies": [
        "AWSLambdaBasicExecutionRole",
        "AmazonS3ReadOnlyAccess",
        "AmazonBedrockFullAccess"
    ],
    "trust_relationship": {
        "Service": "lambda.amazonaws.com"
    }
}

# API认证
API_AUTH = {
    "type": "AWS_IAM",
    "methods": ["sigv4"],
    "cors": {
        "origins": ["https://example.com"],
        "methods": ["POST", "GET"],
        "headers": ["Content-Type", "X-Api-Key"]
    }
}
```

### 7.2 数据安全

```python
# 加密配置
ENCRYPTION = {
    "at_rest": {
        "s3": "AES256",
        "database": "TLS 1.2+"
    },
    "in_transit": {
        "api": "HTTPS only",
        "internal": "VPC endpoints"
    },
    "secrets": {
        "manager": "AWS Secrets Manager",
        "rotation": "30 days"
    }
}

# 数据脱敏
DATA_MASKING = {
    "pii_detection": True,
    "patterns": [
        r"\d{3}-\d{2}-\d{4}",  # SSN
        r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b"  # Email
    ],
    "replacement": "[REDACTED]"
}
```

## 8. 监控告警

### 8.1 指标定义

```python
# CloudWatch指标
METRICS = {
    "application": {
        "query_latency": "ms",
        "query_success_rate": "%",
        "document_processing_time": "s",
        "active_users": "count"
    },
    "infrastructure": {
        "lambda_invocations": "count",
        "lambda_errors": "count",
        "api_4xx_errors": "count",
        "api_5xx_errors": "count"
    },
    "business": {
        "queries_per_day": "count",
        "documents_processed": "count",
        "user_satisfaction": "score"
    }
}

# 告警阈值
ALARMS = {
    "high_latency": {
        "metric": "query_latency",
        "threshold": 3000,  # ms
        "evaluation_periods": 2
    },
    "error_rate": {
        "metric": "api_5xx_errors",
        "threshold": 10,
        "evaluation_periods": 1
    }
}
```

### 8.2 日志规范

```python
# 结构化日志格式
LOG_FORMAT = {
    "timestamp": "ISO8601",
    "level": "INFO|WARN|ERROR",
    "request_id": "uuid",
    "user_id": "string",
    "action": "string",
    "duration": "ms",
    "metadata": {}
}

# 日志级别
LOG_LEVELS = {
    "DEBUG": "开发环境详细日志",
    "INFO": "正常操作日志",
    "WARN": "潜在问题警告",
    "ERROR": "错误但服务可继续",
    "CRITICAL": "严重错误需立即处理"
}
```

## 9. 部署架构

### 9.1 环境配置

```yaml
environments:
  development:
    region: us-east-1
    instance_type: t3.medium
    min_capacity: 1
    max_capacity: 2
    
  staging:
    region: us-east-1
    instance_type: t3.large
    min_capacity: 2
    max_capacity: 5
    
  production:
    region: us-east-1
    instance_type: m5.xlarge
    min_capacity: 3
    max_capacity: 10
    multi_az: true
```

### 9.2 CI/CD流程

```yaml
pipeline:
  stages:
    - name: Source
      actions:
        - GitHub
        
    - name: Build
      actions:
        - CodeBuild
        - Unit Tests
        - Code Quality
        
    - name: Test
      actions:
        - Integration Tests
        - Load Tests
        - Security Scan
        
    - name: Deploy-Staging
      actions:
        - CDK Deploy
        - Smoke Tests
        
    - name: Deploy-Production
      actions:
        - Manual Approval
        - CDK Deploy
        - Health Check
```

## 10. 扩展性设计

### 10.1 插件架构

```python
# 插件接口定义
class RAGPlugin:
    def pre_process(self, query: str) -> str:
        """查询预处理"""
        pass
    
    def post_process(self, response: str) -> str:
        """响应后处理"""
        pass
    
    def custom_retrieval(self, query: str) -> List[Document]:
        """自定义检索逻辑"""
        pass

# 插件注册
PLUGINS = {
    "translation": TranslationPlugin(),
    "sentiment": SentimentAnalysisPlugin(),
    "summarization": SummarizationPlugin()
}
```

### 10.2 多模态支持

```python
# 多模态处理器
class MultiModalProcessor:
    def process_image(self, image: bytes) -> Dict:
        """图像处理和理解"""
        pass
    
    def process_audio(self, audio: bytes) -> Dict:
        """音频转文本"""
        pass
    
    def process_video(self, video: bytes) -> Dict:
        """视频内容提取"""
        pass
```

## 11. 成本优化

### 11.1 资源优化策略

```python
# Lambda配置优化
LAMBDA_OPTIMIZATION = {
    "memory": {
        "query_handler": 1024,  # MB
        "ingest_handler": 2048,
        "batch_handler": 3072
    },
    "timeout": {
        "query_handler": 30,  # 秒
        "ingest_handler": 300,
        "batch_handler": 900
    },
    "reserved_concurrency": {
        "query_handler": 100,
        "ingest_handler": 10,
        "batch_handler": 5
    }
}

# 成本监控
COST_MONITORING = {
    "budgets": {
        "monthly": 5000,  # USD
        "alerts": [50, 80, 100]  # 百分比
    },
    "optimization": {
        "spot_instances": True,
        "savings_plans": True,
        "reserved_capacity": False
    }
}
```

## 12. 灾难恢复

### 12.1 备份策略

```python
# 备份配置
BACKUP_CONFIG = {
    "frequency": {
        "vectors": "daily",
        "documents": "realtime",
        "metadata": "hourly"
    },
    "retention": {
        "daily": 7,
        "weekly": 4,
        "monthly": 12
    },
    "replication": {
        "cross_region": True,
        "regions": ["us-west-2", "eu-west-1"]
    }
}

# 恢复流程
RECOVERY_PROCEDURE = {
    "RTO": 4,  # 小时
    "RPO": 1,  # 小时
    "steps": [
        "切换到备用区域",
        "恢复向量数据库",
        "验证数据完整性",
        "更新DNS记录",
        "通知相关方"
    ]
}
```

## 附录：技术决策记录

| 决策 | 选择 | 理由 |
|------|------|------|
| 向量数据库 | Zilliz Cloud | 托管服务、高性能、自动扩展 |
| LLM服务 | AWS Bedrock | 无需管理基础设施、按需付费 |
| 计算平台 | AWS Lambda | 无服务器、自动扩展、成本优化 |
| RAG框架 | LangChain | 成熟生态、社区活跃、易于扩展 |
| 存储服务 | Amazon S3 | 高可用、低成本、与其他AWS服务集成 |
| API网关 | API Gateway | 托管服务、内置认证、流量管理 |
| 监控服务 | CloudWatch | 原生集成、统一监控、告警功能 |
| IaC工具 | AWS CDK | Python原生、类型安全、高级抽象 |