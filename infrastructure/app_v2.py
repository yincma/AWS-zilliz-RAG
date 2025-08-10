#!/usr/bin/env python3
"""
AWS CDK应用入口 V2 - 使用改进的栈
"""

import os
from pathlib import Path
from aws_cdk import App, Environment, Tags

# 自动加载.env文件
try:
    from dotenv import load_dotenv
    env_path = Path(__file__).parent.parent / '.env'
    if env_path.exists():
        load_dotenv(env_path, override=True)
        print(f"✅ 已加载.env配置: {env_path}")
        # 验证关键配置
        if os.environ.get('ZILLIZ_ENDPOINT'):
            print(f"  Zilliz Endpoint: {os.environ.get('ZILLIZ_ENDPOINT')[:50]}...")
        if os.environ.get('ZILLIZ_TOKEN'):
            print(f"  Zilliz Token: ***已配置***")
        if os.environ.get('BEDROCK_MODEL_ID'):
            print(f"  Bedrock Model: {os.environ.get('BEDROCK_MODEL_ID')}")
except ImportError:
    print("⚠️ python-dotenv未安装，跳过.env加载")

# 动态导入，支持选择不同版本的栈
USE_V2 = os.environ.get('USE_API_V2', 'true').lower() == 'true'

if USE_V2:
    from stacks.api_stack_v2 import ApiStackV2 as ApiStack
    print("✅ 使用API栈 V2（包含CORS修复）")
else:
    from stacks.api_stack import ApiStack
    print("ℹ️ 使用原始API栈")

from stacks.web_stack import WebStack
from stacks.data_stack import DataStack

# 获取环境变量
ACCOUNT = os.environ.get('CDK_DEFAULT_ACCOUNT') or os.environ.get('AWS_ACCOUNT')
REGION = os.environ.get('CDK_DEFAULT_REGION') or os.environ.get('AWS_REGION', 'us-east-1')

# 如果没有账号信息，尝试从AWS CLI获取
if not ACCOUNT:
    try:
        import boto3
        sts = boto3.client('sts')
        caller_identity = sts.get_caller_identity()
        ACCOUNT = caller_identity['Account']
        print(f"✅ 自动检测AWS账号: {ACCOUNT}")
    except Exception as e:
        print(f"⚠️ 警告: 无法自动获取AWS账号ID: {str(e)}")
        print("请设置环境变量:")
        print("  export CDK_DEFAULT_ACCOUNT=your-account-id")
        print("  export CDK_DEFAULT_REGION=your-region")

# 创建CDK应用
app = App()

# 环境配置
env = Environment(
    account=ACCOUNT,
    region=REGION
)

# 打印配置信息
print(f"📋 CDK部署配置:")
print(f"  账号: {ACCOUNT or '将从AWS CLI获取'}")
print(f"  区域: {REGION}")
print(f"  阶段: {app.node.try_get_context('stage') or 'prod'}")
print(f"  API版本: {'V2 (带CORS修复)' if USE_V2 else 'V1 (原始版本)'}")

# 项目名称前缀
project_name = "RAG"
stage = app.node.try_get_context("stage") or "prod"

# 创建数据栈（S3, DynamoDB等）
data_stack = DataStack(
    app,
    f"{project_name}-Data-{stage}",
    env=env,
    description="RAG应用数据存储栈"
)

# 创建API栈（Lambda, API Gateway）
api_stack = ApiStack(
    app,
    f"{project_name}-API-{stage}",
    env=env,
    data_bucket=data_stack.document_bucket,
    description="RAG应用API服务栈 V2" if USE_V2 else "RAG应用API服务栈"
)
api_stack.add_dependency(data_stack)

# 创建Web栈（S3静态托管, CloudFront）
web_stack = WebStack(
    app,
    f"{project_name}-Web-{stage}",
    env=env,
    api_url=api_stack.api_url,
    description="RAG应用前端Web栈"
)
web_stack.add_dependency(api_stack)

# 添加标签
Tags.of(app).add("Project", "RAG")
Tags.of(app).add("Stage", stage)
Tags.of(app).add("ManagedBy", "CDK")
Tags.of(app).add("Version", "V2" if USE_V2 else "V1")

app.synth()