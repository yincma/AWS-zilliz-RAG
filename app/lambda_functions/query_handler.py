"""
Lambda函数 - RAG查询处理
"""

import json
import os
import boto3
from typing import Dict, List, Any
import logging

# 设置日志
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# 初始化AWS客户端
bedrock_runtime = boto3.client('bedrock-runtime', region_name=os.environ.get('AWS_REGION', 'us-east-1'))
s3_client = boto3.client('s3')


def lambda_handler(event, context):
    """
    RAG查询Lambda处理器
    """
    try:
        # 解析请求
        if event.get('body'):
            body = json.loads(event['body']) if isinstance(event['body'], str) else event['body']
        else:
            body = event
        
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
        
        logger.info(f"Processing query: {query}")
        
        # 1. 生成查询向量
        query_embedding = generate_embedding(query)
        
        # 2. 从向量数据库检索相关文档
        relevant_docs = search_similar_documents(query_embedding, top_k)
        
        # 3. 构建上下文
        context = build_context(relevant_docs)
        
        # 4. 生成回答
        answer = generate_answer(query, context)
        
        # 构建响应
        response = {
            'answer': answer,
            'sources': relevant_docs,
            'query': query,
            'context_used': len(relevant_docs) > 0
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
        logger.error(f"Error processing query: {str(e)}")
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({'error': str(e)})
        }


def generate_embedding(text: str) -> List[float]:
    """
    使用Titan生成文本向量
    """
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
        raise


def search_similar_documents(query_embedding: List[float], top_k: int) -> List[Dict]:
    """
    从Zilliz搜索相似文档
    """
    try:
        # 这里需要连接到Zilliz
        # 由于Lambda环境的限制，可能需要使用HTTP API或者打包pymilvus
        
        # 临时返回模拟数据
        return [
            {
                'content': 'RAG系统通过检索增强生成，提供更准确的回答。',
                'score': 0.95,
                'metadata': {'source': 'doc1.txt'}
            }
        ]
    
    except Exception as e:
        logger.error(f"Error searching documents: {str(e)}")
        return []


def build_context(documents: List[Dict]) -> str:
    """
    构建上下文
    """
    if not documents:
        return ""
    
    context_parts = []
    for doc in documents:
        context_parts.append(doc.get('content', ''))
    
    return "\n\n".join(context_parts)


def generate_answer(query: str, context: str) -> str:
    """
    使用Nova生成回答
    """
    try:
        # 构建提示
        if context:
            prompt = f"""基于以下上下文信息回答问题。

上下文：
{context}

问题：{query}

请提供准确、相关的回答。"""
        else:
            prompt = query
        
        # 调用Nova模型
        response = bedrock_runtime.invoke_model(
            modelId=os.environ.get('BEDROCK_MODEL_ID', 'amazon.nova-pro-v1:0'),
            body=json.dumps({
                "messages": [
                    {
                        "role": "user",
                        "content": [
                            {
                                "text": prompt
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
        logger.info(f"Nova response structure: {json.dumps(result, indent=2)[:500]}")  # 日志记录响应结构
        
        # Nova模型的正确响应解析路径
        if "output" in result:
            output = result["output"]
            if "message" in output:
                message = output["message"]
                if "content" in message:
                    content = message["content"]
                    if isinstance(content, list) and len(content) > 0:
                        text = content[0].get("text", "")
                        if text:
                            return text
        
        # 备用解析路径（向后兼容）
        if "content" in result:
            content = result["content"]
            if isinstance(content, list) and len(content) > 0:
                text = content[0].get("text", "")
                if text:
                    return text
        
        logger.warning("Unable to parse Nova response")
        return "无法生成回答"
    
    except Exception as e:
        logger.error(f"Error generating answer: {str(e)}")
        return f"生成回答时出错: {str(e)}"