// 自适应API客户端 - 根据API实际路径自动调整
class AdaptiveRAGApiClient {
    constructor() {
        this.baseUrl = null;
        this.apiVersion = null;
        this.initialized = false;
        this.initPromise = this.initialize();
    }

    async initialize() {
        try {
            // 确定基础URL
            if (window.location.hostname === 'localhost') {
                this.baseUrl = 'http://localhost:8000';
            } else {
                // 生产环境 - 使用API Gateway URL
                this.baseUrl = 'https://gbgn92f6v9.execute-api.us-east-1.amazonaws.com/prod';
            }

            // 检测API版本和路径结构
            await this.detectApiStructure();
            
            this.initialized = true;
            console.log('API Client initialized:', {
                baseUrl: this.baseUrl,
                apiVersion: this.apiVersion
            });
        } catch (error) {
            console.error('Failed to initialize API client:', error);
            // 使用默认配置
            this.apiVersion = 'simple';
            this.initialized = true;
        }
        return this;
    }

    async detectApiStructure() {
        // 尝试不同的健康检查端点
        const endpoints = [
            { path: '/health', version: 'simple' },
            { path: '/api/v1/health', version: 'v1' },
            { path: '/api/health', version: 'api' }
        ];

        for (const endpoint of endpoints) {
            try {
                const response = await fetch(`${this.baseUrl}${endpoint.path}`, {
                    method: 'GET',
                    headers: {
                        'Accept': 'application/json'
                    }
                });
                
                if (response.ok) {
                    this.apiVersion = endpoint.version;
                    console.log(`API structure detected: ${endpoint.version} at ${endpoint.path}`);
                    return;
                }
            } catch (error) {
                // 继续尝试下一个
            }
        }
        
        // 默认使用简单版本（当前API Gateway配置）
        this.apiVersion = 'simple';
        console.log('Using default API structure: simple');
    }

    getEndpoint(resource) {
        const endpoints = {
            'simple': {
                'query': '/query',
                'health': '/health',
                'documents': '/documents',
                'ingest': '/documents',
                'stats': '/stats',
                'search': '/search'
            },
            'v1': {
                'query': '/api/v1/query',
                'health': '/api/v1/health',
                'documents': '/api/v1/documents',
                'ingest': '/api/v1/ingest',
                'stats': '/api/v1/collection/stats',
                'search': '/api/v1/search'
            },
            'api': {
                'query': '/api/query',
                'health': '/api/health',
                'documents': '/api/documents',
                'ingest': '/api/ingest',
                'stats': '/api/stats',
                'search': '/api/search'
            }
        };

        return endpoints[this.apiVersion][resource] || `/${resource}`;
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
            const response = await fetch(`${this.baseUrl}${this.getEndpoint('health')}`, {
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
        await this.ensureInitialized();
        try {
            const response = await fetch(`${this.baseUrl}${this.getEndpoint('query')}`, {
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
            const response = await fetch(`${this.baseUrl}${this.getEndpoint('ingest')}`, {
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
            const response = await fetch(`${this.baseUrl}${this.getEndpoint('search')}`, {
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
            const response = await fetch(`${this.baseUrl}${this.getEndpoint('stats')}`, {
                headers: {
                    'Accept': 'application/json'
                }
            });
            
            if (!response.ok) {
                // 如果统计端点不存在，返回默认值
                return {
                    documents: 0,
                    vectors: 0,
                    dimension: 1536,
                    collection: 'rag_collection'
                };
            }
            
            return await response.json();
        } catch (error) {
            console.error('Get stats failed:', error);
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
        await this.ensureInitialized();
        try {
            const response = await fetch(`${this.baseUrl}${this.getEndpoint('documents')}`, {
                headers: {
                    'Accept': 'application/json'
                }
            });
            
            if (!response.ok) {
                // 如果文档端点不存在，返回空列表
                return { documents: [] };
            }
            
            return await response.json();
        } catch (error) {
            console.error('List documents failed:', error);
            // 返回空列表而不是抛出错误
            return { documents: [] };
        }
    }

    // 删除文档
    async deleteDocument(filename) {
        await this.ensureInitialized();
        try {
            const response = await fetch(`${this.baseUrl}${this.getEndpoint('documents')}/${filename}`, {
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
            const response = await fetch(`${this.baseUrl}${this.getEndpoint('ingest')}`, {
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
            const endpoint = this.apiVersion === 'v1' 
                ? '/api/v1/collection/clear'
                : '/collection/clear';
                
            const response = await fetch(`${this.baseUrl}${endpoint}`, {
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
            apiVersion: this.apiVersion,
            initialized: this.initialized,
            endpoints: {
                query: `${this.baseUrl}${this.getEndpoint('query')}`,
                health: `${this.baseUrl}${this.getEndpoint('health')}`,
                documents: `${this.baseUrl}${this.getEndpoint('documents')}`,
                stats: `${this.baseUrl}${this.getEndpoint('stats')}`
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
const apiClient = new AdaptiveRAGApiClient();

// 导出
if (typeof module !== 'undefined' && module.exports) {
    module.exports = AdaptiveRAGApiClient;
}