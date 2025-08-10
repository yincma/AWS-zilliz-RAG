"""
LLM Model - 大语言模型
使用Amazon Bedrock Nova模型进行文本生成
"""

from typing import Optional, Dict, Any, List
import json
import logging
import boto3
from botocore.exceptions import ClientError

from config.settings import settings

logger = logging.getLogger(__name__)


class LLMModel:
    """
    LLM模型类
    使用Amazon Bedrock的Nova模型
    """
    
    def __init__(self, model_id: Optional[str] = None):
        """
        初始化LLM模型
        
        Args:
            model_id: Bedrock模型ID，默认使用配置中的值
        """
        self.model_id = model_id or settings.aws.bedrock_model_id
        self.max_tokens = settings.rag.max_tokens
        self.temperature = settings.rag.temperature
        
        # 初始化Bedrock客户端
        self.bedrock_client = boto3.client(
            'bedrock-runtime',
            region_name=settings.aws.region,
            aws_access_key_id=settings.aws.access_key_id,
            aws_secret_access_key=settings.aws.secret_access_key
        )
        
        logger.info(f"初始化LLM模型: {self.model_id}")
    
    def generate(self, prompt: str, **kwargs) -> str:
        """
        生成文本响应
        
        Args:
            prompt: 输入提示
            **kwargs: 额外的生成参数
            
        Returns:
            生成的文本
        """
        try:
            # 合并参数
            max_tokens = kwargs.get('max_tokens', self.max_tokens)
            temperature = kwargs.get('temperature', self.temperature)
            
            # 准备请求体（Nova模型格式）
            # Nova Pro需要content为数组格式
            request_body = {
                "messages": [
                    {
                        "role": "user",
                        "content": [{"text": prompt}]  # content必须是数组
                    }
                ],
                "inferenceConfig": {
                    "maxTokens": max_tokens,
                    "temperature": temperature
                }
            }
            
            # Nova Pro不支持system角色，将系统提示合并到用户消息中
            if 'system_prompt' in kwargs:
                combined_prompt = f"{kwargs['system_prompt']}\n\n{prompt}"
                request_body["messages"][0]["content"] = [{"text": combined_prompt}]
            
            # 调用Bedrock API
            response = self.bedrock_client.invoke_model(
                modelId=self.model_id,
                body=json.dumps(request_body),
                contentType='application/json',
                accept='application/json'
            )
            
            # 解析响应
            response_body = json.loads(response['body'].read())
            
            # Nova Pro模型的响应格式
            if 'output' in response_body:
                # Nova Pro的响应格式
                if 'message' in response_body['output']:
                    content = response_body['output']['message']['content']
                    if isinstance(content, list) and len(content) > 0:
                        return content[0].get('text', '')
                    elif isinstance(content, str):
                        return content
            elif 'content' in response_body:
                return response_body['content'][0]['text']
            elif 'completion' in response_body:
                return response_body['completion']
            else:
                raise ValueError(f"未知的响应格式: {response_body}")
            
        except ClientError as e:
            logger.error(f"Bedrock API调用失败: {e}")
            raise
        except Exception as e:
            logger.error(f"生成文本失败: {e}")
            raise
    
    def generate_with_context(self, query: str, context: str, 
                            system_prompt: Optional[str] = None) -> str:
        """
        基于上下文生成响应
        
        Args:
            query: 用户查询
            context: 检索到的上下文
            system_prompt: 系统提示
            
        Returns:
            生成的响应
        """
        # 使用默认系统提示或自定义提示
        if system_prompt is None:
            system_prompt = settings.rag.system_prompt
        
        # 构建完整的提示
        prompt = f"""基于以下上下文信息回答用户的问题。如果上下文中没有相关信息，请诚实地说你不知道。

上下文信息：
{context}

用户问题：{query}

请提供准确、有帮助的回答："""
        
        return self.generate(
            prompt=prompt,
            system_prompt=system_prompt
        )
    
    def batch_generate(self, prompts: List[str], **kwargs) -> List[str]:
        """
        批量生成文本
        
        Args:
            prompts: 提示列表
            **kwargs: 生成参数
            
        Returns:
            生成的文本列表
        """
        responses = []
        for prompt in prompts:
            try:
                response = self.generate(prompt, **kwargs)
                responses.append(response)
            except Exception as e:
                logger.error(f"批量生成失败: {e}")
                responses.append("")
        
        return responses
    
    def stream_generate(self, prompt: str, **kwargs):
        """
        流式生成文本（如果Nova支持）
        
        Args:
            prompt: 输入提示
            **kwargs: 生成参数
            
        Yields:
            生成的文本片段
        """
        try:
            # 准备请求体
            request_body = {
                "messages": [
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                "max_tokens": kwargs.get('max_tokens', self.max_tokens),
                "temperature": kwargs.get('temperature', self.temperature),
                "stream": True  # 启用流式响应
            }
            
            # 调用Bedrock API with streaming
            response = self.bedrock_client.invoke_model_with_response_stream(
                modelId=self.model_id,
                body=json.dumps(request_body),
                contentType='application/json',
                accept='application/json'
            )
            
            # 处理流式响应
            for event in response['body']:
                chunk = json.loads(event['chunk']['bytes'])
                if 'delta' in chunk and 'text' in chunk['delta']:
                    yield chunk['delta']['text']
                    
        except ClientError as e:
            logger.error(f"流式生成失败: {e}")
            # 如果不支持流式，回退到普通生成
            yield self.generate(prompt, **kwargs)
        except Exception as e:
            logger.error(f"流式生成异常: {e}")
            raise
    
    def test_connection(self) -> bool:
        """
        测试与Bedrock的连接
        
        Returns:
            连接是否成功
        """
        try:
            test_prompt = "Hello, please respond with 'OK'"
            response = self.generate(test_prompt, max_tokens=10)
            return bool(response)
        except Exception as e:
            logger.error(f"连接测试失败: {e}")
            return False