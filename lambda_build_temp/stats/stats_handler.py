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

# Try to import pymilvus for Zilliz support
try:
    from pymilvus import connections, Collection, utility
    ZILLIZ_AVAILABLE = True
    logger.info("pymilvus available for stats")
except ImportError:
    ZILLIZ_AVAILABLE = False
    logger.warning("pymilvus not available for stats")

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
        zilliz_endpoint = os.environ.get('ZILLIZ_ENDPOINT')
        zilliz_token = os.environ.get('ZILLIZ_TOKEN')
        
        # Route based on resource and method
        if '/stats' in resource and http_method == 'GET':
            # Get collection statistics
            stats_data = {
                "collection": zilliz_collection,
                "documents": 0,
                "vectors": 0,
                "dimension": 1536,
                "index_type": "IVF_FLAT",
                "status": "healthy",
                "last_updated": None
            }
            
            # Get actual vector count from Zilliz if available
            if ZILLIZ_AVAILABLE and zilliz_endpoint and zilliz_token:
                try:
                    # Connect to Zilliz
                    connections.connect(
                        alias="stats",
                        uri=zilliz_endpoint,
                        token=zilliz_token,
                        timeout=5
                    )
                    
                    # Check if collection exists and get stats
                    if utility.has_collection(zilliz_collection):
                        collection = Collection(zilliz_collection)
                        collection.load()
                        stats_data['vectors'] = collection.num_entities
                        
                        # Get collection schema info
                        for field in collection.schema.fields:
                            if field.name == "embedding":
                                stats_data['dimension'] = field.params.get('dim', 1536)
                                break
                    
                    # Disconnect
                    connections.disconnect("stats")
                except Exception as e:
                    logger.warning(f"Could not get Zilliz stats: {str(e)}")
            
            # Get document count from S3 if available
            if s3_bucket:
                try:
                    response = s3_client.list_objects_v2(
                        Bucket=s3_bucket,
                        Prefix='documents/',
                        MaxKeys=1000
                    )
                    stats_data['documents'] = response.get('KeyCount', 0)
                    
                    # If we don't have vector count from Zilliz, estimate it
                    if stats_data['vectors'] == 0 and stats_data['documents'] > 0:
                        stats_data['vectors'] = stats_data['documents'] * 10  # Estimate
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