"""
Fixed Lambda function for handling RAG queries with proper CORS
"""
import json
import os
import boto3
import logging
from typing import Dict, Any, List
from cors_helper import create_response, create_error_response, handle_options_request

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Initialize AWS clients
bedrock_runtime = boto3.client('bedrock-runtime', region_name=os.environ.get('AWS_REGION', 'us-east-1'))

def handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """
    Handle RAG query requests with proper CORS support
    
    Args:
        event: API Gateway event containing query parameters
        context: Lambda context
        
    Returns:
        API Gateway response with query results and CORS headers
    """
    try:
        # Handle OPTIONS request for CORS preflight
        if event.get('httpMethod') == 'OPTIONS':
            return handle_options_request(event)
        
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
        zilliz_endpoint = os.environ.get('ZILLIZ_ENDPOINT')
        zilliz_token = os.environ.get('ZILLIZ_TOKEN')
        
        # Prepare response
        if use_rag and zilliz_endpoint and zilliz_token:
            # TODO: Implement actual RAG logic with Zilliz
            # For now, return a mock response
            response_text = f"This is a RAG-enhanced response for your query: {query}"
            sources = [
                {
                    "content": "Sample document content related to your query",
                    "metadata": {
                        "source": "document1.pdf",
                        "page": 1,
                        "relevance_score": 0.92
                    }
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
        
        # Build successful response
        response_data = {
            "answer": response_text,
            "sources": sources,
            "query": query,
            "use_rag": use_rag,
            "top_k": top_k,
            "model": model_id
        }
        
        logger.info("Query processed successfully")
        return create_response(200, response_data, event)
        
    except json.JSONDecodeError as e:
        logger.error(f"Invalid JSON in request: {str(e)}")
        return create_error_response(
            Exception("Invalid JSON in request body"),
            400,
            event
        )
    except Exception as e:
        logger.error(f"Error processing request: {str(e)}")
        return create_error_response(e, 500, event)