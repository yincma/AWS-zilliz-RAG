#!/usr/bin/env python3
"""分析lambda_functions目录中的文件，识别可删除的虚拟函数"""

import os
import hashlib
from pathlib import Path

def get_file_hash(filepath):
    """计算文件的MD5哈希值"""
    try:
        with open(filepath, 'rb') as f:
            return hashlib.md5(f.read()).hexdigest()
    except:
        return None

def analyze_lambda_files():
    base_dir = Path("/Users/umatoratatsu/Documents/AWS/AWS-Handson/AWS-Zilliz-RAG/infrastructure/lambda_functions")
    
    print("=" * 80)
    print("Lambda Functions 文件分析")
    print("=" * 80)
    
    # 1. 收集所有Python文件
    all_files = list(base_dir.glob("*.py"))
    deploy_files = list((base_dir / "deploy_package").glob("*.py")) if (base_dir / "deploy_package").exists() else []
    
    print(f"\n📁 文件统计:")
    print(f"  主目录文件: {len(all_files)} 个")
    print(f"  deploy_package文件: {len(deploy_files)} 个")
    
    # 2. 按功能分组文件
    file_groups = {
        'query': [],
        'ingest': [],
        'stats': [],
        'list_docs': [],
        'cors': [],
        'other': []
    }
    
    for file in all_files:
        name = file.name
        if 'query' in name:
            file_groups['query'].append(name)
        elif 'ingest' in name:
            file_groups['ingest'].append(name)
        elif 'stats' in name:
            file_groups['stats'].append(name)
        elif 'list_docs' in name:
            file_groups['list_docs'].append(name)
        elif 'cors' in name:
            file_groups['cors'].append(name)
        else:
            file_groups['other'].append(name)
    
    # 3. 分析每个功能组
    print("\n📊 按功能分组分析:")
    print("-" * 80)
    
    for func_type, files in file_groups.items():
        if not files:
            continue
            
        print(f"\n🔹 {func_type.upper()} 相关文件 ({len(files)} 个):")
        
        # 识别主文件和变体
        main_file = None
        variants = []
        
        for file in sorted(files):
            if file == f"{func_type}_handler.py":
                main_file = file
                print(f"  ✅ {file} - 【主文件】CDK使用中")
            elif '_mock' in file:
                variants.append(file)
                print(f"  🧪 {file} - 模拟版本（可删除）")
            elif '_placeholder' in file:
                variants.append(file)
                print(f"  📝 {file} - 占位符版本（可删除）")
            elif '_fixed' in file:
                variants.append(file)
                print(f"  🔧 {file} - 修复版本（可删除）")
            elif '_real' in file:
                variants.append(file)
                print(f"  💡 {file} - 真实实现版本（可能已合并到主文件）")
            elif '_v2' in file:
                variants.append(file)
                print(f"  🆕 {file} - V2版本（可能已合并到主文件）")
            else:
                print(f"  ❓ {file}")
    
    # 4. 检查文件内容相似性
    print("\n🔍 检查文件内容重复:")
    print("-" * 80)
    
    file_hashes = {}
    for file in all_files:
        hash_val = get_file_hash(file)
        if hash_val:
            if hash_val not in file_hashes:
                file_hashes[hash_val] = []
            file_hashes[hash_val].append(file.name)
    
    duplicates = {k: v for k, v in file_hashes.items() if len(v) > 1}
    
    if duplicates:
        print("发现内容相同的文件:")
        for hash_val, files in duplicates.items():
            print(f"  • {' = '.join(files)}")
    else:
        print("✅ 没有发现内容完全相同的文件")
    
    # 5. CDK实际使用的文件
    print("\n📦 CDK配置分析:")
    print("-" * 80)
    print("根据api_stack.py的配置，CDK实际使用的handler:")
    print("  • query_handler.handler - QueryFunction")
    print("  • ingest_handler.handler - IngestFunction")
    print("  • index.handler - 内联函数（Stats, Health, ListDocs）")
    
    # 6. 清理建议
    print("\n🧹 清理建议:")
    print("-" * 80)
    
    deletable_files = []
    
    # 收集可删除的文件
    for file in all_files:
        name = file.name
        if any(suffix in name for suffix in ['_mock', '_placeholder', '_fixed', '_v2']):
            deletable_files.append(name)
        elif '_real' in name and name.replace('_real', '') in [f.name for f in all_files]:
            # 如果存在对应的主文件，real版本可能是多余的
            deletable_files.append(name)
    
    # 特殊文件
    keep_files = [
        'query_handler.py',      # CDK使用
        'ingest_handler.py',      # CDK使用
        'cors_helper.py',         # 可能被其他文件引用
        '__init__.py',            # Python包必需
        'requirements.txt'        # 依赖管理
    ]
    
    print("\n✅ 必须保留的文件:")
    for file in keep_files:
        print(f"  • {file}")
    
    print("\n🗑️ 可以安全删除的文件:")
    safe_to_delete = []
    for file in deletable_files:
        if file not in keep_files:
            safe_to_delete.append(file)
            print(f"  • {file}")
    
    # 生成删除命令
    if safe_to_delete:
        print("\n💻 删除命令:")
        print("```bash")
        print("cd /Users/umatoratatsu/Documents/AWS/AWS-Handson/AWS-Zilliz-RAG/infrastructure/lambda_functions")
        print("# 备份文件（以防万一）")
        print("mkdir -p backup")
        for file in safe_to_delete:
            print(f"cp {file} backup/")
        print("\n# 删除文件")
        for file in safe_to_delete:
            print(f"rm {file}")
        print("\n# 同时删除deploy_package中的副本")
        print("cd deploy_package")
        for file in safe_to_delete:
            print(f"rm -f {file}")
        print("```")
    
    # 7. 特别注意事项
    print("\n⚠️ 注意事项:")
    print("-" * 80)
    print("1. 删除前建议先备份文件")
    print("2. 确保CDK栈正常运行后再删除")
    print("3. stats_handler.py可能需要保留（如果将来要分离内联函数）")
    print("4. list_docs_real.py可能包含有用的代码（检查是否已合并到主文件）")
    
    # 8. deploy_package目录
    print("\n📂 deploy_package目录:")
    print("-" * 80)
    print("这个目录似乎是文件的副本，可以考虑:")
    print("  • 如果不再需要，整个目录都可以删除")
    print("  • 或者只保留与主目录同步的必要文件")

if __name__ == "__main__":
    analyze_lambda_files()