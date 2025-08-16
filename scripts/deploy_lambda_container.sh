#!/bin/bash

# Lambda Container Deployment Script
# 使用容器镜像部署Lambda，彻底解决依赖问题

set -e

echo "🐳 开始Lambda容器镜像部署流程..."

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# 配置
AWS_REGION=${AWS_REGION:-"us-east-1"}
AWS_ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
ECR_REPOSITORY_NAME="rag-lambda-query"
IMAGE_TAG="latest"
LAMBDA_FUNCTION_NAME="RAG-API-prod-QueryFunctionBDF4DE5B-fefZmPcq2NrF"

# 项目根目录
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PROJECT_ROOT="$( cd "$SCRIPT_DIR/.." && pwd )"
cd "$PROJECT_ROOT"

echo -e "${BLUE}📋 配置信息：${NC}"
echo "  AWS账号: $AWS_ACCOUNT_ID"
echo "  区域: $AWS_REGION"
echo "  ECR仓库: $ECR_REPOSITORY_NAME"
echo "  Lambda函数: $LAMBDA_FUNCTION_NAME"
echo ""

# 1. 创建或确认ECR仓库存在
echo -e "${YELLOW}1️⃣ 检查ECR仓库...${NC}"
if aws ecr describe-repositories --repository-names "$ECR_REPOSITORY_NAME" --region "$AWS_REGION" 2>/dev/null; then
    echo -e "${GREEN}✅ ECR仓库已存在${NC}"
else
    echo "创建ECR仓库..."
    aws ecr create-repository \
        --repository-name "$ECR_REPOSITORY_NAME" \
        --region "$AWS_REGION" \
        --image-scanning-configuration scanOnPush=true \
        --image-tag-mutability MUTABLE
    echo -e "${GREEN}✅ ECR仓库创建成功${NC}"
fi

# 2. 获取ECR登录token
echo -e "${YELLOW}2️⃣ 登录到ECR...${NC}"
aws ecr get-login-password --region "$AWS_REGION" | \
    docker login --username AWS --password-stdin \
    "$AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com"
echo -e "${GREEN}✅ ECR登录成功${NC}"

# 3. 构建Docker镜像
echo -e "${YELLOW}3️⃣ 构建Docker镜像...${NC}"
ECR_IMAGE_URI="$AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$ECR_REPOSITORY_NAME:$IMAGE_TAG"

docker build \
    --platform linux/amd64 \
    -t "$ECR_REPOSITORY_NAME:$IMAGE_TAG" \
    -f Dockerfile.lambda \
    . || {
    echo -e "${RED}❌ Docker构建失败！${NC}"
    exit 1
}
echo -e "${GREEN}✅ Docker镜像构建成功${NC}"

# 4. 标记镜像
echo -e "${YELLOW}4️⃣ 标记Docker镜像...${NC}"
docker tag "$ECR_REPOSITORY_NAME:$IMAGE_TAG" "$ECR_IMAGE_URI"
echo -e "${GREEN}✅ 镜像标记完成${NC}"

# 5. 推送镜像到ECR
echo -e "${YELLOW}5️⃣ 推送镜像到ECR...${NC}"
docker push "$ECR_IMAGE_URI" || {
    echo -e "${RED}❌ 镜像推送失败！${NC}"
    exit 1
}
echo -e "${GREEN}✅ 镜像推送成功${NC}"

# 6. 更新Lambda函数使用容器镜像
echo -e "${YELLOW}6️⃣ 更新Lambda函数配置...${NC}"
aws lambda update-function-code \
    --function-name "$LAMBDA_FUNCTION_NAME" \
    --image-uri "$ECR_IMAGE_URI" \
    --region "$AWS_REGION" \
    --query 'LastUpdateStatus' \
    --output text || {
    echo -e "${RED}❌ Lambda更新失败！${NC}"
    exit 1
}

echo "等待Lambda更新完成..."
sleep 20

# 7. 检查Lambda状态
echo -e "${YELLOW}7️⃣ 检查Lambda函数状态...${NC}"
STATUS=$(aws lambda get-function-configuration \
    --function-name "$LAMBDA_FUNCTION_NAME" \
    --region "$AWS_REGION" \
    --query 'LastUpdateStatus' \
    --output text)

if [ "$STATUS" == "Successful" ]; then
    echo -e "${GREEN}✅ Lambda函数更新成功！${NC}"
else
    echo -e "${YELLOW}⚠️  Lambda状态: $STATUS${NC}"
fi

# 8. 测试API
echo -e "${YELLOW}8️⃣ 测试API功能...${NC}"
echo "健康检查："
curl -s https://9j0pdvhnya.execute-api.us-east-1.amazonaws.com/prod/health | python3 -m json.tool

echo ""
echo "系统测试："
curl -s -X POST https://9j0pdvhnya.execute-api.us-east-1.amazonaws.com/prod/query \
    -H "Content-Type: application/json" \
    -d '{"operation": "test"}' | python3 -m json.tool

echo ""
echo -e "${GREEN}🎉 容器镜像部署完成！${NC}"
echo ""
echo "镜像URI: $ECR_IMAGE_URI"
echo "Lambda函数: $LAMBDA_FUNCTION_NAME"
echo ""
echo "下一步："
echo "1. 验证Zilliz连接是否正常"
echo "2. 测试完整的RAG功能"
echo "3. 上传文档到S3进行测试"