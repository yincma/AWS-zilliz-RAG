"""
Lambda function for handling collection statistics and document management
"""
import json
import os
import boto3
import logging
from typing import Dict, Any
from cors_helper import create_response, create_error_response, handle_options_request

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Initialize AWS clients
s3_client = boto3.client('s3')

def handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """
    Handle collection statistics and document management requests
    
    Args:
        event: API Gateway event
        context: Lambda context
        
    Returns:
        API Gateway response with appropriate data
    """
    try:
        # Handle OPTIONS request for CORS preflight
        if event.get('httpMethod') == 'OPTIONS':
            return handle_options_request(event)
        
        # Get the resource path to determine the operation
        resource = event.get('resource', '')
        http_method = event.get('httpMethod', '')
        
        logger.info(f"Handling {http_method} request for {resource}")
        
        # Get environment variables
        s3_bucket = os.environ.get('S3_BUCKET')
        zilliz_collection = os.environ.get('ZILLIZ_COLLECTION', 'rag_collection')
        
        # Route based on resource and method
        if '/stats' in resource and http_method == 'GET':
            # Get collection statistics
            stats_data = {
                "collection_name": zilliz_collection,
                "total_documents": 0,  # TODO: Implement actual count from Zilliz
                "total_vectors": 0,    # TODO: Implement actual count from Zilliz
                "embedding_dimension": 1536,
                "index_type": "IVF_FLAT",
                "status": "healthy",
                "last_updated": None
            }
            
            # Get document count from S3 if available
            if s3_bucket:
                try:
                    response = s3_client.list_objects_v2(
                        Bucket=s3_bucket,
                        Prefix='documents/',
                        MaxKeys=1000
                    )
                    stats_data['total_documents'] = response.get('KeyCount', 0)
                except Exception as e:
                    logger.warning(f"Could not get S3 document count: {str(e)}")
            
            return create_response(200, stats_data, event)
        
        elif '/documents' in resource and http_method == 'GET':
            # List documents
            documents = []
            
            if s3_bucket:
                try:
                    response = s3_client.list_objects_v2(
                        Bucket=s3_bucket,
                        Prefix='documents/',
                        MaxKeys=100
                    )
                    
                    for obj in response.get('Contents', []):
                        documents.append({
                            "filename": obj['Key'].replace('documents/', ''),
                            "size": obj['Size'],
                            "last_modified": obj['LastModified'].isoformat(),
                            "etag": obj.get('ETag', '').strip('"')
                        })
                except Exception as e:
                    logger.warning(f"Could not list S3 documents: {str(e)}")
            
            return create_response(200, {"documents": documents}, event)
        
        elif '/documents' in resource and http_method == 'DELETE':
            # Delete a specific document
            path_params = event.get('pathParameters', {})
            filename = path_params.get('proxy') or path_params.get('filename')
            
            if not filename:
                return create_error_response(
                    Exception("Filename not provided"),
                    400,
                    event
                )
            
            if s3_bucket:
                try:
                    s3_client.delete_object(
                        Bucket=s3_bucket,
                        Key=f'documents/{filename}'
                    )
                    
                    # TODO: Also delete from Zilliz collection
                    
                    return create_response(
                        200,
                        {"message": f"Document {filename} deleted successfully"},
                        event
                    )
                except Exception as e:
                    logger.error(f"Error deleting document: {str(e)}")
                    return create_error_response(e, 500, event)
            else:
                return create_error_response(
                    Exception("S3 bucket not configured"),
                    500,
                    event
                )
        
        elif '/clear' in resource and http_method == 'DELETE':
            # Clear the entire collection
            # TODO: Implement actual Zilliz collection clearing
            
            # Clear S3 documents
            if s3_bucket:
                try:
                    response = s3_client.list_objects_v2(
                        Bucket=s3_bucket,
                        Prefix='documents/'
                    )
                    
                    if 'Contents' in response:
                        objects = [{'Key': obj['Key']} for obj in response['Contents']]
                        s3_client.delete_objects(
                            Bucket=s3_bucket,
                            Delete={'Objects': objects}
                        )
                    
                    return create_response(
                        200,
                        {"message": "Collection cleared successfully"},
                        event
                    )
                except Exception as e:
                    logger.error(f"Error clearing collection: {str(e)}")
                    return create_error_response(e, 500, event)
            else:
                return create_response(
                    200,
                    {"message": "Collection cleared (no S3 bucket configured)"},
                    event
                )
        
        else:
            # Unknown endpoint
            return create_error_response(
                Exception(f"Unknown endpoint: {http_method} {resource}"),
                404,
                event
            )
        
    except Exception as e:
        logger.error(f"Error processing request: {str(e)}")
        return create_error_response(e, 500, event)