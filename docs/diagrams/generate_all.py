#!/usr/bin/env python3
"""Unified script for generating all architecture diagrams"""

import subprocess
import sys
import os
from pathlib import Path

def generate_diagram(script_name):
    """Execute specified diagram generation script"""
    print(f"🔄 Generating {script_name}...")
    
    # Ensure execution in the correct directory
    diagrams_dir = Path(__file__).parent
    script_path = diagrams_dir / script_name
    
    if not script_path.exists():
        print(f"❌ Script file does not exist: {script_path}")
        return False
    
    result = subprocess.run([sys.executable, str(script_path)], 
                          cwd=diagrams_dir,
                          capture_output=True, text=True)
    
    if result.returncode == 0:
        print(f"✅ Successfully generated {script_name}")
        return True
    else:
        print(f"❌ Failed to generate {script_name}:")
        print(f"   Error message: {result.stderr}")
        if result.stdout:
            print(f"   Output message: {result.stdout}")
        return False

def main():
    """Main function: Generate all architecture diagrams"""
    print("🎨 Starting to generate AWS-Zilliz-RAG architecture diagrams...")
    
    # Ensure images directory exists (relative to docs directory)
    images_dir = Path(__file__).parent.parent / "images"
    images_dir.mkdir(exist_ok=True)
    
    # List of diagram scripts to generate
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
    
    print(f"\n📊 Generation complete: {success_count}/{total_count} diagrams successfully generated")
    
    if success_count == total_count:
        print("🎉 All architecture diagrams generated successfully!")
        return True
    else:
        print("⚠️  Some diagrams failed to generate, please check error messages")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)