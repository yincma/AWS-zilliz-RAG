"""
CORS Helper for Lambda Functions
Provides consistent CORS headers for all responses
"""
import os
import json
from typing import Dict, Any, Optional


def get_cors_headers(event: Dict[str, Any] = None) -> Dict[str, str]:
    """
    Get CORS headers based on environment configuration
    
    Args:
        event: API Gateway event containing request headers
        
    Returns:
        Dictionary of CORS headers
    """
    # Get allowed origins from environment variable
    # 支持多种环境变量名称以保持兼容性
    allowed_origins = (
        os.environ.get('CORS_ALLOWED_ORIGINS') or  # 新的统一名称
        os.environ.get('CORS_ALLOW_ORIGINS') or     # CDK 栈中使用的名称
        os.environ.get('ALLOWED_ORIGINS') or        # 旧名称
        '*'                                          # 默认值
    )
    
    # Get the request origin
    request_origin = None
    if event and 'headers' in event:
        request_origin = event['headers'].get('origin') or event['headers'].get('Origin')
    
    # Determine the origin to use in the response
    if allowed_origins == '*':
        # If allowing all origins and we have a request origin, use it
        # This is important for CORS to work properly with credentials
        origin = request_origin if request_origin else '*'
    else:
        # If specific origins are configured, validate the request origin
        allowed_list = [o.strip() for o in allowed_origins.split(',')]
        if request_origin and request_origin in allowed_list:
            origin = request_origin
        else:
            # Use the first allowed origin as default or '*' if no origins configured
            origin = allowed_list[0] if allowed_list else '*'
    
    # 获取其他 CORS 配置
    allow_methods = (
        os.environ.get('CORS_ALLOWED_METHODS') or
        os.environ.get('CORS_ALLOW_METHODS') or
        'GET,POST,OPTIONS,DELETE,PUT'
    )
    allow_headers = (
        os.environ.get('CORS_ALLOWED_HEADERS') or
        os.environ.get('CORS_ALLOW_HEADERS') or
        'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token'
    )
    allow_credentials = os.environ.get('CORS_ALLOW_CREDENTIALS', 'false').lower() == 'true'
    max_age = os.environ.get('CORS_MAX_AGE', '86400')
    
    headers = {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': origin,
        'Access-Control-Allow-Headers': allow_headers,
        'Access-Control-Allow-Methods': allow_methods,
        'Access-Control-Max-Age': max_age
    }
    
    # 仅在明确配置时添加 credentials 头
    if allow_credentials:
        headers['Access-Control-Allow-Credentials'] = 'true'
    
    return headers


def create_response(
    status_code: int,
    body: Any,
    event: Dict[str, Any] = None,
    additional_headers: Optional[Dict[str, str]] = None
) -> Dict[str, Any]:
    """
    Create a Lambda response with proper CORS headers
    
    Args:
        status_code: HTTP status code
        body: Response body (will be JSON serialized if not a string)
        event: API Gateway event for extracting origin
        additional_headers: Additional headers to include
        
    Returns:
        Properly formatted Lambda response
    """
    # Get CORS headers
    headers = get_cors_headers(event)
    
    # Add any additional headers
    if additional_headers:
        headers.update(additional_headers)
    
    # Serialize body if necessary
    if not isinstance(body, str):
        body = json.dumps(body, default=str)
    
    return {
        'statusCode': status_code,
        'headers': headers,
        'body': body
    }


def create_error_response(
    error: Exception,
    status_code: int = 500,
    event: Dict[str, Any] = None
) -> Dict[str, Any]:
    """
    Create an error response with proper CORS headers
    
    Args:
        error: The exception that occurred
        status_code: HTTP status code (default 500)
        event: API Gateway event for extracting origin
        
    Returns:
        Properly formatted error response
    """
    error_body = {
        'error': str(error),
        'message': 'An error occurred processing your request',
        'type': type(error).__name__
    }
    
    return create_response(status_code, error_body, event)


def handle_options_request(event: Dict[str, Any]) -> Dict[str, Any]:
    """
    Handle OPTIONS preflight requests
    
    Args:
        event: API Gateway event
        
    Returns:
        Preflight response with CORS headers
    """
    return create_response(
        200,
        {'message': 'CORS preflight successful'},
        event
    )