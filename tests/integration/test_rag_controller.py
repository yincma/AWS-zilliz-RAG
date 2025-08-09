"""
Integration tests for the RAG Controller.
Tests the complete RAG pipeline flow from query to response.
"""

import pytest
from unittest.mock import Mock, patch, MagicMock
import json
from typing import List, Dict, Any

from app.controllers.rag_controller import RAGController
from app.models.embedding import EmbeddingModel
from app.models.vector_store import VectorStore
from app.models.llm import LLMModel


class TestRAGControllerIntegration:
    """Integration test cases for RAGController."""
    
    @pytest.fixture
    def mock_embedding_model(self):
        """Create a mock embedding model."""
        mock = Mock(spec=EmbeddingModel)
        mock.generate_embedding.return_value = [0.5] * 1024
        mock.dimension = 1024
        return mock
    
    @pytest.fixture
    def mock_vector_store(self):
        """Create a mock vector store."""
        mock = Mock(spec=VectorStore)
        mock.search.return_value = [
            {
                "id": 1,
                "distance": 0.95,
                "entity": {
                    "text": "RAG combines retrieval and generation for better AI responses.",
                    "source": "rag_guide.pdf",
                    "page": 5
                }
            },
            {
                "id": 2,
                "distance": 0.88,
                "entity": {
                    "text": "Vector databases enable semantic search in RAG systems.",
                    "source": "vector_db.pdf",
                    "page": 12
                }
            }
        ]
        return mock
    
    @pytest.fixture
    def mock_llm_model(self):
        """Create a mock LLM model."""
        mock = Mock(spec=LLMModel)
        mock.generate_with_context.return_value = (
            "Based on the provided documents, RAG (Retrieval-Augmented Generation) "
            "combines retrieval mechanisms with generative AI models to provide "
            "more accurate and contextual responses."
        )
        return mock
    
    @pytest.fixture
    def rag_controller(self, mock_embedding_model, mock_vector_store, mock_llm_model):
        """Create a RAGController with mocked dependencies."""
        with patch('app.controllers.rag_controller.EmbeddingModel', return_value=mock_embedding_model):
            with patch('app.controllers.rag_controller.VectorStore', return_value=mock_vector_store):
                with patch('app.controllers.rag_controller.LLMModel', return_value=mock_llm_model):
                    controller = RAGController(
                        collection_name="test_collection",
                        embedding_model_id="amazon.titan-embed-image-v1",
                        llm_model_id="amazon.nova-1"
                    )
                    controller.embedding_model = mock_embedding_model
                    controller.vector_store = mock_vector_store
                    controller.llm_model = mock_llm_model
                    return controller
    
    @pytest.mark.integration
    def test_process_query_full_pipeline(self, rag_controller):
        """Test the complete RAG pipeline from query to response."""
        query = "What is RAG and how does it work?"
        
        # Process query through the pipeline
        result = rag_controller.process_query(query)
        
        # Assertions
        assert result is not None
        assert "answer" in result
        assert "sources" in result
        assert "query" in result
        
        # Verify answer content
        assert "RAG" in result["answer"]
        assert "Retrieval-Augmented Generation" in result["answer"]
        
        # Verify sources
        assert len(result["sources"]) == 2
        assert result["sources"][0]["source"] == "rag_guide.pdf"
        assert result["sources"][1]["source"] == "vector_db.pdf"
        
        # Verify pipeline execution order
        rag_controller.embedding_model.generate_embedding.assert_called_once_with(query)
        rag_controller.vector_store.search.assert_called_once()
        rag_controller.llm_model.generate_with_context.assert_called_once()
    
    @pytest.mark.integration
    def test_process_query_with_filters(self, rag_controller, mock_vector_store):
        """Test query processing with metadata filters."""
        query = "What is machine learning?"
        filters = {"source": "ml_guide.pdf"}
        
        # Mock filtered search results
        mock_vector_store.search_with_filter.return_value = [
            {
                "id": 3,
                "distance": 0.92,
                "entity": {
                    "text": "Machine learning is a subset of AI.",
                    "source": "ml_guide.pdf",
                    "page": 1
                }
            }
        ]
        
        # Process query with filters
        result = rag_controller.process_query_with_filters(query, filters)
        
        # Assertions
        assert len(result["sources"]) == 1
        assert result["sources"][0]["source"] == "ml_guide.pdf"
        
        # Verify filtered search was used
        mock_vector_store.search_with_filter.assert_called_once()
    
    @pytest.mark.integration
    def test_ingest_documents(self, rag_controller, mock_embedding_model, mock_vector_store):
        """Test document ingestion into the vector store."""
        documents = [
            {
                "text": "This is the first document about AI.",
                "metadata": {"source": "doc1.pdf", "page": 1}
            },
            {
                "text": "This is the second document about ML.",
                "metadata": {"source": "doc2.pdf", "page": 1}
            }
        ]
        
        # Mock embedding generation
        mock_embedding_model.generate_batch_embeddings.return_value = [
            [0.1] * 1024,
            [0.2] * 1024
        ]
        
        # Mock insertion
        mock_vector_store.insert_embeddings.return_value = [1, 2]
        
        # Ingest documents
        result = rag_controller.ingest_documents(documents)
        
        # Assertions
        assert result["success"] is True
        assert result["document_count"] == 2
        assert result["ids"] == [1, 2]
        
        # Verify embeddings were generated
        mock_embedding_model.generate_batch_embeddings.assert_called_once()
        texts = mock_embedding_model.generate_batch_embeddings.call_args[0][0]
        assert len(texts) == 2
        
        # Verify insertion
        mock_vector_store.insert_embeddings.assert_called_once()
    
    @pytest.mark.integration
    def test_query_with_reranking(self, rag_controller):
        """Test query processing with result reranking."""
        query = "What are the benefits of RAG?"
        
        # Process with reranking enabled
        result = rag_controller.process_query(
            query,
            top_k=5,
            rerank=True,
            rerank_top_k=3
        )
        
        # Should return reranked results
        assert len(result["sources"]) <= 3
        assert result.get("reranked", False) is True
    
    @pytest.mark.integration
    def test_streaming_response(self, rag_controller, mock_llm_model):
        """Test streaming response generation."""
        query = "Explain vector databases"
        
        # Mock streaming response
        chunks = ["Vector ", "databases ", "are ", "specialized ", "systems."]
        mock_llm_model.generate_stream.return_value = iter(chunks)
        
        # Process with streaming
        response_chunks = []
        for chunk in rag_controller.process_query_stream(query):
            response_chunks.append(chunk)
        
        # Assertions
        assert len(response_chunks) == len(chunks)
        assert "".join(response_chunks) == "Vector databases are specialized systems."
        
        # Verify streaming was used
        mock_llm_model.generate_stream.assert_called_once()
    
    @pytest.mark.integration
    def test_error_handling_embedding_failure(self, rag_controller, mock_embedding_model):
        """Test error handling when embedding generation fails."""
        # Simulate embedding failure
        mock_embedding_model.generate_embedding.side_effect = Exception("Embedding API error")
        
        # Process query
        result = rag_controller.process_query("Test query")
        
        # Should handle error gracefully
        assert result["success"] is False
        assert "error" in result
        assert "Embedding API error" in result["error"]
    
    @pytest.mark.integration
    def test_error_handling_vector_search_failure(self, rag_controller, mock_vector_store):
        """Test error handling when vector search fails."""
        # Simulate search failure
        mock_vector_store.search.side_effect = Exception("Vector database error")
        
        # Process query
        result = rag_controller.process_query("Test query")
        
        # Should handle error gracefully
        assert result["success"] is False
        assert "error" in result
        assert "Vector database error" in result["error"]
    
    @pytest.mark.integration
    def test_error_handling_llm_failure(self, rag_controller, mock_llm_model):
        """Test error handling when LLM generation fails."""
        # Simulate LLM failure
        mock_llm_model.generate_with_context.side_effect = Exception("LLM generation error")
        
        # Process query
        result = rag_controller.process_query("Test query")
        
        # Should handle error gracefully
        assert result["success"] is False
        assert "error" in result
        assert "LLM generation error" in result["error"]
    
    @pytest.mark.integration
    def test_cache_integration(self, rag_controller):
        """Test query result caching."""
        query = "What is caching?"
        
        # First query - should hit all components
        result1 = rag_controller.process_query(query, use_cache=True)
        
        # Second identical query - should use cache
        result2 = rag_controller.process_query(query, use_cache=True)
        
        # Results should be identical
        assert result1 == result2
        
        # Embedding should only be called once (cached)
        assert rag_controller.embedding_model.generate_embedding.call_count == 1
    
    @pytest.mark.integration
    def test_batch_query_processing(self, rag_controller):
        """Test processing multiple queries in batch."""
        queries = [
            "What is machine learning?",
            "Explain deep learning",
            "What are neural networks?"
        ]
        
        # Process batch
        results = rag_controller.process_batch_queries(queries)
        
        # Assertions
        assert len(results) == 3
        for i, result in enumerate(results):
            assert result["query"] == queries[i]
            assert "answer" in result
            assert "sources" in result
    
    @pytest.mark.integration
    def test_context_window_management(self, rag_controller):
        """Test handling of context window limits."""
        query = "Summarize everything"
        
        # Mock many search results
        large_results = [
            {
                "id": i,
                "distance": 0.9 - (i * 0.01),
                "entity": {
                    "text": f"Document {i} " * 100,  # Long text
                    "source": f"doc{i}.pdf",
                    "page": 1
                }
            }
            for i in range(20)
        ]
        
        rag_controller.vector_store.search.return_value = large_results
        
        # Process query
        result = rag_controller.process_query(
            query,
            max_context_length=2000  # Limit context
        )
        
        # Should truncate context to fit
        assert result["success"] is True
        assert len(result["sources"]) < 20  # Some docs should be excluded
        assert result.get("context_truncated", False) is True
    
    @pytest.mark.integration
    def test_metadata_enrichment(self, rag_controller):
        """Test metadata enrichment in responses."""
        query = "Test query"
        
        # Process with metadata enrichment
        result = rag_controller.process_query(
            query,
            enrich_metadata=True
        )
        
        # Should include enriched metadata
        assert "processing_time" in result
        assert "model_versions" in result
        assert "timestamp" in result
        assert result["model_versions"]["embedding"] == "amazon.titan-embed-image-v1"
        assert result["model_versions"]["llm"] == "amazon.nova-1"