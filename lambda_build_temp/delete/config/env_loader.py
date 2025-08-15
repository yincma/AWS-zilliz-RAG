"""
环境变量加载工具
确保在各种环境中都能正确加载.env文件
"""

import os
import sys
from pathlib import Path
from typing import Optional

def load_environment(env_file: Optional[str] = None, verbose: bool = True) -> bool:
    """
    加载环境变量
    
    Args:
        env_file: .env文件路径，默认为项目根目录的.env
        verbose: 是否打印加载信息
    
    Returns:
        bool: 是否成功加载
    """
    try:
        from dotenv import load_dotenv
        
        # 确定.env文件路径
        if env_file:
            env_path = Path(env_file)
        else:
            # 查找项目根目录的.env文件
            current = Path.cwd()
            env_path = current / '.env'
            
            # 如果当前目录没有，向上查找
            if not env_path.exists():
                for parent in current.parents:
                    potential_env = parent / '.env'
                    if potential_env.exists():
                        env_path = potential_env
                        break
        
        # 检查文件是否存在
        if not env_path.exists():
            if verbose:
                print(f"⚠️  .env文件未找到: {env_path}")
                print("   使用系统环境变量")
            return False
        
        # 加载.env文件
        load_dotenv(env_path, override=False)
        
        if verbose:
            print(f"✅ 成功加载环境变量: {env_path}")
            # 检查关键变量
            required_vars = [
                'AWS_REGION',
                'ZILLIZ_ENDPOINT', 
                'ZILLIZ_TOKEN',
                'ZILLIZ_COLLECTION'
            ]
            
            missing = []
            for var in required_vars:
                if not os.getenv(var):
                    missing.append(var)
            
            if missing:
                print(f"⚠️  缺少必需的环境变量: {', '.join(missing)}")
                return False
                
        return True
        
    except ImportError:
        if verbose:
            print("⚠️  python-dotenv未安装，使用系统环境变量")
            print("   运行: pip install python-dotenv")
        return False
    except Exception as e:
        if verbose:
            print(f"❌ 加载环境变量时出错: {e}")
        return False


def validate_aws_config() -> bool:
    """
    验证AWS配置
    
    Returns:
        bool: 配置是否有效
    """
    required = ['AWS_REGION']
    optional = ['AWS_ACCESS_KEY_ID', 'AWS_SECRET_ACCESS_KEY']
    
    # 检查必需配置
    for var in required:
        if not os.getenv(var):
            print(f"❌ 缺少AWS配置: {var}")
            return False
    
    # 检查可选配置
    for var in optional:
        if not os.getenv(var):
            print(f"⚠️  {var}未设置，将使用IAM角色或AWS配置文件")
    
    return True


def validate_zilliz_config() -> bool:
    """
    验证Zilliz配置
    
    Returns:
        bool: 配置是否有效
    """
    required = ['ZILLIZ_ENDPOINT', 'ZILLIZ_TOKEN', 'ZILLIZ_COLLECTION']
    
    for var in required:
        value = os.getenv(var)
        if not value:
            print(f"❌ 缺少Zilliz配置: {var}")
            return False
        elif var == 'ZILLIZ_ENDPOINT' and not value.startswith('http'):
            print(f"⚠️  {var}格式可能不正确: {value}")
    
    return True


def get_env_summary() -> dict:
    """
    获取环境变量摘要
    
    Returns:
        dict: 环境变量摘要信息
    """
    return {
        'aws': {
            'region': os.getenv('AWS_REGION', 'not set'),
            'bedrock_model': os.getenv('BEDROCK_MODEL_ID', 'not set'),
            'embedding_model': os.getenv('EMBEDDING_MODEL_ID', 'not set'),
        },
        'zilliz': {
            'endpoint': os.getenv('ZILLIZ_ENDPOINT', 'not set'),
            'collection': os.getenv('ZILLIZ_COLLECTION', 'not set'),
            'has_token': bool(os.getenv('ZILLIZ_TOKEN'))
        },
        's3': {
            'bucket': os.getenv('S3_BUCKET', 'not set'),
            'prefix': os.getenv('S3_PREFIX', 'documents/')
        }
    }


# 自动加载环境变量（在导入时执行）
if __name__ != "__main__":
    load_environment(verbose=False)