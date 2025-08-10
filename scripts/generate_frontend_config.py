#!/usr/bin/env python3
"""
生成前端配置文件，自动从CDK输出获取API URL
"""

import json
import os
import sys
import boto3
from datetime import datetime


def get_stack_outputs(stack_name):
    """从CloudFormation栈获取输出"""
    try:
        cf = boto3.client('cloudformation', region_name='us-east-1')
        response = cf.describe_stacks(StackName=stack_name)
        
        outputs = {}
        for output in response['Stacks'][0].get('Outputs', []):
            outputs[output['OutputKey']] = output['OutputValue']
        
        return outputs
    except Exception as e:
        print(f"❌ 获取栈输出失败: {e}")
        return None


def generate_api_config(api_url, cloudfront_url=None):
    """生成前端API配置"""
    
    # 确保API URL没有尾部斜杠
    api_url = api_url.rstrip('/')
    
    config = f"""// 自动生成的API配置文件
// 生成时间: {datetime.now().isoformat()}
// 注意: 此文件由部署脚本自动生成，请勿手动修改

class RAGApiClient {{
    constructor() {{
        // 根据环境设置基础URL
        if (window.location.hostname === 'localhost') {{
            this.baseUrl = 'http://localhost:8000';
        }} else {{
            // 生产环境 - 使用API Gateway URL
            this.baseUrl = '{api_url}';
        }}
        
        console.log('API Client initialized with baseUrl:', this.baseUrl);
    }}

    // 健康检查
    async checkHealth() {{
        try {{
            const response = await fetch(`${{this.baseUrl}}/health`, {{
                method: 'GET',
                headers: {{
                    'Accept': 'application/json'
                }}
            }});
            
            if (response.ok) {{
                return await response.json();
            }}
            return {{ status: 'error', message: `HTTP ${{response.status}}` }};
        }} catch (error) {{
            console.error('Health check failed:', error);
            return {{ status: 'error', message: error.message }};
        }}
    }}

    // 查询
    async query(question, topK = 5, useRag = true) {{
        try {{
            const url = `${{this.baseUrl}}/query`;
            console.log('Sending query to:', url);
            
            const response = await fetch(url, {{
                method: 'POST',
                headers: {{
                    'Content-Type': 'application/json',
                    'Accept': 'application/json'
                }},
                body: JSON.stringify({{
                    query: question,
                    top_k: topK,
                    use_rag: useRag
                }})
            }});
            
            if (!response.ok) {{
                const errorText = await response.text();
                throw new Error(`HTTP ${{response.status}}: ${{errorText}}`);
            }}
            
            return await response.json();
        }} catch (error) {{
            console.error('Query failed:', error);
            throw error;
        }}
    }}

    // 文档管理
    async ingestDocuments(filePaths) {{
        try {{
            const url = `${{this.baseUrl}}/documents`;
            const response = await fetch(url, {{
                method: 'POST',
                headers: {{
                    'Content-Type': 'application/json',
                    'Accept': 'application/json'
                }},
                body: JSON.stringify({{
                    file_paths: filePaths
                }})
            }});
            
            if (!response.ok) {{
                const errorText = await response.text();
                throw new Error(`HTTP ${{response.status}}: ${{errorText}}`);
            }}
            
            return await response.json();
        }} catch (error) {{
            console.error('Document ingestion failed:', error);
            throw error;
        }}
    }}

    async listDocuments() {{
        try {{
            const url = `${{this.baseUrl}}/documents`;
            const response = await fetch(url, {{
                method: 'GET',
                headers: {{
                    'Accept': 'application/json'
                }}
            }});
            
            if (!response.ok) {{
                return {{ documents: [] }};
            }}
            
            return await response.json();
        }} catch (error) {{
            console.log('Documents endpoint not available');
            return {{ documents: [] }};
        }}
    }}

    // 统计信息
    async getStats() {{
        try {{
            const url = `${{this.baseUrl}}/stats`;
            const response = await fetch(url, {{
                headers: {{
                    'Accept': 'application/json'
                }}
            }});
            
            if (!response.ok) {{
                return {{
                    documents: 0,
                    vectors: 0,
                    dimension: 1536,
                    collection: 'rag_collection'
                }};
            }}
            
            return await response.json();
        }} catch (error) {{
            console.log('Stats endpoint not available, using defaults');
            return {{
                documents: 0,
                vectors: 0,
                dimension: 1536,
                collection: 'rag_collection'
            }};
        }}
    }}

    // 搜索
    async search(query, topK = 10) {{
        try {{
            const url = `${{this.baseUrl}}/search`;
            const response = await fetch(url, {{
                method: 'POST',
                headers: {{
                    'Content-Type': 'application/json',
                    'Accept': 'application/json'
                }},
                body: JSON.stringify({{
                    query: query,
                    top_k: topK
                }})
            }});
            
            if (!response.ok) {{
                // 降级到查询端点
                return this.query(query, topK, true);
            }}
            
            return await response.json();
        }} catch (error) {{
            console.error('Search failed, falling back to query:', error);
            return this.query(query, topK, true);
        }}
    }}
    
    // 文档上传
    async uploadDocument(uploadData) {{
        try {{
            const url = `${{this.baseUrl}}/documents`;
            console.log('Uploading document to:', url);
            
            // 准备请求体
            const requestBody = {{
                content: uploadData.content,
                filename: uploadData.filename,
                content_type: uploadData.content_type || 'text/plain'
            }};
            
            // 如果内容是base64编码的（对于二进制文件）
            if (uploadData.content && uploadData.content.startsWith('data:')) {{
                const base64Content = uploadData.content.split(',')[1];
                requestBody.file_content = base64Content;
                requestBody.content = ''; // 清空content字段
            }}
            
            const response = await fetch(url, {{
                method: 'POST',
                headers: {{
                    'Content-Type': 'application/json',
                    'Accept': 'application/json'
                }},
                body: JSON.stringify(requestBody)
            }});
            
            if (!response.ok) {{
                const errorText = await response.text();
                throw new Error(`HTTP ${{response.status}}: ${{errorText}}`);
            }}
            
            return await response.json();
        }} catch (error) {{
            console.error('Document upload failed:', error);
            throw error;
        }}
    }}
    
    // 删除文档
    async deleteDocument(filename) {{
        try {{
            const url = `${{this.baseUrl}}/documents/${{encodeURIComponent(filename)}}`;
            const response = await fetch(url, {{
                method: 'DELETE',
                headers: {{
                    'Accept': 'application/json'
                }}
            }});
            
            if (!response.ok) {{
                const errorText = await response.text();
                throw new Error(`HTTP ${{response.status}}: ${{errorText}}`);
            }}
            
            return await response.json();
        }} catch (error) {{
            console.error('Document deletion failed:', error);
            throw error;
        }}
    }}

    // 其他方法...
    
    getConfiguration() {{
        return {{
            baseUrl: this.baseUrl,
            endpoints: {{
                query: `${{this.baseUrl}}/query`,
                health: `${{this.baseUrl}}/health`,
                documents: `${{this.baseUrl}}/documents`,
                stats: `${{this.baseUrl}}/stats`,
                search: `${{this.baseUrl}}/search`
            }},
            environment: {{
                hostname: window.location.hostname,
                origin: window.location.origin,
                protocol: window.location.protocol
            }}
        }};
    }}
}}

// 创建全局API客户端实例
const apiClient = new RAGApiClient();

// 配置信息
console.log('RAG API Client Configuration:', apiClient.getConfiguration());
"""
    
    return config


def main():
    """主函数"""
    
    # 获取环境变量或使用默认值
    stage = os.environ.get('STAGE', 'prod')
    api_stack_name = f"RAG-API-{stage}"
    web_stack_name = f"RAG-Web-{stage}"
    
    print(f"📋 生成前端配置...")
    print(f"  API栈: {api_stack_name}")
    print(f"  Web栈: {web_stack_name}")
    
    # 获取API栈输出
    api_outputs = get_stack_outputs(api_stack_name)
    if not api_outputs:
        print("❌ 无法获取API栈输出")
        sys.exit(1)
    
    api_url = api_outputs.get('ApiUrl', '').rstrip('/')
    if not api_url:
        print("❌ API URL未找到")
        sys.exit(1)
    
    print(f"✅ API URL: {api_url}")
    
    # 获取Web栈输出（可选）
    web_outputs = get_stack_outputs(web_stack_name)
    cloudfront_url = None
    if web_outputs:
        cloudfront_url = web_outputs.get('CloudFrontURL')
        print(f"✅ CloudFront URL: {cloudfront_url}")
    
    # 生成配置文件
    config = generate_api_config(api_url, cloudfront_url)
    
    # 保存配置文件
    output_path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        'app', 'views', 'web', 'static', 'js', 'api.js'
    )
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(config)
    
    print(f"✅ 配置文件已生成: {output_path}")
    
    # 生成元数据文件
    metadata = {
        "generated_at": datetime.now().isoformat(),
        "api_url": api_url,
        "cloudfront_url": cloudfront_url,
        "stage": stage
    }
    
    metadata_path = output_path.replace('.js', '.meta.json')
    with open(metadata_path, 'w') as f:
        json.dump(metadata, f, indent=2)
    
    print(f"✅ 元数据文件已生成: {metadata_path}")
    
    # 生成config.json文件（供前端动态加载）
    config_path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        'app', 'views', 'web', 'config.json'
    )
    
    config_data = {
        "apiUrl": api_url,
        "region": os.environ.get('AWS_REGION', 'us-east-1'),
        "stage": stage,
        "updated": datetime.now().isoformat()
    }
    
    with open(config_path, 'w') as f:
        json.dump(config_data, f, indent=2)
    
    print(f"✅ 配置文件已生成: {config_path}")


if __name__ == "__main__":
    main()