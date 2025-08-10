# CDK 配置修复说明

## 修复日期
2025-08-10

## 问题描述

CDK部署存在以下问题：

1. **多路径行为配置冲突**
   - CDK代码定义了多个API路径模式（`/api/*`, `/query`, `/documents`等）
   - 实际部署时只有`/api/*`一个行为被创建
   - 原因：CloudFront路径模式存在优先级冲突

2. **Origin Path配置错误**
   - API Gateway的stage路径未正确配置
   - 导致请求无法正确路由到API Gateway的prod stage

3. **Stage配置不一致**
   - 不同文件中的默认stage值不一致（dev vs prod）
   - 导致部署和运行时行为不匹配

## 修复内容

### 1. web_stack.py 修改

**主要改动：**
- 智能解析API Gateway URL，自动提取stage路径
- 简化路径配置，只保留`/api/*`行为，避免路径冲突
- 添加正则表达式解析API Gateway URL格式
- 动态设置origin_path为正确的stage路径

**关键代码：**
```python
# 使用正则表达式解析API Gateway URL
api_gateway_pattern = r'https?://([^/]+\.execute-api\.[^/]+\.amazonaws\.com)/?(.*)'
match = re.match(api_gateway_pattern, api_url.rstrip('/'))

if match:
    api_domain = match.group(1)
    # 获取stage路径，如果URL中有stage就使用，否则使用context中的stage
    stage_path = match.group(2)
    if not stage_path:
        stage = self.node.try_get_context('stage') or 'prod'
        stage_path = f'/{stage}'
```

### 2. api_stack.py 修改

**主要改动：**
- 统一默认stage为`prod`
- 确保API Gateway的stage配置一致

**修改内容：**
```python
stage_name=self.node.try_get_context('stage') or 'prod',  # 统一默认使用prod
```

### 3. app.py 修改

**主要改动：**
- 统一默认stage为`prod`
- 保持整个应用的stage配置一致

**修改内容：**
```python
stage = app.node.try_get_context("stage") or "prod"  # 统一默认使用prod
```

### 4. cdk.json 修改

**主要改动：**
- 将默认stage从`dev`改为`prod`

**修改内容：**
```json
"stage": "prod"
```

### 5. 新增deploy.py部署脚本

**功能：**
- 自动化部署流程
- 检查先决条件（AWS CLI、CDK、环境变量）
- 按正确顺序部署栈
- 验证部署配置，特别是CloudFront和API Gateway的配置
- 确保Origin Path正确包含stage

**使用方法：**
```bash
cd infrastructure
python3 deploy.py [stage]
```

## 验证步骤

1. **检查CloudFront配置：**
```bash
aws cloudfront get-distribution-config --id YOUR_DISTRIBUTION_ID | grep -A 5 "OriginPath"
```
应该看到`"OriginPath": "/prod"`

2. **测试API调用：**
```bash
curl https://YOUR_CLOUDFRONT_URL/api/health
```
应该返回健康检查响应

3. **验证前端访问：**
- 访问CloudFront URL
- 检查开发者工具中的API调用是否使用`/api/`前缀
- 确认请求正确路由到API Gateway

## 重要说明

1. **不使用硬编码**
   - 所有配置都动态获取或从context读取
   - stage可以通过CDK context覆盖

2. **部署命令**
   - 使用特定stage: `cdk deploy --context stage=prod`
   - 使用部署脚本: `python3 deploy.py prod`

3. **回滚方法**
   如果需要回滚，可以：
   - 恢复cdk.json中的stage为`dev`
   - 重新部署: `cdk deploy --all --context stage=dev`

## 后续建议

1. **升级CDK版本**
   - 当前版本较旧，建议升级到最新的CDK v2版本
   - 命令: `npm install -g aws-cdk@latest`

2. **简化配置**
   - 考虑使用CDK的Stack参数而不是context
   - 使用环境变量管理不同环境的配置

3. **监控和日志**
   - 启用CloudFront日志
   - 配置API Gateway的详细日志
   - 设置CloudWatch告警

## 联系方式

如有问题，请参考：
- AWS CDK文档: https://docs.aws.amazon.com/cdk/
- CloudFront文档: https://docs.aws.amazon.com/cloudfront/
- API Gateway文档: https://docs.aws.amazon.com/apigateway/