"""
Lambda handler for document ingestion operations
"""
import json
import os
import logging
from typing import Dict, Any
import boto3

# 设置日志
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# 初始化 S3 客户端
s3_client = boto3.client('s3')

def handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """
    Lambda handler for document ingestion
    
    Args:
        event: API Gateway event or S3 event
        context: Lambda context
        
    Returns:
        API Gateway response or processing result
    """
    try:
        logger.info(f"Received event: {json.dumps(event)}")
        
        # 检查是否是S3事件
        if 'Records' in event and event['Records'][0].get('s3'):
            return handle_s3_event(event)
        
        # 否则处理API Gateway事件
        return handle_api_event(event)
        
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


def handle_s3_event(event: Dict[str, Any]) -> Dict[str, Any]:
    """
    处理S3事件触发的文档摄入
    """
    try:
        for record in event['Records']:
            bucket = record['s3']['bucket']['name']
            key = record['s3']['object']['key']
            
            logger.info(f"Processing S3 object: s3://{bucket}/{key}")
            
            # TODO: 实际的文档处理逻辑
            try:
                from app.models.document import DocumentModel
                from app.models.embedding import EmbeddingModel
                from app.models.vector_store import VectorStoreModel
                
                # 初始化模型
                doc_model = DocumentModel()
                embedding_model = EmbeddingModel()
                vector_store = VectorStoreModel()
                
                # 从S3加载文档
                document = doc_model.load_from_s3(bucket, key)
                
                # 分割文档
                chunks = doc_model.split_document(document)
                
                # 生成嵌入
                embeddings = embedding_model.generate_embeddings(chunks)
                
                # 存储到向量数据库
                vector_store.store_embeddings(embeddings, chunks)
                
                logger.info(f"Successfully processed document: {key}")
                
            except ImportError:
                logger.warning("Document processing modules not found")
            except Exception as e:
                logger.error(f"Error processing document: {str(e)}")
                raise
        
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Documents processed successfully'})
        }
        
    except Exception as e:
        logger.error(f"Error handling S3 event: {str(e)}")
        raise


def handle_api_event(event: Dict[str, Any]) -> Dict[str, Any]:
    """
    处理API Gateway事件
    """
    try:
        # 解析请求体
        body = json.loads(event.get('body', '{}'))
        operation = body.get('operation', 'ingest')
        
        if operation == 'stats':
            # 返回统计信息
            return get_stats()
        
        elif operation == 's3_ingest':
            # 处理S3文档摄入请求
            s3_keys = body.get('s3_keys', [])
            bucket = body.get('bucket', os.environ.get('S3_BUCKET'))
            
            if not s3_keys:
                return {
                    'statusCode': 400,
                    'headers': {
                        'Content-Type': 'application/json',
                        'Access-Control-Allow-Origin': '*'
                    },
                    'body': json.dumps({'error': 's3_keys is required'})
                }
            
            results = []
            for key in s3_keys:
                try:
                    logger.info(f"Ingesting document from S3: {key}")
                    # TODO: 实际的文档处理
                    results.append({
                        'key': key,
                        'status': 'success',
                        'message': 'Document queued for processing'
                    })
                except Exception as e:
                    results.append({
                        'key': key,
                        'status': 'error',
                        'message': str(e)
                    })
            
            return {
                'statusCode': 200,
                'headers': {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*'
                },
                'body': json.dumps({
                    'operation': operation,
                    'results': results
                })
            }
        
        elif operation == 'direct_ingest':
            # 直接文档摄入
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
            
            # TODO: 处理直接内容摄入
            logger.info(f"Direct ingestion of content with length: {len(content)}")
            
            return {
                'statusCode': 200,
                'headers': {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*'
                },
                'body': json.dumps({
                    'operation': operation,
                    'status': 'success',
                    'message': 'Content ingested successfully'
                })
            }
        
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
        return {
            'statusCode': 400,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({'error': 'Invalid JSON in request body'})
        }
    except Exception as e:
        logger.error(f"Error handling API event: {str(e)}")
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({'error': 'Internal server error', 'details': str(e)})
        }


def get_stats() -> Dict[str, Any]:
    """
    获取系统统计信息
    """
    try:
        # TODO: 从向量数据库获取实际统计
        stats = {
            'total_documents': 0,
            'total_chunks': 0,
            'collection_name': os.environ.get('ZILLIZ_COLLECTION', 'rag_collection'),
            'last_update': None,
            'status': 'healthy'
        }
        
        try:
            from app.models.vector_store import VectorStoreModel
            vector_store = VectorStoreModel()
            db_stats = vector_store.get_stats()
            stats.update(db_stats)
        except:
            logger.warning("Unable to get vector store stats")
        
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps(stats)
        }
        
    except Exception as e:
        logger.error(f"Error getting stats: {str(e)}")
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({'error': 'Failed to get stats', 'details': str(e)})
        }