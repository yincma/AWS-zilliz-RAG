# AWS部署指南

## 前置要求

1. **AWS账户**：需要有AWS账户和适当权限
2. **AWS CLI**：安装并配置AWS CLI
3. **Node.js**：需要Node.js 14.x或更高版本（用于CDK）
4. **Python**：Python 3.9或更高版本
5. **Zilliz账户**：注册Zilliz Cloud并创建集群

## 配置步骤

### 1. 设置AWS凭证

```bash
# 配置AWS CLI
aws configure

# 或使用环境变量
export AWS_ACCESS_KEY_ID=your-access-key
export AWS_SECRET_ACCESS_KEY=your-secret-key
export AWS_REGION=us-east-1
```

### 2. 配置Zilliz

1. 登录[Zilliz Cloud](https://cloud.zilliz.com)
2. 创建新集群或使用现有集群
3. 获取连接端点和API密钥
4. 创建集合（Collection）

### 3. 设置环境变量

```bash
# 复制环境变量模板
cp env.example .env

# 编辑.env文件，填入实际值
vi .env

# 加载环境变量
source .env
```

必需的环境变量：
- `ZILLIZ_ENDPOINT`: Zilliz集群端点
- `ZILLIZ_TOKEN`: Zilliz API密钥
- `BEDROCK_MODEL_ID`: Bedrock模型ID（默认：amazon.nova-pro-v1:0）
- `EMBEDDING_MODEL_ID`: 嵌入模型ID（默认：amazon.titan-embed-image-v1）

### 4. 安装CDK

```bash
# 全局安装AWS CDK
npm install -g aws-cdk

# 验证安装
cdk --version
```

### 5. 构建Lambda层

```bash
cd infrastructure/lambda_layer
./build_layer.sh
cd ../..
```

## 部署流程

### 1. 一键部署

```bash
# 运行部署脚本
./scripts/deploy.sh

# 选择部署阶段（dev/staging/prod）
# 脚本会自动：
# - 安装依赖
# - 引导CDK环境
# - 合成CloudFormation模板
# - 部署所有栈
# - 输出访问URL
```

### 2. 手动部署

```bash
cd infrastructure

# 安装Python依赖
pip3 install -r requirements.txt

# 引导CDK（首次使用）
cdk bootstrap

# 合成CloudFormation模板
cdk synth

# 部署数据栈
cdk deploy RAG-Data-dev

# 部署API栈
cdk deploy RAG-API-dev \
  --parameters BedrockModelId=$BEDROCK_MODEL_ID \
  --parameters EmbeddingModelId=$EMBEDDING_MODEL_ID \
  --parameters ZillizEndpoint=$ZILLIZ_ENDPOINT \
  --parameters ZillizToken=$ZILLIZ_TOKEN

# 部署Web栈
cdk deploy RAG-Web-dev
```

### 3. 验证部署

部署完成后，获取访问URL：

```bash
# 获取Web界面URL
aws cloudformation describe-stacks \
  --stack-name RAG-Web-dev \
  --query "Stacks[0].Outputs[?OutputKey=='DistributionUrl'].OutputValue" \
  --output text

# 获取API端点
aws cloudformation describe-stacks \
  --stack-name RAG-API-dev \
  --query "Stacks[0].Outputs[?OutputKey=='ApiUrl'].OutputValue" \
  --output text
```

## 部署架构

```
┌─────────────────────────────────────────┐
│           CloudFront CDN                │
│         (全球内容分发网络)                │
└─────────────┬───────────────────────────┘
              │
              ▼
┌─────────────────────────────────────────┐
│          S3 Static Website              │
│      (React前端应用托管)                  │
└─────────────────────────────────────────┘
              │
              ▼
┌─────────────────────────────────────────┐
│         API Gateway REST API            │
│         (RESTful API端点)                │
└─────────────┬───────────────────────────┘
              │
              ▼
┌─────────────────────────────────────────┐
│          Lambda Functions               │
│   ┌──────────────┐  ┌──────────────┐   │
│   │ Query Handler│  │Ingest Handler│   │
│   └──────────────┘  └──────────────┘   │
└─────────────┬───────────────────────────┘
              │
              ▼
┌─────────────────────────────────────────┐
│         External Services               │
│  ┌─────────────┐     ┌──────────────┐  │
│  │   Bedrock   │     │    Zilliz    │  │
│  │  (LLM/Embed)│     │ (Vector DB)  │  │
│  └─────────────┘     └──────────────┘  │
└─────────────────────────────────────────┘
```

## 成本估算

基于典型使用场景（每月）：

| 服务 | 用量 | 预估成本 |
|------|------|----------|
| Lambda | 10,000次调用 | $2 |
| API Gateway | 10,000请求 | $3.5 |
| S3 | 10GB存储 + 1GB传输 | $0.5 |
| CloudFront | 10GB传输 | $1 |
| Bedrock | 100K tokens | $10 |
| Zilliz | Starter集群 | $65 |
| **总计** | | **~$82/月** |

## 监控和日志

### CloudWatch日志组

- `/aws/lambda/rag-query-{stage}`: 查询函数日志
- `/aws/lambda/rag-ingest-{stage}`: 摄入函数日志
- `/aws/apigateway/rag-api-{stage}`: API Gateway日志

### 查看日志

```bash
# 查看查询函数日志
aws logs tail /aws/lambda/rag-query-dev --follow

# 查看最近错误
aws logs filter-log-events \
  --log-group-name /aws/lambda/rag-query-dev \
  --filter-pattern "ERROR"
```

### CloudWatch指标

自动收集的指标：
- Lambda调用次数、错误率、持续时间
- API Gateway请求数、4XX/5XX错误
- S3请求数、带宽使用

## 故障排除

### 常见问题

1. **CDK引导失败**
   ```bash
   # 确保有正确的AWS权限
   aws sts get-caller-identity
   
   # 手动创建引导栈
   cdk bootstrap aws://ACCOUNT-ID/REGION
   ```

2. **Lambda超时**
   - 检查Zilliz连接
   - 增加Lambda超时设置（默认30秒）
   - 优化查询参数（减少top_k）

3. **CORS错误**
   - 确保API Gateway配置了CORS
   - 检查Lambda响应头包含Access-Control-Allow-Origin

4. **Zilliz连接失败**
   - 验证端点URL格式正确
   - 检查API密钥有效性
   - 确保集群状态为Running

## 清理资源

删除所有部署的资源：

```bash
# 删除所有栈
cdk destroy --all

# 或单独删除
cdk destroy RAG-Web-dev
cdk destroy RAG-API-dev
cdk destroy RAG-Data-dev

# 清理S3存储桶（如果有内容）
aws s3 rm s3://rag-documents-{account}-{region} --recursive
aws s3 rm s3://rag-web-{account}-{region} --recursive
```

## 更新部署

更新代码后重新部署：

```bash
# 更新Lambda代码
cd infrastructure
cdk deploy RAG-API-dev

# 更新前端
cd app/views/web
# 构建前端（如果需要）
npm run build
# 部署
cd ../../../infrastructure
cdk deploy RAG-Web-dev
```

## 安全最佳实践

1. **密钥管理**
   - 使用AWS Secrets Manager存储敏感信息
   - 避免在代码中硬编码密钥

2. **访问控制**
   - 配置API Gateway API密钥
   - 使用AWS IAM角色和策略

3. **网络安全**
   - 启用CloudFront HTTPS
   - 配置WAF规则（可选）

4. **数据保护**
   - 启用S3加密
   - 定期备份向量数据库

## 支持

如有问题，请参考：
- [AWS CDK文档](https://docs.aws.amazon.com/cdk/)
- [Zilliz文档](https://docs.zilliz.com/)
- [项目Issues](https://github.com/your-repo/issues)