# AWS-Zilliz-RAG 系统架构与数据流程

## 项目简介

基于 AWS 和 Zilliz 的 RAG (Retrieval-Augmented Generation) 应用，采用 MVC 架构模式，使用 LangChain 框架实现文档检索增强生成。

## 系统架构图

```mermaid
graph TB
    subgraph "前端层 (View Layer)"
        A[Web浏览器] --> B[CloudFront CDN]
        B --> C[S3 静态网站托管]
        C --> D[HTML/CSS/JS]
    end
    
    subgraph "API层 (Controller Layer)"
        E[API Gateway] --> F[Lambda Functions]
        F --> F1[Query Handler]
        F --> F2[Ingest Handler]
        F --> F3[Search Controller]
        F --> F4[Document Controller]
    end
    
    subgraph "业务逻辑层 (Model Layer)"
        G[RAG Chain Model]
        H[Document Model]
        I[Embedding Model]
        J[LLM Model]
        K[Vector Store Model]
    end
    
    subgraph "AWS服务"
        L[Amazon Bedrock]
        L --> L1[Nova LLM]
        L --> L2[Titan Embeddings]
        M[Amazon S3]
        M --> M1[文档存储桶]
    end
    
    subgraph "外部服务"
        N[Zilliz Cloud]
        N --> N1[Vector Database]
        N --> N2[Collection Management]
    end
    
    A --> E
    F1 --> G
    F2 --> H
    F3 --> K
    F4 --> H
    
    G --> I
    G --> J
    G --> K
    
    I --> L2
    J --> L1
    H --> M1
    K --> N1
    
    style A fill:#e1f5fe
    style B fill:#e1f5fe
    style C fill:#e1f5fe
    style D fill:#e1f5fe
    style E fill:#fff3e0
    style F fill:#fff3e0
    style G fill:#f3e5f5
    style H fill:#f3e5f5
    style I fill:#f3e5f5
    style J fill:#f3e5f5
    style K fill:#f3e5f5
    style L fill:#e8f5e9
    style M fill:#e8f5e9
    style N fill:#fce4ec
```

## 数据流程图

### 1. 文档摄入流程

```mermaid
sequenceDiagram
    participant User as 用户
    participant API as API Gateway
    participant Lambda as Lambda Handler
    participant S3 as S3 Bucket
    participant Bedrock as Amazon Bedrock
    participant Zilliz as Zilliz Cloud
    
    User->>API: 上传文档
    API->>Lambda: 触发 Ingest Handler
    Lambda->>S3: 存储原始文档
    S3-->>Lambda: 返回文档URL
    
    Lambda->>Lambda: 文档分割处理
    Note over Lambda: 使用 LangChain<br/>文档加载器和分割器
    
    Lambda->>Bedrock: 请求 Titan Embeddings
    Bedrock-->>Lambda: 返回向量化结果
    
    Lambda->>Zilliz: 存储向量和元数据
    Zilliz-->>Lambda: 确认存储成功
    
    Lambda-->>API: 返回处理结果
    API-->>User: 显示上传成功
```

### 2. 查询处理流程

```mermaid
sequenceDiagram
    participant User as 用户
    participant Web as Web前端
    participant API as API Gateway
    participant Lambda as Query Handler
    participant Bedrock as Amazon Bedrock
    participant Zilliz as Zilliz Cloud
    participant S3 as S3 Bucket
    
    User->>Web: 输入查询问题
    Web->>API: 发送查询请求
    API->>Lambda: 触发 Query Handler
    
    Lambda->>Bedrock: 生成查询向量
    Note over Bedrock: Titan Embeddings
    Bedrock-->>Lambda: 返回查询向量
    
    Lambda->>Zilliz: 向量相似度搜索
    Note over Zilliz: Top-K 检索
    Zilliz-->>Lambda: 返回相关文档ID和分数
    
    Lambda->>S3: 获取文档内容
    S3-->>Lambda: 返回文档片段
    
    Lambda->>Lambda: 构建增强上下文
    Note over Lambda: 组合查询和检索结果
    
    Lambda->>Bedrock: 请求 Nova LLM 生成回答
    Note over Bedrock: 基于上下文生成
    Bedrock-->>Lambda: 返回生成的回答
    
    Lambda-->>API: 返回响应结果
    API-->>Web: 展示回答和来源
    Web-->>User: 显示结果
```

## 核心组件说明

### MVC 架构层次

| 层次 | 职责 | 主要组件 |
|------|------|----------|
| **View (视图层)** | 用户界面和数据展示 | Web前端、API响应格式化、模板渲染 |
| **Controller (控制器层)** | 请求处理和流程控制 | Lambda处理器、路由管理、业务流程协调 |
| **Model (模型层)** | 数据和业务逻辑 | 向量存储、LLM集成、文档处理、Embedding生成 |

### AWS 服务集成

| 服务 | 用途 | 配置要点 |
|------|------|----------|
| **Amazon Bedrock** | LLM推理和向量化 | Nova模型用于生成，Titan用于Embedding |
| **Amazon S3** | 文档和静态资源存储 | 分离文档存储桶和前端资源桶 |
| **AWS Lambda** | 无服务器API处理 | Python 3.9运行时，配置适当的内存和超时 |
| **API Gateway** | RESTful API管理 | 配置CORS、认证、限流策略 |
| **CloudFront** | CDN分发 | 缓存策略优化，边缘位置选择 |

### 向量数据库 (Zilliz Cloud)

| 特性 | 说明 |
|------|------|
| **Collection** | 存储文档向量和元数据 |
| **Index Type** | IVF_FLAT 或 HNSW |
| **Metric Type** | L2 或 IP (内积) |
| **Dimension** | 1536 (Titan Embeddings) |

## 数据流特点

### 异步处理
- 文档摄入采用异步处理，支持大批量文档
- 使用 SQS 队列管理处理任务

### 缓存策略
- CloudFront 缓存静态资源
- Lambda 内存缓存热点查询
- Zilliz 缓存频繁访问的向量

### 错误处理
- Lambda 死信队列 (DLQ)
- S3 多版本控制
- API Gateway 错误映射

## 部署架构

```mermaid
graph LR
    subgraph "开发环境"
        A1[本地开发] --> A2[单元测试]
        A2 --> A3[集成测试]
    end
    
    subgraph "CI/CD Pipeline"
        B1[GitHub] --> B2[GitHub Actions]
        B2 --> B3[AWS CDK]
        B3 --> B4[CloudFormation]
    end
    
    subgraph "AWS 环境"
        C1[Dev Stack] --> C2[Staging Stack]
        C2 --> C3[Production Stack]
    end
    
    A3 --> B1
    B4 --> C1
    
    style A1 fill:#e3f2fd
    style B1 fill:#fff9c4
    style C1 fill:#c8e6c9
```

## 监控与日志

```mermaid
graph TB
    subgraph "监控指标"
        A[CloudWatch Metrics]
        A --> A1[Lambda执行时间]
        A --> A2[API延迟]
        A --> A3[错误率]
        A --> A4[向量搜索性能]
    end
    
    subgraph "日志管理"
        B[CloudWatch Logs]
        B --> B1[Lambda函数日志]
        B --> B2[API Gateway日志]
        B --> B3[应用日志]
    end
    
    subgraph "告警"
        C[CloudWatch Alarms]
        C --> C1[高错误率告警]
        C --> C2[性能降级告警]
        C --> C3[资源使用告警]
    end
    
    subgraph "追踪"
        D[X-Ray Tracing]
        D --> D1[请求追踪]
        D --> D2[性能分析]
        D --> D3[依赖映射]
    end
```

## 安全架构

```mermaid
graph TB
    subgraph "认证授权"
        A[AWS IAM] --> A1[Lambda执行角色]
        A --> A2[用户访问控制]
        B[API Keys] --> B1[API访问控制]
    end
    
    subgraph "网络安全"
        C[VPC] --> C1[私有子网]
        C --> C2[安全组]
        D[CloudFront] --> D1[DDoS防护]
        D --> D2[WAF规则]
    end
    
    subgraph "数据安全"
        E[加密] --> E1[S3加密存储]
        E --> E2[传输加密 TLS]
        E --> E3[Zilliz数据加密]
        F[密钥管理] --> F1[AWS KMS]
        F --> F2[Secrets Manager]
    end
    
    style A fill:#ffebee
    style C fill:#e8f5e9
    style E fill:#e3f2fd
```

## 性能优化策略

| 优化领域 | 策略 | 预期效果 |
|----------|------|----------|
| **向量检索** | 使用 HNSW 索引，优化 ef_construction 参数 | 检索速度提升 50% |
| **文档处理** | 批量处理，并行化 Embedding 生成 | 处理吞吐量提升 3x |
| **API响应** | Lambda 预热，连接池复用 | 冷启动时间减少 70% |
| **前端加载** | CloudFront 缓存，资源压缩 | 页面加载时间减少 60% |
| **模型推理** | Bedrock 模型缓存，批量请求 | 推理成本降低 40% |

## 扩展性设计

- **水平扩展**: Lambda 自动扩展，Zilliz 分片
- **垂直扩展**: 增加 Lambda 内存，升级 Bedrock 配额
- **多区域部署**: CloudFront 全球分发，多区域 S3 复制
- **负载均衡**: API Gateway 自动负载均衡

## 成本优化

- **按需付费**: Lambda 和 Bedrock 按使用量计费
- **预留容量**: Zilliz 预留实例折扣
- **生命周期管理**: S3 智能分层存储
- **监控优化**: 基于 CloudWatch 指标调整资源

---

*本文档使用 Mermaid 图表语法，可在支持 Mermaid 的 Markdown 查看器中正确渲染。*