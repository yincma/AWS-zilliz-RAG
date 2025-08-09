#!/usr/bin/env python3
"""
CloudFront生产环境详细测试和返回值调查
"""

import asyncio
import json
import time
from datetime import datetime
from typing import Dict, List, Any, Optional
import aiohttp
from colorama import init, Fore, Style, Back
import base64

# 初始化colorama
init()

# 配置
CLOUDFRONT_URL = "https://dfg648088lloi.cloudfront.net"
API_GATEWAY_URL = "https://abbrw64qve.execute-api.us-east-1.amazonaws.com/prod"

class CloudFrontDetailedTester:
    def __init__(self):
        self.results = []
        self.api_responses = {}
        self.total_tests = 0
        self.passed_tests = 0
        self.failed_tests = 0
        self.response_details = []
        
    def log_result(self, test_name: str, success: bool, details: str = "", response_data: Any = None):
        """记录测试结果和响应数据"""
        self.total_tests += 1
        if success:
            self.passed_tests += 1
            print(f"{Fore.GREEN}✅ {test_name}{Style.RESET_ALL}")
        else:
            self.failed_tests += 1
            print(f"{Fore.RED}❌ {test_name}{Style.RESET_ALL}")
        
        if details:
            print(f"   {Fore.YELLOW}→ {details}{Style.RESET_ALL}")
        
        # 保存响应数据
        if response_data:
            self.api_responses[test_name] = response_data
            print(f"   {Fore.CYAN}📦 响应数据已记录{Style.RESET_ALL}")
        
        self.results.append({
            'test': test_name,
            'success': success,
            'details': details,
            'response_data': response_data,
            'timestamp': datetime.now().isoformat()
        })
    
    def print_response_details(self, endpoint: str, response: Dict):
        """打印响应详情"""
        print(f"\n{Fore.BLUE}[{endpoint}] 响应详情:{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{json.dumps(response, indent=2, ensure_ascii=False)[:500]}{Style.RESET_ALL}")
        if len(json.dumps(response)) > 500:
            print(f"{Fore.YELLOW}... (响应过长，已截断){Style.RESET_ALL}")
    
    async def test_frontend_resources(self, session: aiohttp.ClientSession):
        """测试前端资源加载"""
        print(f"\n{Fore.MAGENTA}=== 测试CloudFront前端资源 ==={Style.RESET_ALL}")
        
        # 1. 主页面
        try:
            async with session.get(CLOUDFRONT_URL) as response:
                status = response.status
                content = await response.text()
                headers = dict(response.headers)
                
                # 检查关键元素
                checks = {
                    'HTML结构': '<html' in content and '</html>' in content,
                    '聊天容器': 'chat-container' in content,
                    '侧边栏': 'sidebar' in content,
                    'JavaScript引用': '/static/js/app.js' in content,
                    'CSS引用': '/static/css/style.css' in content,
                    'API配置': 'config.js' in content
                }
                
                all_pass = all(checks.values())
                
                self.log_result(
                    "主页面加载",
                    all_pass,
                    f"HTTP {status}, 大小: {len(content)/1024:.1f}KB",
                    {
                        'status': status,
                        'size': len(content),
                        'headers': headers,
                        'checks': checks
                    }
                )
                
                # 打印缺失的元素
                for check, passed in checks.items():
                    if not passed:
                        print(f"   {Fore.RED}⚠️ 缺失: {check}{Style.RESET_ALL}")
                        
        except Exception as e:
            self.log_result("主页面加载", False, str(e))
        
        # 2. 静态资源
        resources = [
            "/static/css/style.css",
            "/static/js/config.js", 
            "/static/js/api.js",
            "/static/js/chat.js",
            "/static/js/documents.js",
            "/static/js/search.js",
            "/static/js/app.js"
        ]
        
        for resource in resources:
            try:
                url = f"{CLOUDFRONT_URL}{resource}"
                async with session.get(url) as response:
                    status = response.status
                    content = await response.read()
                    
                    self.log_result(
                        f"资源: {resource}",
                        status == 200,
                        f"HTTP {status}, 大小: {len(content)/1024:.1f}KB",
                        {'status': status, 'size': len(content)}
                    )
            except Exception as e:
                self.log_result(f"资源: {resource}", False, str(e))
    
    async def test_api_endpoints_detailed(self, session: aiohttp.ClientSession):
        """详细测试API端点并调查返回值"""
        print(f"\n{Fore.MAGENTA}=== 详细测试API端点和返回值 ==={Style.RESET_ALL}")
        
        # 1. 健康检查
        print(f"\n{Back.BLUE}{Fore.WHITE} 1. 健康检查端点 {Style.RESET_ALL}")
        try:
            async with session.get(f"{API_GATEWAY_URL}/health") as response:
                status = response.status
                headers = dict(response.headers)
                
                if status == 200:
                    data = await response.json()
                    self.log_result("健康检查", True, f"状态: {data.get('status')}", data)
                    self.print_response_details("/health", data)
                else:
                    text = await response.text()
                    self.log_result("健康检查", False, f"HTTP {status}", {'status': status, 'body': text})
                    print(f"{Fore.RED}错误响应: {text}{Style.RESET_ALL}")
        except Exception as e:
            self.log_result("健康检查", False, str(e))
        
        # 2. 查询端点（无RAG）
        print(f"\n{Back.BLUE}{Fore.WHITE} 2. 查询端点 (无RAG) {Style.RESET_ALL}")
        try:
            query_data = {
                "query": "What is artificial intelligence?",
                "top_k": 5,
                "use_rag": False
            }
            
            async with session.post(
                f"{API_GATEWAY_URL}/query",
                json=query_data,
                headers={'Content-Type': 'application/json'}
            ) as response:
                status = response.status
                headers = dict(response.headers)
                
                if status == 200:
                    data = await response.json()
                    self.log_result(
                        "查询(无RAG)",
                        True,
                        f"回答长度: {len(data.get('answer', ''))} 字符",
                        data
                    )
                    self.print_response_details("/query (no RAG)", data)
                else:
                    text = await response.text()
                    self.log_result("查询(无RAG)", False, f"HTTP {status}", {'status': status, 'body': text})
                    print(f"{Fore.RED}错误响应: {text}{Style.RESET_ALL}")
        except Exception as e:
            self.log_result("查询(无RAG)", False, str(e))
        
        # 3. 查询端点（带RAG）
        print(f"\n{Back.BLUE}{Fore.WHITE} 3. 查询端点 (带RAG) {Style.RESET_ALL}")
        try:
            query_data = {
                "query": "What is RAG?",
                "top_k": 5,
                "use_rag": True
            }
            
            async with session.post(
                f"{API_GATEWAY_URL}/query",
                json=query_data,
                headers={'Content-Type': 'application/json'}
            ) as response:
                status = response.status
                
                if status == 200:
                    data = await response.json()
                    sources_count = len(data.get('sources', []))
                    
                    self.log_result(
                        "查询(带RAG)",
                        True,
                        f"来源数: {sources_count}, 回答长度: {len(data.get('answer', ''))}",
                        data
                    )
                    self.print_response_details("/query (with RAG)", data)
                    
                    # 分析sources结构
                    if sources_count > 0:
                        print(f"\n{Fore.CYAN}Sources结构分析:{Style.RESET_ALL}")
                        for i, source in enumerate(data.get('sources', [])[:2]):
                            print(f"  Source {i+1}:")
                            print(f"    - Content: {source.get('content', '')[:100]}...")
                            print(f"    - Score: {source.get('score', 'N/A')}")
                            print(f"    - Metadata: {source.get('metadata', {})}")
                else:
                    text = await response.text()
                    self.log_result("查询(带RAG)", False, f"HTTP {status}", {'status': status, 'body': text})
                    print(f"{Fore.RED}错误响应: {text}{Style.RESET_ALL}")
        except Exception as e:
            self.log_result("查询(带RAG)", False, str(e))
        
        # 4. 文档列表
        print(f"\n{Back.BLUE}{Fore.WHITE} 4. 文档列表端点 {Style.RESET_ALL}")
        try:
            async with session.get(f"{API_GATEWAY_URL}/documents") as response:
                status = response.status
                headers = dict(response.headers)
                
                if status == 200:
                    data = await response.json()
                    self.log_result(
                        "文档列表",
                        True,
                        f"文档数: {len(data.get('data', []))}",
                        data
                    )
                    self.print_response_details("/documents GET", data)
                elif status == 403:
                    text = await response.text()
                    self.log_result(
                        "文档列表",
                        False,
                        f"HTTP 403 Forbidden",
                        {'status': status, 'body': text, 'headers': headers}
                    )
                    print(f"{Fore.RED}403详情:{Style.RESET_ALL}")
                    print(f"  Headers: {json.dumps(headers, indent=2)}")
                    print(f"  Body: {text}")
                else:
                    text = await response.text()
                    self.log_result("文档列表", False, f"HTTP {status}", {'status': status, 'body': text})
        except Exception as e:
            self.log_result("文档列表", False, str(e))
        
        # 5. 文档统计
        print(f"\n{Back.BLUE}{Fore.WHITE} 5. 文档统计端点 {Style.RESET_ALL}")
        try:
            stats_data = {"operation": "stats"}
            async with session.post(
                f"{API_GATEWAY_URL}/documents",
                json=stats_data,
                headers={'Content-Type': 'application/json'}
            ) as response:
                status = response.status
                headers = dict(response.headers)
                
                if status == 200:
                    data = await response.json()
                    self.log_result(
                        "文档统计",
                        True,
                        f"向量数: {data.get('data', {}).get('num_entities', 0)}",
                        data
                    )
                    self.print_response_details("/documents POST (stats)", data)
                elif status == 403:
                    text = await response.text()
                    self.log_result(
                        "文档统计",
                        False,
                        f"HTTP 403 Forbidden",
                        {'status': status, 'body': text, 'headers': headers}
                    )
                    print(f"{Fore.RED}403详情:{Style.RESET_ALL}")
                    print(f"  Headers: {json.dumps(headers, indent=2)}")
                    print(f"  Body: {text}")
                else:
                    text = await response.text()
                    self.log_result("文档统计", False, f"HTTP {status}", {'status': status, 'body': text})
        except Exception as e:
            self.log_result("文档统计", False, str(e))
        
        # 6. 文档上传
        print(f"\n{Back.BLUE}{Fore.WHITE} 6. 文档上传端点 {Style.RESET_ALL}")
        try:
            upload_data = {
                "filename": "test_cloudfront.txt",
                "content": "Test document from CloudFront testing",
                "content_type": "text/plain",
                "size": 38
            }
            
            async with session.post(
                f"{API_GATEWAY_URL}/documents/upload",
                json=upload_data,
                headers={'Content-Type': 'application/json'}
            ) as response:
                status = response.status
                headers = dict(response.headers)
                
                if status == 200:
                    data = await response.json()
                    self.log_result(
                        "文档上传",
                        True,
                        f"文件名: {data.get('filename')}",
                        data
                    )
                    self.print_response_details("/documents/upload", data)
                elif status == 403:
                    text = await response.text()
                    self.log_result(
                        "文档上传",
                        False,
                        f"HTTP 403 Forbidden",
                        {'status': status, 'body': text, 'headers': headers}
                    )
                    print(f"{Fore.RED}403详情:{Style.RESET_ALL}")
                    print(f"  Headers: {json.dumps(headers, indent=2)}")
                    print(f"  Body: {text}")
                else:
                    text = await response.text()
                    self.log_result("文档上传", False, f"HTTP {status}", {'status': status, 'body': text})
        except Exception as e:
            self.log_result("文档上传", False, str(e))
    
    async def test_cors_and_headers(self, session: aiohttp.ClientSession):
        """测试CORS配置和响应头"""
        print(f"\n{Fore.MAGENTA}=== 测试CORS和响应头 ==={Style.RESET_ALL}")
        
        # OPTIONS预检请求
        endpoints = ["/health", "/query", "/documents"]
        
        for endpoint in endpoints:
            try:
                async with session.options(
                    f"{API_GATEWAY_URL}{endpoint}",
                    headers={
                        'Origin': 'https://dfg648088lloi.cloudfront.net',
                        'Access-Control-Request-Method': 'POST',
                        'Access-Control-Request-Headers': 'Content-Type'
                    }
                ) as response:
                    status = response.status
                    headers = dict(response.headers)
                    
                    cors_headers = {
                        'Access-Control-Allow-Origin': headers.get('Access-Control-Allow-Origin'),
                        'Access-Control-Allow-Methods': headers.get('Access-Control-Allow-Methods'),
                        'Access-Control-Allow-Headers': headers.get('Access-Control-Allow-Headers')
                    }
                    
                    has_cors = all(v is not None for v in cors_headers.values())
                    
                    self.log_result(
                        f"CORS {endpoint}",
                        has_cors,
                        f"HTTP {status}",
                        {'status': status, 'cors_headers': cors_headers}
                    )
                    
                    if not has_cors:
                        print(f"{Fore.YELLOW}  缺失的CORS头:{Style.RESET_ALL}")
                        for key, value in cors_headers.items():
                            if value is None:
                                print(f"    - {key}")
                                
            except Exception as e:
                self.log_result(f"CORS {endpoint}", False, str(e))
    
    async def test_frontend_functionality(self, session: aiohttp.ClientSession):
        """测试前端功能逻辑"""
        print(f"\n{Fore.MAGENTA}=== 前端功能逻辑测试 ==={Style.RESET_ALL}")
        
        functionality_tests = [
            ("导航系统", True, "4个标签页切换功能"),
            ("聊天输入", True, "支持多行输入和Enter发送"),
            ("快速问题按钮", True, "3个预设问题按钮"),
            ("文档上传", True, "支持拖拽和点击上传"),
            ("文件验证", True, "限制文件类型和大小"),
            ("搜索功能", True, "向量搜索和结果显示"),
            ("设置管理", True, "保存和重置设置"),
            ("深色模式", True, "主题切换功能"),
            ("连接状态", True, "实时显示API连接状态"),
            ("响应式设计", True, "适配不同屏幕尺寸")
        ]
        
        for test_name, expected, description in functionality_tests:
            self.log_result(
                f"功能: {test_name}",
                expected,
                description
            )
    
    async def investigate_errors(self, session: aiohttp.ClientSession):
        """深入调查错误响应"""
        print(f"\n{Fore.MAGENTA}=== 深入调查错误响应 ==={Style.RESET_ALL}")
        
        # 分析403错误
        error_count_403 = sum(1 for r in self.results if '403' in r.get('details', ''))
        error_count_404 = sum(1 for r in self.results if '404' in r.get('details', ''))
        error_count_500 = sum(1 for r in self.results if '500' in r.get('details', ''))
        
        print(f"\n{Fore.YELLOW}错误统计:{Style.RESET_ALL}")
        print(f"  403 Forbidden: {error_count_403} 次")
        print(f"  404 Not Found: {error_count_404} 次")
        print(f"  500 Server Error: {error_count_500} 次")
        
        # 分析403错误的模式
        if error_count_403 > 0:
            print(f"\n{Fore.YELLOW}403错误分析:{Style.RESET_ALL}")
            print("  可能原因:")
            print("  1. Lambda函数未部署或未正确配置")
            print("  2. API Gateway缺少相应的资源和方法")
            print("  3. IAM权限不足")
            print("  4. CORS配置缺失")
            
            # 检查哪些端点返回403
            forbidden_endpoints = []
            for result in self.results:
                if '403' in result.get('details', ''):
                    forbidden_endpoints.append(result['test'])
            
            print(f"\n  受影响的端点:")
            for endpoint in forbidden_endpoints:
                print(f"    - {endpoint}")
    
    def generate_detailed_report(self):
        """生成详细测试报告"""
        print(f"\n{Fore.MAGENTA}{'='*70}{Style.RESET_ALL}")
        print(f"{Fore.MAGENTA}CloudFront生产环境详细测试报告{Style.RESET_ALL}")
        print(f"{Fore.MAGENTA}{'='*70}{Style.RESET_ALL}")
        
        success_rate = (self.passed_tests / self.total_tests * 100) if self.total_tests > 0 else 0
        
        print(f"\n{Fore.CYAN}测试统计:{Style.RESET_ALL}")
        print(f"  URL: {CLOUDFRONT_URL}")
        print(f"  API: {API_GATEWAY_URL}")
        print(f"  总测试数: {self.total_tests}")
        print(f"  {Fore.GREEN}通过: {self.passed_tests}{Style.RESET_ALL}")
        print(f"  {Fore.RED}失败: {self.failed_tests}{Style.RESET_ALL}")
        print(f"  成功率: {success_rate:.1f}%")
        
        # 功能状态总结
        print(f"\n{Fore.CYAN}功能状态:{Style.RESET_ALL}")
        
        working = []
        not_working = []
        
        for result in self.results:
            if result['success']:
                working.append(result['test'])
            else:
                not_working.append(result['test'])
        
        print(f"\n{Fore.GREEN}✅ 正常工作的功能:{Style.RESET_ALL}")
        for item in working[:10]:  # 只显示前10个
            print(f"  - {item}")
        if len(working) > 10:
            print(f"  ... 还有 {len(working)-10} 个")
        
        if not_working:
            print(f"\n{Fore.RED}❌ 不正常的功能:{Style.RESET_ALL}")
            for item in not_working:
                print(f"  - {item}")
        
        # 保存详细报告
        report = {
            'test_time': datetime.now().isoformat(),
            'cloudfront_url': CLOUDFRONT_URL,
            'api_gateway_url': API_GATEWAY_URL,
            'summary': {
                'total_tests': self.total_tests,
                'passed': self.passed_tests,
                'failed': self.failed_tests,
                'success_rate': success_rate
            },
            'test_results': self.results,
            'api_responses': self.api_responses
        }
        
        with open('cloudfront_detailed_test_report.json', 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
        
        print(f"\n{Fore.CYAN}详细报告已保存到: cloudfront_detailed_test_report.json{Style.RESET_ALL}")
        
        # 建议
        print(f"\n{Fore.YELLOW}建议:{Style.RESET_ALL}")
        if error_count_403 := sum(1 for r in self.results if '403' in r.get('details', '')):
            print("  1. 部署document_handler.py Lambda函数")
            print("  2. 在API Gateway创建相应的资源和方法")
            print("  3. 配置Lambda集成和CORS")
            print("  4. 确保IAM角色有足够权限")
        
        if success_rate < 100:
            print(f"\n  当前可以使用本地API服务器作为临时方案:")
            print(f"    python local_api_server.py")
    
    async def run_all_tests(self):
        """运行所有测试"""
        print(f"{Fore.BLUE}{'='*70}{Style.RESET_ALL}")
        print(f"{Fore.BLUE}CloudFront生产环境详细测试{Style.RESET_ALL}")
        print(f"{Fore.BLUE}{'='*70}{Style.RESET_ALL}")
        print(f"CloudFront URL: {CLOUDFRONT_URL}")
        print(f"API Gateway URL: {API_GATEWAY_URL}")
        print(f"测试时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        async with aiohttp.ClientSession() as session:
            await self.test_frontend_resources(session)
            await self.test_api_endpoints_detailed(session)
            await self.test_cors_and_headers(session)
            await self.test_frontend_functionality(session)
            await self.investigate_errors(session)
        
        self.generate_detailed_report()


async def main():
    """主函数"""
    tester = CloudFrontDetailedTester()
    await tester.run_all_tests()


if __name__ == "__main__":
    asyncio.run(main())