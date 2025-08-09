#!/bin/bash

# 启动FastAPI服务器脚本

echo "启动 FastAPI 服务器..."

# 检查是否已经在运行
if lsof -Pi :8000 -sTCP:LISTEN -t >/dev/null ; then
    echo "⚠️ 服务器已在端口 8000 运行"
    echo "使用 './stop_server.sh' 停止服务器"
    exit 1
fi

# 后台启动服务器
nohup python3 main.py > server.log 2>&1 &
SERVER_PID=$!

echo "服务器 PID: $SERVER_PID"
echo $SERVER_PID > server.pid

# 等待服务器启动
echo -n "等待服务器启动"
for i in {1..30}; do
    if curl -s http://localhost:8000/health > /dev/null 2>&1; then
        echo ""
        echo "✅ 服务器已成功启动！"
        echo "访问: http://localhost:8000"
        echo "API文档: http://localhost:8000/docs"
        echo "日志文件: server.log"
        exit 0
    fi
    echo -n "."
    sleep 1
done

echo ""
echo "❌ 服务器启动失败"
echo "检查日志: tail -f server.log"
exit 1