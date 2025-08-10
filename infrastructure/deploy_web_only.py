#!/usr/bin/env python3
"""
独立部署Web栈的脚本
不依赖API栈，用于修复CloudFront 403问题
"""

import os
from aws_cdk import App, Environment, Tags
from stacks.web_stack import WebStack

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
stage = app.node.try_get_context("stage") or "prod"

# 获取API URL（从上下文或环境变量）
api_url = app.node.try_get_context("apiUrl") or os.environ.get('API_URL', 'https://api.example.com')

print(f"Deploying Web Stack with API URL: {api_url}")

# 创建Web栈（独立部署，不依赖API栈）
web_stack = WebStack(
    app,
    f"{project_name}-Web-{stage}",
    env=env,
    api_url=api_url,
    description="RAG应用前端Web栈（独立部署）"
)

# 添加标签
Tags.of(app).add("Project", "RAG")
Tags.of(app).add("Stage", stage)
Tags.of(app).add("DeploymentType", "WebOnly")

app.synth()