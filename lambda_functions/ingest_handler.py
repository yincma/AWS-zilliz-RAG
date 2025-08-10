"""
Real Lambda function for document ingestion with S3 storage and embedding generation
"""
import json
import os
import boto3
import logging
from typing import Dict, Any, List
import hashlib
from datetime import datetime
import base64

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Initialize AWS clients
s3_client = boto3.client('s3')
bedrock_runtime = boto3.client('bedrock-runtime', region_name=os.environ.get('AWS_REGION', 'us-east-1'))
dynamodb = boto3.resource('dynamodb')

class DocumentProcessor:
    """Process and store documents for RAG"""
    
    def __init__(self):
        self.s3_bucket = os.environ.get('S3_BUCKET', 'rag-documents-375004070918-us-east-1')
        self.embedding_model_id = os.environ.get('EMBEDDING_MODEL_ID', 'amazon.titan-embed-text-v2:0')
        
        # Try to get DynamoDB table for metadata
        try:
            table_name = os.environ.get('DOCUMENT_TABLE', 'rag-document-metadata')
            self.metadata_table = dynamodb.Table(table_name)
        except Exception as e:
            logger.warning(f"DynamoDB table not available: {str(e)}")
            self.metadata_table = None
    
    def chunk_text(self, text: str, chunk_size: int = 1000, overlap: int = 200) -> List[str]:
        """Split text into overlapping chunks"""
        chunks = []
        start = 0
        text_len = len(text)
        
        while start < text_len:
            end = min(start + chunk_size, text_len)
            
            # Try to break at a sentence or paragraph boundary
            if end < text_len:
                # Look for a period, newline, or space
                for delimiter in ['\n\n', '\n', '. ', ' ']:
                    delimiter_pos = text.rfind(delimiter, start, end)
                    if delimiter_pos != -1 and delimiter_pos > start + chunk_size // 2:
                        end = delimiter_pos + len(delimiter)
                        break
            
            chunk = text[start:end].strip()
            if chunk:
                chunks.append(chunk)
            
            start = end - overlap if end < text_len else end
        
        return chunks
    
    def generate_embeddings(self, text: str) -> List[float]:
        """Generate embeddings using Amazon Titan"""
        try:
            # Titan has a limit on input text
            truncated_text = text[:2048] if len(text) > 2048 else text
            
            response = bedrock_runtime.invoke_model(
                modelId=self.embedding_model_id,
                body=json.dumps({
                    "inputText": truncated_text
                })
            )
            
            response_body = json.loads(response['body'].read())
            return response_body.get('embedding', [])
            
        except Exception as e:
            logger.error(f"Error generating embeddings: {str(e)}")
            return []
    
    def save_to_s3(self, content: str, filename: str, metadata: Dict = None) -> str:
        """Save document to S3"""
        try:
            # Generate unique key
            timestamp = datetime.utcnow().strftime('%Y%m%d_%H%M%S')
            file_hash = hashlib.md5(content.encode()).hexdigest()[:8]
            s3_key = f"documents/{timestamp}_{file_hash}_{filename}"
            
            # Upload to S3
            s3_client.put_object(
                Bucket=self.s3_bucket,
                Key=s3_key,
                Body=content.encode('utf-8'),
                ContentType='text/plain',
                Metadata=metadata or {}
            )
            
            logger.info(f"Saved document to S3: {s3_key}")
            return s3_key
            
        except Exception as e:
            logger.error(f"Error saving to S3: {str(e)}")
            raise
    
    def save_metadata(self, document_id: str, filename: str, s3_key: str, chunks: int, embeddings_generated: bool):
        """Save document metadata to DynamoDB"""
        if not self.metadata_table:
            return
        
        try:
            self.metadata_table.put_item(
                Item={
                    'document_id': document_id,
                    'filename': filename,
                    's3_key': s3_key,
                    'chunks': chunks,
                    'embeddings_generated': embeddings_generated,
                    'uploaded_at': datetime.utcnow().isoformat(),
                    'status': 'processed'
                }
            )
            logger.info(f"Saved metadata for document {document_id}")
        except Exception as e:
            logger.warning(f"Could not save metadata: {str(e)}")
    
    def process_document(self, content: str, filename: str) -> Dict[str, Any]:
        """Process a document: save to S3, chunk, and generate embeddings"""
        
        # Generate document ID
        document_id = f"doc_{hashlib.md5(content.encode()).hexdigest()[:16]}"
        
        # Save original document to S3
        s3_key = self.save_to_s3(content, filename, {
            'document_id': document_id,
            'original_filename': filename
        })
        
        # Chunk the document
        chunks = self.chunk_text(content)
        logger.info(f"Created {len(chunks)} chunks from document")
        
        # Generate embeddings for each chunk
        chunk_embeddings = []
        for i, chunk in enumerate(chunks):
            embedding = self.generate_embeddings(chunk)
            if embedding:
                chunk_embeddings.append({
                    'chunk_id': f"{document_id}_chunk_{i}",
                    'content': chunk,
                    'embedding': embedding,
                    'metadata': {
                        'document_id': document_id,
                        'filename': filename,
                        's3_key': s3_key,
                        'chunk_index': i,
                        'total_chunks': len(chunks)
                    }
                })
        
        # Save chunks and embeddings to S3 as JSON
        if chunk_embeddings:
            embeddings_key = s3_key.replace('documents/', 'embeddings/') + '.json'
            s3_client.put_object(
                Bucket=self.s3_bucket,
                Key=embeddings_key,
                Body=json.dumps(chunk_embeddings),
                ContentType='application/json'
            )
            logger.info(f"Saved {len(chunk_embeddings)} embeddings to {embeddings_key}")
        
        # Save metadata
        self.save_metadata(
            document_id=document_id,
            filename=filename,
            s3_key=s3_key,
            chunks=len(chunks),
            embeddings_generated=len(chunk_embeddings) > 0
        )
        
        return {
            'document_id': document_id,
            'filename': filename,
            's3_key': s3_key,
            'chunks': len(chunks),
            'embeddings': len(chunk_embeddings),
            'status': 'success'
        }

# Global processor instance
processor = None

def get_processor():
    """Get or create document processor instance"""
    global processor
    if processor is None:
        processor = DocumentProcessor()
    return processor

def handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """
    Lambda handler for document ingestion
    """
    try:
        # Handle OPTIONS request for CORS preflight
        http_method = event.get('httpMethod', event.get('requestContext', {}).get('http', {}).get('method', 'POST'))
        
        if http_method == 'OPTIONS':
            logger.info("Handling OPTIONS preflight request")
            return {
                "statusCode": 200,
                "headers": {
                    "Access-Control-Allow-Origin": "*",
                    "Access-Control-Allow-Headers": "Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token",
                    "Access-Control-Allow-Methods": "OPTIONS,POST,GET",
                    "Content-Type": "application/json"
                },
                "body": json.dumps({"message": "CORS preflight successful"})
            }
        
        logger.info(f"Processing ingestion request")
        
        # Parse request body for POST requests
        if event.get('body'):
            if isinstance(event['body'], str):
                body = json.loads(event['body'])
            else:
                body = event['body']
        else:
            body = {}
        
        # Extract document content and filename
        content = body.get('content', '')
        file_paths = body.get('file_paths', [])
        filename = file_paths[0] if file_paths else body.get('filename', 'document.txt')
        
        if not content:
            # Try to decode base64 content
            if 'file_content' in body:
                try:
                    content = base64.b64decode(body['file_content']).decode('utf-8')
                except Exception as e:
                    logger.error(f"Error decoding base64 content: {str(e)}")
                    content = body['file_content']
        
        if not content:
            return {
                "statusCode": 400,
                "headers": {
                    "Content-Type": "application/json",
                    "Access-Control-Allow-Origin": "*"
                },
                "body": json.dumps({
                    "error": "No content provided for ingestion"
                })
            }
        
        logger.info(f"Processing document: {filename} ({len(content)} bytes)")
        
        # Process the document
        doc_processor = get_processor()
        result = doc_processor.process_document(content, filename)
        
        # Build response
        response = {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Methods": "OPTIONS,POST"
            },
            "body": json.dumps({
                "status": "success",
                "message": f"Document '{filename}' ingested successfully",
                "document_id": result['document_id'],
                "chunks": result['chunks'],
                "embeddings": result['embeddings'],
                "s3_key": result['s3_key']
            })
        }
        
        logger.info(f"Document ingestion completed: {result['document_id']}")
        return response
        
    except Exception as e:
        logger.error(f"Error in ingestion handler: {str(e)}", exc_info=True)
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