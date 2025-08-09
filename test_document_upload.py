#!/usr/bin/env python3
"""
诊断文档上传失败问题
"""
import asyncio
import aiohttp
import json
import base64
from datetime import datetime
from colorama import init, Fore, Style

init(autoreset=True)

# API端点
API_GATEWAY_URL = "https://abbrw64qve.execute-api.us-east-1.amazonaws.com/prod"

class DocumentUploadDiagnostics:
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
                
    async def test_document_endpoints(self, session: aiohttp.ClientSession):
        """测试文档管理端点"""
        print(f"\n{Fore.CYAN}=== 测试文档管理端点 ==={Style.RESET_ALL}")
        
        # 1. 测试文档列表
        try:
            async with session.get(f"{self.api_url}/documents") as response:
                if response.status == 200:
                    data = await response.json()
                    self.log_result("GET /documents", True, 
                                  f"文档数: {data.get('count', 0)}")
                else:
                    text = await response.text()
                    self.log_result("GET /documents", False, 
                                  f"HTTP {response.status}: {text[:200]}")
        except Exception as e:
            self.log_result("GET /documents", False, f"错误: {str(e)}")
            
    async def test_simple_upload(self, session: aiohttp.ClientSession):
        """测试简单文档上传"""
        print(f"\n{Fore.CYAN}=== 测试简单文档上传 ==={Style.RESET_ALL}")
        
        # 准备测试数据
        test_content = "This is a test document for upload testing."
        test_filename = f"test_upload_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        
        upload_data = {
            "filename": test_filename,
            "content": test_content,
            "size": len(test_content),
            "type": "text/plain"
        }
        
        try:
            headers = {
                'Content-Type': 'application/json',
                'Origin': 'https://dfg648088lloi.cloudfront.net'
            }
            
            async with session.post(
                f"{self.api_url}/documents/upload",
                json=upload_data,
                headers=headers
            ) as response:
                
                response_text = await response.text()
                
                if response.status == 200:
                    try:
                        data = json.loads(response_text)
                        self.log_result("POST /documents/upload", True, 
                                      f"文件: {test_filename}",
                                      data)
                    except json.JSONDecodeError:
                        self.log_result("POST /documents/upload", True, 
                                      f"上传成功但响应不是JSON: {response_text[:100]}")
                else:
                    self.log_result("POST /documents/upload", False, 
                                  f"HTTP {response.status}: {response_text[:200]}")
                    
        except Exception as e:
            self.log_result("POST /documents/upload", False, 
                          f"异常: {str(e)}")
            
    async def test_base64_upload(self, session: aiohttp.ClientSession):
        """测试Base64编码上传"""
        print(f"\n{Fore.CYAN}=== 测试Base64编码上传 ==={Style.RESET_ALL}")
        
        # 准备Base64编码的内容
        test_content = "Base64 encoded test document"
        base64_content = base64.b64encode(test_content.encode()).decode()
        test_filename = f"test_base64_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        
        upload_data = {
            "filename": test_filename,
            "content": f"data:text/plain;base64,{base64_content}",
            "size": len(test_content),
            "type": "text/plain"
        }
        
        try:
            headers = {
                'Content-Type': 'application/json'
            }
            
            async with session.post(
                f"{self.api_url}/documents/upload",
                json=upload_data,
                headers=headers
            ) as response:
                
                if response.status == 200:
                    data = await response.json()
                    self.log_result("Base64上传", True, 
                                  f"文件: {test_filename}")
                else:
                    text = await response.text()
                    self.log_result("Base64上传", False, 
                                  f"HTTP {response.status}: {text[:200]}")
                    
        except Exception as e:
            self.log_result("Base64上传", False, f"错误: {str(e)}")
            
    async def test_lambda_function(self, session: aiohttp.ClientSession):
        """测试Lambda函数状态"""
        print(f"\n{Fore.CYAN}=== 检查Lambda函数 ==={Style.RESET_ALL}")
        
        # 测试文档统计
        try:
            stats_data = {
                "operation": "stats"
            }
            
            async with session.post(
                f"{self.api_url}/documents",
                json=stats_data
            ) as response:
                
                if response.status == 200:
                    data = await response.json()
                    self.log_result("文档统计", True,
                                  f"向量数: {data.get('data', {}).get('num_entities', 0)}")
                else:
                    text = await response.text()
                    self.log_result("文档统计", False,
                                  f"HTTP {response.status}")
                    
        except Exception as e:
            self.log_result("文档统计", False, f"错误: {str(e)}")
            
    async def test_s3_permissions(self, session: aiohttp.ClientSession):
        """测试S3权限"""
        print(f"\n{Fore.CYAN}=== 测试S3权限 ==={Style.RESET_ALL}")
        
        # 通过上传小文件测试S3权限
        test_data = {
            "filename": "permission_test.txt",
            "content": "Testing S3 permissions",
            "size": 22,
            "type": "text/plain"
        }
        
        try:
            async with session.post(
                f"{self.api_url}/documents/upload",
                json=test_data
            ) as response:
                
                if response.status == 200:
                    self.log_result("S3写入权限", True, "可以写入S3")
                elif response.status == 403:
                    self.log_result("S3写入权限", False, "权限拒绝")
                else:
                    self.log_result("S3写入权限", False, f"HTTP {response.status}")
                    
        except Exception as e:
            self.log_result("S3写入权限", False, f"错误: {str(e)}")
            
    def generate_solution(self):
        """生成解决方案"""
        print(f"\n{Fore.CYAN}=== 诊断结果和解决方案 ==={Style.RESET_ALL}")
        
        failed_tests = [r for r in self.results if not r['success']]
        
        if not failed_tests:
            print(f"{Fore.GREEN}✅ 所有测试通过！文档上传功能应该正常工作。{Style.RESET_ALL}")
            return
            
        print(f"\n{Fore.YELLOW}发现 {len(failed_tests)} 个问题：{Style.RESET_ALL}")
        
        for result in failed_tests:
            print(f"\n❌ {result['test']}")
            
            if 'upload' in result['test'].lower():
                print(f"   可能的原因：")
                print(f"   1. Lambda函数没有正确处理上传请求")
                print(f"   2. S3 bucket权限问题")
                print(f"   3. 请求格式不正确")
                print(f"   解决方案：")
                print(f"   - 检查Lambda函数日志")
                print(f"   - 验证S3 bucket存在且有写入权限")
                print(f"   - 检查IAM角色权限")
                
            elif 's3' in result['test'].lower():
                print(f"   解决方案：")
                print(f"   1. 检查S3 bucket是否存在")
                print(f"   2. 验证Lambda执行角色有S3写入权限")
                print(f"   3. 检查bucket策略")
                
    async def run_diagnostics(self):
        """运行所有诊断测试"""
        print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}文档上传功能诊断工具{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}")
        
        async with aiohttp.ClientSession() as session:
            # 运行测试
            await self.test_document_endpoints(session)
            await self.test_simple_upload(session)
            await self.test_base64_upload(session)
            await self.test_lambda_function(session)
            await self.test_s3_permissions(session)
            
        # 生成解决方案
        self.generate_solution()
        
        # 保存结果
        with open('document_upload_diagnosis.json', 'w', encoding='utf-8') as f:
            json.dump({
                'timestamp': datetime.now().isoformat(),
                'api_url': self.api_url,
                'results': self.results,
                'summary': {
                    'total_tests': len(self.results),
                    'passed': len([r for r in self.results if r['success']]),
                    'failed': len([r for r in self.results if not r['success']])
                }
            }, f, ensure_ascii=False, indent=2)
            
        print(f"\n{Fore.GREEN}诊断报告已保存到: document_upload_diagnosis.json{Style.RESET_ALL}")
        
        # 显示Lambda日志查看命令
        print(f"\n{Fore.CYAN}查看Lambda日志命令：{Style.RESET_ALL}")
        print(f"aws logs tail /aws/lambda/rag-document-handler --follow --region us-east-1")

if __name__ == "__main__":
    diagnostics = DocumentUploadDiagnostics()
    asyncio.run(diagnostics.run_diagnostics())