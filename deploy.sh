#!/bin/bash

# RAG应用一键部署脚本
# 使用方法: ./deploy.sh

set -e

echo "🚀 AWS RAG应用部署脚本"
echo "========================"
echo ""

# 检查环境变量
check_env() {
    local var_name=$1
    local var_value=${!var_name}
    
    if [ -z "$var_value" ]; then
        echo "❌ 错误: $var_name 未设置"
        return 1
    fi
    echo "✅ $var_name: 已设置"
    return 0
}

# 1. 检查必要的环境变量
echo "1️⃣ 检查环境变量..."
echo ""

# 如果.env文件存在，加载它
if [ -f .env ]; then
    echo "📝 加载 .env 文件..."
    export $(cat .env | grep -v '^#' | xargs)
fi

# 检查必需的环境变量
REQUIRED_VARS=(
    "AWS_REGION"
    "ZILLIZ_ENDPOINT"
    "ZILLIZ_TOKEN"
    "ZILLIZ_COLLECTION"
)

ALL_VARS_SET=true
for var in "${REQUIRED_VARS[@]}"; do
    if ! check_env "$var"; then
        ALL_VARS_SET=false
    fi
done

if [ "$ALL_VARS_SET" = false ]; then
    echo ""
    echo "请设置缺失的环境变量后重试"
    echo "可以创建 .env 文件或导出环境变量"
    exit 1
fi

echo ""
echo "2️⃣ 检查AWS配置..."
AWS_ACCOUNT=$(aws sts get-caller-identity --query Account --output text 2>/dev/null || echo "")
if [ -z "$AWS_ACCOUNT" ]; then
    echo "❌ AWS CLI未配置或无法访问AWS"
    echo "请运行: aws configure"
    exit 1
fi
echo "✅ AWS账号: $AWS_ACCOUNT"
echo "✅ AWS区域: $AWS_REGION"

echo ""
echo "3️⃣ 检查依赖..."

# 检查Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3未安装"
    exit 1
fi
echo "✅ Python3: $(python3 --version)"

# 检查Node.js
if ! command -v node &> /dev/null; then
    echo "❌ Node.js未安装"
    echo "请安装Node.js 14+: https://nodejs.org/"
    exit 1
fi
echo "✅ Node.js: $(node --version)"

# 检查CDK
if ! command -v cdk &> /dev/null; then
    echo "⚠️ CDK未安装，正在安装..."
    npm install -g aws-cdk@latest
fi
echo "✅ CDK: $(cdk --version)"

echo ""
echo "4️⃣ 部署配置..."
echo ""
echo "  Stage: ${STAGE:-dev}"
echo "  Bedrock模型: ${BEDROCK_MODEL_ID:-amazon.nova-lite-v1:0}"
echo "  Embedding模型: ${EMBEDDING_MODEL_ID:-amazon.titan-embed-text-v2:0}"
echo "  Zilliz集合: $ZILLIZ_COLLECTION"
echo ""

read -p "确认开始部署? (y/n): " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "部署已取消"
    exit 0
fi

echo ""
echo "5️⃣ 开始部署..."
echo ""

# 设置默认值
export STAGE=${STAGE:-dev}
export BEDROCK_MODEL_ID=${BEDROCK_MODEL_ID:-amazon.nova-lite-v1:0}
export EMBEDDING_MODEL_ID=${EMBEDDING_MODEL_ID:-amazon.titan-embed-text-v2:0}

# 执行部署
make deploy-fast

echo ""
echo "6️⃣ 获取部署输出..."
echo ""

# 获取API Gateway URL
API_URL=$(aws cloudformation describe-stacks \
    --stack-name RAG-API-${STAGE} \
    --query "Stacks[0].Outputs[?OutputKey=='ApiUrl'].OutputValue" \
    --output text 2>/dev/null || echo "")

if [ -n "$API_URL" ]; then
    echo "🌐 API端点: $API_URL"
    echo ""
    echo "测试API:"
    echo "  curl -X GET ${API_URL}health"
    echo ""
    echo "测试查询:"
    echo "  curl -X POST ${API_URL}query \\"
    echo "    -H 'Content-Type: application/json' \\"
    echo "    -d '{\"query\": \"你好\"}'"
else
    echo "⚠️ 无法获取API端点，请检查CDK输出"
fi

# 如果设置了WEB_BUCKET，部署前端
if [ -n "$WEB_BUCKET" ]; then
    echo ""
    echo "7️⃣ 部署前端..."
    make deploy-frontend
    echo ""
    echo "🌐 前端URL: https://${WEB_BUCKET}.s3.amazonaws.com/index.html"
fi

echo ""
echo "✅ 部署完成！"
echo ""
echo "下一步："
echo "1. 访问API端点测试功能"
echo "2. 使用 'make logs' 查看Lambda日志"
echo "3. 使用 'make destroy' 销毁资源"
echo ""
echo "📚 更多命令请运行: make help"