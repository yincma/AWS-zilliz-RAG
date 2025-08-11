// 动态配置加载的API客户端
// 生成时间: 2025-08-12T01:45:15.110455
// 此文件实现动态配置加载，避免硬编码

class RAGApiClient {
    constructor() {
        // 初始化时使用默认值，稍后从配置文件加载
        this.baseUrl = null;
        this.configLoaded = false;
        this.configPromise = null;
        this.initializeConfig();
    }
    
    // 异步初始化配置
    async initializeConfig() {
        if (this.configPromise) {
            return this.configPromise;
        }
        
        this.configPromise = this.loadConfiguration();
        await this.configPromise;
        this.configLoaded = true;
        return this.baseUrl;
    }
    
    // 从配置文件加载配置
    async loadConfiguration() {
        try {
            // 开发环境
            if (window.location.hostname === 'localhost') {
                this.baseUrl = 'http://localhost:8000';
                this.setConfigSource('localhost');
                console.log('Development mode - using localhost');
                return this.baseUrl;
            }
            
            // 生产环境 - 尝试从config.json加载
            try {
                const response = await fetch('/config.json?t=' + Date.now());
                if (response.ok) {
                    const config = await response.json();
                    if (config.apiUrl) {
                        this.baseUrl = config.apiUrl.replace(/\/$/, '');
                        this.setConfigSource('config.json');
                        console.log('API URL loaded from config.json:', this.baseUrl);
                        // 存储完整配置供其他组件使用
                        window.RAG_CONFIG_DATA = config;
                        return this.baseUrl;
                    }
                }
            } catch (configError) {
                console.warn('Could not load config.json, using fallback');
            }
            
            // 如果无法加载config.json，使用元数据标签
            const metaApiUrl = document.querySelector('meta[name="api-url"]')?.content;
            if (metaApiUrl) {
                this.baseUrl = metaApiUrl.replace(/\/$/, '');
                this.setConfigSource('meta-tag');
                console.log('API URL loaded from meta tag:', this.baseUrl);
                return this.baseUrl;
            }
            
            // 最后的备用方案：使用相对路径（假设API和前端同源）
            this.baseUrl = window.location.origin;
            this.setConfigSource('same-origin-fallback');
            console.log('Using fallback API URL (same origin):', this.baseUrl);
            return this.baseUrl;
            
        } catch (error) {
            console.error('Error loading configuration:', error);
            // 错误时使用相对路径
            this.baseUrl = window.location.origin;
            this.setConfigSource('error-fallback');
            return this.baseUrl;
        }
    }
    
    // 确保配置已加载
    async ensureConfigLoaded() {
        if (!this.configLoaded) {
            await this.initializeConfig();
        }
        return this.baseUrl;
    }

    // 健康检查
    async checkHealth() {
        try {
            await this.ensureConfigLoaded();
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
            await this.ensureConfigLoaded();
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
            await this.ensureConfigLoaded();
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
            await this.ensureConfigLoaded();
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
            await this.ensureConfigLoaded();
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
            await this.ensureConfigLoaded();
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
            await this.ensureConfigLoaded();
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
            await this.ensureConfigLoaded();
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

    // 获取配置信息
    async getConfiguration() {
        await this.ensureConfigLoaded();
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
            },
            configLoaded: this.configLoaded,
            configSource: this.configSource || 'unknown'
        };
    }
    
    // 设置配置源标记（用于调试）
    setConfigSource(source) {
        this.configSource = source;
    }
    
    // 验证API URL格式
    validateApiUrl(url) {
        if (!url) return false;
        
        try {
            const parsedUrl = new URL(url);
            // 检查协议
            if (!['http:', 'https:'].includes(parsedUrl.protocol)) {
                return false;
            }
            // 检查主机名
            if (!parsedUrl.hostname) {
                return false;
            }
            return true;
        } catch (error) {
            // 如果不是完整URL，可能是相对路径
            return url === '' || url === '/';
        }
    }
    
    // 健康检查重试机制
    async checkHealthWithRetry(maxRetries = 3, delay = 1000) {
        for (let i = 0; i < maxRetries; i++) {
            try {
                const result = await this.checkHealth();
                if (result && result.status !== 'error') {
                    return result;
                }
            } catch (error) {
                console.warn(`Health check attempt ${i + 1} failed:`, error);
            }
            
            if (i < maxRetries - 1) {
                await new Promise(resolve => setTimeout(resolve, delay));
            }
        }
        
        return { status: 'error', message: 'Max retries exceeded' };
    }
    
    // 获取配置状态（用于调试和监控）
    getConfigStatus() {
        return {
            loaded: this.configLoaded,
            baseUrl: this.baseUrl,
            source: this.configSource,
            valid: this.validateApiUrl(this.baseUrl),
            timestamp: new Date().toISOString()
        };
    }
}

// 创建全局API客户端实例
const apiClient = new RAGApiClient();

// 配置将异步加载，在初始化完成后输出配置信息
apiClient.initializeConfig().then(() => {
    apiClient.getConfiguration().then(config => {
        console.log('RAG API Client Configuration:', config);
    });
});
