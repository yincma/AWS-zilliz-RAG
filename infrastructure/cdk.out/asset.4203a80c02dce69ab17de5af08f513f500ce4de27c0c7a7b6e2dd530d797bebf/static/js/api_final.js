// 最终修复版API客户端 - 使用正确的API路径
class RAGApiClient {
    constructor() {
        // 根据环境设置基础URL
        if (window.location.hostname === 'localhost') {
            this.baseUrl = 'http://localhost:8000';
        } else {
            // 生产环境 - 使用API Gateway URL（注意：没有尾部斜杠）
            this.baseUrl = 'https://gbgn92f6v9.execute-api.us-east-1.amazonaws.com/prod';
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

    // 查询 - 使用正确的路径 /query
    async query(question, topK = 5, useRag = true) {
        try {
            // 使用简单路径 /query，而不是 /api/v1/query
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
            
            const data = await response.json();
            console.log('Query response received:', data);
            return data;
        } catch (error) {
            console.error('Query failed:', error);
            throw error;
        }
    }

    // 摄入文档 - 使用正确的路径 /documents
    async ingestDocuments(filePaths) {
        try {
            const url = `${this.baseUrl}/documents`;
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

    // 向量搜索 - 使用可能存在的路径
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

    // 获取统计信息 - 返回默认值如果端点不存在
    async getStats() {
        try {
            const url = `${this.baseUrl}/stats`;
            const response = await fetch(url, {
                headers: {
                    'Accept': 'application/json'
                }
            });
            
            if (!response.ok) {
                // 返回默认统计信息
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
            // 返回默认值而不是抛出错误
            return {
                documents: 0,
                vectors: 0,
                dimension: 1536,
                collection: 'rag_collection'
            };
        }
    }

    // 列出文档 - 返回空列表如果端点不存在
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

    // 删除文档
    async deleteDocument(filename) {
        try {
            const url = `${this.baseUrl}/documents/${filename}`;
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
            const url = `${this.baseUrl}/documents`;
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
            const url = `${this.baseUrl}/collection/clear`;
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
                query: `${this.baseUrl}/query`,
                health: `${this.baseUrl}/health`,
                documents: `${this.baseUrl}/documents`,
                stats: `${this.baseUrl}/stats`
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