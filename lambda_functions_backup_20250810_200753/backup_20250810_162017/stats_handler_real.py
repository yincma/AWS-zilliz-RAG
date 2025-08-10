"""
Real stats handler for document and vector statistics
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
    """Get real statistics from S3"""
    try:
        bucket = os.environ.get('S3_BUCKET', 'rag-documents-375004070918-us-east-1')
        
        # Count documents in S3
        doc_count = 0
        vector_count = 0
        
        try:
            # Count documents
            response = s3_client.list_objects_v2(
                Bucket=bucket,
                Prefix='documents/',
                MaxKeys=1000
            )
            doc_count = response.get('KeyCount', 0)
            
            # Count embeddings
            emb_response = s3_client.list_objects_v2(
                Bucket=bucket,
                Prefix='embeddings/',
                MaxKeys=1000
            )
            
            # Each embedding file contains multiple vectors
            for obj in emb_response.get('Contents', []):
                try:
                    # Get the embedding file to count vectors
                    emb_obj = s3_client.get_object(Bucket=bucket, Key=obj['Key'])
                    emb_data = json.loads(emb_obj['Body'].read())
                    vector_count += len(emb_data)
                except:
                    pass
                    
        except Exception as e:
            logger.warning(f"Error counting S3 objects: {str(e)}")
        
        stats = {
            'documents': doc_count,
            'vectors': vector_count,
            'dimension': 1536,  # Titan embedding dimension
            'collection': os.environ.get('ZILLIZ_COLLECTION', 'rag_collection'),
            'status': 'operational',
            's3_bucket': bucket
        }
        
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'GET,OPTIONS',
                'Access-Control-Allow-Headers': 'Content-Type'
            },
            'body': json.dumps(stats)
        }
        
    except Exception as e:
        logger.error(f"Error getting stats: {str(e)}")
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({'error': str(e)})
        }
