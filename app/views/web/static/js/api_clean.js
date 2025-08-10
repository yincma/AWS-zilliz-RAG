// 清理版API客户端 - 修复双斜杠和端点问题
class RAGApiClient {
    constructor() {
        // 根据环境设置基础URL（确保没有尾部斜杠）
        if (window.location.hostname === 'localhost') {
            this.baseUrl = 'http://localhost:8000';
        } else {
            // 生产环境 - 使用API Gateway URL（去掉尾部斜杠）
            this.baseUrl = 'https://gbgn92f6v9.execute-api.us-east-1.amazonaws.com/prod';
        }
        
        console.log('API Client initialized with baseUrl:', this.baseUrl);
    }

    // 构建URL的辅助方法（防止双斜杠）
    buildUrl(path) {
        // 确保path以斜杠开头
        if (!path.startsWith('/')) {
            path = '/' + path;
        }
        return this.baseUrl + path;
    }

    // 健康检查
    async checkHealth() {
        try {
            const url = this.buildUrl('/health');
            const response = await fetch(url, {
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
            const url = this.buildUrl('/query');
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
            
            const data = await response.json();
            console.log('Query response received:', data);
            return data;
        } catch (error) {
            console.error('Query failed:', error);
            throw error;
        }
    }

    // 文档摄入
    async ingestDocuments(filePaths) {
        try {
            const url = this.buildUrl('/documents');
            console.log('Ingesting documents at:', url);
            
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

    // 向量搜索
    async search(query, topK = 10) {
        try {
            const url = this.buildUrl('/search');
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
                // 如果搜索端点不存在，使用查询端点
                return this.query(query, topK, true);
            }
            
            return await response.json();
        } catch (error) {
            console.error('Search failed, falling back to query:', error);
            // 降级到查询端点
            return this.query(query, topK, true);
        }
    }

    // 获取统计信息
    async getStats() {
        try {
            const url = this.buildUrl('/stats');
            const response = await fetch(url, {
                headers: {
                    'Accept': 'application/json'
                }
            });
            
            if (!response.ok) {
                // 返回默认统计信息
                console.log('Stats endpoint not available, using defaults');
                return {
                    documents: 0,
                    vectors: 0,
                    dimension: 1536,
                    collection: 'rag_collection'
                };
            }
            
            return await response.json();
        } catch (error) {
            console.log('Stats endpoint error, using defaults');
            // 返回默认值而不是抛出错误
            return {
                documents: 0,
                vectors: 0,
                dimension: 1536,
                collection: 'rag_collection'
            };
        }
    }

    // 列出文档
    async listDocuments() {
        try {
            const url = this.buildUrl('/documents');
            const response = await fetch(url, {
                method: 'GET',
                headers: {
                    'Accept': 'application/json'
                }
            });
            
            if (!response.ok) {
                console.log('Documents endpoint not available');
                return { documents: [] };
            }
            
            return await response.json();
        } catch (error) {
            console.log('Documents endpoint error');
            return { documents: [] };
        }
    }

    // 删除文档
    async deleteDocument(filename) {
        try {
            const url = this.buildUrl(`/documents/${filename}`);
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
            console.error('Delete document failed:', error);
            throw error;
        }
    }

    // 上传文档
    async uploadDocument(uploadData) {
        try {
            const url = this.buildUrl('/documents');
            const response = await fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json'
                },
                body: JSON.stringify({
                    file_paths: [uploadData.filename],
                    content: uploadData.content
                })
            });
            
            if (response.ok) {
                try {
                    const result = await response.json();
                    return {
                        status: 'success',
                        data: result
                    };
                } catch (jsonError) {
                    return {
                        status: 'success',
                        data: { message: 'Upload successful' }
                    };
                }
            } else {
                const errorText = await response.text();
                throw new Error(`Upload failed: ${response.status} - ${errorText}`);
            }
        } catch (error) {
            console.error('Document upload failed:', error);
            return {
                status: 'error',
                error: error.message
            };
        }
    }

    // 清空集合
    async clearCollection() {
        try {
            const url = this.buildUrl('/collection/clear');
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
            console.error('Clear collection failed:', error);
            throw error;
        }
    }

    // 调试方法
    getConfiguration() {
        return {
            baseUrl: this.baseUrl,
            endpoints: {
                query: this.buildUrl('/query'),
                health: this.buildUrl('/health'),
                documents: this.buildUrl('/documents'),
                stats: this.buildUrl('/stats'),
                search: this.buildUrl('/search')
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

// 在控制台输出配置信息，方便调试
console.log('RAG API Client Configuration:', apiClient.getConfiguration());