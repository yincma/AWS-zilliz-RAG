#!/usr/bin/env python3
"""
诊断Chat功能"Failed to fetch"错误
"""
import asyncio
import aiohttp
import json
from datetime import datetime
from colorama import init, Fore, Style

init(autoreset=True)

# API端点
CLOUDFRONT_URL = "https://dfg648088lloi.cloudfront.net"
API_GATEWAY_URL = "https://abbrw64qve.execute-api.us-east-1.amazonaws.com/prod"

class ChatErrorDiagnostics:
    def __init__(self):
        self.results = []
        self.api_url = API_GATEWAY_URL
        
    def log_result(self, test_name: str, success: bool, details: str = "", data: dict = None):
        """记录测试结果"""
        result = {
            "test": test_name,
            "success": success,
            "details": details,
            "data": data,
            "timestamp": datetime.now().isoformat()
        }
        self.results.append(result)
        
        # 打印结果
        if success:
            print(f"{Fore.GREEN}✅ {test_name}{Style.RESET_ALL}")
            if details:
                print(f"   {details}")
        else:
            print(f"{Fore.RED}❌ {test_name}{Style.RESET_ALL}")
            if details:
                print(f"   {Fore.YELLOW}{details}{Style.RESET_ALL}")
                
    async def test_cors_headers(self, session: aiohttp.ClientSession):
        """测试CORS配置"""
        print(f"\n{Fore.CYAN}=== 测试CORS配置 ==={Style.RESET_ALL}")
        
        # 测试/query的OPTIONS请求
        try:
            headers = {
                'Origin': CLOUDFRONT_URL,
                'Access-Control-Request-Method': 'POST',
                'Access-Control-Request-Headers': 'Content-Type'
            }
            
            async with session.options(f"{self.api_url}/query", headers=headers) as response:
                cors_headers = {
                    'Allow-Origin': response.headers.get('Access-Control-Allow-Origin'),
                    'Allow-Methods': response.headers.get('Access-Control-Allow-Methods'),
                    'Allow-Headers': response.headers.get('Access-Control-Allow-Headers')
                }
                
                if response.status == 200:
                    self.log_result("CORS预检请求", True, 
                                  f"Headers: {json.dumps(cors_headers, indent=2)}")
                else:
                    self.log_result("CORS预检请求", False, 
                                  f"HTTP {response.status}, Headers: {cors_headers}")
        except Exception as e:
            self.log_result("CORS预检请求", False, f"错误: {str(e)}")
            
    async def test_query_endpoint(self, session: aiohttp.ClientSession):
        """测试查询端点"""
        print(f"\n{Fore.CYAN}=== 测试查询端点 ==={Style.RESET_ALL}")
        
        # 测试简单查询
        query_data = {
            "query": "What is artificial intelligence?",
            "top_k": 5,
            "use_rag": False
        }
        
        try:
            headers = {
                'Content-Type': 'application/json',
                'Origin': CLOUDFRONT_URL
            }
            
            async with session.post(
                f"{self.api_url}/query",
                json=query_data,
                headers=headers
            ) as response:
                
                # 获取响应头
                response_headers = dict(response.headers)
                
                if response.status == 200:
                    data = await response.json()
                    self.log_result("POST /query (无RAG)", True, 
                                  f"成功返回，答案长度: {len(data.get('answer', ''))} 字符",
                                  {"status": response.status, "has_answer": bool(data.get('answer'))})
                    
                    # 检查CORS头
                    cors_origin = response.headers.get('Access-Control-Allow-Origin')
                    if cors_origin:
                        print(f"   {Fore.GREEN}CORS头正确: {cors_origin}{Style.RESET_ALL}")
                    else:
                        print(f"   {Fore.YELLOW}警告: 缺少CORS头{Style.RESET_ALL}")
                else:
                    text = await response.text()
                    self.log_result("POST /query (无RAG)", False, 
                                  f"HTTP {response.status}: {text[:200]}",
                                  {"status": response.status, "headers": response_headers})
                    
        except aiohttp.ClientError as e:
            self.log_result("POST /query (无RAG)", False, 
                          f"网络错误: {str(e)}")
        except Exception as e:
            self.log_result("POST /query (无RAG)", False, 
                          f"未知错误: {str(e)}")
            
    async def test_from_browser_context(self, session: aiohttp.ClientSession):
        """模拟浏览器请求"""
        print(f"\n{Fore.CYAN}=== 模拟浏览器请求 ==={Style.RESET_ALL}")
        
        # 使用浏览器User-Agent和完整的请求头
        browser_headers = {
            'Content-Type': 'application/json',
            'Origin': CLOUDFRONT_URL,
            'Referer': f'{CLOUDFRONT_URL}/',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
            'Accept': 'application/json',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'cross-site'
        }
        
        query_data = {
            "query": "What is RAG?",
            "top_k": 5,
            "use_rag": True
        }
        
        try:
            async with session.post(
                f"{self.api_url}/query",
                json=query_data,
                headers=browser_headers
            ) as response:
                
                if response.status == 200:
                    data = await response.json()
                    self.log_result("浏览器模拟请求", True,
                                  f"成功，来源数: {len(data.get('sources', []))}",
                                  {"status": 200, "mode": data.get('mode')})
                else:
                    text = await response.text()
                    self.log_result("浏览器模拟请求", False,
                                  f"HTTP {response.status}: {text[:200]}")
                    
        except Exception as e:
            self.log_result("浏览器模拟请求", False, f"错误: {str(e)}")
            
    async def test_lambda_directly(self, session: aiohttp.ClientSession):
        """测试Lambda函数是否正常"""
        print(f"\n{Fore.CYAN}=== 测试Lambda函数状态 ==={Style.RESET_ALL}")
        
        # 测试健康检查
        try:
            async with session.get(f"{self.api_url}/health") as response:
                if response.status == 200:
                    data = await response.json()
                    self.log_result("Lambda健康检查", True,
                                  f"服务: {data.get('service')}, 版本: {data.get('version')}")
                else:
                    self.log_result("Lambda健康检查", False,
                                  f"HTTP {response.status}")
        except Exception as e:
            self.log_result("Lambda健康检查", False, f"错误: {str(e)}")
            
    async def test_network_connectivity(self, session: aiohttp.ClientSession):
        """测试网络连通性"""
        print(f"\n{Fore.CYAN}=== 测试网络连通性 ==={Style.RESET_ALL}")
        
        # 测试CloudFront
        try:
            async with session.get(CLOUDFRONT_URL) as response:
                self.log_result("CloudFront访问", response.status == 200,
                              f"HTTP {response.status}")
        except Exception as e:
            self.log_result("CloudFront访问", False, f"错误: {str(e)}")
            
        # 测试API Gateway
        try:
            async with session.get(f"{self.api_url}/health") as response:
                self.log_result("API Gateway访问", response.status == 200,
                              f"HTTP {response.status}")
        except Exception as e:
            self.log_result("API Gateway访问", False, f"错误: {str(e)}")
            
    def generate_solution(self):
        """生成解决方案"""
        print(f"\n{Fore.CYAN}=== 诊断结果和解决方案 ==={Style.RESET_ALL}")
        
        failed_tests = [r for r in self.results if not r['success']]
        
        if not failed_tests:
            print(f"{Fore.GREEN}✅ 所有测试通过！Chat功能应该正常工作。{Style.RESET_ALL}")
            return
            
        print(f"\n{Fore.YELLOW}发现 {len(failed_tests)} 个问题：{Style.RESET_ALL}")
        
        for result in failed_tests:
            print(f"\n❌ {result['test']}")
            if 'CORS' in result['test']:
                print(f"   解决方案：")
                print(f"   1. 在API Gateway为/query添加OPTIONS方法")
                print(f"   2. 配置Mock集成返回CORS头")
                print(f"   3. 确保Lambda返回包含Access-Control-Allow-Origin头")
            elif 'query' in result['test'].lower():
                print(f"   解决方案：")
                print(f"   1. 检查Lambda函数日志")
                print(f"   2. 验证Bedrock权限")
                print(f"   3. 检查请求格式是否正确")
                
    async def run_diagnostics(self):
        """运行所有诊断测试"""
        print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}Chat功能错误诊断工具{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}")
        
        async with aiohttp.ClientSession() as session:
            # 运行测试
            await self.test_network_connectivity(session)
            await self.test_lambda_directly(session)
            await self.test_cors_headers(session)
            await self.test_query_endpoint(session)
            await self.test_from_browser_context(session)
            
        # 生成解决方案
        self.generate_solution()
        
        # 保存结果
        with open('chat_error_diagnosis.json', 'w', encoding='utf-8') as f:
            json.dump({
                'timestamp': datetime.now().isoformat(),
                'api_url': self.api_url,
                'cloudfront_url': CLOUDFRONT_URL,
                'results': self.results,
                'summary': {
                    'total_tests': len(self.results),
                    'passed': len([r for r in self.results if r['success']]),
                    'failed': len([r for r in self.results if not r['success']])
                }
            }, f, ensure_ascii=False, indent=2)
            
        print(f"\n{Fore.GREEN}诊断报告已保存到: chat_error_diagnosis.json{Style.RESET_ALL}")

if __name__ == "__main__":
    diagnostics = ChatErrorDiagnostics()
    asyncio.run(diagnostics.run_diagnostics())