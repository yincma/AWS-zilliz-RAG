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

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Initialize AWS clients
bedrock_runtime = boto3.client('bedrock-runtime', region_name=os.environ.get('AWS_REGION', 'us-east-1'))
s3_client = boto3.client('s3')

# Try to import pymilvus for Zilliz support
try:
    from pymilvus import connections, Collection, utility
    ZILLIZ_AVAILABLE = True
except ImportError:
    logger.warning("pymilvus not available, Zilliz features disabled")
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
            connections.connect(
                alias="default",
                uri=self.zilliz_endpoint,
                token=self.zilliz_token,
                timeout=5
            )
            
            # Check if collection exists
            if utility.has_collection(self.collection_name):
                self.collection = Collection(self.collection_name)
                self.collection.load()
                self.zilliz_connected = True
                logger.info(f"Connected to Zilliz collection: {self.collection_name}")
            else:
                logger.warning(f"Collection {self.collection_name} does not exist")
                
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
            return []
        
        try:
            search_params = {
                "metric_type": "L2",
                "params": {"nprobe": 10}
            }
            
            results = self.collection.search(
                data=[query_embedding],
                anns_field="embeddings",
                param=search_params,
                limit=top_k,
                output_fields=["content", "metadata"]
            )
            
            sources = []
            for hits in results:
                for hit in hits:
                    sources.append({
                        "content": hit.entity.get("content", ""),
                        "metadata": json.loads(hit.entity.get("metadata", "{}")),
                        "score": float(hit.score) if hit.score else 0.0
                    })
            
            return sources
            
        except Exception as e:
            logger.error(f"Error searching vectors: {str(e)}")
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
                formatted_prompt = f"\n\nHuman: {prompt if not context else f'Context: {context}\\n\\nQuestion: {prompt}'}\n\nAssistant:"
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
        # Parse request body
        if event.get('body'):
            if isinstance(event['body'], str):
                body = json.loads(event['body'])
            else:
                body = event['body']
        else:
            body = {}
        
        # Extract parameters
        query = body.get('query', '')
        top_k = body.get('top_k', 5)
        use_rag = body.get('use_rag', True)
        
        if not query:
            return {
                "statusCode": 400,
                "headers": {
                    "Content-Type": "application/json",
                    "Access-Control-Allow-Origin": "*"
                },
                "body": json.dumps({
                    "error": "Query is required"
                })
            }
        
        logger.info(f"Processing query: {query[:100]}...")
        logger.info(f"Parameters: use_rag={use_rag}, top_k={top_k}")
        
        # Get handler and process query
        handler_instance = get_handler()
        
        if use_rag:
            result = handler_instance.process_rag_query(query, top_k)
        else:
            result = handler_instance.process_direct_query(query)
        
        # Build response
        response = {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Methods": "OPTIONS,POST,GET"
            },
            "body": json.dumps(result)
        }
        
        logger.info(f"Query processed successfully. Has context: {result.get('has_context', False)}")
        return response
        
    except Exception as e:
        logger.error(f"Error processing request: {str(e)}", exc_info=True)
        return {
            "statusCode": 500,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({
                "error": str(e),
                "message": "Internal server error"
            })
        }