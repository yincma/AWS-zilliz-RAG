# CORS 问题永久解决方案

## 问题根因分析

### 1. 环境变量名称不一致
- **问题**: CDK 栈使用 `CORS_ALLOW_ORIGINS`，而 Lambda 函数中的 cors_helper.py 查找 `ALLOWED_ORIGINS`
- **影响**: Lambda 函数总是返回默认的 `*`，导致 CORS 配置不正确

### 2. 配置硬编码
- **问题**: API Gateway URL 被硬编码在前端 `api.js` 文件中
- **影响**: 每次重新部署可能生成新的 API URL，导致前后端不匹配

### 3. 部署流程缺陷
- **问题**: 没有自动同步前后端配置的机制
- **影响**: 需要手动更新配置，容易出错

## 解决方案架构

### 1. 统一的 CORS 配置管理

#### cors_helper.py 改进
```python
# 支持多种环境变量名称以保持兼容性
allowed_origins = (
    os.environ.get('CORS_ALLOWED_ORIGINS') or  # 新的统一名称
    os.environ.get('CORS_ALLOW_ORIGINS') or     # CDK 栈中使用的名称
    os.environ.get('ALLOWED_ORIGINS') or        # 旧名称
    '*'                                          # 默认值
)
```

#### 配置优先级
1. 环境变量配置
2. CloudFormation 输出
3. 默认安全配置

### 2. 自动化配置同步

#### 组件说明

##### infrastructure/config/cors_config.py
- 集中管理所有 CORS 配置
- 避免硬编码
- 提供统一的配置接口

##### infrastructure/scripts/update_frontend_config.py
- 自动从 CloudFormation 栈获取配置
- 更新前端 config.json
- 更新 api.js 中的 API URL
- 同步到 S3 并清除 CloudFront 缓存

##### deploy_rag_system.sh
- 一键部署脚本
- 自动处理所有配置同步
- 验证部署结果

### 3. 部署流程

```bash
# 设置环境变量（可选）
export AWS_REGION=us-east-1
export CDK_STACK_NAME=RagApiStackV2

# 运行部署脚本
chmod +x deploy_rag_system.sh
./deploy_rag_system.sh
```

## 配置管理最佳实践

### 1. 环境变量管理
```bash
# .env 文件（不要提交到版本控制）
AWS_REGION=us-east-1
CDK_STACK_NAME=RagApiStackV2
CORS_ALLOWED_ORIGINS=https://your-domain.com,http://localhost:3000
```

### 2. CDK 栈配置
```python
# 在 CDK 栈中使用统一的环境变量
environment = {
    "CORS_ALLOWED_ORIGINS": os.environ.get('CORS_ALLOWED_ORIGINS', '*'),
    "CORS_ALLOWED_METHODS": "GET,POST,PUT,DELETE,OPTIONS",
    "CORS_ALLOWED_HEADERS": "Content-Type,X-Amz-Date,Authorization",
    # ... 其他配置
}
```

### 3. 前端配置
```json
// config.json - 由部署脚本自动生成
{
  "apiUrl": "自动从 CloudFormation 获取",
  "cloudfrontUrl": "自动从 CloudFormation 获取",
  "region": "us-east-1",
  "stage": "prod",
  "updated": "2025-08-11T23:30:00.000000",
  "_comment": "此文件由部署脚本自动生成，请勿手动修改"
}
```

## 故障排查

### 检查 CORS 配置
```bash
# 测试 OPTIONS 预检请求
curl -i -X OPTIONS https://your-api-url/query \
  -H "Origin: https://your-frontend-url" \
  -H "Access-Control-Request-Method: POST"

# 检查响应头
# 应该看到:
# Access-Control-Allow-Origin: https://your-frontend-url
# Access-Control-Allow-Methods: GET,POST,PUT,DELETE,OPTIONS
```

### 检查环境变量
```bash
# 查看 Lambda 函数的环境变量
aws lambda get-function-configuration \
  --function-name your-function-name \
  --query 'Environment.Variables'
```

### 查看 Lambda 日志
```bash
# 查看最近的日志
aws logs tail /aws/lambda/your-function-name --follow
```

## 关键改进点

1. **无硬编码**: 所有配置都从环境变量或 CloudFormation 输出获取
2. **自动同步**: 部署时自动更新前端配置
3. **向后兼容**: 支持多种环境变量名称
4. **错误处理**: 优雅处理配置缺失或错误
5. **验证机制**: 部署后自动验证 CORS 配置

## 维护建议

1. **定期检查**: 使用部署脚本的验证功能定期检查配置
2. **版本控制**: 不要将包含敏感信息的配置文件提交到版本控制
3. **文档更新**: 当修改配置时，更新相关文档
4. **测试覆盖**: 在 CI/CD 中包含 CORS 测试

## 总结

这个解决方案通过以下方式永久解决了 CORS 问题：

1. ✅ 统一环境变量命名
2. ✅ 自动化配置同步
3. ✅ 消除硬编码
4. ✅ 提供完整的部署脚本
5. ✅ 包含验证和故障排查工具

下次部署时，只需运行 `./deploy_rag_system.sh`，所有配置将自动正确设置。