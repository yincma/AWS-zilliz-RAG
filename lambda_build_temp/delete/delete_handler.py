"""
Enhanced Lambda function for document deletion with S3 and Zilliz integration
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
    logger.info("pymilvus successfully imported for delete operations")
except ImportError as e:
    logger.error(f"Failed to import pymilvus: {str(e)}")
    logger.warning("pymilvus not available, Zilliz deletion disabled")
    ZILLIZ_AVAILABLE = False
except Exception as e:
    logger.error(f"Unexpected error importing pymilvus: {str(e)}")
    ZILLIZ_AVAILABLE = False


class DocumentDeleter:
    """Handler for deleting documents from S3 and Zilliz"""
    
    def __init__(self):
        self.s3_bucket = os.environ.get('S3_BUCKET', 'rag-documents-375004070918-us-east-1')
        
        # Zilliz configuration from environment variables
        self.zilliz_endpoint = os.environ.get('ZILLIZ_ENDPOINT')
        self.zilliz_token = os.environ.get('ZILLIZ_TOKEN')
        self.collection_name = os.environ.get('ZILLIZ_COLLECTION', 'rag_collection')
        self.zilliz_connected = False
        self.collection = None
        
        # Try to connect to Zilliz if available
        if ZILLIZ_AVAILABLE and self.zilliz_endpoint and self.zilliz_token:
            self.connect_zilliz()
    
    def connect_zilliz(self):
        """Connect to Zilliz Cloud"""
        try:
            logger.info(f"Connecting to Zilliz at {self.zilliz_endpoint}")
            connections.connect(
                alias="default",
                uri=self.zilliz_endpoint,
                token=self.zilliz_token,
                timeout=10
            )
            
            # Check if collection exists
            if utility.has_collection(self.collection_name):
                self.collection = Collection(self.collection_name)
                self.collection.load()
                self.zilliz_connected = True
                logger.info(f"Connected to Zilliz collection: {self.collection_name}")
            else:
                logger.warning(f"Collection {self.collection_name} does not exist in Zilliz")
                self.zilliz_connected = False
                
        except Exception as e:
            logger.error(f"Failed to connect to Zilliz: {str(e)}")
            self.zilliz_connected = False
    
    def delete_from_s3(self, document_path: str) -> bool:
        """Delete document and its embeddings from S3"""
        try:
            # Construct S3 keys
            s3_key = f"documents/{document_path}" if not document_path.startswith('documents/') else document_path
            
            # Delete main document
            s3_client.delete_object(
                Bucket=self.s3_bucket,
                Key=s3_key
            )
            logger.info(f"Deleted document from S3: {s3_key}")
            
            # Try to delete related embeddings
            try:
                embeddings_key = s3_key.replace('documents/', 'embeddings/') + '.json'
                s3_client.delete_object(
                    Bucket=self.s3_bucket,
                    Key=embeddings_key
                )
                logger.info(f"Deleted embeddings from S3: {embeddings_key}")
            except Exception as e:
                logger.warning(f"Could not delete embeddings (may not exist): {str(e)}")
            
            return True
            
        except Exception as e:
            logger.error(f"Error deleting from S3: {str(e)}")
            return False
    
    def delete_from_zilliz(self, document_path: str) -> bool:
        """Delete document vectors from Zilliz"""
        if not self.zilliz_connected:
            logger.warning("Zilliz not connected, skipping vector deletion")
            return False
        
        try:
            # Build expression to find vectors by document metadata
            # The metadata field should contain the source file information
            expr = f'metadata["source"] == "{document_path}"'
            
            # Search for entities to delete
            results = self.collection.query(
                expr=expr,
                output_fields=["id"]
            )
            
            if results:
                # Extract IDs to delete
                ids_to_delete = [entity["id"] for entity in results]
                
                # Delete entities
                delete_expr = f"id in {ids_to_delete}"
                self.collection.delete(delete_expr)
                
                logger.info(f"Deleted {len(ids_to_delete)} vectors from Zilliz for document: {document_path}")
                return True
            else:
                logger.info(f"No vectors found in Zilliz for document: {document_path}")
                return True
                
        except Exception as e:
            logger.error(f"Error deleting from Zilliz: {str(e)}")
            # If metadata field doesn't exist or has different structure, try alternative approach
            try:
                # Alternative: search by text field containing file path
                expr = f'text like "%{document_path}%"'
                results = self.collection.query(
                    expr=expr,
                    output_fields=["id"]
                )
                
                if results:
                    ids_to_delete = [entity["id"] for entity in results]
                    delete_expr = f"id in {ids_to_delete}"
                    self.collection.delete(delete_expr)
                    logger.info(f"Deleted {len(ids_to_delete)} vectors using alternative method")
                    return True
                    
            except Exception as alt_e:
                logger.error(f"Alternative deletion method also failed: {str(alt_e)}")
            
            return False
    
    def delete_document(self, document_path: str) -> Dict[str, Any]:
        """Delete document from both S3 and Zilliz"""
        result = {
            "document": document_path,
            "s3_deleted": False,
            "zilliz_deleted": False,
            "success": False
        }
        
        # Delete from S3
        result["s3_deleted"] = self.delete_from_s3(document_path)
        
        # Delete from Zilliz
        if self.zilliz_connected:
            result["zilliz_deleted"] = self.delete_from_zilliz(document_path)
        else:
            result["zilliz_deleted"] = None  # Not attempted
        
        # Overall success if S3 deletion succeeded (Zilliz is optional)
        result["success"] = result["s3_deleted"]
        
        return result


# Global deleter instance
document_deleter = None

def get_deleter():
    """Get or create document deleter instance"""
    global document_deleter
    if document_deleter is None:
        document_deleter = DocumentDeleter()
    return document_deleter


def handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """
    Lambda handler for document deletion
    """
    try:
        # Handle OPTIONS request for CORS preflight
        http_method = event.get('httpMethod', event.get('requestContext', {}).get('http', {}).get('method', 'DELETE'))
        
        if http_method == 'OPTIONS':
            logger.info("Handling OPTIONS preflight request")
            return handle_options_request(event)
        
        # Get document path from path parameters
        path_params = event.get('pathParameters', {})
        doc_path = path_params.get('proxy', '')
        
        if not doc_path:
            return create_response(
                400,
                {
                    'error': 'Document path is required',
                    'message': 'Please provide a valid document path'
                },
                event
            )
        
        logger.info(f"Processing deletion request for document: {doc_path}")
        
        # Get deleter instance and delete document
        deleter = get_deleter()
        result = deleter.delete_document(doc_path)
        
        if result["success"]:
            response_body = {
                'status': 'success',
                'message': 'Document deleted successfully',
                'document': doc_path,
                's3_deleted': result["s3_deleted"],
                'zilliz_deleted': result["zilliz_deleted"]
            }
            status_code = 200
        else:
            response_body = {
                'status': 'error',
                'message': 'Failed to delete document',
                'document': doc_path,
                's3_deleted': result["s3_deleted"],
                'zilliz_deleted': result["zilliz_deleted"]
            }
            status_code = 500
        
        return create_response(status_code, response_body, event)
        
    except Exception as e:
        logger.error(f"Error in deletion handler: {str(e)}", exc_info=True)
        return create_error_response(e, 500, event)


# AWS Lambda entry point
lambda_handler = handler