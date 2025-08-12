# 架构图更新记录

## 更新时间
2025-08-12

## 更新内容

### 已完成的更新

1. **修复了错误的图标使用**
   - ✅ 所有向量数据库组件统一使用 Zilliz 官方图标（星形放射状蓝紫渐变图案）
   - ✅ 所有 Python 处理逻辑改为 AWS Lambda 图标（橙色 λ 符号）

2. **更新的架构图文件**
   - `system_architecture.png` - AWS-Zilliz-RAG系统架构图
   - `mvc_architecture.png` - MVC架构层次图  
   - `rag_data_flow.png` - RAG查询处理流程图
   - `document_ingestion.png` - 文档摄入流程图

### 技术实现

- 使用 `diagrams` Python 库生成架构图
- 通过 `Custom` 类加载自定义 Zilliz 图标（`Zilliz.jpeg`）
- 所有 Python 处理组件统一使用 AWS Lambda 服务图标

### 脚本位置

所有架构图生成脚本位于：`/docs/diagrams/`

- `generate_all.py` - 主生成脚本
- `system_architecture.py` - 系统架构图脚本
- `mvc_architecture.py` - MVC架构图脚本
- `rag_data_flow.py` - RAG数据流程图脚本
- `document_ingestion.py` - 文档摄入流程图脚本

## 架构特点

### 无服务器架构
- 所有业务逻辑运行在 AWS Lambda 上
- 无需管理服务器基础设施
- 自动扩展，按需付费

### 向量数据库
- 使用 Zilliz Cloud 作为托管向量数据库
- 高性能向量检索
- 支持大规模向量存储

### AI 服务
- Amazon Bedrock Nova Pro - LLM 生成
- Amazon Titan Embeddings - 向量化
- 完全托管的 AI 服务

## 使用说明

要重新生成架构图：

```bash
cd docs/diagrams
python3 generate_all.py
```

生成的图像将保存在 `docs/images/` 目录下。