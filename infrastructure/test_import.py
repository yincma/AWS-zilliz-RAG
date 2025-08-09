#!/usr/bin/env python3
"""测试CDK导入"""

import sys
print(f"Python: {sys.executable}")
print(f"Version: {sys.version}")
print(f"Path: {sys.path}")

try:
    import aws_cdk
    print(f"✅ aws_cdk imported: {aws_cdk.__file__}")
except ImportError as e:
    print(f"❌ Failed to import aws_cdk: {e}")

try:
    from aws_cdk import App
    print("✅ App imported successfully")
except ImportError as e:
    print(f"❌ Failed to import App: {e}")