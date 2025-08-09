# 部署指南

## 🚀 快速开始

### 一键部署

```bash
# 1. 配置环境变量
cp .env.example .env
# 编辑.env文件，填入实际值

# 2. 执行部署
./deploy.sh
```

或使用Makefile：

```bash
# 完整部署（包含确认步骤）
make deploy

# 快速部署（跳过确认）
make deploy-fast
```

## 📋 前置要求

### 1. 安装依赖

- Python 3.9+
- Node.js 14+
- AWS CLI
- Docker（可选）

```bash
# 安装所有依赖
make install
```

### 2. 配置AWS

```bash
# 配置AWS CLI
aws configure

# 验证配置
aws sts get-caller-identity
```

### 3. 设置环境变量

创建`.env`文件：

```bash
# AWS配置
AWS_REGION=us-east-1
AWS_PROFILE=default

# Bedrock配置
BEDROCK_MODEL_ID=amazon.nova-lite-v1:0
EMBEDDING_MODEL_ID=amazon.titan-embed-text-v2:0

# Zilliz配置
ZILLIZ_ENDPOINT=https://in03-xxxxx.api.gcp-us-west1.zillizcloud.com
ZILLIZ_TOKEN=your-api-key
ZILLIZ_COLLECTION=rag_collection

# S3配置（可选）
S3_BUCKET=rag-documents-bucket
WEB_BUCKET=rag-web-bucket

# 部署配置
STAGE=dev
```

## 🏗️ 部署步骤详解

### 1. 打包Lambda函数

```bash
make package-lambda
```

这会：
- 安装Lambda依赖
- 复制应用代码
- 创建`lambda_deployment.zip`

### 2. 部署基础设施

```bash
# 部署所有栈
make deploy

# 或分别部署
make deploy-stack STACK=RAG-Data  # 数据栈（S3）
make deploy-stack STACK=RAG-API   # API栈（Lambda + API Gateway）
```

### 3. 部署前端（可选）

```bash
# 设置Web存储桶
export WEB_BUCKET=your-web-bucket

# 部署前端文件
make deploy-frontend
```

## 🧪 测试部署

### 1. 健康检查

```bash
# 获取API端点
API_URL=$(aws cloudformation describe-stacks \
  --stack-name RAG-API-dev \
  --query "Stacks[0].Outputs[?OutputKey=='ApiUrl'].OutputValue" \
  --output text)

# 测试健康检查
curl -X GET ${API_URL}health
```

### 2. 摄入文档

```bash
# 摄入S3文档
curl -X POST ${API_URL}documents \
  -H 'Content-Type: application/json' \
  -d '{
    "operation": "s3_ingest",
    "s3_keys": ["documents/sample.pdf"]
  }'
```

### 3. 测试查询

```bash
# 发送查询
curl -X POST ${API_URL}query \
  -H 'Content-Type: application/json' \
  -d '{
    "query": "什么是RAG？",
    "top_k": 5
  }'
```

### 4. 运行E2E测试

```bash
python test_e2e_rag.py
```

## 📊 监控和日志

### 查看Lambda日志

```bash
# 实时查看日志
make logs

# 或使用AWS CLI
aws logs tail /aws/lambda/RAG-Query-dev --follow
```

### 查看系统状态

```bash
curl -X POST ${API_URL}documents \
  -H 'Content-Type: application/json' \
  -d '{"operation": "stats"}'
```

## 🔧 常见操作

### 更新代码

```bash
# 1. 修改代码
# 2. 重新打包
make package-lambda
# 3. 更新Lambda函数
make deploy-stack STACK=RAG-API
```

### 清理资源

```bash
# 销毁所有资源
make destroy

# 清理本地文件
make clean
```

### 本地开发

```bash
# 运行本地API
make run-local

# 运行测试
make test

# 代码检查
make lint
```

## 🐳 Docker部署（可选）

```bash
# 构建镜像
make docker-build

# 运行容器
make docker-run
```

## 🔍 故障排查

### 1. CDK部署失败

```bash
# 清理CDK进程和缓存
make kill-cdk
make clean

# 重新部署
make deploy
```

### 2. Lambda函数错误

```bash
# 查看详细日志
aws logs get-log-events \
  --log-group-name /aws/lambda/RAG-Query-dev \
  --log-stream-name $(aws logs describe-log-streams \
    --log-group-name /aws/lambda/RAG-Query-dev \
    --order-by LastEventTime \
    --descending \
    --limit 1 \
    --query 'logStreams[0].logStreamName' \
    --output text)
```

### 3. Zilliz连接问题

```python
# 测试连接
python -c "
from app.models.vector_store import VectorStoreModel
vs = VectorStoreModel()
print(vs.get_collection_stats())
"
```

## 📝 环境管理

### 多环境部署

```bash
# 开发环境
STAGE=dev make deploy

# 测试环境
STAGE=test make deploy

# 生产环境
STAGE=prod make deploy
```

### 参数覆盖

```bash
# 使用不同的模型
BEDROCK_MODEL_ID=amazon.nova-pro-v1:0 make deploy

# 使用不同的区域
AWS_REGION=us-west-2 make deploy
```

## 🎯 部署检查清单

- [ ] AWS CLI已配置
- [ ] Zilliz凭据已设置
- [ ] Python依赖已安装
- [ ] CDK已安装
- [ ] 环境变量已配置
- [ ] Lambda函数已打包
- [ ] CDK栈已部署
- [ ] API端点可访问
- [ ] 健康检查通过
- [ ] 文档摄入成功
- [ ] 查询功能正常

## 🆘 获取帮助

```bash
# 查看所有可用命令
make help

# 查看当前配置
make show-config

# 查看栈差异
make diff
```