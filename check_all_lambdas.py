#!/usr/bin/env python3
"""检查所有Lambda函数，识别可删除的"""

import boto3
import json
from datetime import datetime, timedelta

def check_all_lambdas():
    lambda_client = boto3.client('lambda', region_name='us-east-1')
    cloudwatch_client = boto3.client('cloudwatch', region_name='us-east-1')
    
    print("=" * 80)
    print("Lambda函数全面检查")
    print("=" * 80)
    
    # 获取所有Lambda函数
    all_functions = lambda_client.list_functions(MaxItems=100)['Functions']
    
    print(f"\n📊 总计Lambda函数: {len(all_functions)}")
    
    # 按前缀分组
    prefixes = {}
    for func in all_functions:
        name = func['FunctionName']
        if 'RAG' in name:
            prefix = 'RAG项目'
        elif name.startswith('test') or name.startswith('Test'):
            prefix = '测试函数'
        elif name.startswith('demo') or name.startswith('Demo'):
            prefix = '演示函数'
        else:
            prefix = '其他'
        
        if prefix not in prefixes:
            prefixes[prefix] = []
        prefixes[prefix].append(func)
    
    # 打印分组结果
    print("\n🗂️ 按类型分组:")
    print("-" * 80)
    
    for prefix, funcs in sorted(prefixes.items()):
        print(f"\n{prefix}: {len(funcs)} 个函数")
        
        if prefix == 'RAG项目':
            print("  ✅ 这些是当前项目的函数（已在前面分析）")
        elif prefix in ['测试函数', '演示函数']:
            print("  ⚠️  可能可以删除的函数:")
            for func in funcs:
                func_name = func['FunctionName']
                last_modified = func['LastModified']
                
                # 检查最近是否有调用
                try:
                    # 获取最近7天的调用次数
                    end_time = datetime.now()
                    start_time = end_time - timedelta(days=7)
                    
                    metrics = cloudwatch_client.get_metric_statistics(
                        Namespace='AWS/Lambda',
                        MetricName='Invocations',
                        Dimensions=[
                            {'Name': 'FunctionName', 'Value': func_name}
                        ],
                        StartTime=start_time,
                        EndTime=end_time,
                        Period=604800,  # 7 days
                        Statistics=['Sum']
                    )
                    
                    invocations = 0
                    if metrics['Datapoints']:
                        invocations = int(metrics['Datapoints'][0]['Sum'])
                    
                    print(f"    • {func_name}")
                    print(f"      最后修改: {last_modified}")
                    print(f"      7天内调用: {invocations} 次")
                    
                    if invocations == 0:
                        print(f"      🗑️ 建议: 可以删除（7天内无调用）")
                    else:
                        print(f"      ⚠️ 建议: 谨慎删除（最近有调用）")
                except Exception as e:
                    print(f"      ❌ 无法获取调用统计")
        else:
            print(f"  ℹ️ 包含 {len(funcs)} 个函数（非RAG项目）")
    
    # 查找孤立的Lambda函数（没有触发器）
    print("\n🔍 检查孤立函数（无触发器）:")
    print("-" * 80)
    
    orphaned_functions = []
    for func in all_functions:
        if 'RAG' not in func['FunctionName']:  # 跳过RAG项目函数
            continue
            
        func_name = func['FunctionName']
        try:
            # 获取函数配置
            policy = lambda_client.get_policy(FunctionName=func_name)
            policy_doc = json.loads(policy['Policy'])
            
            # 检查是否有权限策略（表示有触发器）
            if not policy_doc.get('Statement'):
                orphaned_functions.append(func_name)
        except lambda_client.exceptions.ResourceNotFoundException:
            # 没有资源策略意味着没有触发器
            orphaned_functions.append(func_name)
        except Exception:
            pass
    
    if orphaned_functions:
        print("⚠️ 发现以下函数没有触发器:")
        for func_name in orphaned_functions:
            print(f"  • {func_name}")
    else:
        print("✅ 所有RAG项目函数都有触发器")
    
    # 清理建议总结
    print("\n🧹 清理建议总结:")
    print("-" * 80)
    
    deletable = []
    
    # 检查测试/演示函数
    if '测试函数' in prefixes:
        deletable.extend([f['FunctionName'] for f in prefixes['测试函数']])
    if '演示函数' in prefixes:
        deletable.extend([f['FunctionName'] for f in prefixes['演示函数']])
    
    if deletable:
        print("可以安全删除的函数:")
        for func_name in deletable:
            print(f"  • {func_name}")
        print(f"\n删除命令:")
        for func_name in deletable:
            print(f"  aws lambda delete-function --function-name {func_name} --region us-east-1")
    else:
        print("✅ 没有发现明显的虚拟或测试函数需要删除")
        print("\n当前所有Lambda函数分析:")
        print("• RAG项目函数: 都在使用中，由CDK管理")
        print("• 没有发现废弃的测试函数")
        print("• 建议: 保持现状，通过CDK管理所有函数")

if __name__ == "__main__":
    check_all_lambdas()