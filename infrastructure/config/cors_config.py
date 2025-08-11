"""
CORS Configuration Management
集中管理所有 CORS 相关配置，避免硬编码
"""
import os
from typing import List, Dict, Any


class CORSConfig:
    """CORS 配置管理类"""
    
    @staticmethod
    def get_allowed_origins() -> List[str]:
        """
        获取允许的源列表
        优先级：环境变量 > CloudFormation 输出 > 默认值
        """
        # 从环境变量获取
        env_origins = os.environ.get('CORS_ALLOWED_ORIGINS', '')
        if env_origins:
            return [origin.strip() for origin in env_origins.split(',')]
        
        # 从 CloudFormation 输出获取（如果有的话）
        cf_cloudfront_url = os.environ.get('CLOUDFRONT_URL')
        if cf_cloudfront_url:
            return [
                cf_cloudfront_url,
                'http://localhost:3000',  # 开发环境
                'http://localhost:8080'   # 开发环境备用
            ]
        
        # 默认允许所有源（仅在没有配置时）
        return ['*']
    
    @staticmethod
    def get_allowed_methods() -> List[str]:
        """获取允许的 HTTP 方法"""
        methods = os.environ.get('CORS_ALLOWED_METHODS', 'GET,POST,PUT,DELETE,OPTIONS')
        return [method.strip() for method in methods.split(',')]
    
    @staticmethod
    def get_allowed_headers() -> List[str]:
        """获取允许的请求头"""
        headers = os.environ.get('CORS_ALLOWED_HEADERS', 
                                'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token')
        return [header.strip() for header in headers.split(',')]
    
    @staticmethod
    def get_max_age() -> int:
        """获取预检请求缓存时间（秒）"""
        return int(os.environ.get('CORS_MAX_AGE', '86400'))  # 默认 24 小时
    
    @staticmethod
    def get_allow_credentials() -> bool:
        """是否允许携带凭证"""
        return os.environ.get('CORS_ALLOW_CREDENTIALS', 'false').lower() == 'true'
    
    @staticmethod
    def get_environment_config() -> Dict[str, str]:
        """
        获取用于 Lambda 函数的环境变量配置
        用于 CDK 部署时设置
        """
        cloudfront_url = os.environ.get('CLOUDFRONT_URL', '')
        
        # 如果有 CloudFront URL，构建允许的源列表
        if cloudfront_url:
            allowed_origins = f"{cloudfront_url},http://localhost:3000,http://localhost:8080"
        else:
            allowed_origins = "*"
        
        return {
            "CORS_ALLOWED_ORIGINS": allowed_origins,
            "CORS_ALLOWED_METHODS": "GET,POST,PUT,DELETE,OPTIONS",
            "CORS_ALLOWED_HEADERS": "Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token",
            "CORS_MAX_AGE": "86400",
            "CORS_ALLOW_CREDENTIALS": "false"
        }
    
    @staticmethod
    def validate_origin(origin: str, allowed_origins: List[str]) -> str:
        """
        验证并返回合适的 Access-Control-Allow-Origin 值
        
        Args:
            origin: 请求的 origin
            allowed_origins: 允许的源列表
            
        Returns:
            合适的 Access-Control-Allow-Origin 值
        """
        # 如果允许所有源
        if '*' in allowed_origins:
            # 如果有具体的 origin，返回它（更好的兼容性）
            return origin if origin else '*'
        
        # 如果 origin 在允许列表中
        if origin and origin in allowed_origins:
            return origin
        
        # 否则返回第一个允许的源或拒绝
        return allowed_origins[0] if allowed_origins else None