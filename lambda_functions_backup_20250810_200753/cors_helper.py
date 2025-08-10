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
    allowed_origins = os.environ.get('ALLOWED_ORIGINS', '*')
    
    # Get the request origin
    origin = '*'
    if event and 'headers' in event:
        origin = event['headers'].get('origin') or event['headers'].get('Origin', '*')
    
    # If specific origins are configured, validate the request origin
    if allowed_origins != '*':
        allowed_list = [o.strip() for o in allowed_origins.split(',')]
        if origin not in allowed_list:
            # Use the first allowed origin as default
            origin = allowed_list[0] if allowed_list else '*'
    else:
        # Allow all origins
        origin = '*'
    
    return {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': origin,
        'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token',
        'Access-Control-Allow-Methods': 'GET,POST,OPTIONS,DELETE,PUT',
        'Access-Control-Allow-Credentials': 'true',
        'Access-Control-Max-Age': '86400'
    }


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