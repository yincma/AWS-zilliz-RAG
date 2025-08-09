#!/usr/bin/env python3
"""
测试文档上传的CORS问题
"""
import asyncio
import aiohttp
import json
from datetime import datetime
from colorama import init, Fore, Style

init(autoreset=True)

API_URL = "https://abbrw64qve.execute-api.us-east-1.amazonaws.com/prod"
CLOUDFRONT_URL = "https://dfg648088lloi.cloudfront.net"

async def test_cors_preflight():
    """测试CORS预检请求"""
    print(f"{Fore.CYAN}=== 测试CORS预检请求 ==={Style.RESET_ALL}\n")
    
    async with aiohttp.ClientSession() as session:
        # 测试/documents/upload的OPTIONS请求
        headers = {
            'Origin': CLOUDFRONT_URL,
            'Access-Control-Request-Method': 'POST',
            'Access-Control-Request-Headers': 'Content-Type'
        }
        
        try:
            async with session.options(f"{API_URL}/documents/upload", headers=headers) as response:
                print(f"OPTIONS /documents/upload 状态: {response.status}")
                
                if response.status == 200:
                    print(f"{Fore.GREEN}✅ CORS预检成功{Style.RESET_ALL}")
                    cors_headers = {
                        'Allow-Origin': response.headers.get('Access-Control-Allow-Origin'),
                        'Allow-Methods': response.headers.get('Access-Control-Allow-Methods'),
                        'Allow-Headers': response.headers.get('Access-Control-Allow-Headers')
                    }
                    print(f"CORS头: {json.dumps(cors_headers, indent=2)}")
                else:
                    print(f"{Fore.RED}❌ CORS预检失败{Style.RESET_ALL}")
                    text = await response.text()
                    print(f"响应: {text}")
        except Exception as e:
            print(f"{Fore.RED}❌ 请求错误: {str(e)}{Style.RESET_ALL}")

async def test_actual_upload():
    """测试实际的上传请求"""
    print(f"\n{Fore.CYAN}=== 测试实际上传请求 ==={Style.RESET_ALL}\n")
    
    test_file = {
        "filename": f"cors_test_{datetime.now().strftime('%H%M%S')}.txt",
        "content": "Test document for CORS verification",
        "content_type": "text/plain",
        "size": 36
    }
    
    async with aiohttp.ClientSession() as session:
        headers = {
            'Content-Type': 'application/json',
            'Origin': CLOUDFRONT_URL
        }
        
        try:
            async with session.post(
                f"{API_URL}/documents/upload",
                json=test_file,
                headers=headers
            ) as response:
                
                print(f"POST /documents/upload 状态: {response.status}")
                
                # 检查CORS响应头
                cors_origin = response.headers.get('Access-Control-Allow-Origin')
                if cors_origin:
                    print(f"{Fore.GREEN}✅ CORS头存在: Access-Control-Allow-Origin: {cors_origin}{Style.RESET_ALL}")
                else:
                    print(f"{Fore.YELLOW}⚠️ 缺少CORS头{Style.RESET_ALL}")
                
                if response.status == 200:
                    print(f"{Fore.GREEN}✅ 上传成功{Style.RESET_ALL}")
                    data = await response.json()
                    if 's3_key' in data:
                        print(f"S3 Key: {data['s3_key']}")
                else:
                    text = await response.text()
                    print(f"{Fore.RED}❌ 上传失败: {text}{Style.RESET_ALL}")
                    
        except Exception as e:
            print(f"{Fore.RED}❌ 请求错误: {str(e)}{Style.RESET_ALL}")

async def test_with_browser_headers():
    """使用完整的浏览器请求头测试"""
    print(f"\n{Fore.CYAN}=== 使用浏览器请求头测试 ==={Style.RESET_ALL}\n")
    
    test_file = {
        "filename": "browser_test.txt",
        "content": "Browser upload test",
        "content_type": "text/plain",
        "size": 19
    }
    
    async with aiohttp.ClientSession() as session:
        # 模拟浏览器的完整请求头
        headers = {
            'Content-Type': 'application/json',
            'Origin': CLOUDFRONT_URL,
            'Referer': f'{CLOUDFRONT_URL}/',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
            'Accept': 'application/json',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'cross-site'
        }
        
        try:
            print("发送带浏览器头的POST请求...")
            async with session.post(
                f"{API_URL}/documents/upload",
                json=test_file,
                headers=headers
            ) as response:
                
                print(f"状态码: {response.status}")
                
                if response.status == 200:
                    print(f"{Fore.GREEN}✅ 使用浏览器头上传成功{Style.RESET_ALL}")
                else:
                    text = await response.text()
                    print(f"{Fore.RED}❌ 失败: {text}{Style.RESET_ALL}")
                    
        except Exception as e:
            print(f"{Fore.RED}❌ 错误: {str(e)}{Style.RESET_ALL}")

def print_solution():
    """打印解决方案"""
    print(f"\n{Fore.CYAN}=== 解决方案 ==={Style.RESET_ALL}\n")
    
    print("如果CORS预检失败，可能的解决方法：")
    print("1. API Gateway的OPTIONS方法可能需要时间生效")
    print("2. 可以尝试在Lambda函数中直接处理OPTIONS请求")
    print("3. 或者使用API Gateway的CORS配置向导")
    print("\n临时解决方案：")
    print("1. 使用本地代理服务器绕过CORS")
    print("2. 或者在Lambda函数中添加CORS头处理")
    
    print(f"\n{Fore.YELLOW}检查Lambda日志：{Style.RESET_ALL}")
    print("aws logs tail /aws/lambda/rag-document-handler --follow --region us-east-1")

async def main():
    print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}文档上传CORS诊断工具{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}")
    
    # 运行测试
    await test_cors_preflight()
    await test_actual_upload()
    await test_with_browser_headers()
    
    # 打印解决方案
    print_solution()

if __name__ == "__main__":
    asyncio.run(main())