# RAG API Curl 示例

以下是使用curl调用RAG API的示例。

## 1. 健康检查

```bash
# 检查服务器健康状态
curl http://localhost:8000/health

# 获取系统状态
curl http://localhost:8000/status
```

## 2. 文档摄入

```bash
# 摄入文档
curl -X POST http://localhost:8000/api/v1/ingest \
  -H "Content-Type: application/json" \
  -d '{
    "file_paths": ["sample_docs/rag_intro.txt"]
  }'
```

## 3. 查询问题

```bash
# 查询RAG系统
curl -X POST http://localhost:8000/api/v1/query \
  -H "Content-Type: application/json" \
  -d '{
    "query": "什么是RAG系统？",
    "top_k": 5
  }'

# 查询更多问题
curl -X POST http://localhost:8000/api/v1/query \
  -H "Content-Type: application/json" \
  -d '{
    "query": "RAG有哪些优势？",
    "top_k": 3
  }'
```

## 4. 向量搜索

```bash
# 搜索相关文档
curl -X POST http://localhost:8000/api/v1/search \
  -H "Content-Type: application/json" \
  -d '{
    "query": "RAG技术",
    "top_k": 5
  }'

# 带过滤条件的搜索
curl -X POST http://localhost:8000/api/v1/search \
  -H "Content-Type: application/json" \
  -d '{
    "query": "向量数据库",
    "top_k": 3,
    "filter_expr": "source == \"rag_intro.txt\""
  }'
```

## 5. 文档管理

```bash
# 列出所有文档
curl http://localhost:8000/api/v1/documents

# 获取特定文档信息
curl http://localhost:8000/api/v1/documents/rag_intro.txt

# 删除文档
curl -X DELETE http://localhost:8000/api/v1/documents/test.txt
```

## 6. 集合管理

```bash
# 获取集合统计信息
curl http://localhost:8000/api/v1/collection/stats

# 清空集合（危险操作）
curl -X DELETE http://localhost:8000/api/v1/collection/clear
```

## 7. 使用jq格式化输出

如果安装了jq，可以格式化JSON输出：

```bash
# 格式化查询结果
curl -X POST http://localhost:8000/api/v1/query \
  -H "Content-Type: application/json" \
  -d '{"query": "什么是RAG？", "top_k": 3}' \
  | jq '.'

# 只显示答案
curl -X POST http://localhost:8000/api/v1/query \
  -H "Content-Type: application/json" \
  -d '{"query": "什么是RAG？", "top_k": 3}' \
  | jq '.answer'

# 显示置信度
curl -X POST http://localhost:8000/api/v1/query \
  -H "Content-Type: application/json" \
  -d '{"query": "什么是RAG？", "top_k": 3}' \
  | jq '.confidence'
```

## 8. 批量查询脚本

创建文件 `queries.txt`:
```
什么是RAG？
RAG有哪些优势？
RAG的工作原理是什么？
```

批量查询脚本 `batch_query.sh`:
```bash
#!/bin/bash

while IFS= read -r query; do
  echo "查询: $query"
  curl -s -X POST http://localhost:8000/api/v1/query \
    -H "Content-Type: application/json" \
    -d "{\"query\": \"$query\", \"top_k\": 3}" \
    | jq '.answer'
  echo "---"
done < queries.txt
```

## 9. 性能测试

```bash
# 使用time测量响应时间
time curl -X POST http://localhost:8000/api/v1/query \
  -H "Content-Type: application/json" \
  -d '{"query": "什么是RAG？", "top_k": 3}'

# 并发测试（需要GNU parallel）
seq 1 10 | parallel -j 5 'curl -s -X POST http://localhost:8000/api/v1/query \
  -H "Content-Type: application/json" \
  -d "{\"query\": \"测试查询{}\", \"top_k\": 3}" \
  | jq -r ".answer | length"'
```

## 10. 错误处理

```bash
# 检查HTTP状态码
curl -w "\nHTTP Status: %{http_code}\n" \
  -X POST http://localhost:8000/api/v1/query \
  -H "Content-Type: application/json" \
  -d '{"query": "测试查询"}'

# 静默模式，只显示错误
curl -sf http://localhost:8000/health || echo "服务器不可用"
```

## 注意事项

1. 确保服务器在运行: `./start_server.sh`
2. 默认端口是8000，可以修改BASE_URL
3. 文档路径必须是服务器可访问的路径
4. 大文件可能需要增加超时时间: `--max-time 60`