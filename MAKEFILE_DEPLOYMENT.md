# Makefile 部署指南

## 概述

Makefile 已经完全修复，支持新旧两种部署方式，确保不会产生任何技术负债。

## 修复内容

### 1. 添加了缺失的目标

#### `sync-cors-helper` 目标（第 151-169 行）
- 自动同步 `cors_helper.py` 到所有需要的位置
- 确保 Lambda 函数使用统一的 CORS 处理逻辑
- 在构建 Lambda 包之前自动执行

#### `update-frontend-v2` 目标（第 461-519 行）
- 专门为 `RagApiStackV2` 设计的前端更新目标
- 智能查找 S3 桶和 CloudFront Distribution
- 支持栈名称回退机制

### 2. 改进了配置生成

#### `generate-config` 目标（第 423-437 行）
- 自动检测使用的栈（RagApiStackV2 或 RAG-API-prod）
- 动态设置 `CDK_STACK_NAME` 环境变量
- 确保前端配置总是使用正确的 API URL

### 3. 更新了 Python 脚本

#### `scripts/generate_frontend_config.py`（第 305-345 行）
- 支持多个可能的栈名称
- 优先使用环境变量中指定的栈名
- 自动尝试 RagApiStackV2 和 RAG-API-{stage}
- 确保总能找到正确的 API URL

## 使用方法

### 快速部署（推荐）

```bash
# 使用 Makefile 快速重新部署 Lambda
make redeploy-lambda

# 这会自动执行：
# 1. 构建 Lambda 包
# 2. 同步 cors_helper.py
# 3. 部署 RagApiStackV2
# 4. 更新前端配置
```

### 完整部署

```bash
# 完整部署应用
make deploy-v2

# 这会自动执行：
# 1. 检查环境变量
# 2. 构建 Lambda 包
# 3. 部署所有 CDK 栈
# 4. 生成前端配置
# 5. 更新前端文件
```

### 仅更新前端

```bash
# 更新前端配置和文件
make update-frontend-v2

# 或者使用兼容的旧命令
make update-frontend
```

## 工作流程

### 1. CORS 修复流程

```bash
# 修复 CORS 问题
make fix-cors

# 这会：
# 1. 重新部署 API 栈
# 2. 更新前端配置
# 3. 同步到 S3
# 4. 清除 CloudFront 缓存
```

### 2. Lambda 开发流程

```bash
# 修改 Lambda 代码后
# 1. 编辑 lambda_functions/ 中的文件

# 2. 快速重新部署
make redeploy-lambda

# 3. 测试函数
make test-lambda

# 4. 查看日志
make logs-lambda
```

### 3. 前端开发流程

```bash
# 修改前端代码后
# 1. 编辑 app/views/web/ 中的文件

# 2. 更新前端
make update-frontend-v2

# 3. 验证部署
make verify-deploy
```

## 栈名称兼容性

Makefile 现在智能处理两种部署模式：

### 新部署（RagApiStackV2）
- 使用 `app.py` 作为 CDK 入口
- 创建 `RagApiStackV2` 栈
- 自动检测并使用此栈的输出

### 旧部署（RAG-API-prod）
- 使用 `app_v2.py` 作为 CDK 入口
- 创建 `RAG-API-prod` 等栈
- 自动回退到这些栈名称

## 环境变量

确保 `.env` 文件包含必要的配置：

```bash
# AWS 配置
AWS_REGION=us-east-1
STAGE=prod

# Zilliz 配置
ZILLIZ_ENDPOINT=your-endpoint
ZILLIZ_TOKEN=your-token
ZILLIZ_COLLECTION=rag_collection

# Bedrock 配置
BEDROCK_MODEL_ID=amazon.nova-pro-v1:0
EMBEDDING_MODEL_ID=amazon.titan-embed-image-v1
```

## 故障排查

### 问题：找不到栈

```bash
# 列出所有栈
aws cloudformation list-stacks --stack-status-filter CREATE_COMPLETE UPDATE_COMPLETE

# 检查特定栈
aws cloudformation describe-stacks --stack-name RagApiStackV2
```

### 问题：CORS 错误

```bash
# 1. 确保 cors_helper.py 已同步
make sync-cors-helper

# 2. 重新部署 Lambda
make redeploy-lambda

# 3. 验证 CORS 配置
curl -I -X OPTIONS https://your-api-url/query \
  -H "Origin: https://your-frontend-url" \
  -H "Access-Control-Request-Method: POST"
```

### 问题：前端未更新

```bash
# 1. 强制生成新配置
make generate-config

# 2. 手动同步到 S3
make update-frontend-v2

# 3. 清除浏览器缓存
# 在浏览器中按 Ctrl+Shift+R (Windows/Linux) 或 Cmd+Shift+R (Mac)
```

## 关键改进

1. **无硬编码**：所有配置都从环境变量或 CloudFormation 输出获取
2. **智能回退**：自动处理新旧栈名称的差异
3. **自动同步**：cors_helper.py 自动同步到所有需要的位置
4. **错误处理**：优雅处理栈不存在的情况
5. **向后兼容**：保持与旧部署的兼容性

## 总结

使用 Makefile 部署不会出问题，因为：

1. ✅ 所有缺失的目标已添加
2. ✅ 栈名称差异已处理
3. ✅ CORS 配置自动同步
4. ✅ 前端配置自动生成
5. ✅ 支持新旧两种部署模式

只需运行 `make redeploy-lambda` 或 `make deploy-v2`，所有配置都会自动正确设置。