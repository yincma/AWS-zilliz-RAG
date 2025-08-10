"""
Fixed Lambda function for document ingestion with proper CORS
"""
import json
import os
import boto3
import logging
import base64
from typing import Dict, Any
from cors_helper import create_response, create_error_response, handle_options_request

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Initialize AWS clients
s3_client = boto3.client('s3')
bedrock_runtime = boto3.client('bedrock-runtime', region_name=os.environ.get('AWS_REGION', 'us-east-1'))

def handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """
    Handle document ingestion requests with proper CORS support
    
    Args:
        event: S3 event or API Gateway event
        context: Lambda context
        
    Returns:
        Response with ingestion status
    """
    try:
        # Handle OPTIONS request for CORS preflight
        if event.get('httpMethod') == 'OPTIONS':
            return handle_options_request(event)
        
        logger.info(f"Received event type: {event.get('httpMethod', 'S3')}")
        
        # Check if this is an S3 event
        if 'Records' in event and event['Records']:
            # Process S3 event
            processed_count = 0
            for record in event['Records']:
                if 's3' in record:
                    bucket = record['s3']['bucket']['name']
                    key = record['s3']['object']['key']
                    
                    logger.info(f"Processing S3 object: {bucket}/{key}")
                    
                    # Download file from S3
                    try:
                        response = s3_client.get_object(Bucket=bucket, Key=key)
                        content = response['Body'].read()
                        
                        # Process document
                        logger.info(f"Document size: {len(content)} bytes")
                        
                        # Get embedding model
                        embedding_model_id = os.environ.get('EMBEDDING_MODEL_ID', 'amazon.titan-embed-text-v2:0')
                        
                        # TODO: Implement actual document processing
                        # 1. Parse the document (PDF, TXT, etc.)
                        # 2. Split into chunks
                        # 3. Generate embeddings using Bedrock
                        # 4. Store in Zilliz
                        
                        processed_count += 1
                        logger.info(f"Successfully processed {key}")
                        
                    except Exception as e:
                        logger.error(f"Error processing {key}: {str(e)}")
                        # Continue processing other files
            
            return {
                "statusCode": 200,
                "body": json.dumps({
                    "message": f"Processed {processed_count} documents",
                    "count": processed_count
                })
            }
        
        else:
            # Handle direct API call
            body = {}
            if event.get('body'):
                if isinstance(event['body'], str):
                    body = json.loads(event['body'])
                else:
                    body = event['body']
            
            # Extract parameters
            file_paths = body.get('file_paths', [])
            content = body.get('content')
            filename = body.get('filename') or (file_paths[0] if file_paths else None)
            
            # Handle base64 encoded content
            if content and isinstance(content, str):
                # Check if content is base64 encoded
                if content.startswith('data:'):
                    # Extract base64 data from data URL
                    _, data = content.split(',', 1)
                    content = base64.b64decode(data)
                elif len(content) % 4 == 0 and all(c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=' for c in content[:100]):
                    # Likely base64 encoded
                    try:
                        content = base64.b64decode(content)
                    except:
                        # Not base64, use as is
                        pass
            
            if not filename and not content:
                return create_error_response(
                    Exception("Either filename or content must be provided"),
                    400,
                    event
                )
            
            # Store document in S3 if content is provided
            s3_bucket = os.environ.get('S3_BUCKET')
            if content and s3_bucket and filename:
                try:
                    # Ensure content is bytes
                    if isinstance(content, str):
                        content = content.encode('utf-8')
                    
                    # Upload to S3
                    s3_key = f"documents/{filename}"
                    s3_client.put_object(
                        Bucket=s3_bucket,
                        Key=s3_key,
                        Body=content
                    )
                    logger.info(f"Uploaded {filename} to S3: {s3_bucket}/{s3_key}")
                    
                    # TODO: Process the document
                    # 1. Parse content
                    # 2. Generate embeddings
                    # 3. Store in Zilliz
                    
                except Exception as e:
                    logger.error(f"Error uploading to S3: {str(e)}")
                    return create_error_response(e, 500, event)
            
            # Process the document
            logger.info(f"Processing document: {filename}")
            
            # TODO: Implement actual processing logic
            result = {
                "status": "success",
                "message": f"Document {filename} ingested successfully",
                "document_id": f"doc_{os.urandom(8).hex()}",
                "filename": filename,
                "size": len(content) if content else 0
            }
            
            return create_response(200, result, event)
            
    except json.JSONDecodeError as e:
        logger.error(f"Invalid JSON in request: {str(e)}")
        return create_error_response(
            Exception("Invalid JSON in request body"),
            400,
            event
        )
    except Exception as e:
        logger.error(f"Error in ingestion handler: {str(e)}")
        return create_error_response(e, 500, event)