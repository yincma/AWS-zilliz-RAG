# CLAUDE.md
- 本系统内语言完全为英语
- 永远用中文和我交流
- 执行完所有工作后，执行 `afplay /System/Library/Sounds/Sosumi.aiff` 
- 严禁任何硬编码
- 执行任务时保证SOTA

本文件为 Claude Code 在此 RAG 项目中工作时提供指导。

## 项目概述

基于 AWS 和 Zilliz 的 RAG (Retrieval-Augmented Generation) 应用，使用 LangChain 框架实现文档检索增强生成。

## 项目结构（MVC 架构）

### MVC 架构说明
- **Model（模型层）**：处理所有数据相关操作、业务逻辑、与外部服务交互（Bedrock、Zilliz、S3）
- **View（视图层）**：负责数据展示、用户界面、API响应格式化
- **Controller（控制器层）**：处理请求路由、协调Model和View、控制业务流程

```
.
├── app/               # 应用主目录
│   ├── models/       # Model层 - 数据和业务逻辑
│   │   ├── document.py          # 文档模型
│   │   ├── embedding.py         # Embedding模型（Titan）
│   │   ├── vector_store.py      # 向量存储模型（Zilliz）
│   │   ├── llm.py              # LLM模型（Bedrock Nova）
│   │   └── rag_chain.py        # RAG链模型
│   │
│   ├── views/        # View层 - 展示和响应
│   │   ├── web/                # Web前端视图
│   │   │   ├── templates/      # HTML模板
│   │   │   ├── static/         # 静态资源（CSS/JS）
│   │   │   └── components/     # UI组件
│   │   └── api/                # API响应视图
│   │       ├── responses.py    # 响应格式化
│   │       └── serializers.py  # 数据序列化
│   │
│   └── controllers/  # Controller层 - 请求处理和流程控制
│       ├── rag_controller.py   # RAG主控制器
│       ├── document_controller.py  # 文档管理控制器
│       ├── search_controller.py    # 搜索控制器
│       └── lambda_handlers/    # Lambda函数处理器
│           ├── query_handler.py    # 查询处理
│           └── ingest_handler.py   # 文档摄入处理
│
├── infrastructure/   # AWS CDK 基础设施
│   ├── app.py       # CDK 应用入口
│   └── stacks/      # CDK 栈定义
│       ├── web_stack.py        # S3 + CloudFront（View层部署）
│       ├── api_stack.py        # Lambda + API Gateway（Controller层部署）
│       └── data_stack.py       # S3 + Zilliz（Model层资源）
│
├── config/          # 配置文件
│   ├── settings.py  # 应用设置
│   ├── aws.yaml    # AWS 配置
│   └── database.yaml # 数据库配置
│
├── tests/           # 测试
│   ├── models/     # 模型测试
│   ├── views/      # 视图测试
│   ├── controllers/ # 控制器测试
│   └── integration/ # 集成测试
│
├── scripts/         # 实用脚本
│   └── deploy.py   # 部署脚本
│
└── docs/           # 文档
```

## 开发命令

### 环境设置
```bash
python3 -m venv venv
source venv/bin/activate  # Mac/Linux
pip3 install -r requirements.txt
```

### 代码检查
```bash
# 格式化检查
black --check .
# 导入排序
isort --check-only .
# 代码风格检查
flake8 .
# 类型检查
mypy app/
```

### 测试
```bash
# 运行所有测试
pytest
# 运行特定测试
pytest test/test_specific.py
# 生成覆盖率报告
pytest --cov=application --cov-report=html
```

### 运行应用
```bash
# 本地运行
python application/main.py
# 开发模式
python application/main.py --debug
# 运行结束后发出系统音
python application/main.py && echo '\a'
```

### AWS CDK 命令
```bash
# 安装 CDK
pip install aws-cdk-lib
# 初始化 CDK 应用
cdk init app --language python
# 合成 CloudFormation 模板
cdk synth
# 部署栈
cdk deploy
# 销毁栈
cdk destroy
# 查看栈差异
cdk diff
```

## 技术栈

### 核心技术
- **Python 3.9+** - 主要编程语言
- **LangChain** - RAG 框架
- **boto3** - AWS SDK
- **AWS CDK (Python)** - 基础设施即代码

### AWS 服务
- **Amazon Bedrock** - LLM 服务和 Embeddings
  - Nova 模型用于生成
  - Amazon Titan Multimodal Embeddings G1 用于向量化
- **Amazon S3** - 文档存储
- **AWS Lambda** - 无服务器计算
- **Amazon CloudFront** - CDN 分发

### 数据库
- **Zilliz Cloud/Milvus** - 向量数据库

## 代码规范

遵循 [Google Python Style Guide](https://zh-google-styleguide.readthedocs.io/en/latest/google-python-styleguide/python_style_rules.html)

### 关键要点
- 使用 4 空格缩进
- 行长度限制 80 字符
- 函数和方法使用小写加下划线命名：`function_name()`
- 类名使用驼峰命名：`ClassName`
- 常量使用大写加下划线：`CONSTANT_NAME`
- 所有函数需要文档字符串

### 文档字符串示例
```python
def fetch_documents(query: str, top_k: int = 5) -> List[Document]:
    """从向量数据库检索相关文档。
    
    Args:
        query: 查询字符串
        top_k: 返回的文档数量
        
    Returns:
        相关文档列表
    """
```

## RAG 工作流程（MVC 模式）

### 请求流程
1. **用户请求** → Controller 接收（`controllers/rag_controller.py`）
2. **Controller** 调用 Model 处理业务逻辑
3. **Model** 执行数据操作（`models/`）
4. **Controller** 选择 View 返回结果（`views/`）
5. **View** 格式化响应返回用户

### RAG 具体流程
1. **文档处理**：Model层加载和分割文档 → `app/models/document.py`
2. **向量化**：使用 Amazon Titan Embeddings → `app/models/embedding.py`
3. **存储**：存入Zilliz向量数据库 → `app/models/vector_store.py`
4. **检索**：Controller协调检索流程 → `app/controllers/search_controller.py`
5. **生成**：LLM模型生成回答 → `app/models/llm.py`
6. **响应**：View层格式化输出 → `app/views/api/responses.py`

## 常用任务

### 添加新文档到向量库
```python
# scripts/ingest_documents.py
python scripts/ingest_documents.py --path docs/new_document.pdf
```

### 测试检索质量
```python
# scripts/test_retrieval.py
python scripts/test_retrieval.py --query "测试查询"
```

### 清理向量数据库
```python
# scripts/clean_vectordb.py
python scripts/clean_vectordb.py --collection-name my_collection
```

## 配置管理

配置文件位于 `config/` 目录：
- `config/aws.yaml` - AWS相关配置
- `config/zilliz.yaml` - Zilliz连接配置
- `config/langchain.yaml` - LangChain参数

使用.env覆盖配置：
```
# AWS 配置
AWS_REGION=us-east-1
AWS_ACCESS_KEY=XXXX
AWS_SECRET_ACCESS_KEY=XXXX


# Bedrock 配置
BEDROCK_MODEL_ID=anthropic.claude-3-sonnet-20240229-v1:0
EMBEDDING_MODEL_ID=amazon.titan-embed-image-v1

# Zilliz 配置
ZILLIZ_ENDPOINT=your-endpoint
ZILLIZ_TOKEN=your-token
ZILLIZ_COLLECTION=your-collection

# S3 配置
S3_BUCKET=your-bucket-name
S3_PREFIX=documents/
```

## 开发注意事项

1. **不要**将API密钥提交到代码库
2. **总是**在提交前运行代码检查
3. **确保**新功能有对应的测试
4. **使用**类型提示提高代码可读性
5. **保持**函数单一职责原则

## 调试技巧

```python
# 启用LangChain调试
import langchain
langchain.debug = True

# 查看向量数据库状态
from app.models.vector_store import get_collection_stats
stats = get_collection_stats()

# 测试 Bedrock Embedding
from app.models.embedding import test_titan_embedding
test_titan_embedding("测试文本")

# 查看 Lambda 日志
import boto3
logs = boto3.client('logs')
logs.tail_log_group('/aws/lambda/your-function-name')
```

## MVC 代码示例

### Model 层示例（app/models/vector_store.py）
```python
from pymilvus import Collection, connections
from typing import List, Dict

class VectorStore:
    """向量数据库模型，处理所有向量存储相关操作。"""
    
    def __init__(self, collection_name: str):
        self.collection_name = collection_name
        self._connect()
    
    def insert_embeddings(self, embeddings: List[float], metadata: Dict):
        """插入向量和元数据到Zilliz。"""
        # 业务逻辑实现
        pass
    
    def search(self, query_embedding: List[float], top_k: int = 5):
        """搜索相似向量。"""
        # 搜索逻辑实现
        pass
```

### Controller 层示例（app/controllers/rag_controller.py）
```python
from app.models import VectorStore, LLM, Embedding
from app.views.api import ResponseFormatter

class RAGController:
    """RAG控制器，协调Model和View。"""
    
    def __init__(self):
        self.vector_store = VectorStore("rag_collection")
        self.llm = LLM()
        self.embedding = Embedding()
        self.formatter = ResponseFormatter()
    
    def process_query(self, query: str):
        """处理用户查询请求。"""
        # 1. 生成查询向量
        query_embedding = self.embedding.generate(query)
        
        # 2. 检索相关文档
        results = self.vector_store.search(query_embedding)
        
        # 3. 生成回答
        answer = self.llm.generate_answer(query, results)
        
        # 4. 格式化响应
        return self.formatter.format_response(answer, results)
```

### View 层示例（app/views/api/responses.py）
```python
from typing import Any, Dict
import json

class ResponseFormatter:
    """API响应格式化器。"""
    
    def format_response(self, answer: str, sources: list) -> Dict[str, Any]:
        """格式化RAG响应。"""
        return {
            "status": "success",
            "data": {
                "answer": answer,
                "sources": [self._format_source(s) for s in sources],
                "timestamp": self._get_timestamp()
            }
        }
    
    def format_error(self, error: Exception) -> Dict[str, Any]:
        """格式化错误响应。"""
        return {
            "status": "error",
            "error": str(error),
            "timestamp": self._get_timestamp()
        }
```

## 任务完成提示

在脚本结束时添加系统音提示：
```python
import os
import sys

def notify_completion():
    """任务完成时发出系统提示音。"""
    if sys.platform == 'darwin':  # macOS
        os.system('afplay /System/Library/Sounds/Glass.aiff')
    elif sys.platform == 'linux':
        os.system('paplay /usr/share/sounds/freedesktop/stereo/complete.oga')
    else:  # Windows
        import winsound
        winsound.Beep(1000, 500)

# 在主程序结束时调用
if __name__ == "__main__":
    main()
    notify_completion()
```