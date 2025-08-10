# 部署指南 V2 - 自动化部署包含所有修复

## 概述

V2版本包含以下改进：
- ✅ **自动CORS配置** - API Gateway自动配置正确的CORS头
- ✅ **动态API配置** - 前端自动获取API URL，无需硬编码
- ✅ **正确的路径结构** - API使用简单路径（/query, /health等）
- ✅ **一键部署** - Makefile自动化所有步骤

## 快速开始

### 前置要求

1. **AWS CLI配置**
```bash
aws configure
# 输入你的AWS Access Key ID
# 输入你的AWS Secret Access Key
# 选择区域（如 us-east-1）
```

2. **安装依赖**
```bash
make install
```

3. **初始化CDK**（首次部署）
```bash
make bootstrap
```

### 一键部署

```bash
# 使用V2版本部署（推荐）
make deploy-v2
```

这个命令会：
1. 部署数据栈（S3存储桶）
2. 部署API栈V2（Lambda + API Gateway，带CORS）
3. 部署Web栈（CloudFront + S3）
4. 自动生成前端配置
5. 同步前端文件
6. 清除CloudFront缓存

## 部署选项

### 完整部署（推荐）
```bash
make deploy-v2
```

### 分步部署
```bash
# 1. 部署数据栈
make deploy-data

# 2. 部署API栈
make deploy-api

# 3. 部署Web栈
make deploy-web

# 4. 更新前端配置
make update-frontend
```

### 仅更新前端
```bash
# 当API没变化，只需更新前端代码时
make update-frontend
```

## 环境变量配置

### 必需的环境变量
```bash
# 创建 .env 文件
cat > .env << EOF
# AWS配置
AWS_REGION=us-east-1

# Bedrock配置（可选）
BEDROCK_MODEL_ID=amazon.nova-lite-v1:0
EMBEDDING_MODEL_ID=amazon.titan-embed-text-v2:0

# Zilliz配置（可选）
ZILLIZ_ENDPOINT=your-endpoint
ZILLIZ_TOKEN=your-token
ZILLIZ_COLLECTION=rag_collection

# 部署配置
STAGE=prod
USE_API_V2=true  # 使用V2版本的API栈
EOF
```

### 加载环境变量
```bash
source .env
```

## 验证部署

### 检查部署状态
```bash
make verify-deploy
```

这会显示：
- 所有栈的状态
- API和Web端点URL
- API健康检查结果

### 测试API
```bash
make test-api
```

### 手动测试
1. 访问CloudFront URL（从verify-deploy输出获取）
2. 打开浏览器控制台（F12）
3. 尝试发送聊天消息
4. 检查Network标签，确认请求发送到正确的端点

## 常见问题修复

### CORS错误
```bash
make fix-cors
```

### CloudFront 403错误
```bash
make fix-cloudfront
```

### 完全重新部署
```bash
# 销毁所有资源
make destroy

# 重新部署
make deploy-v2
```

## 架构说明

### API栈V2改进
- 所有Lambda函数包含CORS响应头
- API Gateway配置全局CORS策略
- 支持OPTIONS预检请求
- 环境变量配置CORS允许的源

### 前端配置系统
- `scripts/generate_frontend_config.py` - 自动从CDK输出生成API配置
- 无需硬编码API URL
- 根据环境（本地/生产）自动切换

### 文件结构
```
infrastructure/
├── app_v2.py              # CDK应用入口（V2版本）
├── stacks/
│   ├── api_stack_v2.py    # API栈V2（带CORS修复）
│   ├── web_stack.py       # Web栈
│   └── data_stack.py      # 数据栈
scripts/
├── generate_frontend_config.py  # 前端配置生成器
app/views/web/
├── static/js/
│   ├── api.js             # 自动生成的API客户端
│   └── api.meta.json      # API配置元数据
```

## 更新和维护

### 更新API
1. 修改 `infrastructure/stacks/api_stack_v2.py`
2. 运行 `make deploy-api`
3. 前端配置会自动更新

### 更新前端
1. 修改前端代码
2. 运行 `make update-frontend`

### 添加新的API端点
1. 在 `api_stack_v2.py` 中添加新端点
2. 确保Lambda函数包含CORS头
3. 部署：`make deploy-api`

## 监控和日志

### 查看Lambda日志
```bash
# 查询函数日志
aws logs tail /aws/lambda/RAG-API-prod-QueryFunction --follow

# 摄入函数日志
aws logs tail /aws/lambda/RAG-API-prod-IngestFunction --follow
```

### 查看API Gateway日志
```bash
aws logs tail /aws/apigateway/RAG-API-prod --follow
```

## 成本优化

- Lambda函数使用按需计费
- CloudFront使用价格类100（最便宜）
- S3使用标准存储类
- 日志保留期设为1周

## 安全最佳实践

1. **不要提交密钥到代码库**
   - 使用环境变量或AWS Secrets Manager
   - 添加 `.env` 到 `.gitignore`

2. **使用最小权限原则**
   - Lambda角色只有必需的权限
   - S3桶设为私有

3. **启用日志和监控**
   - CloudWatch日志自动启用
   - API Gateway启用请求日志

## 故障排除

### 部署失败
```bash
# 查看CDK日志
cdk doctor

# 查看CloudFormation事件
aws cloudformation describe-stack-events --stack-name RAG-API-prod
```

### API不工作
1. 检查Lambda函数日志
2. 验证环境变量配置
3. 确认IAM权限

### 前端无法连接API
1. 检查浏览器控制台错误
2. 验证API URL配置
3. 检查CORS设置

## 支持

如有问题，请检查：
1. CloudFormation栈事件
2. Lambda函数日志
3. 浏览器控制台错误

---

生成时间：2025-08-10
版本：V2.0