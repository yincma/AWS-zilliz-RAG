# 架构图表文档

## 1. 系统总体架构图

```mermaid
graph TB
    subgraph "用户层"
        U[用户] --> WEB[Web界面]
        U --> API[API客户端]
    end
    
    subgraph "CDN层"
        WEB --> CF[CloudFront]
        CF --> S3W[S3 静态网站]
    end
    
    subgraph "API网关层"
        API --> APIG[API Gateway]
        CF --> APIG
    end
    
    subgraph "控制器层 - Lambda"
        APIG --> LQ[Query Handler Lambda]
        APIG --> LD[Document Handler Lambda]
        APIG --> LS[Search Handler Lambda]
    end
    
    subgraph "模型层"
        LQ --> BEDROCK[Amazon Bedrock]
        LQ --> ZILLIZ[Zilliz Cloud]
        LD --> S3D[S3 文档存储]
        LD --> BEDROCK
        LD --> ZILLIZ
        LS --> ZILLIZ
    end
    
    subgraph "数据存储层"
        ZILLIZ --> VDB[(向量数据库)]
        S3D --> DOC[(文档存储)]
        LQ --> DDB[DynamoDB]
        LD --> DDB
        DDB --> META[(元数据)]
    end
    
    subgraph "监控层"
        LQ --> CW[CloudWatch]
        LD --> CW
        LS --> CW
        CW --> ALARM[告警]
    end
```

## 2. MVC架构详细图

```mermaid
graph LR
    subgraph "View层"
        V1[Web Templates]
        V2[Static Assets]
        V3[API Responses]
        V4[Serializers]
    end
    
    subgraph "Controller层"
        C1[RAG Controller]
        C2[Document Controller]
        C3[Search Controller]
        C4[Lambda Handlers]
    end
    
    subgraph "Model层"
        M1[Document Model]
        M2[Embedding Model]
        M3[Vector Store Model]
        M4[LLM Model]
        M5[RAG Chain Model]
    end
    
    V1 --> C1
    V2 --> C1
    V3 --> C1
    V4 --> C1
    
    C1 --> M1
    C1 --> M2
    C1 --> M3
    C1 --> M4
    C1 --> M5
    
    C2 --> M1
    C2 --> M2
    C2 --> M3
    
    C3 --> M3
    C3 --> M4
    
    C4 --> C1
    C4 --> C2
    C4 --> C3
```

## 3. RAG处理流程图

```mermaid
flowchart TD
    Start([用户查询]) --> A[接收查询请求]
    A --> B{查询缓存}
    B -->|命中| C[返回缓存结果]
    B -->|未命中| D[查询预处理]
    D --> E[生成查询向量]
    E --> F[向量检索]
    F --> G[关键词检索]
    F --> H[语义检索]
    G --> I[结果融合]
    H --> I
    I --> J[重排序]
    J --> K[构建上下文]
    K --> L[LLM生成答案]
    L --> M[格式化响应]
    M --> N[更新缓存]
    N --> End([返回结果])
    C --> End
```

## 4. 文档处理流程图

```mermaid
flowchart LR
    subgraph "文档摄入"
        A[上传文档] --> B[文件验证]
        B --> C[存储到S3]
        C --> D[触发Lambda]
    end
    
    subgraph "文档处理"
        D --> E[文档解析]
        E --> F[文本提取]
        F --> G[文本清洗]
        G --> H[智能分块]
    end
    
    subgraph "向量化"
        H --> I[批量编码]
        I --> J[生成向量]
        J --> K[向量优化]
    end
    
    subgraph "存储"
        K --> L[存储到Zilliz]
        K --> M[缓存到S3]
        L --> N[更新索引]
        M --> O[更新元数据]
    end
    
    N --> P[完成通知]
    O --> P
```

## 5. 部署架构图

```mermaid
graph TB
    subgraph "开发环境"
        DEV[开发者] --> GIT[GitHub]
    end
    
    subgraph "CI/CD Pipeline"
        GIT --> CB[CodeBuild]
        CB --> TEST[自动测试]
        TEST --> SQ[代码质量检查]
        SQ --> SEC[安全扫描]
    end
    
    subgraph "部署阶段"
        SEC --> STG[Staging环境]
        STG --> SMOKE[冒烟测试]
        SMOKE --> APPROVE{人工审批}
        APPROVE -->|通过| PROD[生产环境]
        APPROVE -->|拒绝| ROLLBACK[回滚]
    end
    
    subgraph "AWS CDK部署"
        PROD --> CDK[CDK Deploy]
        CDK --> STACK1[Web Stack]
        CDK --> STACK2[API Stack]
        CDK --> STACK3[Data Stack]
    end
    
    subgraph "监控"
        STACK1 --> MON[CloudWatch]
        STACK2 --> MON
        STACK3 --> MON
        MON --> ALERT[告警系统]
    end
```

## 6. 数据流图

```mermaid
graph LR
    subgraph "输入"
        DOC[文档]
        QUERY[查询]
    end
    
    subgraph "处理层"
        DOC --> CHUNK[分块处理]
        CHUNK --> EMB[向量化]
        QUERY --> QEMB[查询向量化]
    end
    
    subgraph "存储层"
        EMB --> ZILLIZ[(Zilliz)]
        EMB --> S3[(S3)]
        CHUNK --> DDB[(DynamoDB)]
    end
    
    subgraph "检索层"
        QEMB --> SEARCH[向量搜索]
        SEARCH --> ZILLIZ
        SEARCH --> RANK[结果排序]
    end
    
    subgraph "生成层"
        RANK --> CTX[上下文构建]
        CTX --> LLM[Bedrock LLM]
        LLM --> RESP[响应生成]
    end
    
    RESP --> OUTPUT[输出结果]
```

## 7. 安全架构图

```mermaid
graph TB
    subgraph "外部访问"
        USER[用户] --> WAF[AWS WAF]
        WAF --> CF[CloudFront]
    end
    
    subgraph "认证授权"
        CF --> AUTH[API Gateway认证]
        AUTH --> IAM[IAM角色]
    end
    
    subgraph "网络安全"
        IAM --> VPC[VPC]
        VPC --> SG[安全组]
        SG --> NACL[网络ACL]
    end
    
    subgraph "数据安全"
        NACL --> ENC1[S3加密]
        NACL --> ENC2[DynamoDB加密]
        NACL --> ENC3[传输加密TLS]
    end
    
    subgraph "密钥管理"
        ENC1 --> KMS[AWS KMS]
        ENC2 --> KMS
        ENC3 --> KMS
        KMS --> SM[Secrets Manager]
    end
    
    subgraph "审计"
        ALL[所有服务] --> TRAIL[CloudTrail]
        TRAIL --> LOG[日志分析]
    end
```

## 8. 扩展性架构图

```mermaid
graph TD
    subgraph "负载均衡"
        LB[Application Load Balancer]
    end
    
    subgraph "自动扩展"
        LB --> ASG[Auto Scaling Group]
        ASG --> L1[Lambda 1]
        ASG --> L2[Lambda 2]
        ASG --> L3[Lambda N]
    end
    
    subgraph "数据分片"
        L1 --> P1[Zilliz分区1]
        L2 --> P2[Zilliz分区2]
        L3 --> P3[Zilliz分区N]
    end
    
    subgraph "缓存层"
        L1 --> CACHE[ElastiCache]
        L2 --> CACHE
        L3 --> CACHE
    end
    
    subgraph "队列"
        HEAVY[重负载] --> SQS[SQS队列]
        SQS --> BATCH[批处理Lambda]
    end
```

## 9. 监控告警架构

```mermaid
graph LR
    subgraph "指标收集"
        APP[应用指标] --> CW[CloudWatch]
        INFRA[基础设施指标] --> CW
        CUSTOM[自定义指标] --> CW
    end
    
    subgraph "日志聚合"
        LOGS[应用日志] --> CWL[CloudWatch Logs]
        CWL --> INSIGHTS[Logs Insights]
    end
    
    subgraph "告警"
        CW --> ALARM[CloudWatch Alarms]
        ALARM --> SNS[SNS主题]
    end
    
    subgraph "通知"
        SNS --> EMAIL[邮件]
        SNS --> SLACK[Slack]
        SNS --> PAGER[PagerDuty]
    end
    
    subgraph "仪表板"
        CW --> DASH[CloudWatch Dashboard]
        INSIGHTS --> DASH
    end
```

## 10. 灾难恢复架构

```mermaid
graph TB
    subgraph "主区域 us-east-1"
        PROD1[生产环境]
        DATA1[主数据存储]
        PROD1 --> DATA1
    end
    
    subgraph "备份策略"
        DATA1 --> BACKUP[自动备份]
        BACKUP --> S3REP[S3跨区域复制]
        BACKUP --> SNAPSHOT[数据库快照]
    end
    
    subgraph "备用区域 us-west-2"
        STANDBY[待机环境]
        DATA2[备用数据存储]
        S3REP --> DATA2
        SNAPSHOT --> DATA2
    end
    
    subgraph "故障转移"
        MONITOR[健康检查] --> DETECT{故障检测}
        DETECT -->|故障| FAILOVER[自动故障转移]
        FAILOVER --> R53[Route53 DNS切换]
        R53 --> STANDBY
    end
    
    subgraph "恢复"
        STANDBY --> RECOVER[数据恢复]
        RECOVER --> SYNC[数据同步]
        SYNC --> PROD1
    end
```

## 11. 性能优化架构

```mermaid
graph TD
    subgraph "请求优化"
        REQ[用户请求] --> CDN[CDN缓存]
        CDN --> COMPRESS[响应压缩]
    end
    
    subgraph "计算优化"
        COMPRESS --> PARALLEL[并行处理]
        PARALLEL --> ASYNC[异步执行]
        ASYNC --> BATCH[批量操作]
    end
    
    subgraph "存储优化"
        BATCH --> INDEX[索引优化]
        INDEX --> PARTITION[数据分区]
        PARTITION --> CACHE[多级缓存]
    end
    
    subgraph "缓存策略"
        CACHE --> L1[内存缓存]
        CACHE --> L2[Redis缓存]
        CACHE --> L3[S3缓存]
    end
    
    subgraph "查询优化"
        L1 --> PRECOMPUTE[预计算]
        L2 --> PREFETCH[预取]
        L3 --> LAZY[延迟加载]
    end
```

## 12. 成本优化架构

```mermaid
graph LR
    subgraph "计算成本优化"
        LAMBDA[Lambda] --> RESERVED[预留并发]
        LAMBDA --> SPOT[Spot实例]
    end
    
    subgraph "存储成本优化"
        S3 --> LIFECYCLE[生命周期策略]
        LIFECYCLE --> IA[Infrequent Access]
        LIFECYCLE --> GLACIER[Glacier]
    end
    
    subgraph "数据传输优化"
        TRANSFER[数据传输] --> ENDPOINT[VPC端点]
        ENDPOINT --> COMPRESS2[压缩传输]
    end
    
    subgraph "资源调度"
        SCHEDULE[调度器] --> SCALE[自动缩放]
        SCALE --> OFF[非高峰关闭]
    end
    
    subgraph "成本监控"
        BUDGET[预算告警] --> OPTIMIZE[优化建议]
        OPTIMIZE --> ACTION[执行优化]
    end
```

## 图表说明

### 使用说明
1. **系统总体架构图**：展示整个RAG系统的宏观架构
2. **MVC架构详细图**：详细说明MVC三层的组件关系
3. **RAG处理流程图**：描述查询处理的完整流程
4. **文档处理流程图**：说明文档从上传到向量化的流程
5. **部署架构图**：CI/CD和部署流程
6. **数据流图**：数据在系统中的流转路径
7. **安全架构图**：安全防护的多层架构
8. **扩展性架构图**：系统如何实现水平扩展
9. **监控告警架构**：监控和告警系统设计
10. **灾难恢复架构**：高可用和灾难恢复策略
11. **性能优化架构**：性能优化的多个层面
12. **成本优化架构**：成本控制和优化策略

### 技术栈映射
- **前端**：CloudFront + S3
- **API层**：API Gateway + Lambda
- **业务逻辑**：Lambda Functions (Python)
- **AI服务**：Amazon Bedrock
- **向量数据库**：Zilliz Cloud
- **对象存储**：Amazon S3
- **元数据存储**：DynamoDB
- **监控**：CloudWatch
- **IaC**：AWS CDK