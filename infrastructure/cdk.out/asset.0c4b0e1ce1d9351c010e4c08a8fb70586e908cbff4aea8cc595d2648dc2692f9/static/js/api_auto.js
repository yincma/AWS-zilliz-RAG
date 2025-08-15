// 自动配置API客户端 - 无硬编码，自动获取配置
class RAGApiClient {
    constructor() {
        this.baseUrl = null;
        this.initialized = false;
        this.initPromise = this.initialize();
    }

    async initialize() {
        try {
            // 1. 尝试从运行时配置文件加载
            try {
                const configResponse = await fetch('/static/js/runtime-config.json');
                if (configResponse.ok) {
                    const config = await configResponse.json();
                    if (config.apiUrl) {
                        this.baseUrl = config.apiUrl.replace(/\/$/, ''); // 去掉尾部斜杠
                        console.log('Loaded API URL from runtime config:', this.baseUrl);
                        this.initialized = true;
                        return;
                    }
                }
            } catch (e) {
                console.log('Runtime config not available');
            }

            // 2. 尝试从meta标签获取
            const metaApiUrl = document.querySelector('meta[name="api-url"]');
            if (metaApiUrl && metaApiUrl.content) {
                this.baseUrl = metaApiUrl.content.replace(/\/$/, '');
                console.log('Loaded API URL from meta tag:', this.baseUrl);
                this.initialized = true;
                return;
            }

            // 3. 尝试从环境检测
            if (window.location.hostname === 'localhost') {
                this.baseUrl = 'http://localhost:8000';
            } else {
                // 尝试从API Gateway模式推断
                // 通常CloudFront URL会包含这些模式
                if (window.location.hostname.includes('cloudfront.net')) {
                    // 尝试通过健康检查探测API
                    await this.probeApiEndpoints();
                } else {
                    // 使用相对路径，假设通过代理
                    this.baseUrl = '';
                }
            }

            this.initialized = true;
            console.log('API Client initialized with baseUrl:', this.baseUrl || 'relative path');

        } catch (error) {
            console.error('Failed to initialize API client:', error);
            this.baseUrl = '';
            this.initialized = true;
        }
    }

    async probeApiEndpoints() {
        // 尝试常见的API Gateway模式
        const patterns = [
            'https://*.execute-api.*.amazonaws.com/prod',
            'https://*.execute-api.*.amazonaws.com/dev',
            '/api',
            ''
        ];

        // 这里可以实现更复杂的探测逻辑
        // 暂时使用空路径，通过相对路径访问
        this.baseUrl = '';
    }

    async ensureInitialized() {
        if (!this.initialized) {
            await this.initPromise;
        }
    }

    // 构建URL的辅助方法（防止双斜杠）
    buildUrl(path) {
        // 确保path以斜杠开头
        if (!path.startsWith('/')) {
            path = '/' + path;
        }
        
        // 如果baseUrl为空，返回相对路径
        if (!this.baseUrl) {
            return path;
        }
        
        // 确保没有双斜杠
        return this.baseUrl + path;
    }

    // 健康检查
    async checkHealth() {
        await this.ensureInitialized();
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
        await this.ensureInitialized();
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
        await this.ensureInitialized();
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

    // 获取统计信息（优雅降级）
    async getStats() {
        await this.ensureInitialized();
        try {
            const url = this.buildUrl('/stats');
            const response = await fetch(url, {
                headers: {
                    'Accept': 'application/json'
                }
            });
            
            if (!response.ok) {
                // 静默失败，返回默认值
                return {
                    documents: 0,
                    vectors: 0,
                    dimension: 1536,
                    collection: 'rag_collection'
                };
            }
            
            return await response.json();
        } catch (error) {
            // 静默失败，返回默认值
            return {
                documents: 0,
                vectors: 0,
                dimension: 1536,
                collection: 'rag_collection'
            };
        }
    }

    // 列出文档（优雅降级）
    async listDocuments() {
        await this.ensureInitialized();
        try {
            const url = this.buildUrl('/documents');
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
            return { documents: [] };
        }
    }

    // 向量搜索（带降级）
    async search(query, topK = 10) {
        await this.ensureInitialized();
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
                // 降级到查询端点
                return this.query(query, topK, true);
            }
            
            return await response.json();
        } catch (error) {
            // 降级到查询端点
            return this.query(query, topK, true);
        }
    }

    // 删除文档
    async deleteDocument(filename) {
        await this.ensureInitialized();
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
        await this.ensureInitialized();
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
        await this.ensureInitialized();
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
            initialized: this.initialized,
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

// 等待初始化完成后输出配置
apiClient.initPromise.then(() => {
    console.log('RAG API Client Configuration:', apiClient.getConfiguration());
});