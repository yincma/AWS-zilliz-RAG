// 修复后的API客户端
class RAGApiClient {
    constructor(baseUrl = null) {
        // 优先使用传入的URL，否则从配置文件获取，最后使用默认值
        this.baseUrl = baseUrl || 
                      (window.RAG_CONFIG && window.RAG_CONFIG.API_URL) || 
                      'http://localhost:8000';
    }

    // 健康检查
    async checkHealth() {
        try {
            const response = await fetch(`${this.baseUrl}/health`);
            return await response.json();
        } catch (error) {
            console.error('Health check failed:', error);
            return null;
        }
    }

    // 查询 - 修复API路径
    async query(question, topK = 5, useRag = true) {
        try {
            const response = await fetch(`${this.baseUrl}/api/v1/query`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    query: question,
                    top_k: topK,
                    use_rag: useRag
                })
            });
            
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            
            return await response.json();
        } catch (error) {
            console.error('Query failed:', error);
            throw error;
        }
    }

    // 摄入文档 - 修复API路径
    async ingestDocuments(filePaths) {
        try {
            const response = await fetch(`${this.baseUrl}/api/v1/ingest`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    file_paths: filePaths
                })
            });
            
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            
            return await response.json();
        } catch (error) {
            console.error('Document ingestion failed:', error);
            throw error;
        }
    }

    // 向量搜索 - 修复API路径
    async search(query, topK = 10) {
        try {
            const response = await fetch(`${this.baseUrl}/api/v1/search`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    query: query,
                    top_k: topK
                })
            });
            
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            
            return await response.json();
        } catch (error) {
            console.error('Search failed:', error);
            throw error;
        }
    }

    // 获取统计信息 - 修复API路径
    async getStats() {
        try {
            const response = await fetch(`${this.baseUrl}/api/v1/collection/stats`);
            
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            
            return await response.json();
        } catch (error) {
            console.error('Get stats failed:', error);
            throw error;
        }
    }

    // 列出文档 - 修复API路径
    async listDocuments() {
        try {
            const response = await fetch(`${this.baseUrl}/api/v1/documents`);
            
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            
            return await response.json();
        } catch (error) {
            console.error('List documents failed:', error);
            throw error;
        }
    }

    // 删除文档 - 修复API路径
    async deleteDocument(filename) {
        try {
            const response = await fetch(`${this.baseUrl}/api/v1/documents/${filename}`, {
                method: 'DELETE'
            });
            
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            
            return await response.json();
        } catch (error) {
            console.error('Delete document failed:', error);
            throw error;
        }
    }

    // 上传文档 - 新增功能
    async uploadDocument(uploadData) {
        try {
            // 先保存到S3，然后调用摄入API
            const response = await fetch(`${this.baseUrl}/api/v1/ingest`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
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

    // 清空集合 - 修复API路径
    async clearCollection() {
        try {
            const response = await fetch(`${this.baseUrl}/api/v1/collection/clear`, {
                method: 'DELETE'
            });
            
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            
            return await response.json();
        } catch (error) {
            console.error('Clear collection failed:', error);
            throw error;
        }
    }
}

// 创建全局API客户端实例
const apiClient = new RAGApiClient();