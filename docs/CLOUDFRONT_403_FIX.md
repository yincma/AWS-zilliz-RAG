# CloudFront 403 Forbidden 错误解决方案

## 问题描述

访问CloudFront分发URL时收到403 Forbidden错误：
```
Code: AccessDenied
Message: Access Denied
```

## 根本原因

1. **S3桶权限配置问题**
   - S3桶设置了`BlockPublicAccess.BLOCK_ALL`
   - 桶策略未正确配置CloudFront OAI访问权限

2. **CloudFront配置问题**
   - OAI (Origin Access Identity) 未正确关联
   - 缺少正确的错误页面处理

3. **文件结构问题**
   - index.html可能不在S3桶的根目录
   - 文件权限或内容类型设置不正确

## 永久解决方案

### 1. 更新CDK Web栈 (`web_stack_fixed.py`)

关键改进：
- 确保S3桶完全私有，只允许CloudFront访问
- 正确配置OAI权限
- 添加响应头策略提高安全性
- 配置错误页面处理（404/403返回index.html）

```python
# 关键配置
web_bucket = s3.Bucket(
    block_public_access=s3.BlockPublicAccess.BLOCK_ALL,  # 完全阻止公共访问
    ...
)

# 授予CloudFront OAI权限
web_bucket.add_to_resource_policy(
    iam.PolicyStatement(
        principals=[oai.grant_principal],
        actions=["s3:GetObject", "s3:ListBucket"],
        resources=[bucket_arn, f"{bucket_arn}/*"]
    )
)
```

### 2. 部署流程

```bash
# 使用修复版部署脚本
./deploy_web_fixed.sh prod

# 或手动部署
cd infrastructure
cdk deploy RAG-Web-prod --require-approval never
```

### 3. 验证部署

```bash
# 检查CloudFront状态
aws cloudfront get-distribution --id ${DISTRIBUTION_ID} \
    --query 'Distribution.Status' --output text

# 应该返回 "Deployed"

# 测试访问
curl -I https://your-distribution.cloudfront.net
# 应该返回 HTTP 200
```

## 快速修复（临时方案）

如果需要快速修复现有部署：

```bash
# 运行快速修复脚本
./quick_fix_403.sh

# 等待1-2分钟让缓存失效生效
```

## 预防措施

### 1. 部署前检查清单

- [ ] 确认S3桶策略允许CloudFront OAI访问
- [ ] 验证index.html存在于S3桶根目录
- [ ] 检查CloudFront分发状态为"Deployed"
- [ ] 确认OAI已正确关联到S3源

### 2. 部署后验证

```bash
# 自动验证脚本
cat > verify_deployment.sh << 'EOF'
#!/bin/bash
DIST_ID=$(aws cloudfront list-distributions \
    --query "DistributionList.Items[0].Id" --output text)
    
STATUS=$(aws cloudfront get-distribution --id $DIST_ID \
    --query 'Distribution.Status' --output text)
    
if [ "$STATUS" = "Deployed" ]; then
    echo "✅ CloudFront已部署"
else
    echo "⏳ CloudFront状态: $STATUS"
fi

# 测试访问
URL=$(aws cloudfront get-distribution --id $DIST_ID \
    --query 'Distribution.DomainName' --output text)
    
HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" https://$URL)
echo "HTTP响应代码: $HTTP_CODE"
EOF
chmod +x verify_deployment.sh
./verify_deployment.sh
```

### 3. 监控和告警

建议设置CloudWatch告警监控：
- 4xx错误率
- 5xx错误率
- 源访问错误

## 常见问题

### Q: 部署后仍然403？
A: 等待15-20分钟让CloudFront完全部署，然后创建缓存失效：
```bash
aws cloudfront create-invalidation \
    --distribution-id ${DISTRIBUTION_ID} \
    --paths "/*"
```

### Q: 如何确认OAI配置正确？
A: 检查S3桶策略：
```bash
aws s3api get-bucket-policy --bucket ${BUCKET_NAME} | jq .
```
应该看到CloudFront OAI的访问权限。

### Q: 本地开发如何测试？
A: 使用本地服务器：
```bash
python main.py  # 启动后端
# 访问 http://localhost:8000
```

## 相关文件

- `infrastructure/stacks/web_stack_fixed.py` - 修复版CDK栈
- `deploy_web_fixed.sh` - 安全部署脚本
- `quick_fix_403.sh` - 快速修复脚本
- `verify_deployment.sh` - 部署验证脚本

## 更新历史

- 2025-08-10: 初始修复方案
- 解决了S3权限和CloudFront OAI配置问题
- 添加了完整的错误处理和验证流程