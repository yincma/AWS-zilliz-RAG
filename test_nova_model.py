"""
测试Nova模型响应格式
"""

import json
import boto3
import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# 初始化bedrock客户端
bedrock_runtime = boto3.client(
    'bedrock-runtime',
    region_name='us-east-1'
)

def test_nova_model():
    """测试Nova模型的响应格式"""
    
    test_query = "What is RAG in machine learning?"
    
    try:
        # 使用Nova模型
        response = bedrock_runtime.invoke_model(
            modelId='amazon.nova-pro-v1:0',
            body=json.dumps({
                "messages": [
                    {
                        "role": "user",
                        "content": [
                            {
                                "text": test_query
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
        
        # 读取响应
        response_body = json.loads(response['body'].read())
        
        # 打印完整响应以了解结构
        print("完整响应结构:")
        print(json.dumps(response_body, indent=2, ensure_ascii=False))
        
        # 尝试不同的解析方式
        print("\n尝试解析响应:")
        
        # 方式1: 检查output字段
        if "output" in response_body:
            output = response_body["output"]
            if "message" in output:
                message = output["message"]
                if "content" in message:
                    content = message["content"]
                    if isinstance(content, list) and len(content) > 0:
                        text = content[0].get("text", "")
                        print(f"从output.message.content解析到: {text}")
        
        # 方式2: 直接检查content字段
        if "content" in response_body:
            content = response_body["content"]
            if isinstance(content, list) and len(content) > 0:
                text = content[0].get("text", "")
                print(f"从content解析到: {text}")
        
        # 方式3: 检查completion字段
        if "completion" in response_body:
            completion = response_body["completion"]
            print(f"从completion解析到: {completion}")
        
        return response_body
        
    except Exception as e:
        print(f"错误: {str(e)}")
        import traceback
        traceback.print_exc()
        return None


if __name__ == "__main__":
    print("测试Nova模型响应格式...")
    result = test_nova_model()
    
    if result:
        print("\n测试成功!")
    else:
        print("\n测试失败!")