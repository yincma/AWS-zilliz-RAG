#!/usr/bin/env python3
"""
测试本地API服务器的所有端点
"""

import asyncio
import json
import aiohttp
from colorama import init, Fore, Style
from datetime import datetime

# 初始化colorama
init()

# 配置
LOCAL_API_URL = "http://localhost:8000"
LOCAL_WEB_URL = "http://localhost:8080"

class LocalAPITester:
    def __init__(self):
        self.results = []
        self.total_tests = 0
        self.passed_tests = 0
        self.failed_tests = 0
        
    def log_result(self, test_name: str, success: bool, details: str = ""):
        """记录测试结果"""
        self.total_tests += 1
        if success:
            self.passed_tests += 1
            print(f"{Fore.GREEN}✅ {test_name}{Style.RESET_ALL}")
        else:
            self.failed_tests += 1
            print(f"{Fore.RED}❌ {test_name}{Style.RESET_ALL}")
        
        if details:
            print(f"   {Fore.YELLOW}→ {details}{Style.RESET_ALL}")
        
        self.results.append({
            'test': test_name,
            'success': success,
            'details': details,
            'timestamp': datetime.now().isoformat()
        })
    
    async def test_health_check(self, session: aiohttp.ClientSession):
        """测试健康检查"""
        print(f"\n{Fore.CYAN}=== 测试健康检查 ==={Style.RESET_ALL}")
        
        try:
            async with session.get(f"{LOCAL_API_URL}/health") as response:
                if response.status == 200:
                    data = await response.json()
                    self.log_result("健康检查", True, f"Status: {data.get('status')}")
                else:
                    self.log_result("健康检查", False, f"HTTP {response.status}")
        except Exception as e:
            self.log_result("健康检查", False, str(e))
    
    async def test_document_endpoints(self, session: aiohttp.ClientSession):
        """测试文档管理端点"""
        print(f"\n{Fore.CYAN}=== 测试文档管理端点 ==={Style.RESET_ALL}")
        
        # 1. 获取文档列表
        try:
            async with session.get(f"{LOCAL_API_URL}/documents") as response:
                if response.status == 200:
                    data = await response.json()
                    doc_count = len(data.get('data', []))
                    self.log_result("获取文档列表", True, f"文档数: {doc_count}")
                else:
                    self.log_result("获取文档列表", False, f"HTTP {response.status}")
        except Exception as e:
            self.log_result("获取文档列表", False, str(e))
        
        # 2. 获取统计信息
        try:
            stats_data = {"operation": "stats"}
            async with session.post(
                f"{LOCAL_API_URL}/documents",
                json=stats_data
            ) as response:
                if response.status == 200:
                    data = await response.json()
                    entities = data.get('data', {}).get('num_entities', 0)
                    self.log_result("获取统计信息", True, f"向量数: {entities}")
                else:
                    self.log_result("获取统计信息", False, f"HTTP {response.status}")
        except Exception as e:
            self.log_result("获取统计信息", False, str(e))
        
        # 3. 文件上传
        try:
            upload_data = {
                "filename": "test_doc.txt",
                "content": "这是一个测试文档内容。",
                "content_type": "text/plain",
                "size": 30
            }
            async with session.post(
                f"{LOCAL_API_URL}/documents/upload",
                json=upload_data
            ) as response:
                if response.status == 200:
                    data = await response.json()
                    self.log_result("文件上传", True, f"文件名: {data.get('filename')}")
                else:
                    self.log_result("文件上传", False, f"HTTP {response.status}")
        except Exception as e:
            self.log_result("文件上传", False, str(e))
        
        # 4. 删除文档
        try:
            async with session.delete(f"{LOCAL_API_URL}/documents/test_doc.txt") as response:
                if response.status == 200:
                    data = await response.json()
                    self.log_result("删除文档", True, data.get('message', ''))
                elif response.status == 404:
                    self.log_result("删除文档", True, "文档不存在（预期行为）")
                else:
                    self.log_result("删除文档", False, f"HTTP {response.status}")
        except Exception as e:
            self.log_result("删除文档", False, str(e))
        
        # 5. 清空集合
        try:
            clear_data = {"operation": "clear"}
            async with session.delete(
                f"{LOCAL_API_URL}/documents",
                json=clear_data
            ) as response:
                if response.status == 200:
                    data = await response.json()
                    deleted = data.get('deleted_count', 0)
                    self.log_result("清空集合", True, f"删除数量: {deleted}")
                else:
                    self.log_result("清空集合", False, f"HTTP {response.status}")
        except Exception as e:
            self.log_result("清空集合", False, str(e))
    
    async def test_query_endpoint(self, session: aiohttp.ClientSession):
        """测试查询端点"""
        print(f"\n{Fore.CYAN}=== 测试查询端点 ==={Style.RESET_ALL}")
        
        # 测试无RAG查询
        try:
            query_data = {
                "query": "什么是人工智能？",
                "top_k": 5,
                "use_rag": False
            }
            async with session.post(
                f"{LOCAL_API_URL}/query",
                json=query_data
            ) as response:
                if response.status == 200:
                    data = await response.json()
                    has_answer = bool(data.get('answer'))
                    self.log_result("查询(无RAG)", has_answer, f"回答长度: {len(data.get('answer', ''))}")
                else:
                    self.log_result("查询(无RAG)", False, f"HTTP {response.status}")
        except Exception as e:
            self.log_result("查询(无RAG)", False, str(e))
        
        # 测试带RAG查询
        try:
            query_data = {
                "query": "RAG是什么？",
                "top_k": 5,
                "use_rag": True
            }
            async with session.post(
                f"{LOCAL_API_URL}/query",
                json=query_data
            ) as response:
                if response.status == 200:
                    data = await response.json()
                    has_answer = bool(data.get('answer'))
                    sources_count = len(data.get('sources', []))
                    self.log_result("查询(带RAG)", has_answer, f"来源数: {sources_count}")
                else:
                    self.log_result("查询(带RAG)", False, f"HTTP {response.status}")
        except Exception as e:
            self.log_result("查询(带RAG)", False, str(e))
    
    async def test_cors_headers(self, session: aiohttp.ClientSession):
        """测试CORS配置"""
        print(f"\n{Fore.CYAN}=== 测试CORS配置 ==={Style.RESET_ALL}")
        
        try:
            # 发送OPTIONS请求
            async with session.options(f"{LOCAL_API_URL}/documents") as response:
                headers = response.headers
                has_cors = 'Access-Control-Allow-Origin' in headers
                allow_methods = headers.get('Access-Control-Allow-Methods', '')
                
                self.log_result(
                    "CORS预检请求",
                    has_cors,
                    f"允许方法: {allow_methods}" if has_cors else "缺少CORS头"
                )
        except Exception as e:
            self.log_result("CORS预检请求", False, str(e))
    
    async def test_frontend_api_integration(self, session: aiohttp.ClientSession):
        """测试前端与API集成"""
        print(f"\n{Fore.CYAN}=== 测试前端集成 ==={Style.RESET_ALL}")
        
        # 检查前端是否能访问
        try:
            async with session.get(f"{LOCAL_WEB_URL}") as response:
                if response.status == 200:
                    content = await response.text()
                    has_config = 'config.js' in content
                    self.log_result("前端页面访问", True, "页面加载成功")
                else:
                    self.log_result("前端页面访问", False, f"HTTP {response.status}")
        except Exception as e:
            self.log_result("前端页面访问", False, f"端口8080未开放: {e}")
    
    def print_summary(self):
        """打印测试摘要"""
        print(f"\n{Fore.MAGENTA}{'='*60}{Style.RESET_ALL}")
        print(f"{Fore.MAGENTA}测试摘要{Style.RESET_ALL}")
        print(f"{Fore.MAGENTA}{'='*60}{Style.RESET_ALL}")
        
        success_rate = (self.passed_tests / self.total_tests * 100) if self.total_tests > 0 else 0
        
        print(f"总测试数: {self.total_tests}")
        print(f"{Fore.GREEN}通过: {self.passed_tests}{Style.RESET_ALL}")
        print(f"{Fore.RED}失败: {self.failed_tests}{Style.RESET_ALL}")
        print(f"成功率: {success_rate:.1f}%")
        
        if self.failed_tests > 0:
            print(f"\n{Fore.YELLOW}失败的测试:{Style.RESET_ALL}")
            for result in self.results:
                if not result['success']:
                    print(f"  - {result['test']}: {result['details']}")
        
        # 保存结果
        with open('local_api_test_results.json', 'w', encoding='utf-8') as f:
            json.dump(self.results, f, ensure_ascii=False, indent=2)
        print(f"\n详细结果已保存到: local_api_test_results.json")
    
    async def run_all_tests(self):
        """运行所有测试"""
        print(f"{Fore.BLUE}{'='*60}{Style.RESET_ALL}")
        print(f"{Fore.BLUE}本地API服务器测试{Style.RESET_ALL}")
        print(f"{Fore.BLUE}{'='*60}{Style.RESET_ALL}")
        print(f"API URL: {LOCAL_API_URL}")
        print(f"Web URL: {LOCAL_WEB_URL}")
        print(f"开始时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        async with aiohttp.ClientSession() as session:
            await self.test_health_check(session)
            await self.test_document_endpoints(session)
            await self.test_query_endpoint(session)
            await self.test_cors_headers(session)
            await self.test_frontend_api_integration(session)
        
        self.print_summary()


async def main():
    """主函数"""
    tester = LocalAPITester()
    await tester.run_all_tests()


if __name__ == "__main__":
    asyncio.run(main())