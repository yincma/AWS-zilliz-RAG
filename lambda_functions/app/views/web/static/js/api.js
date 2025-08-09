// API客户端
class RAGApiClient {
    constructor(baseUrl = 'http://localhost:8000') {
        this.baseUrl = baseUrl;
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
    async query(question, topK = 5) {
        try {
            const response = await fetch(`${this.baseUrl}/api/v1/query`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    query: question,
                    top_k: topK
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
            const response = await fetch(`${this.baseUrl}/api/v1/ingest`, {
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
            return await response.json();
        } catch (error) {
            console.error('Search failed:', error);
            throw error;
        }
    }

    // 获取统计信息
    async getStats() {
        try {
            const response = await fetch(`${this.baseUrl}/api/v1/collection/stats`);
            return await response.json();
        } catch (error) {
            console.error('Get stats failed:', error);
            throw error;
        }
    }

    // 列出文档
    async listDocuments() {
        try {
            const response = await fetch(`${this.baseUrl}/api/v1/documents`);
            return await response.json();
        } catch (error) {
            console.error('List documents failed:', error);
            throw error;
        }
    }

    // 删除文档
    async deleteDocument(filename) {
        try {
            const response = await fetch(`${this.baseUrl}/api/v1/documents/${filename}`, {
                method: 'DELETE'
            });
            return await response.json();
        } catch (error) {
            console.error('Delete document failed:', error);
            throw error;
        }
    }

    // 清空集合
    async clearCollection() {
        try {
            const response = await fetch(`${this.baseUrl}/api/v1/collection/clear`, {
                method: 'DELETE'
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