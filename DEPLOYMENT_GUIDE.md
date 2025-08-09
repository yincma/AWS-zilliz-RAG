# 部署指南 - AWS-Zilliz RAG System

## 📋 部署前准备

### 1. AWS账户配置
```bash
# 配置AWS CLI
aws configure
# 输入你的AWS Access Key ID、Secret Access Key、默认区域(us-east-1)
```

### 2. 创建Zilliz集群
1. 访问 [Zilliz Cloud Console](https://cloud.zilliz.com)
2. 创建新集群
3. 记录Endpoint和API Token
4. 创建Collection: `rag_collection`

### 3. 环境配置
```bash
# 复制环境变量模板
cp .env.example .env

# 编辑.env文件
vim .env
```

必要的环境变量：
```env
AWS_REGION=us-east-1
AWS_ACCOUNT_ID=375004070918

ZILLIZ_ENDPOINT=in03-xxx.serverless.aws-eu-central-1.cloud.zilliz.com
ZILLIZ_TOKEN=your-token-here
ZILLIZ_COLLECTION=rag_collection

BEDROCK_MODEL_ID=amazon.nova-pro-v1:0
EMBEDDING_MODEL_ID=amazon.titan-embed-text-v2:0
```

## 🚀 快速部署

### 一键部署脚本
```bash
# 执行快速部署
./quick_deploy.sh
```

脚本将自动完成：
1. 创建S3 buckets
2. 部署Lambda函数
3. 配置API Gateway
4. 部署前端到S3
5. 设置CloudFront分发

## 📦 手动部署步骤

### Step 1: 创建S3 Buckets
```bash
# 文档存储bucket
aws s3api create-bucket \
  --bucket rag-documents-375004070918-us-east-1 \
  --region us-east-1

# 前端静态网站bucket
aws s3api create-bucket \
  --bucket rag-web-375004070918-us-east-1 \
  --region us-east-1

# 配置静态网站托管
aws s3 website s3://rag-web-375004070918-us-east-1/ \
  --index-document index.html \
  --error-document error.html
```

### Step 2: 部署Lambda函数

#### 2.1 创建Lambda执行角色
```bash
# 创建IAM角色
aws iam create-role \
  --role-name rag-lambda-role \
  --assume-role-policy-document file://lambda-trust-policy.json

# 附加策略
aws iam attach-role-policy \
  --role-name rag-lambda-role \
  --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole
```

#### 2.2 打包并部署Lambda函数
```bash
# 打包query handler
cd lambda_functions
zip -r query_handler.zip query_handler.py vector_client.py
aws lambda create-function \
  --function-name rag-query \
  --runtime python3.9 \
  --role arn:aws:iam::375004070918:role/rag-lambda-role \
  --handler query_handler.handler \
  --zip-file fileb://query_handler.zip \
  --timeout 60 \
  --memory-size 1024 \
  --environment Variables="{ZILLIZ_ENDPOINT=$ZILLIZ_ENDPOINT,ZILLIZ_TOKEN=$ZILLIZ_TOKEN}"

# 打包document handler
zip -r document_handler.zip document_handler.py
aws lambda create-function \
  --function-name rag-document-handler \
  --runtime python3.9 \
  --role arn:aws:iam::375004070918:role/rag-lambda-role \
  --handler document_handler.lambda_handler \
  --zip-file fileb://document_handler.zip \
  --timeout 30 \
  --memory-size 512

# 打包health handler
zip -r health_handler.zip health_handler.py
aws lambda create-function \
  --function-name rag-health-check \
  --runtime python3.9 \
  --role arn:aws:iam::375004070918:role/rag-lambda-role \
  --handler health_handler.handler \
  --zip-file fileb://health_handler.zip \
  --timeout 10 \
  --memory-size 256
```

### Step 3: 配置API Gateway

#### 3.1 创建REST API
```bash
# 创建API
aws apigateway create-rest-api \
  --name "RAG-API" \
  --description "RAG System API" \
  --region us-east-1
```

#### 3.2 创建资源和方法
```bash
API_ID=abbrw64qve  # 替换为实际的API ID

# 获取根资源ID
ROOT_ID=$(aws apigateway get-resources \
  --rest-api-id $API_ID \
  --query "items[0].id" \
  --output text)

# 创建/health资源
aws apigateway create-resource \
  --rest-api-id $API_ID \
  --parent-id $ROOT_ID \
  --path-part health

# 创建/query资源
aws apigateway create-resource \
  --rest-api-id $API_ID \
  --parent-id $ROOT_ID \
  --path-part query

# 创建/documents资源
aws apigateway create-resource \
  --rest-api-id $API_ID \
  --parent-id $ROOT_ID \
  --path-part documents
```

#### 3.3 配置Lambda集成
```bash
# 为每个端点配置方法和集成
# 示例：配置/health GET方法
aws apigateway put-method \
  --rest-api-id $API_ID \
  --resource-id $HEALTH_ID \
  --http-method GET \
  --authorization-type NONE

aws apigateway put-integration \
  --rest-api-id $API_ID \
  --resource-id $HEALTH_ID \
  --http-method GET \
  --type AWS_PROXY \
  --integration-http-method POST \
  --uri arn:aws:apigateway:us-east-1:lambda:path/2015-03-31/functions/arn:aws:lambda:us-east-1:375004070918:function:rag-health-check/invocations
```

#### 3.4 配置CORS
```bash
# 为每个资源添加OPTIONS方法
aws apigateway put-method \
  --rest-api-id $API_ID \
  --resource-id $RESOURCE_ID \
  --http-method OPTIONS \
  --authorization-type NONE

# 配置Mock集成返回CORS头
aws apigateway put-integration \
  --rest-api-id $API_ID \
  --resource-id $RESOURCE_ID \
  --http-method OPTIONS \
  --type MOCK \
  --request-templates '{"application/json":"{\"statusCode\": 200}"}'
```

#### 3.5 部署API
```bash
# 创建部署
aws apigateway create-deployment \
  --rest-api-id $API_ID \
  --stage-name prod \
  --description "Production deployment"
```

### Step 4: 部署前端

#### 4.1 上传静态文件
```bash
# 上传所有前端文件
aws s3 sync app/views/web/ s3://rag-web-375004070918-us-east-1/ \
  --exclude ".git/*" \
  --exclude "*.pyc" \
  --exclude "__pycache__/*"
```

#### 4.2 设置bucket策略
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "PublicReadGetObject",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::rag-web-375004070918-us-east-1/*"
    }
  ]
}
```

### Step 5: 配置CloudFront

#### 5.1 创建分发
```bash
aws cloudfront create-distribution \
  --distribution-config file://cloudfront-config.json
```

#### 5.2 等待部署完成
```bash
# 查看分发状态
aws cloudfront get-distribution \
  --id E19PMUT3YKSBNO \
  --query "Distribution.Status" \
  --output text
```

## ✅ 验证部署

### 1. 测试API端点
```bash
# 健康检查
curl https://abbrw64qve.execute-api.us-east-1.amazonaws.com/prod/health

# 测试查询
curl -X POST https://abbrw64qve.execute-api.us-east-1.amazonaws.com/prod/query \
  -H "Content-Type: application/json" \
  -d '{"query": "What is RAG?", "use_rag": true}'
```

### 2. 测试前端
访问: https://dfg648088lloi.cloudfront.net

### 3. 测试文档上传
```bash
python test_document_upload.py
```

## 🔧 常见问题

### CORS错误
```bash
# 检查OPTIONS方法是否配置
aws apigateway get-method \
  --rest-api-id $API_ID \
  --resource-id $RESOURCE_ID \
  --http-method OPTIONS
```

### Lambda权限问题
```bash
# 添加S3权限
aws iam attach-role-policy \
  --role-name rag-lambda-role \
  --policy-arn arn:aws:iam::aws:policy/AmazonS3FullAccess

# 添加Bedrock权限
aws iam attach-role-policy \
  --role-name rag-lambda-role \
  --policy-arn arn:aws:iam::aws:policy/AmazonBedrockFullAccess
```

### CloudFront缓存问题
```bash
# 创建缓存失效
aws cloudfront create-invalidation \
  --distribution-id E19PMUT3YKSBNO \
  --paths "/*"
```

## 📊 监控和日志

### 查看Lambda日志
```bash
# 实时查看日志
aws logs tail /aws/lambda/rag-query --follow

# 搜索错误
aws logs filter-log-events \
  --log-group-name /aws/lambda/rag-query \
  --filter-pattern "ERROR"
```

### CloudWatch指标
```bash
# 查看Lambda指标
aws cloudwatch get-metric-statistics \
  --namespace AWS/Lambda \
  --metric-name Invocations \
  --dimensions Name=FunctionName,Value=rag-query \
  --start-time 2025-08-09T00:00:00Z \
  --end-time 2025-08-10T00:00:00Z \
  --period 3600 \
  --statistics Sum
```

## 🔐 安全建议

1. **使用IAM角色**而不是硬编码凭证
2. **启用S3加密**保护文档
3. **配置API密钥**限制访问
4. **使用VPC**隔离Lambda函数
5. **定期轮换**Zilliz API令牌
6. **监控异常**API调用模式

## 📝 更新和维护

### 更新Lambda函数
```bash
# 更新函数代码
aws lambda update-function-code \
  --function-name rag-query \
  --zip-file fileb://query_handler.zip
```

### 更新前端
```bash
# 同步新文件
aws s3 sync app/views/web/ s3://rag-web-375004070918-us-east-1/

# 清除CDN缓存
aws cloudfront create-invalidation \
  --distribution-id E19PMUT3YKSBNO \
  --paths "/*"
```

## 🎉 部署完成

恭喜！您的RAG系统已成功部署。

访问: **https://dfg648088lloi.cloudfront.net**

---

**支持联系**: support@example.com
**文档版本**: 1.0.0
**最后更新**: 2025-08-09