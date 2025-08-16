// 自动生成的配置文件
const API_CONFIG = {
    // API端点 - 支持本地和远程
    API_URL: window.location.hostname === 'localhost' 
        ? 'http://localhost:8000' 
        : 'https://<<marker:0xbaba:0>>.execute-api.us-east-1.<<marker:0xbaba:1>>/<<marker:0xbaba:2>>/',
    
    // CloudFront分发域名
    CLOUDFRONT_URL: window.location.origin,
    
    // 默认设置
    DEFAULT_TOP_K: 5,
    DEFAULT_USE_RAG: true,
    DEFAULT_TEMPERATURE: 0.7,
    DEFAULT_MAX_TOKENS: 1000,
    
    // 请求超时设置（毫秒）
    REQUEST_TIMEOUT: 30000,
    
    // 健康检查间隔（毫秒）
    HEALTH_CHECK_INTERVAL: 30000,
    
    // 重试设置
    MAX_RETRIES: 3,
    RETRY_DELAY: 1000
};

// 环境检测
const ENV = {
    isProduction: window.location.hostname !== 'localhost',
    isDevelopment: window.location.hostname === 'localhost',
    isCloudFront: window.location.hostname.includes('cloudfront.net'),
    stage: 'prod'
};

// 导出配置
window.RAG_CONFIG = {
    ...API_CONFIG,
    ENV,
    // 兼容旧配置
    API_BASE_URL: API_CONFIG.API_URL,
    MAX_QUERY_LENGTH: 500,
    TIMEOUT: API_CONFIG.REQUEST_TIMEOUT,
    // 添加stage信息
    STAGE: 'prod'
};
