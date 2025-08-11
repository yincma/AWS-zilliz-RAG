# Lambda自动化部署指南

## 快速部署

使用Makefile自动化部署Lambda函数（21MB优化版，包含所有修复）：

```bash
# 一键部署Lambda函数
make deploy-lambda-direct

# 仅构建Lambda包
make build-lambda-fixed

# 仅更新环境变量
make update-lambda-env

# 测试Lambda函数
make test-lambda

# 查看Lambda日志
make logs-lambda
```

## 部署流程

`make deploy-lambda-direct` 会自动执行以下步骤：

1. **构建Lambda包**
   - 清理旧的构建目录
   - 复制handler文件
   - 使用Docker构建Linux兼容的依赖
   - 创建numpy和pandas轻量级stubs
   - 打包成21MB的优化版ZIP文件

2. **部署到AWS**
   - 检查Lambda函数是否存在
   - 更新函数代码
   - 更新环境变量（从.env文件读取）

3. **验证部署**
   - 显示部署结果
   - 可运行 `make test-lambda` 进行测试

## 环境变量配置

确保 `.env` 文件包含以下配置：

```env
# AWS配置
AWS_REGION=us-east-1

# Zilliz配置
ZILLIZ_ENDPOINT=https://your-endpoint.cloud.zilliz.com
ZILLIZ_TOKEN=your-token
ZILLIZ_COLLECTION=rag_collection

# Bedrock配置
BEDROCK_MODEL_ID=amazon.nova-pro-v1:0
EMBEDDING_MODEL_ID=amazon.titan-embed-text-v2:0
```

## 关键特性

### 21MB优化版
- 使用轻量级numpy/pandas stubs替代完整包
- 修复了grpcio C扩展加载问题
- 完全支持pymilvus和Zilliz连接

### 自动化部署
- Docker自动构建Linux兼容依赖
- 自动更新环境变量
- 支持直接调用和API Gateway调用

### 错误处理
- 自动检查Lambda函数是否存在
- 优雅的错误处理和回退机制
- 详细的日志输出

## 故障排查

### 查看日志
```bash
# 查看最近日志
make logs-lambda

# 实时日志
aws logs tail /aws/lambda/rag-query-handler --follow --region us-east-1
```

### 常见问题

1. **Lambda函数不存在**
   - 先运行 `make deploy-v2` 部署基础架构
   - 或使用CDK创建Lambda函数

2. **包大小超限**
   - 确保使用 `make build-lambda-fixed`（21MB版本）
   - 不要使用完整的numpy/pandas包

3. **Zilliz连接失败**
   - 检查环境变量配置
   - 确认Zilliz endpoint和token正确
   - 运行 `make update-lambda-env` 更新配置

## 高级用法

### 单独构建和部署

```bash
# 1. 仅构建Lambda包
make build-lambda-fixed

# 2. 手动部署Query Lambda
aws lambda update-function-code \
  --function-name rag-query-handler \
  --zip-file fileb://zilliz-rag-query.zip \
  --region us-east-1

# 3. 手动部署Ingest Lambda  
aws lambda update-function-code \
  --function-name rag-ingest-handler \
  --zip-file fileb://zilliz-rag-ingest.zip \
  --region us-east-1

# 4. 更新环境变量
make update-lambda-env
```

### 自定义构建

修改Makefile中的 `build-lambda-fixed` 目标：

```makefile
# 添加额外的依赖
bash -c "pip install pymilvus grpcio protobuf boto3 python-dotenv YOUR_PACKAGE -t lambda_build_temp/query/"
```

## 性能优化

- **包大小**: 21MB（原始294MB）
- **冷启动**: <2秒
- **内存使用**: 512MB足够
- **超时设置**: 建议30秒

## 相关命令

```bash
# 完整部署（CDK）
make deploy-v2

# 仅更新前端
make update-frontend

# 查看部署状态
make verify-deploy

# 清理资源
make clean
```