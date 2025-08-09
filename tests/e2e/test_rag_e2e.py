"""
End-to-end tests for the complete RAG system.
Tests the full pipeline from document ingestion to query response.
"""

import pytest
from unittest.mock import Mock, patch, MagicMock
import json
import time
from typing import List, Dict

from app.controllers.rag_controller import RAGController
from app.controllers.document_controller import DocumentController


class TestRAGEndToEnd:
    """End-to-end test cases for the RAG system."""
    
    @pytest.mark.e2e
    @pytest.mark.slow
    def test_complete_rag_workflow(self, mock_aws_credentials, mock_bedrock_client, mock_zilliz_connection):
        """Test the complete RAG workflow from document ingestion to query."""
        with patch('app.models.embedding.boto3.client', return_value=mock_bedrock_client):
            with patch('app.models.llm.boto3.client', return_value=mock_bedrock_client):
                with patch('app.models.vector_store.Collection') as mock_collection:
                    
                    # Setup mock collection
                    mock_collection_instance = Mock()
                    mock_collection.return_value = mock_collection_instance
                    
                    # Mock embedding response
                    mock_bedrock_client.invoke_model.return_value = {
                        'body': MagicMock(read=lambda: json.dumps({
                            'embedding': [0.5] * 1024
                        }).encode())
                    }
                    
                    # Mock vector search results
                    mock_collection_instance.search.return_value = [[
                        {
                            "id": 1,
                            "distance": 0.95,
                            "entity": {
                                "text": "AWS provides cloud computing services.",
                                "source": "aws_guide.pdf",
                                "page": 1
                            }
                        }
                    ]]
                    
                    # Mock LLM response
                    mock_bedrock_client.invoke_model.side_effect = [
                        # First call for embedding
                        {'body': MagicMock(read=lambda: json.dumps({'embedding': [0.5] * 1024}).encode())},
                        # Second call for LLM
                        {'body': MagicMock(read=lambda: json.dumps({
                            'completion': 'AWS provides comprehensive cloud computing services.'
                        }).encode())}
                    ]
                    
                    # Initialize controllers
                    rag_controller = RAGController(
                        collection_name="test_e2e",
                        embedding_model_id="amazon.titan-embed-image-v1",
                        llm_model_id="amazon.nova-1"
                    )
                    
                    # Step 1: Ingest documents
                    documents = [
                        {
                            "text": "AWS provides cloud computing services including EC2, S3, and Lambda.",
                            "metadata": {"source": "aws_guide.pdf", "page": 1}
                        },
                        {
                            "text": "Zilliz is a vector database service for AI applications.",
                            "metadata": {"source": "zilliz_guide.pdf", "page": 1}
                        }
                    ]
                    
                    mock_collection_instance.insert.return_value = MagicMock(primary_keys=[1, 2])
                    
                    ingest_result = rag_controller.ingest_documents(documents)
                    assert ingest_result["success"] is True
                    assert ingest_result["document_count"] == 2
                    
                    # Step 2: Query the system
                    query = "What services does AWS provide?"
                    query_result = rag_controller.process_query(query)
                    
                    assert query_result is not None
                    assert "answer" in query_result
                    assert "AWS" in query_result["answer"]
    
    @pytest.mark.e2e
    def test_document_lifecycle(self, mock_aws_credentials):
        """Test document lifecycle: upload, process, query, delete."""
        with patch('app.controllers.document_controller.S3Client') as mock_s3:
            with patch('app.controllers.document_controller.DocumentProcessor') as mock_processor:
                
                # Setup mocks
                mock_s3_instance = Mock()
                mock_s3.return_value = mock_s3_instance
                mock_processor_instance = Mock()
                mock_processor.return_value = mock_processor_instance
                
                # Initialize document controller
                doc_controller = DocumentController(
                    s3_bucket="test-bucket",
                    s3_prefix="documents/"
                )
                
                # Step 1: Upload document
                mock_s3_instance.upload_file.return_value = True
                upload_result = doc_controller.upload_document(
                    file_path="test.pdf",
                    document_id="doc123"
                )
                assert upload_result["success"] is True
                
                # Step 2: Process document
                mock_processor_instance.process.return_value = {
                    "chunks": ["chunk1", "chunk2"],
                    "metadata": {"pages": 2}
                }
                process_result = doc_controller.process_document("doc123")
                assert process_result["success"] is True
                assert process_result["chunk_count"] == 2
                
                # Step 3: Query document metadata
                mock_s3_instance.get_object_metadata.return_value = {
                    "ContentLength": 1024,
                    "LastModified": "2024-01-01"
                }
                metadata = doc_controller.get_document_metadata("doc123")
                assert metadata is not None
                assert metadata["ContentLength"] == 1024
                
                # Step 4: Delete document
                mock_s3_instance.delete_object.return_value = True
                delete_result = doc_controller.delete_document("doc123")
                assert delete_result["success"] is True
    
    @pytest.mark.e2e
    @pytest.mark.slow
    def test_concurrent_queries(self, mock_aws_credentials, mock_bedrock_client, mock_zilliz_connection):
        """Test handling concurrent queries."""
        import concurrent.futures
        
        with patch('app.models.embedding.boto3.client', return_value=mock_bedrock_client):
            with patch('app.models.llm.boto3.client', return_value=mock_bedrock_client):
                with patch('app.models.vector_store.Collection') as mock_collection:
                    
                    # Setup mocks
                    mock_collection_instance = Mock()
                    mock_collection.return_value = mock_collection_instance
                    
                    # Mock responses
                    mock_bedrock_client.invoke_model.return_value = {
                        'body': MagicMock(read=lambda: json.dumps({
                            'embedding': [0.5] * 1024,
                            'completion': 'Test response'
                        }).encode())
                    }
                    
                    mock_collection_instance.search.return_value = [[
                        {"id": 1, "distance": 0.9, "entity": {"text": "Test"}}
                    ]]
                    
                    # Initialize controller
                    rag_controller = RAGController(
                        collection_name="test_concurrent",
                        embedding_model_id="amazon.titan-embed-image-v1",
                        llm_model_id="amazon.nova-1"
                    )
                    
                    # Define queries
                    queries = [
                        "What is machine learning?",
                        "Explain deep learning",
                        "What are neural networks?",
                        "How does AI work?",
                        "What is natural language processing?"
                    ]
                    
                    # Execute queries concurrently
                    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
                        futures = [
                            executor.submit(rag_controller.process_query, query)
                            for query in queries
                        ]
                        
                        results = [future.result() for future in futures]
                    
                    # Verify all queries were processed
                    assert len(results) == 5
                    for result in results:
                        assert result is not None
                        assert "answer" in result or "error" in result
    
    @pytest.mark.e2e
    def test_error_recovery(self, mock_aws_credentials):
        """Test system recovery from various error conditions."""
        with patch('app.controllers.rag_controller.EmbeddingModel') as mock_embedding:
            with patch('app.controllers.rag_controller.VectorStore') as mock_store:
                with patch('app.controllers.rag_controller.LLMModel') as mock_llm:
                    
                    # Setup controller with mocks
                    rag_controller = RAGController(
                        collection_name="test_recovery",
                        embedding_model_id="amazon.titan-embed-image-v1",
                        llm_model_id="amazon.nova-1"
                    )
                    
                    # Test 1: Embedding failure recovery
                    mock_embedding.return_value.generate_embedding.side_effect = [
                        Exception("Temporary failure"),
                        [0.5] * 1024  # Success on retry
                    ]
                    
                    result = rag_controller.process_query_with_retry("Test query", max_retries=2)
                    assert result is not None
                    
                    # Test 2: Vector store failure recovery
                    mock_store.return_value.search.side_effect = [
                        Exception("Connection timeout"),
                        []  # Empty results on retry
                    ]
                    
                    result = rag_controller.process_query_with_retry("Test query", max_retries=2)
                    assert result is not None
                    
                    # Test 3: LLM failure with fallback
                    mock_llm.return_value.generate_with_context.side_effect = Exception("LLM unavailable")
                    
                    result = rag_controller.process_query_with_fallback("Test query")
                    assert result is not None
                    assert result.get("fallback_used", False) is True
    
    @pytest.mark.e2e
    def test_performance_metrics(self, mock_aws_credentials, mock_bedrock_client, mock_zilliz_connection):
        """Test performance metrics collection."""
        with patch('app.models.embedding.boto3.client', return_value=mock_bedrock_client):
            with patch('app.models.llm.boto3.client', return_value=mock_bedrock_client):
                with patch('app.models.vector_store.Collection') as mock_collection:
                    
                    # Setup mocks
                    mock_collection_instance = Mock()
                    mock_collection.return_value = mock_collection_instance
                    
                    mock_bedrock_client.invoke_model.return_value = {
                        'body': MagicMock(read=lambda: json.dumps({
                            'embedding': [0.5] * 1024,
                            'completion': 'Test response'
                        }).encode())
                    }
                    
                    mock_collection_instance.search.return_value = [[
                        {"id": 1, "distance": 0.9, "entity": {"text": "Test"}}
                    ]]
                    
                    # Initialize controller with metrics enabled
                    rag_controller = RAGController(
                        collection_name="test_metrics",
                        embedding_model_id="amazon.titan-embed-image-v1",
                        llm_model_id="amazon.nova-1",
                        enable_metrics=True
                    )
                    
                    # Process query and collect metrics
                    start_time = time.time()
                    result = rag_controller.process_query("Test query")
                    end_time = time.time()
                    
                    # Verify metrics
                    assert "metrics" in result
                    metrics = result["metrics"]
                    assert "embedding_time" in metrics
                    assert "search_time" in metrics
                    assert "generation_time" in metrics
                    assert "total_time" in metrics
                    
                    # Check performance thresholds
                    assert metrics["total_time"] < 5.0  # Should complete within 5 seconds
                    assert metrics["embedding_time"] < 1.0  # Embedding should be fast
                    assert metrics["search_time"] < 1.0  # Search should be fast
    
    @pytest.mark.e2e
    @pytest.mark.skip_in_ci
    def test_real_aws_integration(self):
        """Test with real AWS services (skipped in CI)."""
        # This test would use real AWS services
        # Only run locally with proper credentials
        
        from app.controllers.rag_controller import RAGController
        
        # Initialize with real services
        rag_controller = RAGController(
            collection_name="test_real_aws",
            embedding_model_id="amazon.titan-embed-image-v1",
            llm_model_id="amazon.nova-1",
            use_real_services=True
        )
        
        # Test with a simple query
        result = rag_controller.process_query("What is AWS?")
        
        assert result is not None
        assert "answer" in result
        assert len(result["answer"]) > 0