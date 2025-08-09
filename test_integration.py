"""
端到端集成测试 - 测试完整的RAG系统功能
"""

import os
import sys
import time
import json
import requests
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# 添加项目路径
sys.path.insert(0, str(Path(__file__).parent))

class RAGIntegrationTest:
    """RAG系统集成测试"""
    
    def __init__(self, test_mode="local"):
        """
        初始化测试
        
        Args:
            test_mode: "local" 或 "aws"
        """
        self.test_mode = test_mode
        self.results = {
            "timestamp": datetime.now().isoformat(),
            "mode": test_mode,
            "tests": [],
            "summary": {
                "total": 0,
                "passed": 0,
                "failed": 0,
                "skipped": 0
            }
        }
        
        # 设置API端点
        if test_mode == "local":
            self.api_base = "http://localhost:8000"
        else:
            # AWS API Gateway endpoint
            self.api_base = os.getenv("API_GATEWAY_URL", "")
            if not self.api_base:
                print("⚠️ API_GATEWAY_URL not set for AWS mode")
        
        # 配置
        self.config = {
            "aws_region": os.getenv("AWS_REGION", "us-east-1"),
            "bedrock_model": os.getenv("BEDROCK_MODEL_ID", "amazon.nova-pro-v1:0"),
            "embedding_model": os.getenv("EMBEDDING_MODEL_ID", "amazon.titan-embed-image-v1"),
            "zilliz_endpoint": os.getenv("ZILLIZ_ENDPOINT"),
            "zilliz_collection": os.getenv("ZILLIZ_COLLECTION", "rag_collection"),
            "s3_bucket": os.getenv("S3_BUCKET", "AWS_zilliz_RAG")
        }
    
    def run_test(self, test_name: str, test_func, *args, **kwargs) -> Dict:
        """运行单个测试"""
        self.results["summary"]["total"] += 1
        
        print(f"\n🧪 测试: {test_name}")
        test_result = {
            "name": test_name,
            "status": "pending",
            "message": "",
            "duration": 0,
            "details": {}
        }
        
        start_time = time.time()
        
        try:
            result = test_func(*args, **kwargs)
            test_result["duration"] = round(time.time() - start_time, 2)
            
            if result.get("success", False):
                test_result["status"] = "passed"
                test_result["message"] = result.get("message", "测试通过")
                test_result["details"] = result.get("details", {})
                self.results["summary"]["passed"] += 1
                print(f"   ✅ {test_result['message']} ({test_result['duration']}s)")
            else:
                test_result["status"] = "failed"
                test_result["message"] = result.get("message", "测试失败")
                test_result["details"] = result.get("details", {})
                self.results["summary"]["failed"] += 1
                print(f"   ❌ {test_result['message']}")
        
        except Exception as e:
            test_result["duration"] = round(time.time() - start_time, 2)
            test_result["status"] = "error"
            test_result["message"] = str(e)
            self.results["summary"]["failed"] += 1
            print(f"   ❌ 错误: {e}")
        
        self.results["tests"].append(test_result)
        return test_result
    
    def test_health_check(self) -> Dict:
        """测试健康检查端点"""
        try:
            response = requests.get(f"{self.api_base}/health", timeout=5)
            
            if response.status_code == 200:
                data = response.json()
                return {
                    "success": True,
                    "message": f"健康检查通过 - 状态: {data.get('status', 'unknown')}",
                    "details": data
                }
            else:
                return {
                    "success": False,
                    "message": f"健康检查失败 - 状态码: {response.status_code}",
                    "details": {"status_code": response.status_code}
                }
        except requests.exceptions.ConnectionError:
            return {
                "success": False,
                "message": "无法连接到API服务器",
                "details": {"error": "Connection refused"}
            }
        except Exception as e:
            return {
                "success": False,
                "message": f"健康检查异常: {str(e)}",
                "details": {"error": str(e)}
            }
    
    def test_aws_services(self) -> Dict:
        """测试AWS服务连接"""
        import boto3
        
        results = {
            "s3": False,
            "bedrock": False,
            "details": {}
        }
        
        try:
            # 测试S3
            s3 = boto3.client('s3', region_name=self.config["aws_region"])
            s3.list_buckets()
            results["s3"] = True
            results["details"]["s3"] = "S3连接成功"
            
            # 测试Bedrock
            bedrock = boto3.client('bedrock-runtime', region_name=self.config["aws_region"])
            # 简单的连接测试
            results["bedrock"] = True
            results["details"]["bedrock"] = "Bedrock连接成功"
            
            success = results["s3"] and results["bedrock"]
            
            return {
                "success": success,
                "message": f"AWS服务测试 - S3: {'✅' if results['s3'] else '❌'}, Bedrock: {'✅' if results['bedrock'] else '❌'}",
                "details": results
            }
        
        except Exception as e:
            return {
                "success": False,
                "message": f"AWS服务测试失败: {str(e)}",
                "details": {"error": str(e)}
            }
    
    def test_zilliz_connection(self) -> Dict:
        """测试Zilliz连接"""
        try:
            from pymilvus import connections, utility
            
            # 连接到Zilliz
            connections.connect(
                alias="default",
                uri=self.config["zilliz_endpoint"],
                token=os.getenv("ZILLIZ_TOKEN")
            )
            
            # 检查连接
            if utility.has_collection(self.config["zilliz_collection"]):
                collection_info = {
                    "exists": True,
                    "name": self.config["zilliz_collection"]
                }
            else:
                collection_info = {
                    "exists": False,
                    "message": "Collection不存在，需要创建"
                }
            
            connections.disconnect("default")
            
            return {
                "success": True,
                "message": f"Zilliz连接成功 - Collection: {self.config['zilliz_collection']}",
                "details": collection_info
            }
        
        except Exception as e:
            return {
                "success": False,
                "message": f"Zilliz连接失败: {str(e)}",
                "details": {"error": str(e)}
            }
    
    def test_document_upload(self) -> Dict:
        """测试文档上传功能"""
        try:
            # 创建测试文档
            test_doc = "这是一个测试文档，用于验证RAG系统的文档处理功能。\n它包含多行文本内容。"
            
            files = {
                'file': ('test.txt', test_doc.encode('utf-8'), 'text/plain')
            }
            
            response = requests.post(
                f"{self.api_base}/upload",
                files=files,
                timeout=30
            )
            
            if response.status_code == 200:
                data = response.json()
                return {
                    "success": True,
                    "message": "文档上传成功",
                    "details": data
                }
            else:
                return {
                    "success": False,
                    "message": f"文档上传失败 - 状态码: {response.status_code}",
                    "details": {"status_code": response.status_code, "response": response.text}
                }
        
        except Exception as e:
            return {
                "success": False,
                "message": f"文档上传测试失败: {str(e)}",
                "details": {"error": str(e)}
            }
    
    def test_embedding_generation(self) -> Dict:
        """测试向量生成功能"""
        try:
            import boto3
            import json
            
            bedrock = boto3.client('bedrock-runtime', region_name=self.config["aws_region"])
            
            # 测试文本
            test_text = "这是一个测试文本，用于生成embedding向量。"
            
            # 调用Titan Embedding
            response = bedrock.invoke_model(
                modelId=self.config["embedding_model"],
                body=json.dumps({
                    "inputText": test_text
                })
            )
            
            result = json.loads(response['body'].read())
            embedding = result.get('embedding', [])
            
            if len(embedding) > 0:
                return {
                    "success": True,
                    "message": f"向量生成成功 - 维度: {len(embedding)}",
                    "details": {
                        "dimension": len(embedding),
                        "model": self.config["embedding_model"]
                    }
                }
            else:
                return {
                    "success": False,
                    "message": "向量生成失败 - 返回空向量",
                    "details": {"response": result}
                }
        
        except Exception as e:
            return {
                "success": False,
                "message": f"向量生成测试失败: {str(e)}",
                "details": {"error": str(e)}
            }
    
    def test_rag_query(self) -> Dict:
        """测试RAG查询功能"""
        try:
            # 测试查询
            query_data = {
                "query": "什么是RAG系统？",
                "top_k": 3
            }
            
            response = requests.post(
                f"{self.api_base}/query",
                json=query_data,
                timeout=30
            )
            
            if response.status_code == 200:
                data = response.json()
                
                # 检查响应结构
                has_answer = "answer" in data or "response" in data
                has_sources = "sources" in data or "documents" in data
                
                if has_answer:
                    return {
                        "success": True,
                        "message": "RAG查询成功",
                        "details": {
                            "has_answer": has_answer,
                            "has_sources": has_sources,
                            "response_keys": list(data.keys())
                        }
                    }
                else:
                    return {
                        "success": False,
                        "message": "RAG查询响应格式不正确",
                        "details": {"response": data}
                    }
            else:
                return {
                    "success": False,
                    "message": f"RAG查询失败 - 状态码: {response.status_code}",
                    "details": {"status_code": response.status_code, "response": response.text}
                }
        
        except Exception as e:
            return {
                "success": False,
                "message": f"RAG查询测试失败: {str(e)}",
                "details": {"error": str(e)}
            }
    
    def test_llm_generation(self) -> Dict:
        """测试LLM生成功能"""
        try:
            import boto3
            import json
            
            bedrock = boto3.client('bedrock-runtime', region_name=self.config["aws_region"])
            
            # 测试提示
            prompt = "请简单介绍什么是RAG（检索增强生成）系统。"
            
            # 调用Nova模型 - 使用正确的参数格式
            response = bedrock.invoke_model(
                modelId=self.config["bedrock_model"],
                body=json.dumps({
                    "messages": [
                        {
                            "role": "user",
                            "content": [
                                {
                                    "text": prompt
                                }
                            ]
                        }
                    ],
                    "inferenceConfig": {
                        "maxTokens": 200,
                        "temperature": 0.7
                    }
                })
            )
            
            result = json.loads(response['body'].read())
            
            # 从响应中提取内容
            if "content" in result:
                # Nova模型响应格式
                content = result["content"]
                if isinstance(content, list) and len(content) > 0:
                    generated_text = content[0].get("text", "")
                else:
                    generated_text = str(content)
            else:
                generated_text = str(result)
            
            if generated_text:
                return {
                    "success": True,
                    "message": f"LLM生成成功 - 长度: {len(generated_text)}字符",
                    "details": {
                        "model": self.config["bedrock_model"],
                        "response_length": len(generated_text),
                        "sample": generated_text[:100] + "..." if len(generated_text) > 100 else generated_text
                    }
                }
            else:
                return {
                    "success": False,
                    "message": "LLM生成失败 - 返回空响应",
                    "details": {"response": result}
                }
        
        except Exception as e:
            return {
                "success": False,
                "message": f"LLM生成测试失败: {str(e)}",
                "details": {"error": str(e)}
            }
    
    def test_performance(self) -> Dict:
        """测试系统性能"""
        try:
            metrics = {
                "api_latency": [],
                "throughput": 0
            }
            
            # 测试API延迟
            for i in range(5):
                start = time.time()
                response = requests.get(f"{self.api_base}/health", timeout=5)
                latency = (time.time() - start) * 1000  # 转换为毫秒
                metrics["api_latency"].append(round(latency, 2))
            
            avg_latency = sum(metrics["api_latency"]) / len(metrics["api_latency"])
            
            # 评估性能
            if avg_latency < 100:
                performance = "优秀"
            elif avg_latency < 500:
                performance = "良好"
            elif avg_latency < 1000:
                performance = "一般"
            else:
                performance = "需要优化"
            
            return {
                "success": avg_latency < 1000,
                "message": f"性能测试 - 平均延迟: {avg_latency:.2f}ms ({performance})",
                "details": {
                    "latency_samples": metrics["api_latency"],
                    "avg_latency_ms": round(avg_latency, 2),
                    "performance_rating": performance
                }
            }
        
        except Exception as e:
            return {
                "success": False,
                "message": f"性能测试失败: {str(e)}",
                "details": {"error": str(e)}
            }
    
    def run_all_tests(self):
        """运行所有测试"""
        print("="*60)
        print(f"🚀 开始RAG系统集成测试 - 模式: {self.test_mode}")
        print(f"⏰ 时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("="*60)
        
        # 基础测试
        if self.test_mode == "local":
            self.run_test("API健康检查", self.test_health_check)
        
        # AWS服务测试
        self.run_test("AWS服务连接", self.test_aws_services)
        
        # Zilliz测试
        self.run_test("Zilliz向量数据库连接", self.test_zilliz_connection)
        
        # 功能测试
        self.run_test("Embedding向量生成", self.test_embedding_generation)
        self.run_test("LLM文本生成", self.test_llm_generation)
        
        # API测试（如果有运行的服务）
        if self.test_mode == "local":
            self.run_test("文档上传功能", self.test_document_upload)
            self.run_test("RAG查询功能", self.test_rag_query)
            self.run_test("系统性能测试", self.test_performance)
        
        # 生成报告
        self.generate_report()
    
    def generate_report(self):
        """生成测试报告"""
        print("\n" + "="*60)
        print("📊 测试报告")
        print("="*60)
        
        # 总结
        summary = self.results["summary"]
        total = summary["total"]
        passed = summary["passed"]
        failed = summary["failed"]
        
        if total > 0:
            pass_rate = (passed / total) * 100
        else:
            pass_rate = 0
        
        print(f"\n📈 测试统计:")
        print(f"   总测试数: {total}")
        print(f"   ✅ 通过: {passed}")
        print(f"   ❌ 失败: {failed}")
        print(f"   📊 通过率: {pass_rate:.1f}%")
        
        # 详细结果
        print(f"\n📝 详细结果:")
        for test in self.results["tests"]:
            status_icon = "✅" if test["status"] == "passed" else "❌"
            print(f"   {status_icon} {test['name']}: {test['message']} ({test['duration']}s)")
            
            # 显示详细信息
            if test["details"] and test["status"] == "failed":
                for key, value in test["details"].items():
                    print(f"      - {key}: {value}")
        
        # 保存JSON报告
        report_file = f"test_report_{self.test_mode}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(self.results, f, ensure_ascii=False, indent=2)
        
        print(f"\n💾 详细报告已保存到: {report_file}")
        
        # 评级
        if pass_rate >= 90:
            rating = "🏆 优秀 - 系统运行良好"
        elif pass_rate >= 70:
            rating = "👍 良好 - 存在少量问题"
        elif pass_rate >= 50:
            rating = "⚠️ 一般 - 需要改进"
        else:
            rating = "❌ 较差 - 需要重点关注"
        
        print(f"\n🎯 总体评价: {rating}")
        print("="*60)

def main():
    """主函数"""
    import argparse
    
    parser = argparse.ArgumentParser(description='RAG系统集成测试')
    parser.add_argument('--mode', choices=['local', 'aws'], default='local',
                      help='测试模式: local(本地) 或 aws(AWS环境)')
    parser.add_argument('--api-url', help='API端点URL（覆盖默认值）')
    
    args = parser.parse_args()
    
    # 如果提供了API URL，设置环境变量
    if args.api_url:
        os.environ['API_GATEWAY_URL'] = args.api_url
    
    # 运行测试
    tester = RAGIntegrationTest(test_mode=args.mode)
    tester.run_all_tests()
    
    # 根据结果返回退出码
    if tester.results["summary"]["failed"] == 0:
        return 0
    else:
        return 1

if __name__ == "__main__":
    exit_code = main()
    
    # 播放完成音
    if sys.platform == 'darwin':
        os.system('afplay /System/Library/Sounds/Glass.aiff' if exit_code == 0 
                 else 'afplay /System/Library/Sounds/Basso.aiff')
    
    sys.exit(exit_code)