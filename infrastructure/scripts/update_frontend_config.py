#!/usr/bin/env python3
"""
自动更新前端配置文件
从 CloudFormation 栈输出获取 API URL 并更新前端配置
"""
import json
import boto3
import os
import sys
from datetime import datetime
from typing import Dict, Any


def get_stack_outputs(stack_name: str, region: str) -> Dict[str, str]:
    """获取 CloudFormation 栈的输出"""
    client = boto3.client('cloudformation', region_name=region)
    
    try:
        response = client.describe_stacks(StackName=stack_name)
        stack = response['Stacks'][0]
        
        outputs = {}
        if 'Outputs' in stack:
            for output in stack['Outputs']:
                outputs[output['OutputKey']] = output['OutputValue']
        
        return outputs
    except Exception as e:
        print(f"❌ 获取栈输出失败: {e}")
        return {}


def update_frontend_config(api_url: str, cloudfront_url: str, region: str) -> bool:
    """更新前端配置文件"""
    # 配置文件路径
    config_paths = [
        'app/views/web/config.json',
        '../app/views/web/config.json'
    ]
    
    config_file = None
    for path in config_paths:
        if os.path.exists(path):
            config_file = path
            break
    
    if not config_file:
        print("❌ 找不到前端配置文件")
        return False
    
    # 创建新配置
    config = {
        "apiUrl": api_url,
        "cloudfrontUrl": cloudfront_url,
        "region": region,
        "stage": "prod",
        "updated": datetime.now().isoformat(),
        "_comment": "此文件由部署脚本自动生成，请勿手动修改"
    }
    
    # 写入配置文件
    try:
        with open(config_file, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=2, ensure_ascii=False)
        print(f"✅ 前端配置已更新: {config_file}")
        return True
    except Exception as e:
        print(f"❌ 更新配置文件失败: {e}")
        return False


def update_api_js(api_url: str) -> bool:
    """更新 api.js 文件中的 API URL"""
    api_js_paths = [
        'app/views/web/static/js/api.js',
        '../app/views/web/static/js/api.js'
    ]
    
    api_js_file = None
    for path in api_js_paths:
        if os.path.exists(path):
            api_js_file = path
            break
    
    if not api_js_file:
        print("⚠️ 找不到 api.js 文件")
        return False
    
    try:
        with open(api_js_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 查找并替换 API URL
        import re
        # 匹配 https://xxx.execute-api.region.amazonaws.com/stage 格式的 URL
        pattern = r'https://[a-z0-9]+\.execute-api\.[a-z0-9-]+\.amazonaws\.com/[a-z0-9]+'
        
        # 统计替换次数
        new_content, count = re.subn(pattern, api_url, content)
        
        if count > 0:
            with open(api_js_file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"✅ api.js 已更新 ({count} 处替换)")
            return True
        else:
            print("ℹ️ api.js 中未找到需要替换的 API URL")
            return True
            
    except Exception as e:
        print(f"❌ 更新 api.js 失败: {e}")
        return False


def sync_to_s3(bucket_name: str, cloudfront_id: str = None) -> bool:
    """同步前端文件到 S3"""
    web_dirs = [
        'app/views/web',
        '../app/views/web'
    ]
    
    web_dir = None
    for path in web_dirs:
        if os.path.exists(path):
            web_dir = path
            break
    
    if not web_dir:
        print("❌ 找不到前端目录")
        return False
    
    try:
        # 同步文件到 S3
        import subprocess
        cmd = [
            'aws', 's3', 'sync',
            web_dir,
            f's3://{bucket_name}/',
            '--delete',
            '--exclude', '.DS_Store',
            '--exclude', '*.pyc',
            '--exclude', '__pycache__'
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ 前端文件已同步到 S3: {bucket_name}")
            
            # 如果提供了 CloudFront ID，清除缓存
            if cloudfront_id:
                invalidate_cmd = [
                    'aws', 'cloudfront', 'create-invalidation',
                    '--distribution-id', cloudfront_id,
                    '--paths', '/*'
                ]
                inv_result = subprocess.run(invalidate_cmd, capture_output=True, text=True)
                if inv_result.returncode == 0:
                    print(f"✅ CloudFront 缓存已清除: {cloudfront_id}")
                else:
                    print(f"⚠️ CloudFront 缓存清除失败: {inv_result.stderr}")
            
            return True
        else:
            print(f"❌ S3 同步失败: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"❌ S3 同步失败: {e}")
        return False


def main():
    """主函数"""
    # 配置
    STACK_NAME = os.environ.get('CDK_STACK_NAME', 'RagApiStackV2')
    REGION = os.environ.get('AWS_REGION', 'us-east-1')
    
    print(f"📋 开始更新前端配置...")
    print(f"   栈名称: {STACK_NAME}")
    print(f"   区域: {REGION}")
    
    # 获取栈输出
    outputs = get_stack_outputs(STACK_NAME, REGION)
    
    if not outputs:
        print("❌ 无法获取栈输出")
        return 1
    
    # 获取必要的输出值
    api_url = outputs.get('ApiUrl', '')
    cloudfront_url = outputs.get('CloudFrontUrl', '')
    web_bucket = outputs.get('WebBucketName', '')
    cloudfront_id = outputs.get('CloudFrontDistributionId', '')
    
    if not api_url:
        print("❌ 未找到 API URL")
        return 1
    
    print(f"\n📍 配置信息:")
    print(f"   API URL: {api_url}")
    print(f"   CloudFront URL: {cloudfront_url}")
    print(f"   S3 Bucket: {web_bucket}")
    print(f"   CloudFront ID: {cloudfront_id}")
    
    # 更新前端配置
    success = True
    
    if not update_frontend_config(api_url, cloudfront_url, REGION):
        success = False
    
    if not update_api_js(api_url):
        success = False
    
    # 如果有 S3 bucket，同步文件
    if web_bucket and success:
        if not sync_to_s3(web_bucket, cloudfront_id):
            success = False
    
    if success:
        print("\n✅ 前端配置更新成功！")
        print(f"   访问应用: {cloudfront_url}")
        return 0
    else:
        print("\n❌ 前端配置更新失败")
        return 1


if __name__ == '__main__':
    sys.exit(main())