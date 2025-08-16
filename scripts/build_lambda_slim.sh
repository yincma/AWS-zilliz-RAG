#!/bin/bash

# Lambda Package Builder Script - SLIM版本（仅远程Zilliz连接）
# 不包含milvus-lite，大幅减小包大小

set -e  # 遇到错误立即退出

echo "📦 构建精简版Lambda部署包（远程Zilliz专用）..."

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
BUILD_DIR="lambda_build_slim"
QUERY_BUILD="$BUILD_DIR/query"
INGEST_BUILD="$BUILD_DIR/ingest"

# 清理旧的构建目录
echo "🧹 清理旧的构建目录..."
rm -rf "$BUILD_DIR"
rm -f zilliz-rag-slim-*.zip

# 创建构建目录
echo "📁 创建构建目录..."
mkdir -p "$QUERY_BUILD"
mkdir -p "$INGEST_BUILD"

# 复制Lambda处理器文件
echo "📋 复制Lambda处理器文件..."
cp app/controllers/lambda_handlers/query_handler_v2.py "$QUERY_BUILD/query_handler.py"
cp app/controllers/lambda_handlers/ingest_handler.py "$INGEST_BUILD/"
cp app/controllers/lambda_handlers/cors_helper.py "$QUERY_BUILD/" 2>/dev/null || true
cp app/controllers/lambda_handlers/cors_helper.py "$INGEST_BUILD/" 2>/dev/null || true

# 复制必要的模型文件
echo "📋 复制模型和工具文件..."
for dir in "$QUERY_BUILD" "$INGEST_BUILD"; do
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

# 检查Docker
if ! command -v docker &> /dev/null; then
    echo -e "${RED}❌ Docker未安装！${NC}"
    exit 1
fi

if ! docker info &> /dev/null; then
    echo -e "${RED}❌ Docker daemon未运行！${NC}"
    exit 1
fi

echo -e "${GREEN}✅ Docker已就绪${NC}"

# 创建精简的requirements文件（不包含milvus-lite）
cat > "$BUILD_DIR/requirements-slim.txt" << EOF
boto3>=1.34.0
python-dotenv>=1.0.0
pydantic>=2.6.1
pydantic-settings>=2.2.1
numpy<2.0,>=1.19.0
pymilvus[grpc]>=2.3.0
grpcio>=1.48.0
protobuf>=3.20.0
ujson>=5.0.0
EOF

echo "🐳 使用Docker构建Linux兼容的依赖（精简版）..."

# 使用Docker构建依赖（修复grpcio兼容性）
docker run --rm \
    -v "$PROJECT_ROOT:/workspace" \
    -w /workspace \
    --platform linux/amd64 \
    python:3.9-slim \
    bash -c "
        # Query Handler依赖 - 使用兼容的grpcio版本
        pip install --no-cache-dir -t $QUERY_BUILD/ \
            --only-binary :all: \
            'grpcio==1.53.0' \
            'grpcio-status==1.53.0' && \
        pip install --no-cache-dir -t $QUERY_BUILD/ \
            'pymilvus>=2.3.0' \
            'numpy<2.0,>=1.19.0' \
            'protobuf==4.25.1' \
            'boto3>=1.34.0' \
            'python-dotenv>=1.0.0' \
            'pydantic>=2.6.1' \
            'pydantic-settings>=2.2.1' \
            'ujson>=5.0.0' \
            'setuptools>69' \
            'pandas<2.0.0' \
            'certifi' \
            'urllib3<2' && \
        # Ingest Handler依赖
        pip install --no-cache-dir -t $INGEST_BUILD/ \
            --only-binary :all: \
            'grpcio==1.53.0' \
            'grpcio-status==1.53.0' && \
        pip install --no-cache-dir -t $INGEST_BUILD/ \
            'pymilvus>=2.3.0' \
            'numpy<2.0,>=1.19.0' \
            'protobuf==4.25.1' \
            'boto3>=1.34.0' \
            'python-dotenv>=1.0.0' \
            'pydantic>=2.6.1' \
            'pydantic-settings>=2.2.1' \
            'ujson>=5.0.0' \
            'setuptools>69' \
            'pandas<2.0.0' \
            'certifi' \
            'urllib3<2'
    " || {
    echo -e "${RED}❌ Docker构建失败！${NC}"
    exit 1
}

echo -e "${GREEN}✅ Docker构建完成！${NC}"

# 清理不必要的文件以减小包大小
echo "🧹 清理不必要的文件..."
for dir in "$QUERY_BUILD" "$INGEST_BUILD"; do
    if [ -d "$dir" ]; then
        find "$dir" -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
        find "$dir" -type d -name "*.dist-info" -exec rm -rf {} + 2>/dev/null || true
        find "$dir" -type d -name "tests" -exec rm -rf {} + 2>/dev/null || true
        find "$dir" -type d -name "test" -exec rm -rf {} + 2>/dev/null || true
        find "$dir" -type f -name "*.pyc" -delete 2>/dev/null || true
        find "$dir" -type f -name "*.pyo" -delete 2>/dev/null || true
        find "$dir" -type f -name "*.so" -size +5M -delete 2>/dev/null || true
        
        # 删除milvus_lite如果存在
        rm -rf "$dir/milvus_lite" 2>/dev/null || true
        
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
    zip -r9q "../../zilliz-rag-slim-query.zip" . \
        -x "*.pyc" \
        -x "*__pycache__*" \
        -x "*.egg-info/*" \
        -x "*.dist-info/RECORD" \
        -x "*.dist-info/WHEEL" \
        -x "*.dist-info/top_level.txt" \
        -x "milvus_lite/*"
    cd "$PROJECT_ROOT"
    echo -e "${GREEN}✅ zilliz-rag-slim-query.zip 创建成功${NC}"
fi

# Ingest Handler包
if [ -d "$INGEST_BUILD" ] && [ -f "$INGEST_BUILD/ingest_handler.py" ]; then
    cd "$INGEST_BUILD"
    zip -r9q "../../zilliz-rag-slim-ingest.zip" . \
        -x "*.pyc" \
        -x "*__pycache__*" \
        -x "*.egg-info/*" \
        -x "*.dist-info/RECORD" \
        -x "*.dist-info/WHEEL" \
        -x "*.dist-info/top_level.txt" \
        -x "milvus_lite/*"
    cd "$PROJECT_ROOT"
    echo -e "${GREEN}✅ zilliz-rag-slim-ingest.zip 创建成功${NC}"
fi

# 显示包大小
echo ""
echo "📊 Lambda包大小（精简版）："
for zip_file in zilliz-rag-slim-*.zip; do
    if [ -f "$zip_file" ]; then
        filename=$(basename "$zip_file")
        size=$(ls -lh "$zip_file" | awk '{print $5}')
        echo -e "  ${YELLOW}$filename${NC}: $size"
        
        # 检查大小是否超过Lambda限制
        size_bytes=$(stat -f%z "$zip_file" 2>/dev/null || stat -c%s "$zip_file" 2>/dev/null)
        if [ "$size_bytes" -gt 52428800 ]; then  # 50MB
            echo -e "  ${YELLOW}⚠️  警告: $filename 接近50MB Lambda限制${NC}"
        fi
        if [ "$size_bytes" -gt 262144000 ]; then  # 250MB
            echo -e "  ${RED}❌ 错误: $filename 超过250MB Lambda解压限制！${NC}"
        fi
    fi
done

# 清理构建目录
echo ""
echo "🧹 清理构建目录..."
rm -rf "$BUILD_DIR"

echo ""
echo -e "${GREEN}✅ 精简版Lambda包构建完成！${NC}"
echo ""
echo "注意：此版本仅支持远程Zilliz连接，不包含本地嵌入式Milvus功能"
echo ""
echo "下一步："
echo "1. 使用 'aws lambda update-function-code' 部署"
echo "2. 确保Lambda环境变量中配置了正确的Zilliz连接信息"