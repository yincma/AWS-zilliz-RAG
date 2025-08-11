"""
Enhanced Lambda function for document ingestion with S3 storage, embedding generation, and Zilliz integration
"""
import json
import os
import boto3
import logging
from typing import Dict, Any, List, Optional
import hashlib
from datetime import datetime
import base64
from cors_helper import create_response, create_error_response, handle_options_request

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Initialize AWS clients
s3_client = boto3.client('s3')
bedrock_runtime = boto3.client('bedrock-runtime', region_name=os.environ.get('AWS_REGION', 'us-east-1'))
dynamodb = boto3.resource('dynamodb')

# Try to import pymilvus for Zilliz support
try:
    from pymilvus import (
        connections,
        Collection,
        CollectionSchema,
        FieldSchema,
        DataType,
        utility
    )
    ZILLIZ_AVAILABLE = True
    logger.info("✅ pymilvus imported successfully")
except ImportError as e:
    logger.error(f"❌ pymilvus import failed: {str(e)}")
    ZILLIZ_AVAILABLE = False
except Exception as e:
    logger.error(f"❌ Unexpected error importing pymilvus: {str(e)}")
    ZILLIZ_AVAILABLE = False

class DocumentProcessor:
    """Process and store documents for RAG with Zilliz integration"""
    
    def __init__(self):
        self.s3_bucket = os.environ.get('S3_BUCKET', 'rag-documents-375004070918-us-east-1')
        self.embedding_model_id = os.environ.get('EMBEDDING_MODEL_ID', 'amazon.titan-embed-text-v2:0')
        
        # Zilliz configuration from environment variables
        self.zilliz_endpoint = os.environ.get('ZILLIZ_ENDPOINT')
        self.zilliz_token = os.environ.get('ZILLIZ_TOKEN')
        self.collection_name = os.environ.get('ZILLIZ_COLLECTION', 'rag_collection')
        self.zilliz_connected = False
        self.collection = None
        
        logger.info(f"📋 Zilliz configuration check:")
        logger.info(f"  - ZILLIZ_AVAILABLE: {ZILLIZ_AVAILABLE}")
        logger.info(f"  - Endpoint configured: {bool(self.zilliz_endpoint)}")
        logger.info(f"  - Token configured: {bool(self.zilliz_token)}")
        logger.info(f"  - Collection name: {self.collection_name}")
        
        # Try to connect to Zilliz if available
        if ZILLIZ_AVAILABLE and self.zilliz_endpoint and self.zilliz_token:
            logger.info("🔄 Attempting to connect to Zilliz...")
            self.connect_zilliz()
        else:
            logger.warning(f"⚠️ Skipping Zilliz connection: ZILLIZ_AVAILABLE={ZILLIZ_AVAILABLE}, endpoint={bool(self.zilliz_endpoint)}, token={bool(self.zilliz_token)}")
        
        # Try to get DynamoDB table for metadata
        try:
            table_name = os.environ.get('DOCUMENT_TABLE', 'rag-document-metadata')
            self.metadata_table = dynamodb.Table(table_name)
        except Exception as e:
            logger.warning(f"DynamoDB table not available: {str(e)}")
            self.metadata_table = None
    
    def connect_zilliz(self):
        """Connect to Zilliz Cloud and initialize collection"""
        try:
            logger.info(f"Connecting to Zilliz at {self.zilliz_endpoint}")
            connections.connect(
                alias="default",
                uri=self.zilliz_endpoint,
                token=self.zilliz_token,
                timeout=10
            )
            
            # Check if collection exists, if not create it
            if utility.has_collection(self.collection_name):
                self.collection = Collection(self.collection_name)
                logger.info(f"Using existing collection: {self.collection_name}")
            else:
                self.create_collection()
                logger.info(f"Created new collection: {self.collection_name}")
            
            # Load collection to memory
            self.collection.load()
            self.zilliz_connected = True
            logger.info(f"Successfully connected to Zilliz collection: {self.collection_name}")
            
        except Exception as e:
            logger.error(f"Failed to connect to Zilliz: {str(e)}")
            self.zilliz_connected = False
    
    def create_collection(self):
        """Create Zilliz collection with proper schema"""
        # Define fields to match existing collection schema
        fields = [
            FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=True),
            FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=1024),  # Note: singular "embedding"
            FieldSchema(name="text", dtype=DataType.VARCHAR, max_length=65535),     # Note: "text" not "content"
            FieldSchema(name="metadata", dtype=DataType.JSON)                        # Note: JSON type not VARCHAR
        ]
        
        # Create schema
        schema = CollectionSchema(
            fields=fields,
            description="RAG document embeddings collection"
        )
        
        # Create collection
        self.collection = Collection(
            name=self.collection_name,
            schema=schema
        )
        
        # Create index for vector field
        index_params = {
            "metric_type": "L2",  # Use L2 distance
            "index_type": "IVF_FLAT",
            "params": {"nlist": 128}
        }
        
        self.collection.create_index(
            field_name="embedding",  # Match the field name
            index_params=index_params
        )
        logger.info(f"Created index for collection {self.collection_name}")
    
    def store_embeddings_in_zilliz(self, chunks: List[Dict]) -> bool:
        """Store document chunks and embeddings in Zilliz"""
        if not self.zilliz_connected or not chunks:
            logger.warning("Zilliz not connected or no chunks to store")
            return False
        
        try:
            # Prepare data for batch insert (matching existing schema)
            embeddings_list = []
            texts_list = []
            metadatas_list = []
            
            for chunk in chunks:
                embeddings_list.append(chunk['embedding'])
                texts_list.append(chunk['content'][:65535])  # Use 'text' field name
                metadatas_list.append(chunk['metadata'])  # Keep as dict for JSON field
            
            # Insert data into collection (order must match schema)
            insert_data = [
                embeddings_list,  # embedding field (singular)
                texts_list,       # text field (not content)
                metadatas_list    # metadata field (JSON type accepts dict directly)
            ]
            
            result = self.collection.insert(insert_data)
            
            # Flush to ensure data is persisted
            self.collection.flush()
            
            logger.info(f"Successfully inserted {len(chunks)} chunks into Zilliz")
            return True
            
        except Exception as e:
            logger.error(f"Failed to store embeddings in Zilliz: {str(e)}")
            return False
    
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
        
        # Store embeddings in Zilliz if connected
        zilliz_stored = False
        if chunk_embeddings and self.zilliz_connected:
            zilliz_stored = self.store_embeddings_in_zilliz(chunk_embeddings)
            if zilliz_stored:
                logger.info(f"Successfully stored {len(chunk_embeddings)} embeddings in Zilliz")
            else:
                logger.warning("Failed to store embeddings in Zilliz, falling back to S3 only")
        
        # Always save chunks and embeddings to S3 as backup
        if chunk_embeddings:
            embeddings_key = s3_key.replace('documents/', 'embeddings/') + '.json'
            s3_client.put_object(
                Bucket=self.s3_bucket,
                Key=embeddings_key,
                Body=json.dumps(chunk_embeddings),
                ContentType='application/json'
            )
            logger.info(f"Saved {len(chunk_embeddings)} embeddings to S3 at {embeddings_key}")
        
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
            'zilliz_stored': zilliz_stored,
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
            "embeddings": result['embeddings'],
            "s3_key": result['s3_key'],
            "zilliz_stored": result.get('zilliz_stored', False)
        }
        
        logger.info(f"Document ingestion completed: {result['document_id']}")
        return create_response(200, response_body, event)
        
    except Exception as e:
        logger.error(f"Error in ingestion handler: {str(e)}", exc_info=True)
        return create_error_response(e, 500, event)

# AWS Lambda entry point
lambda_handler = handler