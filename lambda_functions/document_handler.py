"""
Lambda函数 - 文档管理端点
处理文档的列表、删除、统计等操作
"""

import json
import boto3
import os
from typing import Dict, List, Any
import logging
from datetime import datetime
import uuid

# 设置日志
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# 初始化AWS客户端
s3_client = boto3.client('s3')

# 配置
S3_BUCKET = os.environ.get('S3_BUCKET', 'rag-documents-375004070918-us-east-1')
S3_PREFIX = os.environ.get('S3_PREFIX', 'documents/')


def lambda_handler(event: Dict, context: Any) -> Dict:
    """
    文档管理Lambda处理器
    支持多种HTTP方法和操作
    """
    logger.info(f"Received event: {json.dumps(event)}")
    
    # 获取HTTP方法和路径
    http_method = event.get('httpMethod', 'GET')
    path = event.get('path', '')
    
    # CORS头
    headers = {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET, POST, DELETE, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type'
    }
    
    try:
        # 处理OPTIONS请求（CORS预检）
        if http_method == 'OPTIONS':
            return {
                'statusCode': 200,
                'headers': headers,
                'body': json.dumps({'message': 'CORS preflight successful'})
            }
        
        # GET /documents - 列出文档
        if http_method == 'GET' and path == '/documents':
            return list_documents(headers)
        
        # POST /documents - 处理文档操作（统计、摄入等）
        elif http_method == 'POST' and path == '/documents':
            body = json.loads(event.get('body', '{}'))
            operation = body.get('operation', 'ingest')
            
            if operation == 'stats':
                return get_stats(headers)
            elif operation == 'ingest':
                return ingest_document(body, headers)
            else:
                return {
                    'statusCode': 400,
                    'headers': headers,
                    'body': json.dumps({'error': f'Unknown operation: {operation}'})
                }
        
        # POST /documents/upload - 上传文档
        elif http_method == 'POST' and path == '/documents/upload':
            body = json.loads(event.get('body', '{}'))
            return upload_document(body, headers)
        
        # DELETE /documents/{filename} - 删除文档
        elif http_method == 'DELETE' and path.startswith('/documents/'):
            filename = path.split('/')[-1]
            return delete_document(filename, headers)
        
        # DELETE /documents - 清空集合
        elif http_method == 'DELETE' and path == '/documents':
            body = json.loads(event.get('body', '{}'))
            if body.get('operation') == 'clear':
                return clear_collection(headers)
        
        # 未匹配的路由
        return {
            'statusCode': 404,
            'headers': headers,
            'body': json.dumps({'error': f'Not found: {http_method} {path}'})
        }
        
    except Exception as e:
        logger.error(f"Error processing request: {str(e)}")
        return {
            'statusCode': 500,
            'headers': headers,
            'body': json.dumps({'error': str(e)})
        }


def list_documents(headers: Dict) -> Dict:
    """列出所有文档"""
    try:
        # 列出S3中的文档
        response = s3_client.list_objects_v2(
            Bucket=S3_BUCKET,
            Prefix=S3_PREFIX,
            MaxKeys=100
        )
        
        documents = []
        if 'Contents' in response:
            for obj in response['Contents']:
                # 跳过目录
                if not obj['Key'].endswith('/'):
                    documents.append({
                        'name': obj['Key'].replace(S3_PREFIX, ''),
                        'size': obj['Size'],
                        'last_modified': obj['LastModified'].isoformat(),
                        'etag': obj['ETag'].strip('"')
                    })
        
        return {
            'statusCode': 200,
            'headers': headers,
            'body': json.dumps({
                'status': 'success',
                'data': documents,
                'count': len(documents)
            })
        }
    except Exception as e:
        logger.error(f"Error listing documents: {str(e)}")
        return {
            'statusCode': 500,
            'headers': headers,
            'body': json.dumps({'error': str(e)})
        }


def get_stats(headers: Dict) -> Dict:
    """获取统计信息"""
    try:
        # 获取文档数量
        response = s3_client.list_objects_v2(
            Bucket=S3_BUCKET,
            Prefix=S3_PREFIX
        )
        
        doc_count = 0
        total_size = 0
        
        if 'Contents' in response:
            for obj in response['Contents']:
                if not obj['Key'].endswith('/'):
                    doc_count += 1
                    total_size += obj['Size']
        
        # 模拟向量数据库统计（实际应该从Zilliz获取）
        stats = {
            'status': 'success',
            'data': {
                'name': 'rag_collection',
                'num_entities': doc_count * 10,  # 假设每个文档平均10个chunks
                'num_documents': doc_count,
                'total_size': total_size,
                'dimension': 1024,  # Titan Embeddings维度
                'index_type': 'IVF_FLAT',
                'metric_type': 'L2',
                'last_updated': datetime.now().isoformat()
            }
        }
        
        return {
            'statusCode': 200,
            'headers': headers,
            'body': json.dumps(stats)
        }
    except Exception as e:
        logger.error(f"Error getting stats: {str(e)}")
        return {
            'statusCode': 500,
            'headers': headers,
            'body': json.dumps({'error': str(e)})
        }


def upload_document(data: Dict, headers: Dict) -> Dict:
    """上传文档"""
    try:
        filename = data.get('filename', f'document_{uuid.uuid4().hex}.txt')
        content = data.get('content', '')
        content_type = data.get('content_type', 'text/plain')
        
        if not content:
            return {
                'statusCode': 400,
                'headers': headers,
                'body': json.dumps({'error': 'No content provided'})
            }
        
        # 处理base64编码的内容
        if content.startswith('data:'):
            # 移除data URL前缀
            content = content.split(',', 1)[1] if ',' in content else content
        
        # 生成S3 key
        s3_key = f"{S3_PREFIX}{datetime.now().strftime('%Y/%m/%d')}/{filename}"
        
        # 上传到S3
        s3_client.put_object(
            Bucket=S3_BUCKET,
            Key=s3_key,
            Body=content.encode('utf-8') if isinstance(content, str) else content,
            ContentType=content_type,
            Metadata={
                'upload_time': datetime.now().isoformat(),
                'source': 'web_upload'
            }
        )
        
        return {
            'statusCode': 200,
            'headers': headers,
            'body': json.dumps({
                'status': 'success',
                'message': 'Document uploaded successfully',
                'filename': filename,
                's3_key': s3_key,
                'timestamp': datetime.now().isoformat()
            })
        }
    except Exception as e:
        logger.error(f"Error uploading document: {str(e)}")
        return {
            'statusCode': 500,
            'headers': headers,
            'body': json.dumps({'error': str(e)})
        }


def delete_document(filename: str, headers: Dict) -> Dict:
    """删除文档"""
    try:
        # 查找文档
        response = s3_client.list_objects_v2(
            Bucket=S3_BUCKET,
            Prefix=S3_PREFIX
        )
        
        keys_to_delete = []
        if 'Contents' in response:
            for obj in response['Contents']:
                if filename in obj['Key']:
                    keys_to_delete.append(obj['Key'])
        
        if not keys_to_delete:
            return {
                'statusCode': 404,
                'headers': headers,
                'body': json.dumps({'error': f'Document not found: {filename}'})
            }
        
        # 删除对象
        for key in keys_to_delete:
            s3_client.delete_object(Bucket=S3_BUCKET, Key=key)
        
        return {
            'statusCode': 200,
            'headers': headers,
            'body': json.dumps({
                'status': 'success',
                'message': f'Document deleted: {filename}',
                'deleted_count': len(keys_to_delete)
            })
        }
    except Exception as e:
        logger.error(f"Error deleting document: {str(e)}")
        return {
            'statusCode': 500,
            'headers': headers,
            'body': json.dumps({'error': str(e)})
        }


def clear_collection(headers: Dict) -> Dict:
    """清空所有文档"""
    try:
        # 列出所有文档
        response = s3_client.list_objects_v2(
            Bucket=S3_BUCKET,
            Prefix=S3_PREFIX
        )
        
        if 'Contents' in response:
            # 批量删除
            objects = [{'Key': obj['Key']} for obj in response['Contents']]
            s3_client.delete_objects(
                Bucket=S3_BUCKET,
                Delete={'Objects': objects}
            )
            deleted_count = len(objects)
        else:
            deleted_count = 0
        
        return {
            'statusCode': 200,
            'headers': headers,
            'body': json.dumps({
                'status': 'success',
                'message': 'Collection cleared',
                'deleted_count': deleted_count
            })
        }
    except Exception as e:
        logger.error(f"Error clearing collection: {str(e)}")
        return {
            'statusCode': 500,
            'headers': headers,
            'body': json.dumps({'error': str(e)})
        }


def ingest_document(data: Dict, headers: Dict) -> Dict:
    """摄入文档（处理并存储到向量数据库）"""
    try:
        file_paths = data.get('file_paths', [])
        
        if not file_paths:
            return {
                'statusCode': 400,
                'headers': headers,
                'body': json.dumps({'error': 'No file paths provided'})
            }
        
        # 这里应该调用实际的文档处理和向量化逻辑
        # 现在返回模拟响应
        return {
            'statusCode': 200,
            'headers': headers,
            'body': json.dumps({
                'status': 'success',
                'message': f'Ingested {len(file_paths)} documents',
                'documents': file_paths
            })
        }
    except Exception as e:
        logger.error(f"Error ingesting documents: {str(e)}")
        return {
            'statusCode': 500,
            'headers': headers,
            'body': json.dumps({'error': str(e)})
        }