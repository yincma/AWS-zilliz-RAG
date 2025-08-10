#!/usr/bin/env python3
"""检查Lambda函数使用情况"""

import boto3
import json
from datetime import datetime, timedelta

def check_lambda_usage():
    # 初始化客户端
    lambda_client = boto3.client('lambda', region_name='us-east-1')
    api_client = boto3.client('apigateway', region_name='us-east-1')
    logs_client = boto3.client('logs', region_name='us-east-1')
    
    print("=" * 80)
    print("Lambda函数使用情况分析")
    print("=" * 80)
    
    # 1. 获取所有RAG相关Lambda函数
    functions = lambda_client.list_functions()['Functions']
    rag_functions = [f for f in functions if 'RAG' in f['FunctionName']]
    
    # 2. API Gateway配置
    api_id = 'gbgn92f6v9'
    resources = api_client.get_resources(restApiId=api_id)['items']
    
    # 3. 分析每个函数
    function_analysis = {}
    
    for func in rag_functions:
        func_name = func['FunctionName']
        func_arn = func['FunctionArn']
        
        analysis = {
            'name': func_name,
            'runtime': func['Runtime'],
            'last_modified': func['LastModified'],
            'code_size': func['CodeSize'],
            'handler': func.get('Handler', 'N/A'),
            'api_endpoints': [],
            'category': '',
            'status': '',
            'recommendation': ''
        }
        
        # 检查API Gateway集成
        for resource in resources:
            path = resource.get('path', '')
            for method in ['GET', 'POST', 'DELETE', 'PUT']:
                try:
                    method_info = api_client.get_method(
                        restApiId=api_id,
                        resourceId=resource['id'],
                        httpMethod=method
                    )
                    integration_uri = method_info.get('methodIntegration', {}).get('uri', '')
                    if func_arn in integration_uri or func_name in integration_uri:
                        analysis['api_endpoints'].append(f"{method} {path}")
                except:
                    pass
        
        # 分类函数
        if 'QueryFunction' in func_name:
            analysis['category'] = '核心功能'
            analysis['status'] = '✅ 生产使用中'
            analysis['recommendation'] = '保留 - 处理查询请求'
        elif 'IngestFunction' in func_name:
            analysis['category'] = '核心功能'
            analysis['status'] = '✅ 生产使用中'
            analysis['recommendation'] = '保留 - 处理文档上传'
        elif 'StatsFunction' in func_name:
            analysis['category'] = '辅助功能'
            analysis['status'] = '✅ 生产使用中'
            analysis['recommendation'] = '保留 - 提供统计信息'
        elif 'ListDocsFunction' in func_name:
            analysis['category'] = '辅助功能'
            analysis['status'] = '✅ 生产使用中'
            analysis['recommendation'] = '保留 - 列出文档'
        elif 'HealthFunction' in func_name:
            analysis['category'] = '监控功能'
            analysis['status'] = '✅ 生产使用中'
            analysis['recommendation'] = '保留 - 健康检查'
        elif 'LogRetention' in func_name:
            analysis['category'] = 'CDK管理'
            analysis['status'] = '⚙️ CDK内部函数'
            analysis['recommendation'] = '保留 - CDK自动管理日志保留'
        elif 'CustomS3AutoDelete' in func_name:
            analysis['category'] = 'CDK管理'
            analysis['status'] = '⚙️ CDK内部函数'
            analysis['recommendation'] = '保留 - CDK自动清理S3'
        elif 'CustomCDKBucketDeployment' in func_name:
            analysis['category'] = 'CDK管理'
            analysis['status'] = '⚙️ CDK内部函数'
            analysis['recommendation'] = '保留 - CDK部署静态资源'
        else:
            analysis['category'] = '未知'
            analysis['status'] = '❓ 需要检查'
            analysis['recommendation'] = '需要进一步分析'
        
        function_analysis[func_name] = analysis
    
    # 4. 打印分析结果
    print("\n📋 Lambda函数清单:")
    print("-" * 80)
    
    # 按类别分组打印
    categories = ['核心功能', '辅助功能', '监控功能', 'CDK管理', '未知']
    
    for category in categories:
        funcs = [fa for fa in function_analysis.values() if fa['category'] == category]
        if funcs:
            print(f"\n🔹 {category}:")
            for func in funcs:
                print(f"  • {func['name']}")
                print(f"    状态: {func['status']}")
                print(f"    处理器: {func['handler']}")
                if func['api_endpoints']:
                    print(f"    API端点: {', '.join(func['api_endpoints'])}")
                print(f"    建议: {func['recommendation']}")
                print()
    
    # 5. 统计信息
    print("\n📊 统计信息:")
    print("-" * 80)
    print(f"总计Lambda函数: {len(rag_functions)}")
    print(f"核心功能: {len([f for f in function_analysis.values() if f['category'] == '核心功能'])}")
    print(f"辅助功能: {len([f for f in function_analysis.values() if f['category'] == '辅助功能'])}")
    print(f"CDK管理: {len([f for f in function_analysis.values() if f['category'] == 'CDK管理'])}")
    
    # 6. 清理建议
    print("\n🧹 清理建议:")
    print("-" * 80)
    
    # 检查是否有重复或未使用的函数
    has_unused = False
    for func_name, analysis in function_analysis.items():
        if analysis['category'] == '未知' or not analysis['api_endpoints'] and analysis['category'] not in ['CDK管理', '监控功能']:
            print(f"⚠️  {func_name}: 可能未使用，建议进一步检查")
            has_unused = True
    
    if not has_unused:
        print("✅ 所有Lambda函数都在使用中，没有需要删除的虚拟或测试函数")
    
    print("\n💡 建议:")
    print("1. 所有CDK管理的函数由CDK自动创建和管理，不要手动删除")
    print("2. 核心功能函数（Query、Ingest）是系统必需的")
    print("3. 辅助功能函数（Stats、ListDocs、Health）提供重要的运维支持")
    print("4. 如需清理，应通过CDK重新部署而不是手动删除")

if __name__ == "__main__":
    check_lambda_usage()