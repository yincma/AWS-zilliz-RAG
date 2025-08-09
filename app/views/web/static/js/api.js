// API客户端
class RAGApiClient {
    constructor(baseUrl = null) {
        // 优先使用传入的URL，否则从配置文件获取，最后使用默认值
        this.baseUrl = baseUrl || 
                      (window.RAG_CONFIG && window.RAG_CONFIG.API_URL) || 
                      'https://abbrw64qve.execute-api.us-east-1.amazonaws.com/prod';
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

    // 查询
    async query(question, topK = 5, useRag = true) {
        try {
            const response = await fetch(`${this.baseUrl}/query`, {
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
            return await response.json();
        } catch (error) {
            console.error('Query failed:', error);
            throw error;
        }
    }

    // 摄入文档
    async ingestDocuments(filePaths) {
        try {
            const response = await fetch(`${this.baseUrl}/documents`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    file_paths: filePaths
                })
            });
            return await response.json();
        } catch (error) {
            console.error('Document ingestion failed:', error);
            throw error;
        }
    }

    // 向量搜索
    async search(query, topK = 10) {
        try {
            const response = await fetch(`${this.baseUrl}/query`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    query: query,
                    top_k: topK
                })
            });
            return await response.json();
        } catch (error) {
            console.error('Search failed:', error);
            throw error;
        }
    }

    // 获取统计信息
    async getStats() {
        try {
            const response = await fetch(`${this.baseUrl}/documents`, {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({operation: 'stats'})
            });
            return await response.json();
        } catch (error) {
            console.error('Get stats failed:', error);
            throw error;
        }
    }

    // 列出文档
    async listDocuments() {
        try {
            const response = await fetch(`${this.baseUrl}/documents`);
            return await response.json();
        } catch (error) {
            console.error('List documents failed:', error);
            throw error;
        }
    }

    // 删除文档
    async deleteDocument(filename) {
        try {
            const response = await fetch(`${this.baseUrl}/documents/${filename}`, {
                method: 'DELETE'
            });
            return await response.json();
        } catch (error) {
            console.error('Delete document failed:', error);
            throw error;
        }
    }

    // 上传文档
    async uploadDocument(uploadData) {
        try {
            const response = await fetch(`${this.baseUrl}/documents/upload`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(uploadData)
            });
            
            // 如果响应成功，即使不是JSON也认为成功
            if (response.ok) {
                try {
                    const result = await response.json();
                    return {
                        status: 'success',
                        data: result
                    };
                } catch (jsonError) {
                    // JSON解析失败但请求成功，仍然返回成功
                    console.warn('Response is not JSON, but upload succeeded');
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
            const response = await fetch(`${this.baseUrl}/documents`, {
                method: 'DELETE',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({operation: 'clear'})
            });
            return await response.json();
        } catch (error) {
            console.error('Clear collection failed:', error);
            throw error;
        }
    }
}

// 创建全局API客户端实例
const apiClient = new RAGApiClient();