# AWS 资源清理指南

## 问题说明

执行 `make destroy` 后，AWS上仍有资源残留的原因：

### 1. CDK 管理范围限制
`make destroy` 只删除CDK直接管理的CloudFormation栈中的资源，但不会删除：
- **CDK Bootstrap 资源** - CDKToolkit栈和相关S3存储桶
- **手动创建的资源** - 在CDK之外创建的Lambda、S3等
- **有依赖关系的资源** - 如非空的S3存储桶
- **CloudFront distributions** - 需要先禁用才能删除

### 2. 常见残留资源
- `cdk-*-assets-*` - CDK资产存储桶
- `rag-documents-*` - 文档存储桶（如果有版本控制）
- `rag-web-*` - 前端静态资源桶
- 独立的Lambda函数
- CloudFront分发（需要时间禁用）
- IAM角色和策略

## 解决方案

### 方法1：使用增强的Makefile命令（推荐）

```bash
# 标准CDK资源清理
make destroy

# 完全清理所有资源（包括CDK未管理的）
make destroy-all
```

### 方法2：使用清理脚本

```bash
# 完整清理（包含所有检查和等待）
./cleanup_aws_resources.sh

# 快速清理（不等待CloudFront）
./quick_cleanup.sh
```

### 方法3：手动清理

1. **清理S3存储桶**
```bash
# 列出所有相关存储桶
aws s3 ls | grep -E "(rag|RAG|cdk)"

# 强制删除存储桶（包括内容）
aws s3 rb s3://bucket-name --force
```

2. **删除Lambda函数**
```bash
# 列出相关函数
aws lambda list-functions --query "Functions[?contains(FunctionName, 'rag')].FunctionName"

# 删除函数
aws lambda delete-function --function-name function-name
```

3. **删除CloudFormation栈**
```bash
# 列出栈
aws cloudformation list-stacks --stack-status-filter CREATE_COMPLETE

# 删除栈
aws cloudformation delete-stack --stack-name stack-name
```

4. **删除CDK Bootstrap（可选）**
```bash
# 删除CDK bootstrap栈
cdk bootstrap --terminate

# 或手动删除
aws cloudformation delete-stack --stack-name CDKToolkit
```

## 预防措施

### 1. 使用标签管理资源
在CDK代码中为所有资源添加标签：
```typescript
Tags.of(app).add('Project', 'RAG');
Tags.of(app).add('ManagedBy', 'CDK');
```

### 2. 启用S3存储桶的自动清理
在CDK中设置：
```typescript
new s3.Bucket(this, 'Bucket', {
  removalPolicy: cdk.RemovalPolicy.DESTROY,
  autoDeleteObjects: true, // 自动删除对象
});
```

### 3. 定期审计资源
```bash
# 查看所有RAG相关资源
aws resourcegroupstaggingapi get-resources \
  --tag-filters Key=Project,Values=RAG
```

## 成本优化建议

1. **定期清理未使用资源**
   - 使用AWS Cost Explorer识别未使用资源
   - 设置预算警报

2. **使用资源组**
   - 创建基于标签的资源组便于管理
   - 批量操作和监控

3. **自动化清理**
   - 使用Lambda定期清理临时资源
   - 配置生命周期策略

## 故障排除

### 问题：S3存储桶无法删除
**原因**：存储桶非空或有版本控制
**解决**：
```bash
# 删除所有版本
aws s3api delete-objects --bucket bucket-name \
  --delete "$(aws s3api list-object-versions \
  --bucket bucket-name --query='{Objects: Versions[].{Key:Key,VersionId:VersionId}}')"
```

### 问题：CloudFront distribution删除超时
**原因**：需要先禁用才能删除，过程较慢
**解决**：使用AWS Console手动删除或等待更长时间

### 问题：IAM角色无法删除
**原因**：有附加的策略或被其他服务使用
**解决**：先分离所有策略，确保无服务依赖

## 最佳实践

1. **使用统一的命名规范** - 便于批量识别和清理
2. **记录所有创建的资源** - 维护资源清单
3. **使用IaC工具管理所有资源** - 避免手动创建
4. **定期审查和清理** - 避免资源堆积
5. **设置成本预算和警报** - 及时发现异常

## 命令速查

```bash
# 查看所有RAG资源
make info

# 标准清理
make destroy

# 完全清理
make destroy-all

# 验证清理结果
aws s3 ls | grep -i rag
aws lambda list-functions | grep -i rag
aws cloudformation list-stacks
```