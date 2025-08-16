#!/bin/bash

# Lambda Package Builder Script
# 构建优化的Lambda部署包，包含所有必要依赖

set -e  # 遇到错误立即退出

echo "🔧 开始构建Lambda部署包..."

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# 获取脚本所在目录的父目录（项目根目录）
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PROJECT_ROOT="$( cd "$SCRIPT_DIR/.." && pwd )"
cd "$PROJECT_ROOT"

# 构建目录
BUILD_DIR="lambda_build_temp"
QUERY_BUILD="$BUILD_DIR/query"
INGEST_BUILD="$BUILD_DIR/ingest"
STATS_BUILD="$BUILD_DIR/stats"
DELETE_BUILD="$BUILD_DIR/delete"

# 清理旧的构建目录
echo "🧹 清理旧的构建目录..."
rm -rf "$BUILD_DIR"
rm -f zilliz-rag-*.zip

# 创建构建目录
echo "📁 创建构建目录..."
mkdir -p "$QUERY_BUILD"
mkdir -p "$INGEST_BUILD"
mkdir -p "$STATS_BUILD"
mkdir -p "$DELETE_BUILD"

# 复制Lambda处理器文件
echo "📋 复制Lambda处理器文件..."
cp app/controllers/lambda_handlers/query_handler_v2.py "$QUERY_BUILD/query_handler.py"
cp app/controllers/lambda_handlers/ingest_handler.py "$INGEST_BUILD/"
cp app/controllers/lambda_handlers/stats_handler.py "$STATS_BUILD/" 2>/dev/null || true
cp app/controllers/lambda_handlers/delete_handler.py "$DELETE_BUILD/" 2>/dev/null || true

# 复制CORS helper
echo "📋 复制CORS helper..."
cp app/controllers/lambda_handlers/cors_helper.py "$QUERY_BUILD/" 2>/dev/null || true
cp app/controllers/lambda_handlers/cors_helper.py "$INGEST_BUILD/" 2>/dev/null || true
cp app/controllers/lambda_handlers/cors_helper.py "$STATS_BUILD/" 2>/dev/null || true
cp app/controllers/lambda_handlers/cors_helper.py "$DELETE_BUILD/" 2>/dev/null || true

# 复制必要的模型文件
echo "📋 复制模型和工具文件..."
for dir in "$QUERY_BUILD" "$INGEST_BUILD" "$STATS_BUILD" "$DELETE_BUILD"; do
    if [ -d "$dir" ]; then
        # 创建app目录结构
        mkdir -p "$dir/app/models"
        mkdir -p "$dir/app/controllers"
        mkdir -p "$dir/app/views/api"
        mkdir -p "$dir/config"
        
        # 复制模型文件
        cp app/models/*.py "$dir/app/models/" 2>/dev/null || true
        cp app/controllers/*.py "$dir/app/controllers/" 2>/dev/null || true
        cp app/views/api/*.py "$dir/app/views/api/" 2>/dev/null || true
        
        # 复制配置文件
        cp config/*.py "$dir/config/" 2>/dev/null || true
        
        # 创建__init__.py文件
        touch "$dir/app/__init__.py"
        touch "$dir/app/models/__init__.py"
        touch "$dir/app/controllers/__init__.py"
        touch "$dir/app/views/__init__.py"
        touch "$dir/app/views/api/__init__.py"
        touch "$dir/config/__init__.py"
    fi
done

# 检查Docker是否安装并运行
check_docker() {
    if ! command -v docker &> /dev/null; then
        echo -e "${RED}❌ Docker未安装！${NC}"
        echo "请安装Docker后再运行此脚本："
        echo "  macOS: brew install --cask docker"
        echo "  Linux: curl -fsSL https://get.docker.com | sh"
        exit 1
    fi
    
    if ! docker info &> /dev/null; then
        echo -e "${RED}❌ Docker daemon未运行！${NC}"
        echo "请启动Docker后再运行此脚本："
        echo "  macOS: 打开Docker Desktop应用"
        echo "  Linux: sudo systemctl start docker"
        exit 1
    fi
    
    echo -e "${GREEN}✅ Docker已就绪${NC}"
}

# 强制检查Docker
check_docker

echo "🐳 使用Docker构建Linux兼容的Lambda依赖..."

# 创建精简的requirements文件
cat > "$BUILD_DIR/requirements-lambda.txt" << EOF
boto3>=1.34.0
python-dotenv>=1.0.0
pydantic>=2.6.1
pydantic-settings>=2.2.1
numpy<2.0,>=1.19.0
pymilvus>=2.3.0
grpcio>=1.48.0
protobuf>=3.20.0
ujson>=5.0.0
pandas<2.0.0
EOF

# 使用Docker构建依赖（显示进度）
echo "📦 构建Query Lambda依赖..."
docker run --rm \
    -v "$PROJECT_ROOT:/workspace" \
    -w /workspace \
    --platform linux/amd64 \
    python:3.9-slim \
    bash -c "
        pip install --no-cache-dir -r $BUILD_DIR/requirements-lambda.txt -t $QUERY_BUILD/ --upgrade
    " || {
    echo -e "${RED}❌ Docker构建失败！${NC}"
    exit 1
}

echo "📦 构建Ingest Lambda依赖..."
docker run --rm \
    -v "$PROJECT_ROOT:/workspace" \
    -w /workspace \
    --platform linux/amd64 \
    python:3.9-slim \
    bash -c "
        pip install --no-cache-dir -r $BUILD_DIR/requirements-lambda.txt -t $INGEST_BUILD/ --upgrade
    " || {
    echo -e "${RED}❌ Docker构建失败！${NC}"
    exit 1
}

echo "📦 构建Stats Lambda依赖..."
docker run --rm \
    -v "$PROJECT_ROOT:/workspace" \
    -w /workspace \
    --platform linux/amd64 \
    python:3.9-slim \
    bash -c "
        pip install --no-cache-dir boto3 python-dotenv pydantic pydantic-settings -t $STATS_BUILD/ --upgrade
    " || {
    echo -e "${RED}❌ Docker构建失败！${NC}"
    exit 1
}

echo "📦 构建Delete Lambda依赖..."
docker run --rm \
    -v "$PROJECT_ROOT:/workspace" \
    -w /workspace \
    --platform linux/amd64 \
    python:3.9-slim \
    bash -c "
        pip install --no-cache-dir boto3 python-dotenv pydantic pydantic-settings -t $DELETE_BUILD/ --upgrade
    " || {
    echo -e "${RED}❌ Docker构建失败！${NC}"
    exit 1
}

echo -e "${GREEN}✅ Docker构建完成！${NC}"

# 不再需要numpy和pandas stubs，因为SimpleRAG不依赖它们
echo "📋 跳过numpy和pandas stubs（不再需要）..."

# 清理不必要的文件以减小包大小
echo "🧹 清理不必要的文件..."
for dir in "$QUERY_BUILD" "$INGEST_BUILD" "$STATS_BUILD" "$DELETE_BUILD"; do
    if [ -d "$dir" ]; then
        find "$dir" -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
        find "$dir" -type d -name "*.dist-info" -exec rm -rf {} + 2>/dev/null || true
        find "$dir" -type d -name "tests" -exec rm -rf {} + 2>/dev/null || true
        find "$dir" -type d -name "test" -exec rm -rf {} + 2>/dev/null || true
        find "$dir" -type f -name "*.pyc" -delete 2>/dev/null || true
        find "$dir" -type f -name "*.pyo" -delete 2>/dev/null || true
        find "$dir" -type f -name "*.so" -size +5M -delete 2>/dev/null || true
        
        # 删除不必要的大文件
        rm -rf "$dir/numpy.libs" 2>/dev/null || true
        rm -rf "$dir/scipy" 2>/dev/null || true
        rm -rf "$dir/matplotlib" 2>/dev/null || true
    fi
done

# 创建ZIP包
echo "📦 创建ZIP部署包..."

# Query Handler包
if [ -d "$QUERY_BUILD" ] && [ -f "$QUERY_BUILD/query_handler.py" ]; then
    cd "$QUERY_BUILD"
    zip -r9q "../query_lambda.zip" . \
        -x "*.pyc" \
        -x "*__pycache__*" \
        -x "*.egg-info/*" \
        -x "*.dist-info/RECORD" \
        -x "*.dist-info/WHEEL" \
        -x "*.dist-info/top_level.txt"
    cd "$PROJECT_ROOT"
    echo -e "${GREEN}✅ query_lambda.zip 创建成功${NC}"
fi

# Ingest Handler包
if [ -d "$INGEST_BUILD" ] && [ -f "$INGEST_BUILD/ingest_handler.py" ]; then
    cd "$INGEST_BUILD"
    zip -r9q "../ingest_lambda.zip" . \
        -x "*.pyc" \
        -x "*__pycache__*" \
        -x "*.egg-info/*" \
        -x "*.dist-info/RECORD" \
        -x "*.dist-info/WHEEL" \
        -x "*.dist-info/top_level.txt"
    cd "$PROJECT_ROOT"
    echo -e "${GREEN}✅ ingest_lambda.zip 创建成功${NC}"
fi

# Stats Handler包（如果存在）
if [ -d "$STATS_BUILD" ] && [ -f "$STATS_BUILD/stats_handler.py" ]; then
    cd "$STATS_BUILD"
    zip -r9q "../stats_lambda.zip" . \
        -x "*.pyc" \
        -x "*__pycache__*" \
        -x "*.egg-info/*" \
        -x "*.dist-info/RECORD" \
        -x "*.dist-info/WHEEL" \
        -x "*.dist-info/top_level.txt"
    cd "$PROJECT_ROOT"
    echo -e "${GREEN}✅ stats_lambda.zip 创建成功${NC}"
fi

# Delete Handler包（如果存在）
if [ -d "$DELETE_BUILD" ] && [ -f "$DELETE_BUILD/delete_handler.py" ]; then
    cd "$DELETE_BUILD"
    zip -r9q "../delete_lambda.zip" . \
        -x "*.pyc" \
        -x "*__pycache__*" \
        -x "*.egg-info/*" \
        -x "*.dist-info/RECORD" \
        -x "*.dist-info/WHEEL" \
        -x "*.dist-info/top_level.txt"
    cd "$PROJECT_ROOT"
    echo -e "${GREEN}✅ delete_lambda.zip 创建成功${NC}"
fi

# 显示包大小
echo ""
echo "📊 Lambda包大小："
for zip_file in "$BUILD_DIR"/*.zip; do
    if [ -f "$zip_file" ]; then
        filename=$(basename "$zip_file")
        size=$(ls -lh "$zip_file" | awk '{print $5}')
        echo -e "  ${YELLOW}$filename${NC}: $size"
        
        # 检查大小是否超过Lambda限制
        size_bytes=$(stat -f%z "$zip_file" 2>/dev/null || stat -c%s "$zip_file" 2>/dev/null)
        if [ "$size_bytes" -gt 52428800 ]; then  # 50MB
            echo -e "  ${RED}⚠️  警告: $filename 超过50MB Lambda限制！${NC}"
        elif [ "$size_bytes" -gt 262144000 ]; then  # 250MB
            echo -e "  ${RED}❌ 错误: $filename 超过250MB Lambda解压限制！${NC}"
        fi
    fi
done

# 清理子目录但保留ZIP文件
echo ""
echo "🧹 清理构建子目录..."
rm -rf "$BUILD_DIR/query" "$BUILD_DIR/ingest" "$BUILD_DIR/stats" "$BUILD_DIR/delete"
rm -f "$BUILD_DIR/requirements-lambda.txt" 2>/dev/null || true

echo ""
echo -e "${GREEN}✅ Lambda包构建完成！${NC}"
echo ""
echo "下一步："
echo "1. 使用 'make deploy' 部署到AWS"
echo "2. 或使用 'make deploy-lambda-direct' 直接更新Lambda函数"
echo "3. 使用 'make test-lambda' 测试Lambda函数"