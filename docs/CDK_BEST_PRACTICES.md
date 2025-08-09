# CDK部署最佳实践

## 常见问题和解决方案

### 1. CDK进程冲突问题

#### 问题描述
```
Another CLI (PID=xxxxx) is currently synthing to cdk.out
```

#### 根本原因
- 多个CDK进程同时访问同一个输出目录
- 前一次部署未正常结束
- 多个终端同时运行部署脚本

#### 解决方案
```bash
# 立即修复
make kill-cdk    # 终止所有CDK进程
make clean       # 清理输出目录
make deploy      # 重新部署

# 或手动执行
ps aux | grep cdk | awk '{print $2}' | xargs kill -9
rm -rf infrastructure/cdk.out
```

### 2. 防止并发部署

#### 使用锁文件机制
```bash
# 在部署脚本中实现
LOCK_FILE="/tmp/rag-deploy.lock"
if [ -f "$LOCK_FILE" ]; then
    echo "另一个部署正在进行中..."
    exit 1
fi
echo $$ > "$LOCK_FILE"
trap "rm -f $LOCK_FILE" EXIT
```

#### 使用CDK的--exclusively标志
```bash
cdk deploy --exclusively  # 确保独占部署
```

### 3. CDK版本管理

#### 保持CDK版本一致
```json
// package.json
{
  "devDependencies": {
    "aws-cdk": "2.110.0"  // 固定版本
  }
}
```

#### 定期更新
```bash
npm update aws-cdk
cdk acknowledge  # 确认通知
```

### 4. 环境隔离

#### 使用不同的输出目录
```bash
# 开发环境
cdk synth --output cdk.out-dev

# 生产环境
cdk synth --output cdk.out-prod
```

#### 使用上下文变量
```bash
cdk deploy --context stage=dev
cdk deploy --context stage=prod
```

## 推荐的部署流程

### 1. 使用Makefile标准化操作
```bash
make clean       # 清理环境
make test        # 运行测试
make synth       # 合成模板
make diff        # 查看变更
make deploy      # 执行部署
```

### 2. CI/CD集成
```yaml
# .github/workflows/deploy.yml
name: Deploy
on:
  push:
    branches: [main]
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Deploy
        run: |
          make clean
          make ci
          make deploy-fast STAGE=prod
```

### 3. 监控和告警

#### 部署前检查
```bash
#!/bin/bash
# pre-deploy-check.sh

# 检查AWS凭证
aws sts get-caller-identity || exit 1

# 检查环境变量
[ -z "$ZILLIZ_ENDPOINT" ] && exit 1

# 检查磁盘空间
df -h | grep -E "^/dev" | awk '{print $5}' | sed 's/%//g' | \
  while read usage; do
    if [ $usage -gt 90 ]; then
      echo "磁盘空间不足"
      exit 1
    fi
  done

# 检查CDK进程
ps aux | grep cdk | grep -v grep && {
  echo "发现运行中的CDK进程"
  exit 1
}
```

#### 部署后验证
```bash
#!/bin/bash
# post-deploy-verify.sh

# 检查栈状态
aws cloudformation describe-stacks \
  --stack-name RAG-API-$STAGE \
  --query "Stacks[0].StackStatus" \
  --output text | grep -E "CREATE_COMPLETE|UPDATE_COMPLETE"

# 健康检查
curl -f $API_URL/health || exit 1
```

## 故障排除清单

### 部署失败时的检查步骤

1. **检查AWS凭证**
   ```bash
   aws sts get-caller-identity
   aws configure list
   ```

2. **检查CDK进程**
   ```bash
   ps aux | grep cdk
   lsof | grep cdk.out
   ```

3. **检查Docker**
   ```bash
   docker ps -a
   docker system prune -f
   ```

4. **检查日志**
   ```bash
   # CloudFormation事件
   aws cloudformation describe-stack-events \
     --stack-name RAG-API-dev \
     --max-items 10
   
   # Lambda日志
   aws logs tail /aws/lambda/RAG-Query-dev
   ```

5. **检查资源限制**
   ```bash
   # 检查配额
   aws service-quotas list-service-quotas \
     --service-code lambda
   
   # 检查成本
   aws ce get-cost-and-usage \
     --time-period Start=2024-01-01,End=2024-01-31 \
     --granularity MONTHLY \
     --metrics "UnblendedCost"
   ```

## 安全最佳实践

### 1. 不要硬编码敏感信息
```python
# 错误
ZILLIZ_TOKEN = "abc123"  # 永远不要这样做

# 正确
ZILLIZ_TOKEN = os.environ.get("ZILLIZ_TOKEN")
```

### 2. 使用AWS Secrets Manager
```python
import boto3

def get_secret(secret_name):
    client = boto3.client('secretsmanager')
    response = client.get_secret_value(SecretId=secret_name)
    return response['SecretString']
```

### 3. 限制IAM权限
```python
# CDK中定义最小权限
lambda_role.add_to_policy(
    iam.PolicyStatement(
        effect=iam.Effect.ALLOW,
        actions=["bedrock:InvokeModel"],
        resources=[f"arn:aws:bedrock:*::foundation-model/{model_id}"]
    )
)
```

## 性能优化

### 1. 并行部署（谨慎使用）
```bash
# 仅在栈之间无依赖时使用
cdk deploy --all --concurrency 10
```

### 2. 增量部署
```bash
# 仅部署有变更的栈
cdk deploy --hotswap
```

### 3. 缓存Docker层
```dockerfile
# Dockerfile
FROM public.ecr.aws/lambda/python:3.9

# 先复制依赖文件
COPY requirements.txt .
RUN pip install -r requirements.txt

# 再复制应用代码
COPY app/ ./app/
```

## 团队协作

### 1. 使用分支策略
```bash
# 功能分支
git checkout -b feature/rag-improvement

# 部署到开发环境
make deploy STAGE=dev

# 合并到主分支后部署生产
git checkout main
git merge feature/rag-improvement
make deploy STAGE=prod
```

### 2. 文档化部署过程
```markdown
## 部署步骤
1. 检查环境变量: `make show-config`
2. 运行测试: `make test`
3. 查看变更: `make diff`
4. 执行部署: `make deploy`
5. 验证部署: `make logs`
```

### 3. 建立部署检查清单
- [ ] 环境变量已设置
- [ ] 测试全部通过
- [ ] 代码已review
- [ ] 文档已更新
- [ ] 监控已配置
- [ ] 回滚计划已准备

## 紧急回滚程序

```bash
#!/bin/bash
# emergency-rollback.sh

STAGE=${1:-dev}
PREVIOUS_VERSION=${2:-PREV}

echo "⚠️  开始紧急回滚到版本: $PREVIOUS_VERSION"

# 1. 停止当前部署
make kill-cdk

# 2. 回滚CloudFormation栈
aws cloudformation cancel-update-stack --stack-name RAG-API-$STAGE
aws cloudformation continue-update-rollback --stack-name RAG-API-$STAGE

# 3. 等待回滚完成
aws cloudformation wait stack-rollback-complete --stack-name RAG-API-$STAGE

# 4. 验证回滚
curl -f https://api-$STAGE.example.com/health || {
  echo "❌ 回滚失败，需要人工介入"
  exit 1
}

echo "✅ 回滚成功"
```