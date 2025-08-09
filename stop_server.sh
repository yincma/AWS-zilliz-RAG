#!/bin/bash

# 停止FastAPI服务器脚本

echo "停止 FastAPI 服务器..."

# 检查PID文件
if [ -f server.pid ]; then
    PID=$(cat server.pid)
    if kill -0 $PID 2>/dev/null; then
        kill $PID
        echo "✅ 服务器已停止 (PID: $PID)"
        rm server.pid
    else
        echo "⚠️ 进程不存在 (PID: $PID)"
        rm server.pid
    fi
else
    # 尝试通过端口查找进程
    PID=$(lsof -ti:8000)
    if [ ! -z "$PID" ]; then
        kill $PID
        echo "✅ 服务器已停止 (PID: $PID)"
    else
        echo "⚠️ 没有找到运行中的服务器"
    fi
fi