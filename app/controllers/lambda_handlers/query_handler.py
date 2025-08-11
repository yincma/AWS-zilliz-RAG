"""
Enhanced Lambda function for handling RAG queries with real Bedrock and Zilliz integration
"""
import json
import os
import sys
import boto3
import logging
from typing import Dict, Any, List, Optional
import base64
from cors_helper import create_response, create_error_response, handle_options_request

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Initialize AWS clients
bedrock_runtime = boto3.client('bedrock-runtime', region_name=os.environ.get('AWS_REGION', 'us-east-1'))
s3_client = boto3.client('s3')

# Try to import pymilvus for Zilliz support
try:
    # Check for all dependencies first
    logger.info("Checking pymilvus dependencies...")
    
    # Check pandas stub
    try:
        import pandas
        logger.info(f"✅ pandas module found: {pandas.__file__ if hasattr(pandas, '__file__') else 'built-in'}")
        import pandas.api.types
        logger.info("✅ pandas.api.types imported successfully")
    except ImportError as pe:
        logger.warning(f"⚠️ pandas import issue: {str(pe)}")
    
    # Check dotenv
    try:
        import dotenv
        logger.info(f"✅ dotenv module found: {dotenv.__file__ if hasattr(dotenv, '__file__') else 'built-in'}")
    except ImportError:
        logger.warning("⚠️ dotenv not found")
    
    # Check ujson
    try:
        import ujson
        logger.info(f"✅ ujson module found")
    except ImportError:
        logger.warning("⚠️ ujson not found")
    
    # Check grpcio
    try:
        import grpc
        logger.info(f"✅ grpcio module found")
    except ImportError:
        logger.warning("⚠️ grpcio not found")
    
    # Now try to import pymilvus
    logger.info("Attempting to import pymilvus...")
    from pymilvus import connections, Collection, utility
    ZILLIZ_AVAILABLE = True
    logger.info("🎉 pymilvus successfully imported!")
except ImportError as e:
    logger.error(f"Failed to import pymilvus: {str(e)}")
    logger.error(f"Import error details: {e.__class__.__name__}: {e}")
    import sys
    logger.error(f"Python path: {sys.path[:5]}")  # Log first 5 paths
    logger.warning("pymilvus not available, Zilliz features disabled")
    ZILLIZ_AVAILABLE = False
except Exception as e:
    logger.error(f"Unexpected error importing pymilvus: {str(e)}")
    logger.error(f"Exception type: {type(e).__name__}")
    import traceback
    logger.error(f"Traceback: {traceback.format_exc()}")
    ZILLIZ_AVAILABLE = False

class RAGHandler:
    """Handler for RAG queries with Bedrock and optional Zilliz integration"""
    
    def __init__(self):
        self.bedrock_runtime = bedrock_runtime
        self.s3_client = s3_client
        self.model_id = os.environ.get('BEDROCK_MODEL_ID', 'amazon.nova-lite-v1:0')
        self.embedding_model_id = os.environ.get('EMBEDDING_MODEL_ID', 'amazon.titan-embed-text-v2:0')
        self.s3_bucket = os.environ.get('S3_BUCKET')
        
        # Zilliz configuration
        self.zilliz_endpoint = os.environ.get('ZILLIZ_ENDPOINT')
        self.zilliz_token = os.environ.get('ZILLIZ_TOKEN')
        self.collection_name = os.environ.get('ZILLIZ_COLLECTION', 'rag_collection')
        self.zilliz_connected = False
        
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
                
                # Get collection info for debugging
                collection_info = self.collection.schema
                logger.info(f"Connected to Zilliz collection: {self.collection_name}")
                logger.info(f"Collection has {self.collection.num_entities} entities")
            else:
                logger.warning(f"Collection {self.collection_name} does not exist in Zilliz")
                self.zilliz_connected = False
                
        except Exception as e:
            logger.error(f"Failed to connect to Zilliz: {str(e)}")
            self.zilliz_connected = False
    
    def get_embeddings(self, text: str) -> List[float]:
        """Generate embeddings using Amazon Titan"""
        try:
            response = self.bedrock_runtime.invoke_model(
                modelId=self.embedding_model_id,
                body=json.dumps({
                    "inputText": text[:2048]  # Titan has input limit
                })
            )
            
            response_body = json.loads(response['body'].read())
            return response_body.get('embedding', [])
            
        except Exception as e:
            logger.error(f"Error generating embeddings: {str(e)}")
            return []
    
    def search_vectors(self, query_embedding: List[float], top_k: int = 5) -> List[Dict]:
        """Search for similar vectors in Zilliz"""
        if not self.zilliz_connected or not query_embedding:
            logger.warning("Zilliz not connected or no query embedding")
            return []
        
        try:
            search_params = {
                "metric_type": "L2",
                "params": {"nprobe": 10}
            }
            
            results = self.collection.search(
                data=[query_embedding],
                anns_field="embedding",  # Match the actual field name (singular)
                param=search_params,
                limit=top_k,
                output_fields=["text", "metadata"]  # Use "text" not "content"
            )
            
            sources = []
            for hits in results:
                for hit in hits:
                    # Access entity fields directly - pymilvus returns a dict-like object
                    entity = hit.entity
                    
                    # Get metadata field (JSON type in Zilliz)
                    metadata = entity.metadata if hasattr(entity, 'metadata') else entity.get('metadata', {})
                    if metadata is None:
                        metadata = {}
                    
                    # Get text field
                    text = entity.text if hasattr(entity, 'text') else entity.get('text', '')
                    if text is None:
                        text = ''
                    
                    # Convert L2 distance to similarity percentage
                    # L2 distance: lower is better, 0 is perfect match
                    # Simple conversion: 100% for distance 0, decreasing as distance increases
                    distance = float(hit.score) if hit.score is not None else 100.0
                    similarity = max(0, min(100, 100 * (1 - distance / 10)))  # Normalize to 0-100%
                    
                    sources.append({
                        "content": text,
                        "metadata": metadata,
                        "score": similarity  # Return as percentage
                    })
            
            logger.info(f"Found {len(sources)} results from Zilliz")
            return sources
            
        except Exception as e:
            logger.error(f"Error searching vectors: {str(e)}")
            logger.error(f"Query embedding length: {len(query_embedding) if query_embedding else 0}")
            return []
    
    def search_s3_documents(self, query: str, top_k: int = 5) -> List[Dict]:
        """Fallback: Search documents in S3 when Zilliz is unavailable"""
        sources = []
        
        if not self.s3_bucket:
            return sources
        
        try:
            # List documents in S3
            response = self.s3_client.list_objects_v2(
                Bucket=self.s3_bucket,
                Prefix='documents/',
                MaxKeys=10
            )
            
            if 'Contents' in response:
                for obj in response['Contents'][:top_k]:
                    # For demo, just return file info
                    sources.append({
                        "content": f"Document: {obj['Key']}",
                        "metadata": {
                            "source": obj['Key'].replace('documents/', ''),
                            "size": obj['Size'],
                            "modified": obj['LastModified'].isoformat()
                        },
                        "score": 0.0
                    })
            
            return sources
            
        except Exception as e:
            logger.error(f"Error searching S3: {str(e)}")
            return []
    
    def call_bedrock_llm(self, prompt: str, context: str = "") -> str:
        """Call Bedrock LLM for text generation"""
        try:
            # Determine model family and format request accordingly
            if "nova" in self.model_id.lower():
                # Amazon Nova format
                messages = [
                    {
                        "role": "user",
                        "content": [
                            {"text": prompt if not context else f"Context:\n{context}\n\nQuestion: {prompt}"}
                        ]
                    }
                ]
                
                request_body = {
                    "messages": messages,
                    "inferenceConfig": {
                        "max_new_tokens": 1000,
                        "temperature": 0.7,
                        "top_p": 0.9
                    }
                }
                
            elif "claude" in self.model_id.lower():
                # Claude format
                if context:
                    formatted_prompt = f"\n\nHuman: Context: {context}\n\nQuestion: {prompt}\n\nAssistant:"
                else:
                    formatted_prompt = f"\n\nHuman: {prompt}\n\nAssistant:"
                request_body = {
                    "prompt": formatted_prompt,
                    "max_tokens_to_sample": 1000,
                    "temperature": 0.7,
                    "top_p": 0.9
                }
                
            else:
                # Default/fallback format
                request_body = {
                    "prompt": prompt,
                    "max_gen_len": 1000,
                    "temperature": 0.7,
                    "top_p": 0.9
                }
            
            response = self.bedrock_runtime.invoke_model(
                modelId=self.model_id,
                body=json.dumps(request_body),
                contentType='application/json',
                accept='application/json'
            )
            
            response_body = json.loads(response['body'].read())
            
            # Extract text based on model response format
            if "output" in response_body and "message" in response_body["output"]:
                # Nova format
                return response_body["output"]["message"]["content"][0]["text"]
            elif "completion" in response_body:
                # Claude format
                return response_body["completion"]
            elif "generation" in response_body:
                # Other models
                return response_body["generation"]
            else:
                logger.warning(f"Unknown response format: {response_body.keys()}")
                return str(response_body)
                
        except Exception as e:
            logger.error(f"Error calling Bedrock: {str(e)}")
            logger.error(f"Model ID: {self.model_id}")
            return f"I apologize, but I encountered an error accessing the language model. Error: {str(e)}"
    
    def process_rag_query(self, query: str, top_k: int = 5) -> Dict[str, Any]:
        """Process a RAG query with vector search and LLM generation"""
        
        # Get query embeddings if Zilliz is available
        sources = []
        context = ""
        
        if self.zilliz_connected:
            query_embedding = self.get_embeddings(query)
            if query_embedding:
                sources = self.search_vectors(query_embedding, top_k)
                context = "\n\n".join([s["content"] for s in sources[:3]])  # Use top 3 for context
        
        # Fallback to S3 search if no Zilliz results
        if not sources:
            sources = self.search_s3_documents(query, top_k)
            if sources:
                context = "Available documents:\n" + "\n".join([s["metadata"]["source"] for s in sources])
        
        # Generate answer using LLM
        if context:
            prompt = f"Based on the following context, please answer the question.\n\nContext:\n{context}\n\nQuestion: {query}"
        else:
            prompt = query
        
        answer = self.call_bedrock_llm(prompt, context)
        
        return {
            "answer": answer,
            "sources": sources,
            "query": query,
            "use_rag": True,
            "top_k": top_k,
            "has_context": bool(context)
        }
    
    def process_direct_query(self, query: str) -> Dict[str, Any]:
        """Process a direct LLM query without RAG"""
        answer = self.call_bedrock_llm(query)
        
        return {
            "answer": answer,
            "sources": [],
            "query": query,
            "use_rag": False,
            "top_k": 0
        }

# Global handler instance
rag_handler = None

def get_handler():
    """Get or create RAG handler instance"""
    global rag_handler
    if rag_handler is None:
        rag_handler = RAGHandler()
    return rag_handler

def handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """
    Lambda handler for RAG queries
    """
    try:
        # Handle OPTIONS request for CORS preflight
        http_method = event.get('httpMethod', event.get('requestContext', {}).get('http', {}).get('method', 'POST'))
        
        if http_method == 'OPTIONS':
            logger.info("Handling OPTIONS preflight request")
            return handle_options_request(event)
        
        # Parse request body for POST requests
        # Support both API Gateway (body field) and direct invocation
        if event.get('body'):
            # API Gateway invocation
            if isinstance(event['body'], str):
                body = json.loads(event['body'])
            else:
                body = event['body']
        elif 'query' in event:
            # Direct invocation - event itself contains the parameters
            body = event
        else:
            body = {}
        
        # Extract parameters
        query = body.get('query', '')
        top_k = body.get('top_k', 5)
        use_rag = body.get('use_rag', True)
        
        if not query:
            return create_response(
                400,
                {"error": "Query is required"},
                event
            )
        
        logger.info(f"Processing query: {query[:100]}...")
        logger.info(f"Parameters: use_rag={use_rag}, top_k={top_k}")
        
        # Get handler and process query
        handler_instance = get_handler()
        
        if use_rag:
            result = handler_instance.process_rag_query(query, top_k)
        else:
            result = handler_instance.process_direct_query(query)
        
        # Build response
        logger.info(f"Query processed successfully. Has context: {result.get('has_context', False)}")
        return create_response(200, result, event)
        
    except Exception as e:
        logger.error(f"Error processing request: {str(e)}", exc_info=True)
        return create_error_response(e, 500, event)

# AWS Lambda entry point
lambda_handler = handler