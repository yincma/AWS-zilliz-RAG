"""
查询处理Lambda函数
"""
import json
import os
import sys

# 添加应用路径
sys.path.insert(0, '/var/task')


def handler(event, context):
    """
    处理查询请求
    """
    try:
        # 解析请求体
        body = json.loads(event.get('body', '{}'))
        query = body.get('query', '')
        
        if not query:
            return {
                'statusCode': 400,
                'headers': {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*'
                },
                'body': json.dumps({
                    'error': 'Query is required'
                })
            }
        
        # 这里应该调用实际的RAG逻辑
        # 临时返回示例响应
        result = {
            'answer': f"Processing query: {query}",
            'sources': [],
            'status': 'success'
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
        print(f"Error processing query: {str(e)}")
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