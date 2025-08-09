"""
文档摄入处理Lambda函数
"""
import json
import os
import sys

# 添加应用路径
sys.path.insert(0, '/var/task')


def handler(event, context):
    """
    处理文档摄入请求
    """
    try:
        # 解析请求体
        body = json.loads(event.get('body', '{}'))
        document_url = body.get('document_url', '')
        document_type = body.get('document_type', 'pdf')
        
        if not document_url:
            return {
                'statusCode': 400,
                'headers': {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*'
                },
                'body': json.dumps({
                    'error': 'Document URL is required'
                })
            }
        
        # 这里应该调用实际的文档处理逻辑
        # 临时返回示例响应
        result = {
            'message': f"Document ingestion started for: {document_url}",
            'document_type': document_type,
            'status': 'processing'
        }
        
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps(result)
        }
        
    except Exception as e:
        print(f"Error processing document: {str(e)}")
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({
                'error': 'Internal server error',
                'message': str(e)
            })
        }