#!/usr/bin/env python3
"""
AWS CDK应用入口
部署RAG应用到AWS
"""

import os
from pathlib import Path
from aws_cdk import App, Environment, Tags

# 自动加载.env文件
try:
    from dotenv import load_dotenv
    env_path = Path(__file__).parent.parent / '.env'
    if env_path.exists():
        load_dotenv(env_path)
        print(f"✅ 已加载.env配置: {env_path}")
except ImportError:
    print("⚠️ python-dotenv未安装，跳过.env加载")

from stacks.web_stack import WebStack
from stacks.api_stack import ApiStack
from stacks.data_stack import DataStack

# 获取环境变量（优先使用.env文件的值）
# 注意：CDK CLI会设置CDK_DEFAULT_REGION为AWS CLI的默认值
# 所以我们优先使用AWS_REGION（来自.env），而不是CDK_DEFAULT_REGION
ACCOUNT = os.environ.get('AWS_ACCOUNT') or os.environ.get('CDK_DEFAULT_ACCOUNT')
REGION = os.environ.get('AWS_REGION') or os.environ.get('CDK_DEFAULT_REGION', 'us-east-1')

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
        # 继续使用None，让CDK尝试从环境中获取

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
print(f"  阶段: {app.node.try_get_context('stage') or 'dev'}")

# 项目名称前缀
project_name = "RAG"
stage = app.node.try_get_context("stage") or "dev"

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
    description="RAG应用API服务栈"
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

app.synth()