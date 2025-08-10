"""
Lambda function for document ingestion
"""
import json
import os
import boto3
import logging
from typing import Dict, Any

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Initialize AWS clients
s3_client = boto3.client('s3')
bedrock_runtime = boto3.client('bedrock-runtime', region_name=os.environ.get('AWS_REGION', 'us-east-1'))

def handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """
    Handle document ingestion requests
    
    Args:
        event: S3 event or API Gateway event
        context: Lambda context
        
    Returns:
        Response with ingestion status
    """
    try:
        logger.info(f"Received event: {json.dumps(event)}")
        
        # Check if this is an S3 event
        if 'Records' in event and event['Records']:
            # Process S3 event
            for record in event['Records']:
                if 's3' in record:
                    bucket = record['s3']['bucket']['name']
                    key = record['s3']['object']['key']
                    
                    logger.info(f"Processing S3 object: {bucket}/{key}")
                    
                    # Download file from S3
                    try:
                        response = s3_client.get_object(Bucket=bucket, Key=key)
                        content = response['Body'].read()
                        
                        # Process document (placeholder logic)
                        logger.info(f"Document size: {len(content)} bytes")
                        
                        # Generate embeddings using Titan
                        embedding_model_id = os.environ.get('EMBEDDING_MODEL_ID', 'amazon.titan-embed-text-v2:0')
                        
                        # Here you would:
                        # 1. Parse the document
                        # 2. Split into chunks
                        # 3. Generate embeddings
                        # 4. Store in Zilliz
                        
                        logger.info(f"Successfully processed {key}")
                        
                    except Exception as e:
                        logger.error(f"Error processing {key}: {str(e)}")
                        raise
            
            return {
                "statusCode": 200,
                "body": json.dumps({
                    "message": "Documents processed successfully",
                    "count": len(event['Records'])
                })
            }
            
        else:
            # Handle direct API call
            body = json.loads(event.get('body', '{}')) if event.get('body') else {}
            
            document_url = body.get('document_url')
            document_content = body.get('content')
            
            if not document_url and not document_content:
                return {
                    "statusCode": 400,
                    "headers": {
                        "Content-Type": "application/json",
                        "Access-Control-Allow-Origin": "*"
                    },
                    "body": json.dumps({
                        "error": "Either document_url or content must be provided"
                    })
                }
            
            # Process the document
            logger.info("Processing document from API request")
            
            # Placeholder for document processing logic
            result = {
                "status": "success",
                "message": "Document ingested successfully",
                "document_id": "doc_" + os.urandom(8).hex()
            }
            
            return {
                "statusCode": 200,
                "headers": {
                    "Content-Type": "application/json",
                    "Access-Control-Allow-Origin": "*",
                    "Access-Control-Allow-Headers": "Content-Type",
                    "Access-Control-Allow-Methods": "OPTIONS,POST"
                },
                "body": json.dumps(result)
            }
            
    except Exception as e:
        logger.error(f"Error in ingestion handler: {str(e)}")
        return {
            "statusCode": 500,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({
                "error": str(e),
                "message": "Internal server error during ingestion"
            })
        }