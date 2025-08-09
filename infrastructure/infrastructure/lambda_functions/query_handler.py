"""
Lambda查询处理器 - 简化版本
"""

import json
import os
import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

bedrock_runtime = boto3.client('bedrock-runtime', region_name=os.environ.get('AWS_REGION', 'us-east-1'))


def handler(event, context):
    """Lambda处理器函数"""
    try:
        # 解析请求
        body = json.loads(event.get('body', '{}')) if isinstance(event.get('body'), str) else event.get('body', {})
        query = body.get('query', '')
        
        if not query:
            return {
                'statusCode': 400,
                'headers': {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*'
                },
                'body': json.dumps({'error': 'Query is required'})
            }
        
        logger.info(f"Processing query: {query}")
        
        # 生成回答
        answer = generate_answer(query)
        
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({
                'answer': answer,
                'query': query,
                'status': 'success'
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


def generate_answer(query):
    """使用Bedrock生成回答"""
    try:
        response = bedrock_runtime.invoke_model(
            modelId=os.environ.get('BEDROCK_MODEL_ID', 'amazon.nova-pro-v1:0'),
            body=json.dumps({
                "messages": [
                    {
                        "role": "user",
                        "content": [
                            {
                                "text": query
                            }
                        ]
                    }
                ],
                "inferenceConfig": {
                    "maxTokens": 500,
                    "temperature": 0.7
                }
            })
        )
        
        result = json.loads(response['body'].read())
        
        if "content" in result:
            content = result["content"]
            if isinstance(content, list) and len(content) > 0:
                return content[0].get("text", "无法生成回答")
        
        return "无法生成回答"
        
    except Exception as e:
        logger.error(f"Error generating answer: {str(e)}")
        return f"生成回答时出错: {str(e)}"
EOF < /dev/null