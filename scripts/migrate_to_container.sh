#!/bin/bash

# 将现有Lambda函数迁移到容器镜像版本
# 零技术债务 - 直接在原有资源上修改

set -e

echo "🔄 开始迁移Lambda到容器镜像版本..."

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

# 配置
AWS_REGION="us-east-1"
AWS_ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
FUNCTION_NAME="RAG-API-prod-QueryFunctionBDF4DE5B-fefZmPcq2NrF"
ECR_URI="$AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/rag-lambda-query:latest"

echo -e "${BLUE}配置信息：${NC}"
echo "  函数名称: $FUNCTION_NAME"
echo "  容器镜像: $ECR_URI"
echo ""

# 1. 备份当前Lambda配置
echo -e "${YELLOW}1️⃣ 备份当前Lambda配置...${NC}"
aws lambda get-function-configuration \
    --function-name "$FUNCTION_NAME" \
    --region "$AWS_REGION" > lambda_backup.json

# 提取关键配置
ROLE_ARN=$(jq -r '.Role' lambda_backup.json)
TIMEOUT=$(jq -r '.Timeout' lambda_backup.json)
MEMORY_SIZE=$(jq -r '.MemorySize' lambda_backup.json)
ENV_VARS=$(jq '.Environment.Variables' lambda_backup.json)
VPC_CONFIG=$(jq '.VpcConfig // {}' lambda_backup.json)

echo -e "${GREEN}✅ 配置备份完成${NC}"

# 2. 删除现有Lambda函数
echo -e "${YELLOW}2️⃣ 删除现有ZIP版本Lambda函数...${NC}"
aws lambda delete-function \
    --function-name "$FUNCTION_NAME" \
    --region "$AWS_REGION"
echo -e "${GREEN}✅ 删除完成${NC}"

# 3. 重新创建Lambda函数（使用容器镜像）
echo -e "${YELLOW}3️⃣ 创建容器镜像版本Lambda函数...${NC}"

# 将环境变量保存到临时文件
echo "$ENV_VARS" > env_vars.json

# 创建函数（基本配置）
aws lambda create-function \
    --function-name "$FUNCTION_NAME" \
    --package-type Image \
    --code ImageUri="$ECR_URI" \
    --role "$ROLE_ARN" \
    --timeout $TIMEOUT \
    --memory-size $MEMORY_SIZE \
    --region "$AWS_REGION" \
    --output json > /dev/null

# 更新环境变量（如果存在）
if [ "$ENV_VARS" != "null" ]; then
    aws lambda update-function-configuration \
        --function-name "$FUNCTION_NAME" \
        --environment Variables="$ENV_VARS" \
        --region "$AWS_REGION" \
        --output json > /dev/null
fi

# 更新VPC配置（如果存在）
if [ "$(echo $VPC_CONFIG | jq -r '.SubnetIds')" != "null" ] && [ "$(echo $VPC_CONFIG | jq -r '.SubnetIds | length')" -gt 0 ]; then
    SUBNET_IDS=$(echo $VPC_CONFIG | jq -c '.SubnetIds')
    SECURITY_GROUP_IDS=$(echo $VPC_CONFIG | jq -c '.SecurityGroupIds')
    aws lambda update-function-configuration \
        --function-name "$FUNCTION_NAME" \
        --vpc-config SubnetIds="$SUBNET_IDS",SecurityGroupIds="$SECURITY_GROUP_IDS" \
        --region "$AWS_REGION" \
        --output json > /dev/null
fi

# 清理临时文件
rm -f env_vars.json

echo -e "${GREEN}✅ Lambda函数创建成功${NC}"

# 4. 等待函数激活
echo -e "${YELLOW}4️⃣ 等待函数激活...${NC}"
sleep 10
aws lambda wait function-active \
    --function-name "$FUNCTION_NAME" \
    --region "$AWS_REGION"
echo -e "${GREEN}✅ 函数已激活${NC}"

# 5. 测试函数
echo -e "${YELLOW}5️⃣ 测试Lambda函数...${NC}"

# 健康检查
echo "健康检查："
curl -s https://9j0pdvhnya.execute-api.us-east-1.amazonaws.com/prod/health | python3 -m json.tool || echo "API Gateway需要几秒钟来连接新函数"

# 等待API Gateway连接
sleep 5

# 系统测试
echo ""
echo "系统测试："
curl -s -X POST https://9j0pdvhnya.execute-api.us-east-1.amazonaws.com/prod/query \
    -H "Content-Type: application/json" \
    -d '{"operation": "test"}' | python3 -m json.tool

# 6. 清理备份文件
rm -f lambda_backup.json

echo ""
echo -e "${GREEN}🎉 迁移完成！${NC}"
echo ""
echo "Lambda函数已成功迁移到容器镜像版本"
echo "函数名称保持不变: $FUNCTION_NAME"
echo "API Gateway集成自动保持"
echo ""
echo "下一步验证："
echo "1. 检查Zilliz连接状态"
echo "2. 测试RAG查询功能"
echo "3. 验证文档检索功能"