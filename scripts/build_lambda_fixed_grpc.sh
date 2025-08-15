#!/bin/bash

# Lambda Package Builder - 修复grpcio问题版本

set -e

echo "📦 构建Lambda包（修复grpcio兼容性）..."

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

# 获取项目根目录
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PROJECT_ROOT="$( cd "$SCRIPT_DIR/.." && pwd )"
cd "$PROJECT_ROOT"

# 构建目录
BUILD_DIR="lambda_build_fixed"
QUERY_BUILD="$BUILD_DIR/query"

# 清理
echo "🧹 清理旧的构建目录..."
rm -rf "$BUILD_DIR"
rm -f zilliz-rag-fixed-*.zip

# 创建目录
echo "📁 创建构建目录..."
mkdir -p "$QUERY_BUILD"

# 复制文件
echo "📋 复制应用文件..."
cp app/controllers/lambda_handlers/query_handler_v2.py "$QUERY_BUILD/query_handler.py"

# 创建app目录结构
mkdir -p "$QUERY_BUILD/app/models"
mkdir -p "$QUERY_BUILD/app/controllers"
mkdir -p "$QUERY_BUILD/app/views/api"
mkdir -p "$QUERY_BUILD/config"

# 复制模型文件
cp app/models/*.py "$QUERY_BUILD/app/models/" 2>/dev/null || true
cp app/controllers/*.py "$QUERY_BUILD/app/controllers/" 2>/dev/null || true
cp app/views/api/*.py "$QUERY_BUILD/app/views/api/" 2>/dev/null || true
cp config/*.py "$QUERY_BUILD/config/" 2>/dev/null || true

# 创建__init__.py文件
touch "$QUERY_BUILD/app/__init__.py"
touch "$QUERY_BUILD/app/models/__init__.py"
touch "$QUERY_BUILD/app/controllers/__init__.py"
touch "$QUERY_BUILD/app/views/__init__.py"
touch "$QUERY_BUILD/app/views/api/__init__.py"
touch "$QUERY_BUILD/config/__init__.py"

echo "🐳 使用Docker构建Linux兼容的依赖..."

# 使用Python 3.9镜像，指定平台为linux/amd64
docker run --rm \
    -v "$PROJECT_ROOT:/workspace" \
    -w /workspace \
    --platform linux/amd64 \
    --entrypoint /bin/bash \
    python:3.9 \
    -c "
        # 更新pip
        pip install --upgrade pip && \
        
        # 使用预编译的wheel包
        pip install \
            --no-cache-dir \
            --target $QUERY_BUILD/ \
            --platform manylinux2014_x86_64 \
            --python-version 39 \
            --implementation cp \
            --only-binary :all: \
            --upgrade \
            'grpcio==1.53.0' && \
        
        # 安装其他依赖（让pip自动解决版本兼容性）
        pip install \
            --no-cache-dir \
            --target $QUERY_BUILD/ \
            'pymilvus==2.3.0' \
            'marshmallow<4.0.0' \
            'protobuf==3.20.3' \
            'numpy==1.24.4' \
            'boto3>=1.34.0' \
            'python-dotenv>=1.0.0' \
            'pydantic>=2.6.1' \
            'pydantic-settings>=2.2.1' \
            'ujson>=5.0.0' \
            'certifi' \
            'pandas<2.0.0' \
            'urllib3<2'
    " || {
    echo -e "${RED}❌ Docker构建失败！${NC}"
    exit 1
}

echo -e "${GREEN}✅ Docker构建完成！${NC}"

# 清理不必要的文件
echo "🧹 清理不必要的文件..."
find "$QUERY_BUILD" -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
find "$QUERY_BUILD" -type d -name "*.dist-info" | grep -v grpc | xargs rm -rf 2>/dev/null || true
find "$QUERY_BUILD" -type d -name "tests" -exec rm -rf {} + 2>/dev/null || true
find "$QUERY_BUILD" -type f -name "*.pyc" -delete 2>/dev/null || true
find "$QUERY_BUILD" -type f -name "*.pyo" -delete 2>/dev/null || true

# 创建ZIP包
echo "📦 创建ZIP部署包..."
cd "$QUERY_BUILD"
zip -r9q "../../zilliz-rag-fixed-query.zip" .
cd "$PROJECT_ROOT"

echo -e "${GREEN}✅ zilliz-rag-fixed-query.zip 创建成功${NC}"

# 显示包大小
echo ""
echo "📊 Lambda包大小："
ls -lh zilliz-rag-fixed-query.zip

# 清理
rm -rf "$BUILD_DIR"

echo ""
echo -e "${GREEN}✅ Lambda包构建完成（grpcio修复版）！${NC}"