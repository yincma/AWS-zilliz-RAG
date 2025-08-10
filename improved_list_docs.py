import json
import os
import boto3

def handler(event, context):
    """List documents from S3 with improved naming"""
    try:
        s3 = boto3.client('s3')
        bucket = os.environ.get('S3_BUCKET')
        if not bucket:
            raise ValueError("S3_BUCKET environment variable is required")
        
        documents = []
        
        try:
            response = s3.list_objects_v2(
                Bucket=bucket,
                Prefix='documents/',
                MaxKeys=100
            )
            
            if 'Contents' in response:
                for obj in response['Contents']:
                    key = obj['Key']
                    if key != 'documents/':  # Skip directory itself
                        # Extract original filename from key
                        # Format: documents/YYYYMMDD_HHMMSS_hash_originalname
                        filename = key.replace('documents/', '')
                        parts = filename.split('_', 3)
                        
                        # Get the original name (after timestamp and hash)
                        display_name = parts[3] if len(parts) > 3 else filename
                        
                        documents.append({
                            'name': display_name,  # Show friendly name
                            'key': key,  # Keep full S3 key for operations
                            'size': obj['Size'],
                            'modified': obj['LastModified'].isoformat()
                        })
        except Exception as e:
            print(f"Error listing documents: {str(e)}")
        
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
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({'error': str(e)})
        }