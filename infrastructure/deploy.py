#!/usr/bin/env python3
"""
CDK部署脚本 - 确保部署的一致性和正确性
"""

import os
import sys
import subprocess
import json
from pathlib import Path

def print_step(step_num, message):
    """打印步骤信息"""
    print(f"\n{'='*60}")
    print(f"[步骤 {step_num}] {message}")
    print(f"{'='*60}")

def run_command(command, description):
    """执行命令并检查结果"""
    print(f"\n执行: {command}")
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"❌ {description}失败:")
            print(result.stderr)
            return False
        print(f"✅ {description}成功")
        if result.stdout:
            print(result.stdout)
        return True
    except Exception as e:
        print(f"❌ 执行命令时出错: {e}")
        return False

def load_env():
    """加载环境变量"""
    env_path = Path(__file__).parent.parent / '.env'
    if env_path.exists():
        print(f"✅ 找到.env文件: {env_path}")
        from dotenv import load_dotenv
        load_dotenv(env_path)
        return True
    else:
        print(f"⚠️ 未找到.env文件: {env_path}")
        return False

def check_prerequisites():
    """检查先决条件"""
    print_step(1, "检查先决条件")
    
    # 检查AWS CLI
    if not run_command("aws --version", "检查AWS CLI"):
        print("请安装AWS CLI: https://aws.amazon.com/cli/")
        return False
    
    # 检查CDK
    if not run_command("cdk --version", "检查CDK"):
        print("请安装CDK: npm install -g aws-cdk")
        return False
    
    # 检查Python
    if not run_command("python3 --version", "检查Python"):
        return False
    
    # 加载环境变量
    load_env()
    
    # 检查必要的环境变量
    required_vars = ["ZILLIZ_ENDPOINT", "ZILLIZ_TOKEN"]
    missing_vars = []
    for var in required_vars:
        if not os.environ.get(var):
            missing_vars.append(var)
    
    if missing_vars:
        print(f"❌ 缺少必要的环境变量: {', '.join(missing_vars)}")
        print("请在.env文件中设置这些变量")
        return False
    
    print("✅ 所有先决条件检查通过")
    return True

def get_stage():
    """获取部署阶段"""
    # 从环境变量或命令行参数获取stage
    stage = os.environ.get('CDK_STAGE')
    if not stage and len(sys.argv) > 1:
        stage = sys.argv[1]
    if not stage:
        # 读取cdk.json中的默认stage
        cdk_json_path = Path(__file__).parent / 'cdk.json'
        if cdk_json_path.exists():
            with open(cdk_json_path, 'r') as f:
                cdk_config = json.load(f)
                stage = cdk_config.get('context', {}).get('stage', 'prod')
    return stage

def bootstrap_cdk():
    """Bootstrap CDK（如果需要）"""
    print_step(2, "检查CDK Bootstrap")
    
    # 检查是否已经bootstrap
    check_cmd = "aws cloudformation describe-stacks --stack-name CDKToolkit --query 'Stacks[0].StackStatus' --output text 2>/dev/null"
    result = subprocess.run(check_cmd, shell=True, capture_output=True, text=True)
    
    if result.returncode != 0 or 'CREATE_COMPLETE' not in result.stdout:
        print("需要执行CDK Bootstrap...")
        if not run_command("cdk bootstrap", "CDK Bootstrap"):
            return False
    else:
        print("✅ CDK已经Bootstrap")
    
    return True

def synthesize_stacks():
    """合成CDK栈"""
    print_step(3, "合成CDK栈")
    
    stage = get_stage()
    print(f"使用stage: {stage}")
    
    cmd = f"cdk synth --context stage={stage}"
    if not run_command(cmd, "合成CDK栈"):
        return False
    
    print("✅ CDK栈合成成功")
    return True

def deploy_stacks():
    """部署CDK栈"""
    print_step(4, "部署CDK栈")
    
    stage = get_stage()
    print(f"部署stage: {stage}")
    
    # 部署顺序很重要
    stacks = [
        f"RAG-Data-{stage}",
        f"RAG-API-{stage}",
        f"RAG-Web-{stage}"
    ]
    
    for stack in stacks:
        print(f"\n部署栈: {stack}")
        cmd = f"cdk deploy {stack} --require-approval never --context stage={stage}"
        if not run_command(cmd, f"部署{stack}"):
            print(f"❌ 部署{stack}失败")
            return False
    
    print("✅ 所有栈部署成功")
    return True

def verify_deployment():
    """验证部署"""
    print_step(5, "验证部署")
    
    stage = get_stage()
    
    # 获取CloudFront URL
    cmd = f"aws cloudformation describe-stacks --stack-name RAG-Web-{stage} --query 'Stacks[0].Outputs[?OutputKey==`CloudFrontURL`].OutputValue' --output text"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    
    if result.returncode == 0 and result.stdout.strip():
        cloudfront_url = result.stdout.strip()
        print(f"✅ CloudFront URL: {cloudfront_url}")
        
        # 验证CloudFront配置
        dist_id_cmd = f"aws cloudformation describe-stacks --stack-name RAG-Web-{stage} --query 'Stacks[0].Outputs[?OutputKey==`CloudFrontDistributionId`].OutputValue' --output text"
        dist_result = subprocess.run(dist_id_cmd, shell=True, capture_output=True, text=True)
        
        if dist_result.returncode == 0 and dist_result.stdout.strip():
            dist_id = dist_result.stdout.strip()
            print(f"✅ CloudFront Distribution ID: {dist_id}")
            
            # 获取CloudFront配置并验证
            config_cmd = f"aws cloudfront get-distribution-config --id {dist_id} --query 'DistributionConfig.CacheBehaviors.Items[?PathPattern==`/api/*`]' --output json"
            config_result = subprocess.run(config_cmd, shell=True, capture_output=True, text=True)
            
            if config_result.returncode == 0:
                try:
                    behaviors = json.loads(config_result.stdout)
                    if behaviors:
                        behavior = behaviors[0]
                        print(f"✅ API行为配置:")
                        print(f"   - 路径模式: {behavior.get('PathPattern', 'N/A')}")
                        print(f"   - 目标源: {behavior.get('TargetOriginId', 'N/A')}")
                        
                        # 检查origin配置
                        origin_cmd = f"aws cloudfront get-distribution-config --id {dist_id} --query 'DistributionConfig.Origins.Items[?Id==`{behavior.get(\"TargetOriginId\")}`]' --output json"
                        origin_result = subprocess.run(origin_cmd, shell=True, capture_output=True, text=True)
                        
                        if origin_result.returncode == 0:
                            origins = json.loads(origin_result.stdout)
                            if origins:
                                origin = origins[0]
                                print(f"✅ Origin配置:")
                                print(f"   - 域名: {origin.get('DomainName', 'N/A')}")
                                print(f"   - Origin路径: {origin.get('OriginPath', 'N/A')}")
                                
                                # 验证origin path是否包含stage
                                if origin.get('OriginPath', '').startswith(f'/{stage}'):
                                    print(f"✅ Origin路径正确包含stage: {stage}")
                                else:
                                    print(f"⚠️ Origin路径可能不正确: {origin.get('OriginPath', 'N/A')}")
                except json.JSONDecodeError:
                    print("⚠️ 无法解析CloudFront配置")
    
    # 获取API Gateway URL
    api_cmd = f"aws cloudformation describe-stacks --stack-name RAG-API-{stage} --query 'Stacks[0].Outputs[?OutputKey==`ApiUrl`].OutputValue' --output text"
    api_result = subprocess.run(api_cmd, shell=True, capture_output=True, text=True)
    
    if api_result.returncode == 0 and api_result.stdout.strip():
        api_url = api_result.stdout.strip()
        print(f"✅ API Gateway URL: {api_url}")
    
    return True

def main():
    """主函数"""
    print("\n" + "="*60)
    print("RAG应用CDK部署脚本")
    print("="*60)
    
    # 检查先决条件
    if not check_prerequisites():
        print("\n❌ 先决条件检查失败，退出部署")
        sys.exit(1)
    
    # Bootstrap CDK
    if not bootstrap_cdk():
        print("\n❌ CDK Bootstrap失败，退出部署")
        sys.exit(1)
    
    # 合成栈
    if not synthesize_stacks():
        print("\n❌ CDK栈合成失败，退出部署")
        sys.exit(1)
    
    # 部署栈
    if not deploy_stacks():
        print("\n❌ CDK栈部署失败")
        sys.exit(1)
    
    # 验证部署
    if not verify_deployment():
        print("\n⚠️ 部署验证未完全通过，请检查配置")
    
    print("\n" + "="*60)
    print("🎉 部署完成！")
    print("="*60)
    
    # 播放完成提示音
    if sys.platform == 'darwin':
        os.system('afplay /System/Library/Sounds/Sosumi.aiff')

if __name__ == "__main__":
    main()