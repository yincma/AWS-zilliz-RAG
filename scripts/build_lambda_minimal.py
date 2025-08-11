#!/usr/bin/env python3
"""
构建最小化的Lambda部署包（只包含必要的依赖）
"""
import os
import shutil
import subprocess
import sys

def build_lambda_package():
    """构建最小化的Lambda部署包"""
    
    # 清理旧的构建目录
    if os.path.exists('lambda_package_build'):
        shutil.rmtree('lambda_package_build')
    os.makedirs('lambda_package_build')
    
    # 复制Lambda函数代码
    for file in os.listdir('lambda_functions'):
        if file.endswith('.py'):
            shutil.copy(f'lambda_functions/{file}', 'lambda_package_build/')
    
    # 创建requirements文件 - 排除milvus-lite和其他大型包
    with open('lambda_package_build/requirements.txt', 'w') as f:
        f.write("""boto3>=1.28.0
pymilvus[grpc]>=2.4.0
ujson>=5.0.0
grpcio>=1.60.0
protobuf>=3.20.0
environs>=10.0.0
python-dotenv>=1.0.0
""")
    
    print("📦 Installing minimal packages for Lambda...")
    
    # 使用pip下载特定平台的wheels
    cmd = [
        sys.executable, '-m', 'pip', 'install',
        '--target', 'lambda_package_build',
        '--platform', 'manylinux2014_x86_64',
        '--only-binary', ':all:',
        '--python-version', '39',
        '--implementation', 'cp',
        '--no-deps',  # 不自动安装依赖
        'pymilvus>=2.4.0',
        'ujson>=5.0.0',
        'grpcio>=1.60.0',
        'protobuf>=3.20.0',
        'environs>=10.0.0',
        'python-dotenv>=1.0.0',
        'marshmallow>=3.18.0',
        'typing-extensions',
        'numpy>=1.21.0',  # 添加numpy作为pymilvus的依赖
        'pandas>=1.3.0'  # 添加pandas作为pymilvus的依赖
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print("Platform-specific install failed, trying normal install...")
        # 如果平台特定安装失败，正常安装但排除大型依赖
        cmd = [
            sys.executable, '-m', 'pip', 'install',
            '--target', 'lambda_package_build',
            '--no-deps',
            'pymilvus>=2.4.0'
        ]
        subprocess.run(cmd)
        
        # 安装必需的小型依赖
        for dep in ['ujson', 'grpcio', 'protobuf', 'environs', 'python-dotenv', 'marshmallow', 'typing-extensions']:
            subprocess.run([
                sys.executable, '-m', 'pip', 'install',
                '--target', 'lambda_package_build',
                '--platform', 'manylinux2014_x86_64',
                '--only-binary', ':all:',
                '--python-version', '39',
                '--implementation', 'cp',
                dep
            ])
    
    # 清理不需要的文件和大型包
    print("🧹 Cleaning up unnecessary files...")
    
    # 删除milvus-lite和其他大型包 - 但保留numpy和pandas
    for package in ['milvus_lite', 'pyarrow']:  # 从列表中移除numpy和pandas
        package_path = os.path.join('lambda_package_build', package)
        if os.path.exists(package_path):
            shutil.rmtree(package_path)
            print(f"  Removed {package}")
        
        # 也删除对应的dist-info
        for item in os.listdir('lambda_package_build'):
            if item.startswith(f'{package}-') and item.endswith('.dist-info'):
                shutil.rmtree(os.path.join('lambda_package_build', item))
                print(f"  Removed {item}")
    
    # 清理其他不需要的文件
    for root, dirs, files in os.walk('lambda_package_build'):
        # 删除__pycache__目录
        if '__pycache__' in dirs:
            shutil.rmtree(os.path.join(root, '__pycache__'))
        # 删除.pyc文件
        for file in files:
            if file.endswith('.pyc'):
                os.remove(os.path.join(root, file))
        # 删除测试目录
        for dir_name in ['tests', 'test', 'testing', 'examples', 'benchmarks']:
            if dir_name in dirs:
                shutil.rmtree(os.path.join(root, dir_name))
    
    # 计算包大小
    total_size = 0
    for root, dirs, files in os.walk('lambda_package_build'):
        for file in files:
            total_size += os.path.getsize(os.path.join(root, file))
    
    print(f"📊 Package size: {total_size / (1024*1024):.2f} MB")
    
    # 备份旧的lambda_functions目录
    if os.path.exists('lambda_functions'):
        if os.path.exists('lambda_functions_backup'):
            shutil.rmtree('lambda_functions_backup')
        shutil.move('lambda_functions', 'lambda_functions_backup')
    
    # 移动新的包到lambda_functions
    shutil.move('lambda_package_build', 'lambda_functions')
    
    print("✅ Minimal Lambda package built successfully!")
    
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