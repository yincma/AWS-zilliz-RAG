"""
Lambda文档摄入处理器 - 简化版本
"""

import json
import os
import boto3
import logging
import uuid
from datetime import datetime

logger = logging.getLogger()
logger.setLevel(logging.INFO)

s3_client = boto3.client('s3')
bedrock_runtime = boto3.client('bedrock-runtime', region_name=os.environ.get('AWS_REGION', 'us-east-1'))

S3_BUCKET = os.environ.get('S3_BUCKET', 'rag-documents-375004070918-us-east-1')


def handler(event, context):
    """Lambda处理器函数"""
    try:
        # 解析请求
        body = json.loads(event.get('body', '{}')) if isinstance(event.get('body'), str) else event.get('body', {})
        content = body.get('content', '')
        filename = body.get('filename', f'doc_{uuid.uuid4().hex}.txt')
        
        if not content:
            return {
                'statusCode': 400,
                'headers': {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*'
                },
                'body': json.dumps({'error': 'Content is required'})
            }
        
        logger.info(f"Processing document: {filename}")
        
        # 上传到S3
        s3_key = f"documents/{datetime.now().strftime('%Y/%m/%d')}/{filename}"
        s3_client.put_object(
            Bucket=S3_BUCKET,
            Key=s3_key,
            Body=content.encode('utf-8'),
            ContentType='text/plain'
        )
        
        # 生成向量（简化版本）
        embedding = generate_embedding(content[:500])  # 只使用前500字符
        
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({
                'message': 'Document uploaded successfully',
                'filename': filename,
                's3_key': s3_key,
                'embedding_dimension': len(embedding) if embedding else 0
            })
        }
        
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({'error': str(e)})
        }


def generate_embedding(text):
    """生成文本向量"""
    try:
        response = bedrock_runtime.invoke_model(
            modelId=os.environ.get('EMBEDDING_MODEL_ID', 'amazon.titan-embed-image-v1'),
            body=json.dumps({
                "inputText": text
            })
        )
        
        result = json.loads(response['body'].read())
        return result.get('embedding', [])
        
    except Exception as e:
        logger.error(f"Error generating embedding: {str(e)}")
        return []
EOF < /dev/null