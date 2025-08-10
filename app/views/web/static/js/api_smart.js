// 智能API客户端 - 自动检测和加载配置
class SmartRAGApiClient {
    constructor() {
        this.baseUrl = null;
        this.config = null;
        this.initialized = false;
        this.initPromise = this.initialize();
    }

    async initialize() {
        try {
            // 尝试加载运行时配置
            const configResponse = await fetch('/static/js/runtime-config.json');
            if (configResponse.ok) {
                this.config = await configResponse.json();
                console.log('Loaded runtime config:', this.config);
            }
        } catch (error) {
            console.log('Runtime config not found, using defaults');
        }

        // 确定API基础URL
        if (window.location.hostname === 'localhost') {
            // 本地开发环境
            this.baseUrl = 'http://localhost:8000';
        } else if (this.config && this.config.useProxy) {
            // 使用CloudFront反向代理（相对路径）
            this.baseUrl = '';
        } else if (window.RAG_CONFIG && window.RAG_CONFIG.API_URL) {
            // 使用全局配置
            this.baseUrl = window.RAG_CONFIG.API_URL;
        } else {
            // 默认使用相对路径
            this.baseUrl = '';
        }

        this.initialized = true;
        console.log('API Client initialized with baseUrl:', this.baseUrl || 'relative path');
        return this;
    }

    async ensureInitialized() {
        if (!this.initialized) {
            await this.initPromise;
        }
    }

    // 健康检查
    async checkHealth() {
        await this.ensureInitialized();
        try {
            const response = await fetch(`${this.baseUrl}/health`, {
                method: 'GET',
                headers: {
                    'Accept': 'application/json'
                }
            });
            return await response.json();
        } catch (error) {
            console.error('Health check failed:', error);
            return { status: 'error', message: error.message };
        }
    }

    // 查询
    async query(question, topK = 5, useRag = true) {
        await this.ensureInitialized();
        try {
            const response = await fetch(`${this.baseUrl}/api/v1/query`, {
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

    // 摄入文档
    async ingestDocuments(filePaths) {
        await this.ensureInitialized();
        try {
            const response = await fetch(`${this.baseUrl}/api/v1/ingest`, {
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
        await this.ensureInitialized();
        try {
            const response = await fetch(`${this.baseUrl}/api/v1/search`, {
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
                const errorText = await response.text();
                throw new Error(`HTTP ${response.status}: ${errorText}`);
            }
            
            return await response.json();
        } catch (error) {
            console.error('Search failed:', error);
            throw error;
        }
    }

    // 获取统计信息
    async getStats() {
        await this.ensureInitialized();
        try {
            const response = await fetch(`${this.baseUrl}/api/v1/collection/stats`, {
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
            console.error('Get stats failed:', error);
            throw error;
        }
    }

    // 列出文档
    async listDocuments() {
        await this.ensureInitialized();
        try {
            const response = await fetch(`${this.baseUrl}/api/v1/documents`, {
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
            console.error('List documents failed:', error);
            throw error;
        }
    }

    // 删除文档
    async deleteDocument(filename) {
        await this.ensureInitialized();
        try {
            const response = await fetch(`${this.baseUrl}/api/v1/documents/${filename}`, {
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
        await this.ensureInitialized();
        try {
            const response = await fetch(`${this.baseUrl}/api/v1/ingest`, {
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
        await this.ensureInitialized();
        try {
            const response = await fetch(`${this.baseUrl}/api/v1/collection/clear`, {
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

    // 调试方法 - 获取当前配置
    getConfiguration() {
        return {
            baseUrl: this.baseUrl,
            config: this.config,
            initialized: this.initialized,
            environment: {
                hostname: window.location.hostname,
                origin: window.location.origin,
                protocol: window.location.protocol
            }
        };
    }
}

// 创建全局API客户端实例
const apiClient = new SmartRAGApiClient();

// 导出给其他模块使用
if (typeof module !== 'undefined' && module.exports) {
    module.exports = SmartRAGApiClient;
}