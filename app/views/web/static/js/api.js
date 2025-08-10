// 自动生成的API配置文件
// 生成时间: 2025-08-11T00:38:44.897781
// 注意: 此文件由部署脚本自动生成，请勿手动修改

class RAGApiClient {
    constructor() {
        // 根据环境设置基础URL
        if (window.location.hostname === 'localhost') {
            this.baseUrl = 'http://localhost:8000';
        } else {
            // 生产环境 - 使用API Gateway URL
            this.baseUrl = 'https://lgauddjrh2.execute-api.us-east-1.amazonaws.com/prod';
        }
        
        console.log('API Client initialized with baseUrl:', this.baseUrl);
    }

    // 健康检查
    async checkHealth() {
        try {
            const response = await fetch(`${this.baseUrl}/health`, {
                method: 'GET',
                headers: {
                    'Accept': 'application/json'
                }
            });
            
            if (response.ok) {
                return await response.json();
            }
            return { status: 'error', message: `HTTP ${response.status}` };
        } catch (error) {
            console.error('Health check failed:', error);
            return { status: 'error', message: error.message };
        }
    }

    // 查询
    async query(question, topK = 5, useRag = true) {
        try {
            const url = `${this.baseUrl}/query`;
            console.log('Sending query to:', url);
            
            const response = await fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json'
                },
                body: JSON.stringify({
                    query: question,
                    top_k: topK,
                    use_rag: useRag
                })
            });
            
            if (!response.ok) {
                const errorText = await response.text();
                throw new Error(`HTTP ${response.status}: ${errorText}`);
            }
            
            return await response.json();
        } catch (error) {
            console.error('Query failed:', error);
            throw error;
        }
    }

    // 文档管理
    async ingestDocuments(filePaths) {
        try {
            const url = `${this.baseUrl}/documents`;
            const response = await fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json'
                },
                body: JSON.stringify({
                    file_paths: filePaths
                })
            });
            
            if (!response.ok) {
                const errorText = await response.text();
                throw new Error(`HTTP ${response.status}: ${errorText}`);
            }
            
            return await response.json();
        } catch (error) {
            console.error('Document ingestion failed:', error);
            throw error;
        }
    }

    async listDocuments() {
        try {
            const url = `${this.baseUrl}/documents`;
            const response = await fetch(url, {
                method: 'GET',
                headers: {
                    'Accept': 'application/json'
                }
            });
            
            if (!response.ok) {
                return { documents: [] };
            }
            
            return await response.json();
        } catch (error) {
            console.log('Documents endpoint not available');
            return { documents: [] };
        }
    }

    // 统计信息
    async getStats() {
        try {
            const url = `${this.baseUrl}/stats`;
            const response = await fetch(url, {
                headers: {
                    'Accept': 'application/json'
                }
            });
            
            if (!response.ok) {
                return {
                    documents: 0,
                    vectors: 0,
                    dimension: 1536,
                    collection: 'rag_collection'
                };
            }
            
            return await response.json();
        } catch (error) {
            console.log('Stats endpoint not available, using defaults');
            return {
                documents: 0,
                vectors: 0,
                dimension: 1536,
                collection: 'rag_collection'
            };
        }
    }

    // 搜索
    async search(query, topK = 10) {
        try {
            const url = `${this.baseUrl}/search`;
            const response = await fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json'
                },
                body: JSON.stringify({
                    query: query,
                    top_k: topK
                })
            });
            
            if (!response.ok) {
                // 降级到查询端点
                return this.query(query, topK, true);
            }
            
            return await response.json();
        } catch (error) {
            console.error('Search failed, falling back to query:', error);
            return this.query(query, topK, true);
        }
    }
    
    // 文档上传
    async uploadDocument(uploadData) {
        try {
            const url = `${this.baseUrl}/documents`;
            console.log('Uploading document to:', url);
            
            // 准备请求体
            const requestBody = {
                content: uploadData.content,
                filename: uploadData.filename,
                content_type: uploadData.content_type || 'text/plain'
            };
            
            // 如果内容是base64编码的（对于二进制文件）
            if (uploadData.content && uploadData.content.startsWith('data:')) {
                const base64Content = uploadData.content.split(',')[1];
                requestBody.file_content = base64Content;
                requestBody.content = ''; // 清空content字段
            }
            
            const response = await fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json'
                },
                body: JSON.stringify(requestBody)
            });
            
            if (!response.ok) {
                const errorText = await response.text();
                throw new Error(`HTTP ${response.status}: ${errorText}`);
            }
            
            return await response.json();
        } catch (error) {
            console.error('Document upload failed:', error);
            throw error;
        }
    }
    
    // 删除文档
    async deleteDocument(filename) {
        try {
            const url = `${this.baseUrl}/documents/${encodeURIComponent(filename)}`;
            const response = await fetch(url, {
                method: 'DELETE',
                headers: {
                    'Accept': 'application/json'
                }
            });
            
            if (!response.ok) {
                const errorText = await response.text();
                throw new Error(`HTTP ${response.status}: ${errorText}`);
            }
            
            return await response.json();
        } catch (error) {
            console.error('Document deletion failed:', error);
            throw error;
        }
    }

    // 其他方法...
    
    getConfiguration() {
        return {
            baseUrl: this.baseUrl,
            endpoints: {
                query: `${this.baseUrl}/query`,
                health: `${this.baseUrl}/health`,
                documents: `${this.baseUrl}/documents`,
                stats: `${this.baseUrl}/stats`,
                search: `${this.baseUrl}/search`
            },
            environment: {
                hostname: window.location.hostname,
                origin: window.location.origin,
                protocol: window.location.protocol
            }
        };
    }
}

// 创建全局API客户端实例
const apiClient = new RAGApiClient();

// 配置信息
console.log('RAG API Client Configuration:', apiClient.getConfiguration());
