"""
Integration tests for RAG system components.
Tests the integration between models, controllers, and views.
"""

import os
import sys
import pytest
import json
from unittest.mock import Mock, patch, MagicMock
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))


class TestRAGIntegration:
    """Integration tests for RAG system."""
    
    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup test environment."""
        os.environ["TEST_ENV"] = "true"
        os.environ["AWS_REGION"] = "us-east-1"
        os.environ["ZILLIZ_ENDPOINT"] = "test-endpoint"
        os.environ["ZILLIZ_TOKEN"] = "test-token"
    
    @pytest.mark.integration
    def test_health_check(self):
        """Test system health check."""
        # Basic health check
        assert os.environ.get("TEST_ENV") == "true"
        assert os.environ.get("AWS_REGION") == "us-east-1"
    
    @pytest.mark.integration
    def test_embedding_model_mock(self):
        """Test embedding model with mock."""
        with patch('boto3.client') as mock_boto:
            mock_client = Mock()
            mock_boto.return_value = mock_client
            
            # Mock Bedrock response
            mock_response = {
                'embedding': [0.1] * 1024
            }
            mock_client.invoke_model.return_value = {
                'body': MagicMock(read=lambda: json.dumps(mock_response).encode())
            }
            
            # Test embedding generation
            from app.models.embedding import EmbeddingModel
            model = EmbeddingModel(model_id="amazon.titan-embed-image-v1")
            
            # Generate embedding
            text = "Test document for integration"
            embedding = model.generate_embedding(text)
            
            assert isinstance(embedding, list)
            assert len(embedding) == 1024
    
    @pytest.mark.integration
    def test_vector_store_mock(self):
        """Test vector store with mock."""
        with patch('pymilvus.connections.connect') as mock_connect:
            with patch('pymilvus.Collection') as mock_collection_class:
                mock_connect.return_value = True
                mock_collection = Mock()
                mock_collection_class.return_value = mock_collection
                
                # Mock search results
                mock_collection.search.return_value = [[
                    {
                        "id": 1,
                        "distance": 0.95,
                        "entity": {"text": "Test result"}
                    }
                ]]
                
                from app.models.vector_store import VectorStore
                store = VectorStore(
                    collection_name="test_collection",
                    dimension=1024
                )
                
                # Test search
                results = store.search([0.5] * 1024, top_k=5)
                assert len(results) > 0
    
    @pytest.mark.integration
    def test_llm_model_mock(self):
        """Test LLM model with mock."""
        with patch('boto3.client') as mock_boto:
            mock_client = Mock()
            mock_boto.return_value = mock_client
            
            # Mock Bedrock LLM response
            mock_response = {
                'completion': 'This is a test response from the LLM.'
            }
            mock_client.invoke_model.return_value = {
                'body': MagicMock(read=lambda: json.dumps(mock_response).encode())
            }
            
            from app.models.llm import LLMModel
            model = LLMModel(model_id="amazon.nova-1")
            
            # Generate response
            response = model.generate("What is RAG?")
            assert isinstance(response, str)
            assert len(response) > 0
    
    @pytest.mark.integration
    def test_document_processing(self):
        """Test document processing pipeline."""
        with patch('app.models.document.DocumentLoader') as mock_loader:
            mock_loader.return_value.load.return_value = [
                {"text": "Page 1 content", "metadata": {"page": 1}},
                {"text": "Page 2 content", "metadata": {"page": 2}}
            ]
            
            from app.models.document import DocumentModel
            doc_model = DocumentModel()
            
            # Process document
            chunks = doc_model.process_document("test.pdf")
            assert len(chunks) == 2
            assert chunks[0]["text"] == "Page 1 content"
    
    @pytest.mark.integration
    def test_rag_controller_integration(self):
        """Test RAG controller with all components mocked."""
        with patch('boto3.client') as mock_boto:
            with patch('pymilvus.connections.connect') as mock_connect:
                with patch('pymilvus.Collection') as mock_collection_class:
                    # Setup mocks
                    mock_client = Mock()
                    mock_boto.return_value = mock_client
                    mock_connect.return_value = True
                    mock_collection = Mock()
                    mock_collection_class.return_value = mock_collection
                    
                    # Mock embedding response
                    mock_client.invoke_model.side_effect = [
                        {'body': MagicMock(read=lambda: json.dumps({'embedding': [0.5] * 1024}).encode())},
                        {'body': MagicMock(read=lambda: json.dumps({'completion': 'RAG is a technique.'}).encode())}
                    ]
                    
                    # Mock vector search
                    mock_collection.search.return_value = [[
                        {
                            "id": 1,
                            "distance": 0.95,
                            "entity": {
                                "text": "RAG combines retrieval and generation.",
                                "source": "doc.pdf"
                            }
                        }
                    ]]
                    
                    from app.controllers.rag_controller import RAGController
                    controller = RAGController(
                        collection_name="test",
                        embedding_model_id="amazon.titan-embed-image-v1",
                        llm_model_id="amazon.nova-1"
                    )
                    
                    # Process query
                    result = controller.process_query("What is RAG?")
                    
                    assert result is not None
                    assert "answer" in result
                    assert "sources" in result
    
    @pytest.mark.integration
    def test_api_response_formatting(self):
        """Test API response formatting."""
        from app.views.api.responses import ResponseFormatter
        
        formatter = ResponseFormatter()
        
        # Test success response
        response = formatter.format_success({
            "answer": "Test answer",
            "sources": ["doc1.pdf", "doc2.pdf"]
        })
        
        assert response["status"] == "success"
        assert "data" in response
        assert response["data"]["answer"] == "Test answer"
        
        # Test error response
        error_response = formatter.format_error("Test error")
        assert error_response["status"] == "error"
        assert error_response["error"] == "Test error"
    
    @pytest.mark.integration
    def test_document_controller_integration(self):
        """Test document controller operations."""
        with patch('boto3.client') as mock_boto:
            mock_s3 = Mock()
            mock_boto.return_value = mock_s3
            
            # Mock S3 operations
            mock_s3.upload_fileobj.return_value = None
            mock_s3.list_objects_v2.return_value = {
                'Contents': [
                    {'Key': 'doc1.pdf', 'Size': 1024},
                    {'Key': 'doc2.pdf', 'Size': 2048}
                ]
            }
            
            from app.controllers.document_controller import DocumentController
            controller = DocumentController(
                s3_bucket="test-bucket",
                s3_prefix="documents/"
            )
            
            # List documents
            docs = controller.list_documents()
            assert len(docs) == 2
            assert docs[0]['Key'] == 'doc1.pdf'
    
    @pytest.mark.integration
    def test_search_controller_integration(self):
        """Test search controller functionality."""
        with patch('pymilvus.connections.connect') as mock_connect:
            with patch('pymilvus.Collection') as mock_collection_class:
                mock_connect.return_value = True
                mock_collection = Mock()
                mock_collection_class.return_value = mock_collection
                
                # Mock search with filters
                mock_collection.search.return_value = [[
                    {
                        "id": 1,
                        "distance": 0.92,
                        "entity": {
                            "text": "Filtered result",
                            "source": "specific.pdf"
                        }
                    }
                ]]
                
                from app.controllers.search_controller import SearchController
                controller = SearchController(collection_name="test")
                
                # Search with filter
                results = controller.search_with_filter(
                    query_vector=[0.5] * 1024,
                    filter_expr="source == 'specific.pdf'"
                )
                
                assert len(results) > 0
                assert results[0]["entity"]["source"] == "specific.pdf"
    
    @pytest.mark.integration
    def test_end_to_end_query_flow(self):
        """Test complete query flow from request to response."""
        with patch('boto3.client') as mock_boto:
            with patch('pymilvus.connections.connect') as mock_connect:
                with patch('pymilvus.Collection') as mock_collection_class:
                    # Setup comprehensive mocks
                    mock_client = Mock()
                    mock_boto.return_value = mock_client
                    mock_connect.return_value = True
                    mock_collection = Mock()
                    mock_collection_class.return_value = mock_collection
                    
                    # Mock complete flow
                    mock_client.invoke_model.side_effect = [
                        # Embedding call
                        {'body': MagicMock(read=lambda: json.dumps({'embedding': [0.5] * 1024}).encode())},
                        # LLM call
                        {'body': MagicMock(read=lambda: json.dumps({
                            'completion': 'Based on the documents, here is the answer.'
                        }).encode())}
                    ]
                    
                    mock_collection.search.return_value = [[
                        {
                            "id": 1,
                            "distance": 0.95,
                            "entity": {
                                "text": "Relevant document content.",
                                "source": "source.pdf",
                                "page": 1
                            }
                        }
                    ]]
                    
                    # Import and test
                    from app.controllers.rag_controller import RAGController
                    from app.views.api.responses import ResponseFormatter
                    
                    controller = RAGController(
                        collection_name="test",
                        embedding_model_id="amazon.titan-embed-image-v1",
                        llm_model_id="amazon.nova-1"
                    )
                    formatter = ResponseFormatter()
                    
                    # Process complete request
                    query = "What is the answer?"
                    raw_result = controller.process_query(query)
                    formatted_result = formatter.format_success(raw_result)
                    
                    # Validate complete response
                    assert formatted_result["status"] == "success"
                    assert "data" in formatted_result
                    assert "answer" in formatted_result["data"]
                    assert "sources" in formatted_result["data"]
                    assert len(formatted_result["data"]["sources"]) > 0