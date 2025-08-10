"""
Real document listing handler
"""
import json
import os
import boto3
import logging
from typing import Dict, Any

logger = logging.getLogger()
logger.setLevel(logging.INFO)

s3_client = boto3.client('s3')

def handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """List real documents from S3"""
    try:
        bucket = os.environ.get('S3_BUCKET', 'rag-documents-375004070918-us-east-1')
        
        # List documents from S3
        documents = []
        
        try:
            response = s3_client.list_objects_v2(
                Bucket=bucket,
                Prefix='documents/',
                MaxKeys=100
            )
            
            for obj in response.get('Contents', []):
                # Extract filename from key
                filename = obj['Key'].replace('documents/', '')
                if filename:  # Skip the prefix itself
                    # Parse filename to extract original name
                    parts = filename.split('_', 2)
                    display_name = parts[2] if len(parts) > 2 else filename
                    
                    documents.append({
                        'name': display_name,
                        'key': obj['Key'],
                        'size': obj['Size'],
                        'modified': obj['LastModified'].isoformat(),
                        'type': 'text/plain'
                    })
                    
        except Exception as e:
            logger.warning(f"Error listing S3 objects: {str(e)}")
        
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'GET,OPTIONS',
                'Access-Control-Allow-Headers': 'Content-Type'
            },
            'body': json.dumps({'documents': documents})
        }
        
    except Exception as e:
        logger.error(f"Error listing documents: {str(e)}")
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({'error': str(e)})
        }
