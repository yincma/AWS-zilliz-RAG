"""
Lambda handler for RAG query operations
"""
import json
import os
import logging
from typing import Dict, Any

# 设置日志
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """
    Lambda handler for RAG query
    
    Args:
        event: API Gateway event
        context: Lambda context
        
    Returns:
        API Gateway response
    """
    try:
        logger.info(f"Received event: {json.dumps(event)}")
        
        # 处理 health check
        if event.get('path') == '/health' or event.get('rawPath') == '/health':
            return {
                'statusCode': 200,
                'headers': {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*'
                },
                'body': json.dumps({'status': 'healthy'})
            }
        
        # 解析请求体
        body = json.loads(event.get('body', '{}'))
        query = body.get('query', '')
        top_k = body.get('top_k', 5)
        
        if not query:
            return {
                'statusCode': 400,
                'headers': {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*'
                },
                'body': json.dumps({'error': 'Query is required'})
            }
        
        logger.info(f"Processing query: {query} with top_k: {top_k}")
        
        # TODO: 实际的RAG处理逻辑
        # 这里暂时返回模拟响应
        try:
            # 导入必要的模块
            from app.models.rag_chain import RAGChain
            
            # 初始化RAG链
            rag_chain = RAGChain()
            
            # 执行查询
            result = rag_chain.query(query, top_k=top_k)
            
            response_body = {
                'query': query,
                'answer': result.get('answer', 'Unable to generate answer'),
                'sources': result.get('sources', []),
                'metadata': {
                    'top_k': top_k,
                    'model': os.environ.get('BEDROCK_MODEL_ID', 'amazon.nova-pro-v1:0')
                }
            }
            
        except ImportError:
            # 如果模块不存在，返回模拟响应
            logger.warning("RAG modules not found, returning mock response")
            response_body = {
                'query': query,
                'answer': f"This is a mock response for: {query}. RAG system is being initialized.",
                'sources': [],
                'metadata': {
                    'top_k': top_k,
                    'status': 'mock_response'
                }
            }
        except Exception as e:
            logger.error(f"Error in RAG processing: {str(e)}")
            response_body = {
                'query': query,
                'answer': f"RAG system is currently unavailable. Error: {str(e)}",
                'sources': [],
                'metadata': {
                    'top_k': top_k,
                    'error': str(e)
                }
            }
        
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps(response_body)
        }
        
    except json.JSONDecodeError:
        logger.error("Invalid JSON in request body")
        return {
            'statusCode': 400,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({'error': 'Invalid JSON in request body'})
        }
        
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({'error': 'Internal server error', 'details': str(e)})
        }