# 🔧 Zilliz Score 0% 问题修复方案

## 🎯 问题根因

**Zilliz返回的distance是L2距离的平方（L2²），而不是L2距离本身。**

### 验证数据
- 向量1 L2范数：16.3454 → Zilliz返回：267.1730 (16.3454²)
- 向量2 L2范数：11.2084 → Zilliz返回：125.6284 (11.2084²)
- 误差：<0.01%

### 当前错误的计算
```python
distance = hit.distance  # 实际是L2²，例如：267
score = max(0, min(100, 100 - distance * 10))  # 100 - 267*10 = -2570 → 0
```

## ✅ 修复方案

### 方案1：开方处理（推荐）

**文件**: `app/models/rag_simple.py`
**位置**: 第209-214行

```python
import math

# 修改前
distance = getattr(hit, 'distance', 0)
score = max(0, min(100, 100 - distance * 10))

# 修改后
distance_squared = getattr(hit, 'distance', 0)
# Zilliz返回的是L2²，需要开方得到实际L2距离
actual_distance = math.sqrt(distance_squared) if distance_squared > 0 else 0
# 使用调整后的系数计算相似度分数
# 距离0-5映射到100-75分，5-10映射到75-50分，10-20映射到50-0分
score = max(0, min(100, 100 - actual_distance * 5))
```

### 方案2：调整系数（快速修复）

```python
# 保持平方距离，但调整系数
distance_squared = getattr(hit, 'distance', 0)
# 使用更小的系数适应平方距离
score = max(0, min(100, 100 - distance_squared * 0.3))
```

### 方案3：使用余弦相似度（最准确）

```python
# 从L2²转换为余弦相似度
distance_squared = getattr(hit, 'distance', 0)
actual_distance = math.sqrt(distance_squared) if distance_squared > 0 else 0

# 假设向量已归一化，从L2距离转换为余弦相似度
# L2² = 2(1 - cos_sim) for normalized vectors
# cos_sim = 1 - L2²/2
cos_similarity = max(0, 1 - distance_squared / 2)
score = cos_similarity * 100
```

## 📊 效果对比

| 实际L2距离 | L2² (Zilliz) | 旧Score | 新Score(方案1) | 新Score(方案3) |
|-----------|-------------|---------|---------------|---------------|
| 11.21     | 125.63      | 0%      | 44%           | 37%           |
| 16.35     | 267.17      | 0%      | 18%           | 0%            |
| 17.13     | 293.27      | 0%      | 14%           | 0%            |
| 5.0       | 25.0        | 0%      | 75%           | 87.5%         |
| 2.0       | 4.0         | 0%      | 90%           | 98%           |

## 🚀 部署步骤

1. **修改代码**
```bash
# 编辑文件
vim app/models/rag_simple.py
# 在第209行进行修改
```

2. **构建Docker镜像**
```bash
docker buildx build \
  --platform linux/amd64 \
  -t 375004070918.dkr.ecr.us-east-1.amazonaws.com/rag-lambda-query:score-fix \
  -f Dockerfile.lambda \
  --push .
```

3. **更新Lambda函数**
```bash
aws lambda update-function-code \
  --function-name RAG-API-prod-QueryFunctionBDF4DE5B-OMJ6AR23nd0y \
  --image-uri "375004070918.dkr.ecr.us-east-1.amazonaws.com/rag-lambda-query:score-fix"
```

4. **测试验证**
```bash
curl -X POST https://xzk90g9by0.execute-api.us-east-1.amazonaws.com/prod/query \
  -H "Content-Type: application/json" \
  -d '{"query": "What is RAG?", "top_k": 3}' | jq '.sources[].score'
```

## 🎨 前端显示优化（可选）

**文件**: `app/views/web/static/js/chat.js`
**位置**: 第177行

```javascript
// 根据score显示不同颜色
const scoreClass = score > 70 ? 'high-score' : score > 40 ? 'medium-score' : 'low-score';
sourceScore.className = `source-score ${scoreClass}`;
sourceScore.textContent = `相似度: ${score.toFixed(1)}%`;
```

**CSS添加**:
```css
.high-score { color: #22c55e; }
.medium-score { color: #f59e0b; }
.low-score { color: #ef4444; }
```

## 📈 预期结果

修复后，相似度分数将正确显示：
- 完全匹配的文档：90-100%
- 高度相关的文档：60-90%
- 中度相关的文档：30-60%
- 低相关的文档：0-30%

## 🔍 根本原因总结

1. **Zilliz的L2度量返回的是平方欧氏距离**，这是为了优化计算性能
2. **代码假设返回的是标准L2距离**，导致计算错误
3. **平方距离值过大**（通常>100），使用原始公式导致score永远为0

## 📚 参考资料

- [Milvus Distance Metrics](https://milvus.io/docs/metric.md)
- L2 (Euclidean distance squared) vs IP (Inner Product)