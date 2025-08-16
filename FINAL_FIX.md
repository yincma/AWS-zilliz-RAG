# 最终修复方案：Score和置信度优化

## 问题总结

1. **置信度硬编码**：永远是80%（有文档）或30%（无文档）
2. **Score计算过于严格**：L2距离16.3 → 18.5%分数太低

## 修复代码

### 文件：`app/models/rag_simple.py`

```python
# 在文件顶部导入
import math

# 修改第209-217行的score计算
# 原代码：
score = max(0, min(100, 100 - actual_distance * 5))

# 改为（方案A - 温和线性）：
score = max(0, min(100, 100 - actual_distance * 2.5))
# 效果：L2=16.3 → 59%，L2=11.2 → 72%

# 或（方案B - 指数衰减，更自然）：
score = math.exp(-actual_distance / 15) * 100
# 效果：L2=16.3 → 34%，L2=11.2 → 47%

# 或（方案C - 分段映射，最精确）：
if actual_distance <= 5:
    score = 100 - actual_distance * 2  # 0-5: 100-90
elif actual_distance <= 10:
    score = 90 - (actual_distance - 5) * 4  # 5-10: 90-70
elif actual_distance <= 20:
    score = 70 - (actual_distance - 10) * 3  # 10-20: 70-40
else:
    score = max(0, 40 - (actual_distance - 20) * 2)  # >20: 40-0
```

### 修改置信度计算（第472-477行）

```python
# 原代码：
confidence=0.8 if relevant_docs else 0.3

# 改为：
# 基于实际相似度计算置信度
if not relevant_docs:
    confidence = 0.2
else:
    # 获取所有文档的分数
    doc_scores = [doc.score for doc in relevant_docs if doc.score is not None]
    if doc_scores:
        # 基于最高分和平均分计算
        max_score = max(doc_scores)
        avg_score = sum(doc_scores) / len(doc_scores)
        # 置信度 = 70%最高分 + 30%平均分
        confidence = (max_score * 0.7 + avg_score * 0.3) / 100
        # 根据文档数量微调（1个文档*0.8，2个*0.9，3个以上*1.0）
        doc_factor = min(1.0, 0.7 + len(doc_scores) * 0.1)
        confidence = min(1.0, confidence * doc_factor)
    else:
        confidence = 0.3  # 有文档但无分数时的默认值
```

## 选择建议

### 🎯 推荐方案：温和线性（系数2.5）

**优点**：
- 简单易懂
- L2=10时仍有75%分数
- 大部分文档都能获得合理分数

**效果**：
- L2=5 → 87.5%
- L2=10 → 75%
- L2=15 → 62.5%
- L2=20 → 50%

### 完整修复代码

```python
# 第209-217行
distance_squared = getattr(hit, 'distance', 0)
actual_distance = math.sqrt(distance_squared) if distance_squared > 0 else 0
# 使用更温和的系数2.5
score = max(0, min(100, 100 - actual_distance * 2.5))

# 第472-477行
if not relevant_docs:
    confidence = 0.2
else:
    doc_scores = [doc.score for doc in relevant_docs if doc.score is not None]
    if doc_scores:
        max_score = max(doc_scores)
        avg_score = sum(doc_scores) / len(doc_scores)
        confidence = min(1.0, (max_score * 0.7 + avg_score * 0.3) / 100)
    else:
        confidence = 0.3
```

## 部署命令

```bash
# 1. 构建新镜像
docker buildx build \
  --platform linux/amd64 \
  --provenance=false \
  -t 375004070918.dkr.ecr.us-east-1.amazonaws.com/rag-lambda-query:final-fix \
  -f Dockerfile.lambda \
  --push .

# 2. 更新Lambda
aws lambda update-function-code \
  --function-name RAG-API-prod-QueryFunctionBDF4DE5B-OMJ6AR23nd0y \
  --image-uri "375004070918.dkr.ecr.us-east-1.amazonaws.com/rag-lambda-query:final-fix"

# 3. 测试
curl -X POST https://xzk90g9by0.execute-api.us-east-1.amazonaws.com/prod/query \
  -H "Content-Type: application/json" \
  -d '{"query": "What is RAG?", "top_k": 3}' | jq .
```

## 预期效果

| 文档 | L2距离 | 旧Score | 新Score | 旧置信度 | 新置信度 |
|------|--------|---------|---------|----------|----------|
| README | 11.2 | 44% | 72% | 80% | ~65% |
| document | 16.3 | 18% | 59% | 80% | ~65% |
| 完美匹配 | 0 | 100% | 100% | 80% | ~90% |
| 无结果 | - | - | - | 30% | 20% |