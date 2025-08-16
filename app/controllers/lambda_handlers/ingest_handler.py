"""
Enhanced Lambda function for document ingestion - Simplified version using SimpleRAG
"""
import json
import os
import sys
import boto3
import logging
from typing import Dict, Any, List, Optional
import hashlib
from datetime import datetime
import base64
from cors_helper import create_response, create_error_response, handle_options_request

# 添加app目录到Python路径
sys.path.insert(0, '/var/task')

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Initialize AWS clients
s3_client = boto3.client('s3')

# 全局变量用于缓存RAG实例
rag_instance = None

def get_rag_instance():
    """获取或创建RAG实例（单例模式）"""
    global rag_instance
    if rag_instance is None:
        try:
            from app.models.rag_simple import SimpleRAG
            rag_instance = SimpleRAG()
            logger.info("SimpleRAG instance created successfully")
        except Exception as e:
            logger.error(f"Failed to create SimpleRAG instance: {str(e)}")
            rag_instance = None
    return rag_instance

class DocumentProcessor:
    """Process and store documents using SimpleRAG"""
    
    def __init__(self):
        self.s3_bucket = os.environ.get('S3_BUCKET', 'rag-documents-375004070918-us-east-1')
        self.rag = get_rag_instance()
        logger.info("DocumentProcessor initialized with SimpleRAG")
    
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
    
    
    def process_document(self, content: str, filename: str) -> Dict[str, Any]:
        """Process a document using SimpleRAG"""
        
        # Generate document ID
        document_id = f"doc_{hashlib.md5(content.encode()).hexdigest()[:16]}"
        
        # Save original document to S3
        s3_key = self.save_to_s3(content, filename, {
            'document_id': document_id,
            'original_filename': filename
        })
        
        # Use SimpleRAG to add document (it handles chunking and embedding internally)
        if self.rag:
            try:
                metadata = {
                    'document_id': document_id,
                    'filename': filename,
                    's3_key': s3_key,
                    'uploaded_at': datetime.utcnow().isoformat()
                }
                
                success = self.rag.add_document(content, metadata)
                
                if success:
                    logger.info(f"Successfully added document {document_id} to RAG system")
                    status = 'success'
                else:
                    logger.warning(f"Failed to add document {document_id} to RAG system")
                    status = 'partial'
                    
            except Exception as e:
                logger.error(f"Error adding document to RAG: {str(e)}")
                status = 'error'
        else:
            logger.warning("RAG instance not available")
            status = 'no_rag'
        
        # Chunk for info purposes
        chunks = self.chunk_text(content)
        
        return {
            'document_id': document_id,
            'filename': filename,
            's3_key': s3_key,
            'chunks': len(chunks),
            'status': status
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
            return handle_options_request(event)
        
        logger.info(f"Processing ingestion request")
        
        # Parse request body for POST requests
        # Support both API Gateway (body field) and direct invocation
        if event.get('body'):
            # API Gateway invocation
            if isinstance(event['body'], str):
                body = json.loads(event['body'])
            else:
                body = event['body']
        elif 'content' in event or 'file_content' in event or 'file_paths' in event:
            # Direct invocation - event itself contains the parameters
            body = event
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
            return create_response(
                400,
                {"error": "No content provided for ingestion"},
                event
            )
        
        logger.info(f"Processing document: {filename} ({len(content)} bytes)")
        
        # Process the document
        doc_processor = get_processor()
        result = doc_processor.process_document(content, filename)
        
        # Build response
        response_body = {
            "status": "success",
            "message": f"Document '{filename}' ingested successfully",
            "document_id": result['document_id'],
            "chunks": result['chunks'],
            "s3_key": result['s3_key'],
            "rag_status": result.get('status', 'unknown')
        }
        
        logger.info(f"Document ingestion completed: {result['document_id']}")
        return create_response(200, response_body, event)
        
    except Exception as e:
        logger.error(f"Error in ingestion handler: {str(e)}", exc_info=True)
        return create_error_response(e, 500, event)

# AWS Lambda entry point
lambda_handler = handler