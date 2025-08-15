"""
Lambda handler for RAG query operations - 完整实现版本
"""
import json
import os
import logging
from typing import Dict, Any
import sys

# 添加app目录到Python路径
sys.path.insert(0, '/var/task')
sys.path.insert(0, '/opt/python')  # Lambda Layer路径（如果有）

# 设置日志
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# 诊断导入环境
try:
    import pymilvus
    logger.info(f"✅ pymilvus successfully imported, version: {pymilvus.__version__}")
except ImportError as e:
    logger.error(f"❌ Failed to import pymilvus: {str(e)}")
    logger.error(f"Python path: {sys.path}")
    import subprocess
    try:
        # 列出已安装的包以帮助诊断
        result = subprocess.run(['pip', 'list'], capture_output=True, text=True)
        logger.info(f"Installed packages: {result.stdout}")
    except:
        pass

# 全局变量用于缓存RAG实例
rag_instance = None

def get_rag_instance():
    """获取或创建RAG实例（单例模式）"""
    global rag_instance
    if rag_instance is None:
        try:
            from app.models.rag_simple import SimpleRAG
            rag_instance = SimpleRAG()
            logger.info("✅ RAG instance created successfully")
        except ImportError as e:
            logger.error(f"❌ Import error creating RAG instance: {str(e)}")
            import traceback
            logger.error(f"Import traceback: {traceback.format_exc()}")
            rag_instance = None
        except Exception as e:
            logger.error(f"❌ General error creating RAG instance: {str(e)}")
            import traceback
            logger.error(f"General traceback: {traceback.format_exc()}")
            rag_instance = None
    return rag_instance

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
        path = event.get('path') or event.get('rawPath', '')
        if 'health' in path:
            return {
                'statusCode': 200,
                'headers': {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*'
                },
                'body': json.dumps({'status': 'healthy', 'version': '2.0'})
            }
        
        # 处理OPTIONS请求（CORS预检）
        if event.get('httpMethod') == 'OPTIONS' or event.get('requestContext', {}).get('http', {}).get('method') == 'OPTIONS':
            return {
                'statusCode': 200,
                'headers': {
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
                    'Access-Control-Allow-Headers': 'Content-Type'
                },
                'body': ''
            }
        
        # 解析请求体
        body = json.loads(event.get('body', '{}'))
        
        # 处理不同的操作
        operation = body.get('operation', 'query')
        
        if operation == 'add_document':
            # 添加文档操作
            return handle_add_document(body)
        
        elif operation == 'query':
            # 查询操作
            return handle_query(body)
        
        elif operation == 'test':
            # 测试操作
            return handle_test()
        
        else:
            return {
                'statusCode': 400,
                'headers': {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*'
                },
                'body': json.dumps({'error': f'Unknown operation: {operation}'})
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
        import traceback
        logger.error(f"Traceback: {traceback.format_exc()}")
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({'error': 'Internal server error', 'details': str(e)})
        }


def handle_query(body: Dict[str, Any]) -> Dict[str, Any]:
    """处理查询请求"""
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
    
    # 获取RAG实例
    rag = get_rag_instance()
    
    if rag is None:
        # RAG初始化失败，返回后备响应
        logger.warning("RAG not available, using fallback response")
        response_body = {
            'query': query,
            'answer': get_fallback_answer(query),
            'sources': [],
            'metadata': {
                'top_k': top_k,
                'status': 'fallback',
                'model': os.environ.get('BEDROCK_MODEL_ID', 'amazon.nova-pro-v1:0')
            }
        }
    else:
        # 执行RAG查询
        try:
            rag_response = rag.query(query, top_k=top_k)
            
            response_body = {
                'query': query,
                'answer': rag_response.answer,
                'sources': rag_response.sources,
                'metadata': {
                    'top_k': top_k,
                    'confidence': rag_response.confidence,
                    'model': os.environ.get('BEDROCK_MODEL_ID', 'amazon.nova-pro-v1:0')
                }
            }
            logger.info("RAG query successful")
            
        except Exception as e:
            logger.error(f"RAG query failed: {str(e)}")
            response_body = {
                'query': query,
                'answer': get_fallback_answer(query),
                'sources': [],
                'metadata': {
                    'top_k': top_k,
                    'status': 'error',
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


def handle_add_document(body: Dict[str, Any]) -> Dict[str, Any]:
    """处理添加文档请求"""
    content = body.get('content', '')
    metadata = body.get('metadata', {})
    
    if not content:
        return {
            'statusCode': 400,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({'error': 'Content is required'})
        }
    
    logger.info(f"Adding document with length: {len(content)}")
    
    # 获取RAG实例
    rag = get_rag_instance()
    
    if rag is None:
        return {
            'statusCode': 503,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({'error': 'RAG service not available'})
        }
    
    # 添加文档
    try:
        success = rag.add_document(content, metadata)
        
        if success:
            return {
                'statusCode': 200,
                'headers': {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*'
                },
                'body': json.dumps({
                    'message': 'Document added successfully',
                    'content_length': len(content),
                    'metadata': metadata
                })
            }
        else:
            return {
                'statusCode': 500,
                'headers': {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*'
                },
                'body': json.dumps({'error': 'Failed to add document'})
            }
            
    except Exception as e:
        logger.error(f"Error adding document: {str(e)}")
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({'error': f'Error adding document: {str(e)}'})
        }


def handle_test() -> Dict[str, Any]:
    """处理测试请求"""
    logger.info("Running system test")
    
    test_results = {
        'environment': {
            'aws_region': os.environ.get('AWS_REGION', 'not set'),
            'bedrock_model': os.environ.get('BEDROCK_MODEL_ID', 'not set'),
            'embedding_model': os.environ.get('EMBEDDING_MODEL_ID', 'not set'),
            'zilliz_endpoint': 'configured' if os.environ.get('ZILLIZ_ENDPOINT') else 'not set',
            'zilliz_collection': os.environ.get('ZILLIZ_COLLECTION', 'not set')
        },
        'rag_status': 'not initialized'
    }
    
    # 测试RAG初始化
    rag = get_rag_instance()
    if rag:
        test_results['rag_status'] = 'initialized'
        
        # 测试查询
        try:
            test_response = rag.query("test query", top_k=1)
            test_results['test_query'] = {
                'success': True,
                'answer_length': len(test_response.answer)
            }
        except Exception as e:
            test_results['test_query'] = {
                'success': False,
                'error': str(e)
            }
    
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps(test_results)
    }


def get_fallback_answer(query: str) -> str:
    """获取后备回答"""
    query_lower = query.lower()
    
    if 'rag' in query_lower:
        return "RAG (Retrieval-Augmented Generation) is a technique that combines information retrieval with language generation. It retrieves relevant documents from a knowledge base and uses them as context to generate more accurate and informed responses."
    elif 'lambda' in query_lower:
        return "AWS Lambda is a serverless compute service that lets you run code without provisioning or managing servers. Lambda Layers allow you to share code and dependencies across multiple functions."
    elif 'zilliz' in query_lower or 'milvus' in query_lower:
        return "Zilliz is a cloud-native vector database service based on Milvus. It's designed for storing and searching high-dimensional vector embeddings, making it ideal for AI applications like semantic search and RAG systems."
    elif 'bedrock' in query_lower:
        return "Amazon Bedrock is a fully managed service that offers foundation models from leading AI companies through a single API. It's used for building generative AI applications."
    else:
        return f"I understand you're asking about '{query}'. This is a RAG system that can provide answers based on stored documents. Please add relevant documents first to get more accurate responses."