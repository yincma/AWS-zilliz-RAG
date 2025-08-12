#!/usr/bin/env python3
"""生成所有架构图的统一脚本"""

import subprocess
import sys
import os
from pathlib import Path

def generate_diagram(script_name):
    """执行指定的图表生成脚本"""
    print(f"🔄 正在生成 {script_name}...")
    
    # 确保在正确的目录中执行
    diagrams_dir = Path(__file__).parent
    script_path = diagrams_dir / script_name
    
    if not script_path.exists():
        print(f"❌ 脚本文件不存在: {script_path}")
        return False
    
    result = subprocess.run([sys.executable, str(script_path)], 
                          cwd=diagrams_dir,
                          capture_output=True, text=True)
    
    if result.returncode == 0:
        print(f"✅ 成功生成 {script_name}")
        return True
    else:
        print(f"❌ 生成 {script_name} 失败:")
        print(f"   错误信息: {result.stderr}")
        if result.stdout:
            print(f"   输出信息: {result.stdout}")
        return False

def main():
    """主函数：生成所有架构图"""
    print("🎨 开始生成 AWS-Zilliz-RAG 架构图...")
    
    # 确保images目录存在 (相对于docs目录)
    images_dir = Path(__file__).parent.parent / "images"
    images_dir.mkdir(exist_ok=True)
    
    # 要生成的图表脚本列表
    scripts = [
        "system_architecture.py",
        "rag_data_flow.py", 
        "document_ingestion.py",
        "mvc_architecture.py"
    ]
    
    success_count = 0
    total_count = len(scripts)
    
    for script in scripts:
        if generate_diagram(script):
            success_count += 1
    
    print(f"\n📊 生成完成: {success_count}/{total_count} 个图表成功生成")
    
    if success_count == total_count:
        print("🎉 所有架构图生成成功！")
        return True
    else:
        print("⚠️  部分图表生成失败，请检查错误信息")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)