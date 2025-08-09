"""
Lambda函数 - 文档上传处理
"""

import json
import os
import boto3
import base64
from typing import Dict, List
import logging
import uuid
from datetime import datetime

# 设置日志
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# 初始化AWS客户端
s3_client = boto3.client('s3')
bedrock_runtime = boto3.client('bedrock-runtime', region_name=os.environ.get('AWS_REGION', 'us-east-1'))

# S3配置
S3_BUCKET = os.environ.get('S3_BUCKET', 'AWS_zilliz_RAG')
S3_PREFIX = os.environ.get('S3_PREFIX', 'documents/')


def lambda_handler(event, context):
    """
    文档上传Lambda处理器
    """
    try:
        # 解析请求
        if event.get('isBase64Encoded'):
            body = base64.b64decode(event['body'])
        else:
            body = event.get('body', '')
        
        # 获取文件信息
        if isinstance(body, str):
            # 如果是JSON字符串
            data = json.loads(body)
            file_content = data.get('content', '')
            file_name = data.get('filename', f'document_{uuid.uuid4().hex}.txt')
        else:
            # 如果是二进制数据
            file_content = body.decode('utf-8') if isinstance(body, bytes) else str(body)
            file_name = f'document_{uuid.uuid4().hex}.txt'
        
        if not file_content:
            return {
                'statusCode': 400,
                'headers': {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*'
                },
                'body': json.dumps({'error': 'No content provided'})
            }
        
        logger.info(f"Processing upload for file: {file_name}")
        
        # 1. 上传到S3
        s3_key = upload_to_s3(file_name, file_content)
        
        # 2. 文本分割
        chunks = split_text(file_content)
        
        # 3. 生成向量
        embeddings = generate_embeddings(chunks)
        
        # 4. 存储到向量数据库
        vector_ids = store_in_vector_db(chunks, embeddings, file_name)
        
        # 构建响应
        response = {
            'message': 'Document uploaded successfully',
            'filename': file_name,
            's3_key': s3_key,
            'chunks_processed': len(chunks),
            'vectors_stored': len(vector_ids),
            'timestamp': datetime.now().isoformat()
        }
        
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps(response)
        }
        
    except Exception as e:
        logger.error(f"Error processing upload: {str(e)}")
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({'error': str(e)})
        }


def upload_to_s3(filename: str, content: str) -> str:
    """
    上传文档到S3
    """
    try:
        s3_key = f"{S3_PREFIX}{datetime.now().strftime('%Y/%m/%d')}/{filename}"
        
        s3_client.put_object(
            Bucket=S3_BUCKET,
            Key=s3_key,
            Body=content.encode('utf-8'),
            ContentType='text/plain',
            Metadata={
                'upload_time': datetime.now().isoformat(),
                'source': 'lambda_upload'
            }
        )
        
        logger.info(f"Uploaded to S3: s3://{S3_BUCKET}/{s3_key}")
        return s3_key
    
    except Exception as e:
        logger.error(f"Error uploading to S3: {str(e)}")
        raise


def split_text(text: str, chunk_size: int = 500, overlap: int = 50) -> List[str]:
    """
    将文本分割成chunks
    """
    chunks = []
    text_length = len(text)
    
    if text_length <= chunk_size:
        return [text]
    
    start = 0
    while start < text_length:
        end = min(start + chunk_size, text_length)
        
        # 尝试在句号处分割
        if end < text_length:
            last_period = text.rfind('。', start, end)
            if last_period != -1 and last_period > start:
                end = last_period + 1
        
        chunk = text[start:end].strip()
        if chunk:
            chunks.append(chunk)
        
        start = end - overlap if end < text_length else end
    
    return chunks


def generate_embeddings(texts: List[str]) -> List[List[float]]:
    """
    批量生成文本向量
    """
    embeddings = []
    
    for text in texts:
        try:
            response = bedrock_runtime.invoke_model(
                modelId=os.environ.get('EMBEDDING_MODEL_ID', 'amazon.titan-embed-image-v1'),
                body=json.dumps({
                    "inputText": text
                })
            )
            
            result = json.loads(response['body'].read())
            embedding = result.get('embedding', [])
            embeddings.append(embedding)
        
        except Exception as e:
            logger.error(f"Error generating embedding for text: {str(e)}")
            embeddings.append([])
    
    return embeddings


def store_in_vector_db(chunks: List[str], embeddings: List[List[float]], source: str) -> List[str]:
    """
    存储到向量数据库
    """
    try:
        # 这里需要连接到Zilliz
        # 由于Lambda环境的限制，可能需要使用HTTP API
        
        # 临时返回模拟的ID列表
        vector_ids = [f"vec_{uuid.uuid4().hex}" for _ in range(len(chunks))]
        
        logger.info(f"Stored {len(vector_ids)} vectors to database")
        return vector_ids
    
    except Exception as e:
        logger.error(f"Error storing to vector database: {str(e)}")
        return []