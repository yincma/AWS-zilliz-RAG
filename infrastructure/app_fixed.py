#!/usr/bin/env python3
"""
Fixed CDK Application for RAG with proper CORS configuration
"""
import os
import aws_cdk as cdk
from stacks.data_stack import DataStack
from stacks.api_stack_fixed import ApiStackFixed
from stacks.web_stack import WebStack

# Get environment variables
env_config = cdk.Environment(
    account=os.environ.get('CDK_DEFAULT_ACCOUNT'),
    region=os.environ.get('CDK_DEFAULT_REGION', 'us-east-1')
)

# Create CDK app
app = cdk.App()

# Get stage from context or environment
stage = app.node.try_get_context('stage') or os.environ.get('STAGE', 'prod')

# Create stacks with proper naming
stack_prefix = f"Rag{stage.capitalize()}"

# 1. Data Stack (S3 buckets)
data_stack = DataStack(
    app,
    f"{stack_prefix}DataStack",
    env=env_config,
    description=f"RAG Data Stack - {stage}"
)

# 2. Web Stack (CloudFront + S3 for frontend)
web_stack = WebStack(
    app,
    f"{stack_prefix}WebStack",
    env=env_config,
    description=f"RAG Web Frontend Stack - {stage}"
)

# 3. API Stack (Lambda + API Gateway) - Fixed version
api_stack = ApiStackFixed(
    app,
    f"{stack_prefix}ApiStack",
    data_bucket=data_stack.data_bucket,
    cloudfront_url=web_stack.distribution_url if hasattr(web_stack, 'distribution_url') else None,
    env=env_config,
    description=f"RAG API Stack with Fixed CORS - {stage}"
)

# Add dependencies
api_stack.add_dependency(data_stack)
web_stack.add_dependency(api_stack)  # Web needs API URL for configuration

# Add tags to all stacks
cdk.Tags.of(app).add("Project", "RAG-Application")
cdk.Tags.of(app).add("Environment", stage)
cdk.Tags.of(app).add("ManagedBy", "CDK")

# Output important information
cdk.CfnOutput(
    api_stack,
    "DeploymentInstructions",
    value="Run 'bash deploy_fixed.sh' to complete deployment with proper configuration",
    description="Next steps for deployment"
)

# Synthesize
app.synth()