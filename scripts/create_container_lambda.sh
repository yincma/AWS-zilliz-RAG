#!/bin/bash

# 创建新的容器版Lambda函数

set -e

echo "🐳 创建容器版Lambda函数..."

# 配置
AWS_REGION="us-east-1"
AWS_ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
FUNCTION_NAME="RAG-API-Container-Query"
ECR_URI="$AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/rag-lambda-query:latest"
ROLE_ARN="arn:aws:iam::$AWS_ACCOUNT_ID:role/RAG-API-prod-LambdaExecutionRoleD5C26073-qyqoOsCzYwmo"

# 颜色
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -e "${YELLOW}创建新的Lambda函数（容器版）...${NC}"

# 获取现有Lambda的环境变量
echo "获取现有Lambda环境变量..."
ENV_VARS=$(aws lambda get-function-configuration \
    --function-name RAG-API-prod-QueryFunctionBDF4DE5B-fefZmPcq2NrF \
    --query 'Environment.Variables' \
    --output json)

# 创建新的Lambda函数
aws lambda create-function \
    --function-name "$FUNCTION_NAME" \
    --package-type Image \
    --code ImageUri="$ECR_URI" \
    --role "$ROLE_ARN" \
    --timeout 300 \
    --memory-size 1536 \
    --environment "Variables=$ENV_VARS" \
    --region "$AWS_REGION" \
    --output json > /dev/null 2>&1 || {
    # 如果函数已存在，更新它
    echo "函数已存在，更新中..."
    aws lambda update-function-code \
        --function-name "$FUNCTION_NAME" \
        --image-uri "$ECR_URI" \
        --region "$AWS_REGION" \
        --output json > /dev/null
    
    aws lambda update-function-configuration \
        --function-name "$FUNCTION_NAME" \
        --environment "Variables=$ENV_VARS" \
        --timeout 300 \
        --memory-size 1536 \
        --region "$AWS_REGION" \
        --output json > /dev/null
}

echo -e "${GREEN}✅ Lambda函数创建/更新成功！${NC}"

# 等待函数激活
echo "等待函数激活..."
aws lambda wait function-active \
    --function-name "$FUNCTION_NAME" \
    --region "$AWS_REGION"

# 测试函数
echo -e "${YELLOW}测试Lambda函数...${NC}"
aws lambda invoke \
    --function-name "$FUNCTION_NAME" \
    --payload '{"httpMethod": "GET", "path": "/health"}' \
    --region "$AWS_REGION" \
    response.json \
    --cli-binary-format raw-in-base64-out

echo "响应内容："
cat response.json | python3 -m json.tool
rm -f response.json

echo ""
echo -e "${GREEN}✅ 容器版Lambda函数已就绪！${NC}"
echo ""
echo "函数名称: $FUNCTION_NAME"
echo "容器镜像: $ECR_URI"
echo ""
echo "下一步："
echo "1. 在API Gateway中将集成切换到新的Lambda函数"
echo "2. 或者删除旧Lambda并重命名新Lambda"