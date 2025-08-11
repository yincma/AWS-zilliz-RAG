#!/usr/bin/env python3
"""
构建适用于AWS Lambda x86_64的Python包
"""
import os
import shutil
import subprocess
import sys

def build_lambda_package():
    """构建Lambda部署包"""
    
    # 清理旧的构建目录
    if os.path.exists('lambda_package_build'):
        shutil.rmtree('lambda_package_build')
    os.makedirs('lambda_package_build')
    
    # 复制Lambda函数代码
    for file in os.listdir('lambda_functions'):
        if file.endswith('.py'):
            shutil.copy(f'lambda_functions/{file}', 'lambda_package_build/')
    
    # 安装依赖包 - 指定平台为manylinux x86_64
    requirements = [
        'boto3>=1.28.0',
        'pymilvus>=2.4.0',
        'ujson>=5.0.0',
        'grpcio>=1.60.0', 
        'protobuf>=3.20.0',
        'environs>=10.0.0',
        'python-dotenv>=1.0.0'
    ]
    
    print("📦 Installing packages for Linux x86_64...")
    for req in requirements:
        print(f"  Installing {req}...")
        cmd = [
            sys.executable, '-m', 'pip', 'install',
            '--target', 'lambda_package_build',
            '--platform', 'manylinux2014_x86_64',
            '--only-binary', ':all:',
            '--python-version', '39',
            '--implementation', 'cp',
            '--abi', 'cp39',
            req
        ]
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0:
            # 如果指定平台失败，尝试正常安装
            print(f"    Platform-specific install failed, trying normal install...")
            cmd = [
                sys.executable, '-m', 'pip', 'install',
                '--target', 'lambda_package_build',
                req
            ]
            subprocess.run(cmd, check=True)
    
    # 清理不需要的文件
    print("🧹 Cleaning up unnecessary files...")
    for root, dirs, files in os.walk('lambda_package_build'):
        # 删除__pycache__目录
        if '__pycache__' in dirs:
            shutil.rmtree(os.path.join(root, '__pycache__'))
        # 删除.pyc文件
        for file in files:
            if file.endswith('.pyc'):
                os.remove(os.path.join(root, file))
        # 删除测试目录
        for dir_name in ['tests', 'test', 'testing']:
            if dir_name in dirs:
                shutil.rmtree(os.path.join(root, dir_name))
    
    # 备份旧的lambda_functions目录
    if os.path.exists('lambda_functions'):
        if os.path.exists('lambda_functions_backup'):
            shutil.rmtree('lambda_functions_backup')
        shutil.move('lambda_functions', 'lambda_functions_backup')
    
    # 移动新的包到lambda_functions
    shutil.move('lambda_package_build', 'lambda_functions')
    
    print("✅ Lambda package built successfully!")
    
    # 检查关键文件
    print("🔍 Checking for key dependencies:")
    for dep in ['pymilvus', 'ujson', 'grpcio', 'protobuf', 'environs']:
        found = False
        for item in os.listdir('lambda_functions'):
            if dep in item.lower():
                print(f"  ✓ {item}")
                found = True
                break
        if not found:
            print(f"  ✗ {dep} not found")

if __name__ == '__main__':
    build_lambda_package()