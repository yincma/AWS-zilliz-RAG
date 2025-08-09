"""
Lambda查询处理器 - 完整RAG版本
"""

import json
import os
import boto3
import logging
from vector_client import get_client

logger = logging.getLogger()
logger.setLevel(logging.INFO)

bedrock_runtime = boto3.client('bedrock-runtime', region_name=os.environ.get('AWS_REGION', 'us-east-1'))
vector_client = get_client()


def handler(event, context):
    """Lambda处理器函数 - 完整RAG流程"""
    try:
        # 解析请求
        body = json.loads(event.get('body', '{}')) if isinstance(event.get('body'), str) else event.get('body', {})
        query = body.get('query', '')
        top_k = body.get('top_k', 5)
        use_rag = body.get('use_rag', True)
        
        if not query:
            return {
                'statusCode': 400,
                'headers': {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*'
                },
                'body': json.dumps({'error': 'Query is required'})
            }
        
        logger.info(f"Processing query: {query}, use_rag: {use_rag}")
        
        # RAG流程
        if use_rag:
            # 1. 生成查询向量
            query_embedding = generate_embedding(query)
            
            # 2. 搜索相似文档
            relevant_docs = vector_client.search(query_embedding, top_k)
            
            # 3. 构建上下文
            context = build_context(relevant_docs)
            
            # 4. 生成增强的回答
            answer = generate_answer_with_context(query, context)
            
            response_data = {
                'answer': answer,
                'query': query,
                'sources': relevant_docs,
                'status': 'success',
                'mode': 'rag'
            }
        else:
            # 直接生成回答（无RAG）
            answer = generate_answer(query)
            response_data = {
                'answer': answer,
                'query': query,
                'sources': [],
                'status': 'success',
                'mode': 'direct'
            }
        
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps(response_data)
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
    """使用Titan生成文本向量"""
    try:
        response = bedrock_runtime.invoke_model(
            modelId=os.environ.get('EMBEDDING_MODEL_ID', 'amazon.titan-embed-text-v2:0'),
            body=json.dumps({
                "inputText": text
            })
        )
        
        result = json.loads(response['body'].read())
        embedding = result.get('embedding', [])
        
        if not embedding:
            logger.error("Failed to generate embedding")
            # 返回默认向量（1024维）
            return [0.0] * 1024
        
        return embedding
        
    except Exception as e:
        logger.error(f"Error generating embedding: {str(e)}")
        # 返回默认向量
        return [0.0] * 1024


def build_context(documents):
    """构建上下文"""
    if not documents:
        return ""
    
    context_parts = []
    for i, doc in enumerate(documents, 1):
        content = doc.get('content', '')
        source = doc.get('metadata', {}).get('source', 'unknown')
        context_parts.append(f"[文档{i} - 来源: {source}]\n{content}")
    
    return "\n\n".join(context_parts)


def generate_answer_with_context(query, context):
    """使用上下文生成增强的回答"""
    try:
        # 构建增强提示
        if context:
            prompt = f"""基于以下相关文档回答用户问题。如果文档中没有相关信息，请诚实地说明。

相关文档：
{context}

用户问题：{query}

请提供准确、详细的回答："""
        else:
            prompt = f"没有找到相关文档。基于一般知识回答：{query}"
        
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
                    "maxTokens": 1000,
                    "temperature": 0.7
                }
            })
        )
        
        result = json.loads(response['body'].read())
        
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
        
        # 备用解析路径
        if "content" in result:
            content = result["content"]
            if isinstance(content, list) and len(content) > 0:
                text = content[0].get("text", "")
                if text:
                    return text
        
        return "无法生成回答"
        
    except Exception as e:
        logger.error(f"Error generating answer with context: {str(e)}")
        return f"生成回答时出错: {str(e)}"


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