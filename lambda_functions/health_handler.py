"""
Lambda健康检查处理器
"""

import json
from datetime import datetime


def handler(event, context):
    """健康检查Lambda处理器"""
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps({
            'status': 'healthy',
            'timestamp': datetime.now().isoformat(),
            'service': 'RAG System Lambda',
            'version': '1.0.0'
        })
    }