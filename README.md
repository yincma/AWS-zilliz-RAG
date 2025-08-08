# AWS-Zilliz-RAG 系统架构与数据流程

## 项目简介

基于 AWS 和 Zilliz 的企业级 RAG (Retrieval-Augmented Generation) 应用，采用标准 MVC 架构模式，使用 LangChain 框架实现高性能文档检索增强生成系统。

## 系统架构图

```mermaid
graph TB
    subgraph "客户端层"
        USER[用户界面]
        API_CLIENT[API客户端]
    end
    
    subgraph "View层 - 展示和响应"
        subgraph "Web前端视图"
            WEB_UI[React/Vue前端]
            STATIC[静态资源<br/>CSS/JS/Images]
            TEMPLATES[HTML模板]
        end
        subgraph "API视图"
            RESPONSE[响应格式化器]
            SERIALIZER[数据序列化器]
        end
        CDN[CloudFront CDN]
        S3_STATIC[S3静态托管]
    end
    
    subgraph "Controller层 - 请求处理和流程控制"
        GATEWAY[API Gateway]
        subgraph "Lambda处理器"
            RAG_CTRL[RAG控制器]
            DOC_CTRL[文档控制器]
            SEARCH_CTRL[搜索控制器]
            QUERY_HANDLER[查询处理器]
            INGEST_HANDLER[摄入处理器]
        end
    end
    
    subgraph "Model层 - 数据和业务逻辑"
        subgraph "核心模型"
            DOC_MODEL[文档模型<br/>- 加载解析<br/>- 文本分割<br/>- 元数据处理]
            EMB_MODEL[嵌入模型<br/>- Titan Embeddings<br/>- 向量生成<br/>- 批处理优化]
            VECTOR_MODEL[向量存储模型<br/>- Zilliz集成<br/>- 索引管理<br/>- 相似度搜索]
            LLM_MODEL[LLM模型<br/>- Bedrock Nova<br/>- 提示工程<br/>- 流式响应]
            RAG_CHAIN[RAG链模型<br/>- 检索策略<br/>- 上下文构建<br/>- 答案生成]
        end
    end
    
    subgraph "基础设施层"
        subgraph "AWS服务"
            BEDROCK[Amazon Bedrock]
            S3_DOCS[S3文档存储]
            LAMBDA[AWS Lambda]
            CLOUDWATCH[CloudWatch]
            SECRETS[Secrets Manager]
        end
        subgraph "向量数据库"
            ZILLIZ[Zilliz Cloud]
            COLLECTION[向量集合]
            INDEX[HNSW索引]
        end
    end
    
    %% 用户交互流
    USER --> WEB_UI
    API_CLIENT --> GATEWAY
    WEB_UI --> CDN
    CDN --> S3_STATIC
    
    %% Controller调度
    GATEWAY --> RAG_CTRL
    GATEWAY --> DOC_CTRL
    GATEWAY --> SEARCH_CTRL
    RAG_CTRL --> QUERY_HANDLER
    DOC_CTRL --> INGEST_HANDLER
    
    %% Model层交互
    QUERY_HANDLER --> RAG_CHAIN
    INGEST_HANDLER --> DOC_MODEL
    SEARCH_CTRL --> VECTOR_MODEL
    
    RAG_CHAIN --> EMB_MODEL
    RAG_CHAIN --> LLM_MODEL
    RAG_CHAIN --> VECTOR_MODEL
    
    %% 基础服务调用
    EMB_MODEL --> BEDROCK
    LLM_MODEL --> BEDROCK
    DOC_MODEL --> S3_DOCS
    VECTOR_MODEL --> ZILLIZ
    
    %% 响应返回
    RAG_CHAIN --> RESPONSE
    RESPONSE --> SERIALIZER
    SERIALIZER --> GATEWAY
    
    style USER fill:#e3f2fd
    style WEB_UI fill:#e1f5fe
    style GATEWAY fill:#fff3e0
    style RAG_CTRL fill:#fff3e0
    style DOC_MODEL fill:#f3e5f5
    style EMB_MODEL fill:#f3e5f5
    style LLM_MODEL fill:#f3e5f5
    style VECTOR_MODEL fill:#f3e5f5
    style RAG_CHAIN fill:#f3e5f5
    style BEDROCK fill:#e8f5e9
    style ZILLIZ fill:#fce4ec
```

## 数据流程图

### 1. 文档摄入流程（MVC分层）

```mermaid
sequenceDiagram
    participant User as 用户
    participant View as View层<br/>(Web UI)
    participant Controller as Controller层<br/>(Document Controller)
    participant Model as Model层<br/>(Document Model)
    participant Storage as 存储层<br/>(S3/Zilliz)
    participant AI as AI服务<br/>(Bedrock)
    
    User->>View: 上传文档
    View->>View: 文件验证
    Note over View: 格式检查<br/>大小限制
    
    View->>Controller: 提交文档请求
    Controller->>Controller: 请求验证
    Note over Controller: 权限检查<br/>配额验证
    
    Controller->>Model: 调用文档处理模型
    
    rect rgb(240, 250, 240)
        Note over Model: Model层处理流程
        Model->>Model: 文档解析
        Note right of Model: PDF/DOCX/TXT<br/>元数据提取
        
        Model->>Storage: 存储原始文档
        Storage-->>Model: 返回存储路径
        
        Model->>Model: 文档分割
        Note right of Model: LangChain分割器<br/>chunk_size: 1000<br/>overlap: 200
        
        Model->>AI: 批量生成向量
        Note over AI: Titan Embeddings<br/>Dimension: 1536
        AI-->>Model: 返回向量数组
        
        Model->>Storage: 存储向量到Zilliz
        Note over Storage: 创建索引<br/>更新元数据
        Storage-->>Model: 确认存储
    end
    
    Model-->>Controller: 返回处理结果
    Controller->>View: 格式化响应
    View-->>User: 显示处理状态
```

### 2. RAG查询处理流程（详细版）

```mermaid
sequenceDiagram
    participant User as 用户
    participant View as View层
    participant Controller as Controller层<br/>(RAG Controller)
    participant Model as Model层
    participant Cache as 缓存层
    participant Vector as 向量数据库<br/>(Zilliz)
    participant LLM as LLM服务<br/>(Bedrock Nova)
    
    User->>View: 输入查询
    View->>View: 输入验证
    View->>Controller: 发送查询请求
    
    Controller->>Cache: 检查缓存
    alt 缓存命中
        Cache-->>Controller: 返回缓存结果
        Controller->>View: 直接返回
    else 缓存未命中
        Controller->>Model: 调用RAG链
        
        rect rgb(250, 240, 250)
            Note over Model: RAG处理链
            Model->>Model: 查询预处理
            Note right of Model: 查询改写<br/>关键词提取
            
            Model->>LLM: 生成查询向量
            LLM-->>Model: Embedding向量
            
            Model->>Vector: 向量检索
            Note over Vector: HNSW索引<br/>Top-K: 10<br/>Score阈值: 0.7
            Vector-->>Model: 相关文档块
            
            Model->>Model: 重排序
            Note right of Model: Cross-encoder<br/>多样性优化
            
            Model->>Model: 构建上下文
            Note right of Model: 提示模板<br/>文档拼接<br/>元数据注入
            
            Model->>LLM: 生成回答
            Note over LLM: Nova模型<br/>Temperature: 0.7<br/>Max tokens: 2000
            LLM-->>Model: 流式响应
            
            Model->>Model: 后处理
            Note right of Model: 引用标注<br/>格式优化
        end
        
        Model-->>Controller: 返回结果
        Controller->>Cache: 更新缓存
        Controller->>View: 格式化响应
    end
    
    View->>View: 渲染结果
    View-->>User: 展示回答
```

### 3. 增量学习流程

```mermaid
sequenceDiagram
    participant Admin as 管理员
    participant System as 系统调度器
    participant Analytics as 分析模块
    participant Model as Model层
    participant Vector as Zilliz
    participant Monitor as 监控系统
    
    System->>Analytics: 定时触发分析
    Analytics->>Vector: 查询使用统计
    Vector-->>Analytics: 返回查询日志
    
    Analytics->>Analytics: 分析查询模式
    Note over Analytics: 高频查询识别<br/>失败查询分析<br/>响应时间统计
    
    alt 发现知识空白
        Analytics->>Admin: 推送改进建议
        Admin->>Model: 上传补充文档
        Model->>Model: 处理新文档
        Model->>Vector: 更新向量库
    else 发现性能问题
        Analytics->>Vector: 优化索引
        Note over Vector: 重建索引<br/>调整参数
        Vector->>Monitor: 报告优化结果
    end
    
    Monitor->>System: 更新系统状态
    System->>Admin: 发送报告
```

## 核心组件说明

### MVC 架构层次详解

| 层次 | 职责 | 主要组件 | 技术实现 |
|------|------|----------|----------|
| **View (视图层)** | 用户界面和数据展示 | • Web前端组件<br/>• API响应格式化器<br/>• 模板引擎<br/>• 静态资源管理 | • React/Vue.js<br/>• Jinja2模板<br/>• JSON序列化<br/>• CDN优化 |
| **Controller (控制器层)** | 请求处理和业务流程控制 | • RAG控制器<br/>• 文档控制器<br/>• 搜索控制器<br/>• Lambda处理器 | • API Gateway路由<br/>• Lambda函数<br/>• 请求验证<br/>• 流程编排 |
| **Model (模型层)** | 数据处理和业务逻辑 | • 文档模型<br/>• 嵌入模型<br/>• 向量存储模型<br/>• LLM模型<br/>• RAG链模型 | • LangChain<br/>• Bedrock SDK<br/>• Zilliz客户端<br/>• Boto3 |

### 技术栈详细配置

#### Amazon Bedrock 配置
```yaml
LLM配置:
  模型: amazon.nova-pro-v1:0
  参数:
    temperature: 0.7
    max_tokens: 2000
    top_p: 0.9
    top_k: 40

Embedding配置:
  模型: amazon.titan-embed-image-v1
  参数:
    dimension: 1536
    batch_size: 100
    normalize: true
```

#### Zilliz Cloud 向量数据库
```yaml
集合配置:
  名称: rag_documents
  向量维度: 1536
  距离度量: IP (内积)
  
索引配置:
  类型: HNSW
  参数:
    M: 16              # 连接数
    ef_construction: 200  # 构建时的搜索范围
    ef_search: 100       # 查询时的搜索范围

分片配置:
  分片数: 2
  副本数: 1
```

#### AWS Lambda 函数配置
```yaml
运行时配置:
  runtime: python3.9
  内存: 3008 MB
  超时: 300 秒
  并发: 100

环境变量:
  BEDROCK_REGION: us-east-1
  ZILLIZ_ENDPOINT: ${ZILLIZ_ENDPOINT}
  S3_BUCKET: ${DOCUMENT_BUCKET}
  LOG_LEVEL: INFO

层配置:
  - langchain-layer
  - numpy-scipy-layer
  - aws-sdk-layer
```

## 数据流特点

### 异步处理架构
```mermaid
graph LR
    subgraph "异步任务队列"
        SQS[SQS队列] --> BATCH[批处理器]
        BATCH --> WORKER1[Worker 1]
        BATCH --> WORKER2[Worker 2]
        BATCH --> WORKER3[Worker N]
    end
    
    subgraph "处理监控"
        WORKER1 --> METRICS[CloudWatch Metrics]
        WORKER2 --> METRICS
        WORKER3 --> METRICS
        METRICS --> ALARM[告警系统]
    end
    
    style SQS fill:#ffd54f
    style METRICS fill:#a5d6a7
```

### 缓存策略分层
| 缓存层级 | 缓存内容 | TTL | 实现技术 |
|----------|----------|-----|----------|
| **CDN缓存** | 静态资源、API响应 | 24小时 | CloudFront |
| **应用缓存** | 热点查询结果 | 15分钟 | Lambda内存/Redis |
| **向量缓存** | 高频向量检索 | 1小时 | Zilliz内存缓存 |
| **模型缓存** | LLM预测结果 | 30分钟 | DynamoDB |

### 基础设施即代码（CDK Stack）

```yaml
栈结构:
  BaseStack:                 # 基础资源栈
    - VPC和网络配置
    - IAM角色和策略
    - KMS密钥
    
  DataStack:                 # 数据层栈
    - S3存储桶
    - DynamoDB表
    - SQS队列
    
  ComputeStack:              # 计算层栈
    - Lambda函数
    - Lambda层
    - Step Functions
    
  APIStack:                  # API层栈
    - API Gateway
    - CloudFront分发
    - WAF规则
    
```

## 扩展性设计

- **水平扩展**: Lambda 自动扩展，Zilliz 分片
- **负载均衡**: API Gateway 自动负载均衡

## 关键决策点

### 技术选型理由

| 技术选择 | 选择理由 | 备选方案 |
|----------|----------|----------|
| **Amazon Bedrock** | • 无需GPU管理<br/>• 按需付费<br/>• 多模型支持 | OpenAI API, 自托管LLM |
| **Zilliz Cloud** | • 托管服务<br/>• 高性能HNSW<br/>• 自动扩展 | Pinecone, Weaviate, 自建Milvus |
| **LangChain** | • 成熟框架<br/>• 丰富生态<br/>• 活跃社区 | LlamaIndex, 自研框架 |
| **AWS Lambda** | • 无服务器<br/>• 自动扩展<br/>• 成本优化 | ECS, EC2, Kubernetes |
| **MVC架构** | • 清晰分层<br/>• 易于维护<br/>• 团队协作 | 微服务, 单体架构 |

## 项目交付物

- ✅ **架构文档**：完整的系统架构和数据流程图
- ✅ **MVC代码结构**：标准化的三层架构实现
- ✅ **CDK基础设施**：可重复部署的IaC代码
- ✅ **部署指南**：详细的部署和配置步骤

---

*本文档使用 Mermaid 图表语法，可在支持 Mermaid 的 Markdown 查看器中正确渲染。*
*最后更新：2025年8月*