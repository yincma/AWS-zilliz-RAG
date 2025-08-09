#!/usr/bin/env python3
"""
AWS CDK应用入口
部署RAG应用到AWS
"""

import os
from aws_cdk import App, Environment, Tags

from stacks.web_stack import WebStack
from stacks.api_stack import ApiStack
from stacks.data_stack import DataStack

# 获取环境变量
ACCOUNT = os.environ.get('CDK_DEFAULT_ACCOUNT')
REGION = os.environ.get('CDK_DEFAULT_REGION', 'us-east-1')

# 创建CDK应用
app = App()

# 环境配置
env = Environment(
    account=ACCOUNT,
    region=REGION
)

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