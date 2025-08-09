#!/usr/bin/env python3
"""
验证文档上传修复
"""
import asyncio
import aiohttp
import json
from datetime import datetime
from colorama import init, Fore, Style

init(autoreset=True)

API_URL = "https://abbrw64qve.execute-api.us-east-1.amazonaws.com/prod"

async def test_upload():
    """测试文档上传"""
    print(f"{Fore.CYAN}测试文档上传功能...{Style.RESET_ALL}\n")
    
    # 创建测试文档
    test_files = [
        {
            "filename": f"fix_test_1_{datetime.now().strftime('%H%M%S')}.txt",
            "content": "This is test document 1 to verify the upload fix.",
            "content_type": "text/plain"
        },
        {
            "filename": f"fix_test_2_{datetime.now().strftime('%H%M%S')}.txt",
            "content": "This is test document 2 with special characters: 中文测试 & symbols!",
            "content_type": "text/plain"
        },
        {
            "filename": f"fix_test_3_{datetime.now().strftime('%H%M%S')}.md",
            "content": "# Markdown Test\n\nThis is a **markdown** document.",
            "content_type": "text/markdown"
        }
    ]
    
    async with aiohttp.ClientSession() as session:
        success_count = 0
        fail_count = 0
        
        for file_data in test_files:
            print(f"上传文件: {file_data['filename']}")
            
            upload_data = {
                "filename": file_data["filename"],
                "content": file_data["content"],
                "content_type": file_data["content_type"],
                "size": len(file_data["content"])
            }
            
            try:
                async with session.post(
                    f"{API_URL}/documents/upload",
                    json=upload_data,
                    headers={'Content-Type': 'application/json'}
                ) as response:
                    
                    if response.status == 200:
                        print(f"  {Fore.GREEN}✅ 成功{Style.RESET_ALL}")
                        success_count += 1
                        
                        # 尝试解析JSON响应
                        try:
                            data = await response.json()
                            if 's3_key' in data:
                                print(f"  S3 Key: {data['s3_key']}")
                        except:
                            # 即使不是JSON，只要状态码是200就认为成功
                            pass
                    else:
                        text = await response.text()
                        print(f"  {Fore.RED}❌ 失败: HTTP {response.status}{Style.RESET_ALL}")
                        print(f"  响应: {text[:100]}")
                        fail_count += 1
                        
            except Exception as e:
                print(f"  {Fore.RED}❌ 错误: {str(e)}{Style.RESET_ALL}")
                fail_count += 1
        
        # 显示结果
        print(f"\n{Fore.CYAN}{'='*50}{Style.RESET_ALL}")
        print(f"测试结果:")
        print(f"  成功: {Fore.GREEN}{success_count}{Style.RESET_ALL}")
        print(f"  失败: {Fore.RED}{fail_count}{Style.RESET_ALL}")
        
        if success_count == len(test_files):
            print(f"\n{Fore.GREEN}✅ 所有文档上传成功！修复有效。{Style.RESET_ALL}")
        elif success_count > 0:
            print(f"\n{Fore.YELLOW}⚠️ 部分文档上传成功{Style.RESET_ALL}")
        else:
            print(f"\n{Fore.RED}❌ 所有文档上传失败{Style.RESET_ALL}")
        
        # 验证上传的文件
        print(f"\n{Fore.CYAN}验证上传的文件...{Style.RESET_ALL}")
        try:
            async with session.get(f"{API_URL}/documents") as response:
                if response.status == 200:
                    data = await response.json()
                    uploaded_files = [f["name"] for f in data.get("data", [])]
                    
                    for file_data in test_files:
                        # 检查文件是否在列表中（需要匹配S3路径格式）
                        found = any(file_data["filename"] in name for name in uploaded_files)
                        if found:
                            print(f"  {Fore.GREEN}✅ {file_data['filename']} 已确认上传{Style.RESET_ALL}")
                        else:
                            print(f"  {Fore.YELLOW}⚠️ {file_data['filename']} 未在列表中找到{Style.RESET_ALL}")
                    
                    print(f"\n当前文档总数: {data.get('count', 0)}")
        except Exception as e:
            print(f"验证失败: {str(e)}")

if __name__ == "__main__":
    print(f"{Fore.CYAN}{'='*50}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}文档上传修复验证工具{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'='*50}{Style.RESET_ALL}\n")
    
    asyncio.run(test_upload())
    
    print(f"\n{Fore.CYAN}提示:{Style.RESET_ALL}")
    print("1. 打开 https://dfg648088lloi.cloudfront.net")
    print("2. 进入'文档管理'标签")
    print("3. 尝试上传文件")
    print("4. 如果仍有问题，打开浏览器控制台查看详细错误")
    print("\n或者打开 debug_upload_frontend.html 进行详细调试")