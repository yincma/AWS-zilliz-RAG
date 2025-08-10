"""
Lambda function for handling RAG queries
"""
import json
import os
import sys
import boto3
import logging
from typing import Dict, Any, List

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Initialize AWS clients
bedrock_runtime = boto3.client('bedrock-runtime', region_name=os.environ.get('AWS_REGION', 'us-east-1'))

def handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """
    Handle RAG query requests
    
    Args:
        event: API Gateway event containing query parameters
        context: Lambda context
        
    Returns:
        API Gateway response with query results
    """
    try:
        # Parse request body
        if event.get('body'):
            if isinstance(event['body'], str):
                body = json.loads(event['body'])
            else:
                body = event['body']
        else:
            body = {}
        
        # Extract parameters
        query = body.get('query', '')
        top_k = body.get('top_k', 5)
        use_rag = body.get('use_rag', True)
        
        logger.info(f"Processing query: {query[:100]}...")
        
        # Get environment variables
        model_id = os.environ.get('BEDROCK_MODEL_ID', 'amazon.nova-lite-v1:0')
        embedding_model_id = os.environ.get('EMBEDDING_MODEL_ID', 'amazon.titan-embed-text-v2:0')
        
        # Prepare response
        if use_rag:
            # RAG logic would go here
            # For now, return a mock response
            response_text = f"RAG response for query: {query}"
            sources = [
                {
                    "content": "Sample document content",
                    "metadata": {"source": "document1.pdf", "page": 1}
                }
            ]
        else:
            # Direct LLM query
            prompt = f"Human: {query}\n\nAssistant:"
            
            # Call Bedrock
            try:
                bedrock_response = bedrock_runtime.invoke_model(
                    modelId=model_id,
                    body=json.dumps({
                        "prompt": prompt,
                        "max_gen_len": 1000,
                        "temperature": 0.7,
                        "top_p": 0.9
                    })
                )
                
                response_body = json.loads(bedrock_response['body'].read())
                response_text = response_body.get('generation', 'No response generated')
            except Exception as e:
                logger.error(f"Bedrock error: {str(e)}")
                response_text = f"Error calling Bedrock: {str(e)}"
            
            sources = []
        
        # Build response
        response = {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Methods": "OPTIONS,POST,GET"
            },
            "body": json.dumps({
                "answer": response_text,
                "sources": sources,
                "query": query,
                "use_rag": use_rag,
                "top_k": top_k
            })
        }
        
        logger.info("Query processed successfully")
        return response
        
    except Exception as e:
        logger.error(f"Error processing request: {str(e)}")
        return {
            "statusCode": 500,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({
                "error": str(e),
                "message": "Internal server error"
            })
        }