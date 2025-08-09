"""
Unit tests for the VectorStore model.
Tests Zilliz/Milvus integration for vector storage and retrieval.
"""

import pytest
from unittest.mock import Mock, patch, MagicMock
from typing import List, Dict, Any

from app.models.vector_store import VectorStore


class TestVectorStore:
    """Test cases for VectorStore class."""
    
    @pytest.fixture
    def mock_collection(self):
        """Create a mock Milvus collection."""
        mock_col = Mock()
        mock_col.name = "test_collection"
        mock_col.num_entities = 100
        return mock_col
    
    @pytest.fixture
    def vector_store(self, mock_collection):
        """Create a VectorStore instance with mocked collection."""
        with patch('app.models.vector_store.connections.connect'):
            with patch('app.models.vector_store.Collection', return_value=mock_collection):
                store = VectorStore(
                    collection_name="test_collection",
                    dimension=1024,
                    endpoint="localhost:19530",
                    token="test_token"
                )
                store.collection = mock_collection
                return store
    
    @pytest.mark.unit
    def test_initialization(self):
        """Test VectorStore initialization."""
        with patch('app.models.vector_store.connections.connect') as mock_connect:
            with patch('app.models.vector_store.Collection') as mock_collection_class:
                store = VectorStore(
                    collection_name="rag_collection",
                    dimension=1024,
                    endpoint="localhost:19530",
                    token="test_token"
                )
                
                assert store.collection_name == "rag_collection"
                assert store.dimension == 1024
                mock_connect.assert_called_once()
    
    @pytest.mark.unit
    def test_create_collection_if_not_exists(self, vector_store):
        """Test collection creation when it doesn't exist."""
        with patch('app.models.vector_store.utility.has_collection', return_value=False):
            with patch('app.models.vector_store.CollectionSchema') as mock_schema:
                with patch('app.models.vector_store.Collection') as mock_collection_class:
                    
                    vector_store.create_collection_if_not_exists()
                    
                    # Verify schema was created with correct fields
                    mock_schema.assert_called_once()
                    # Verify collection was created
                    mock_collection_class.assert_called()
    
    @pytest.mark.unit
    def test_insert_embeddings(self, vector_store, mock_collection):
        """Test inserting embeddings with metadata."""
        # Prepare test data
        embeddings = [
            [0.1] * 1024,
            [0.2] * 1024,
            [0.3] * 1024
        ]
        
        metadata = [
            {"text": "Document 1", "source": "file1.pdf", "page": 1},
            {"text": "Document 2", "source": "file2.pdf", "page": 2},
            {"text": "Document 3", "source": "file3.pdf", "page": 3}
        ]
        
        # Mock insert response
        mock_collection.insert.return_value = MagicMock(primary_keys=[1, 2, 3])
        
        # Insert data
        ids = vector_store.insert_embeddings(embeddings, metadata)
        
        # Assertions
        assert ids == [1, 2, 3]
        mock_collection.insert.assert_called_once()
        
        # Verify data format
        call_args = mock_collection.insert.call_args
        data = call_args[0][0]
        assert len(data) == 3  # 3 records
    
    @pytest.mark.unit
    def test_search_similar_vectors(self, vector_store, mock_collection):
        """Test searching for similar vectors."""
        # Mock search results
        mock_results = [
            [
                {"id": 1, "distance": 0.95, "entity": {"text": "Similar doc 1"}},
                {"id": 2, "distance": 0.85, "entity": {"text": "Similar doc 2"}},
                {"id": 3, "distance": 0.75, "entity": {"text": "Similar doc 3"}}
            ]
        ]
        mock_collection.search.return_value = mock_results
        
        # Perform search
        query_vector = [0.5] * 1024
        results = vector_store.search(
            query_vector=query_vector,
            top_k=3,
            score_threshold=0.7
        )
        
        # Assertions
        assert len(results) == 3
        assert results[0]["distance"] == 0.95
        assert results[0]["entity"]["text"] == "Similar doc 1"
        
        # Verify search parameters
        mock_collection.search.assert_called_once()
        call_args = mock_collection.search.call_args
        assert call_args.kwargs.get("limit") == 3
    
    @pytest.mark.unit
    def test_delete_by_ids(self, vector_store, mock_collection):
        """Test deleting vectors by IDs."""
        # Mock delete response
        mock_collection.delete.return_value = MagicMock(delete_count=3)
        
        # Delete vectors
        ids_to_delete = [1, 2, 3]
        delete_count = vector_store.delete_by_ids(ids_to_delete)
        
        # Assertions
        assert delete_count == 3
        mock_collection.delete.assert_called_once_with(expr=f"id in {ids_to_delete}")
    
    @pytest.mark.unit
    def test_get_collection_stats(self, vector_store, mock_collection):
        """Test getting collection statistics."""
        # Mock collection properties
        mock_collection.num_entities = 1000
        mock_collection.name = "test_collection"
        
        with patch('app.models.vector_store.utility.get_collection_stats') as mock_stats:
            mock_stats.return_value = {
                "row_count": 1000,
                "data_size": 1024000,
                "index_size": 512000
            }
            
            stats = vector_store.get_collection_stats()
            
            # Assertions
            assert stats["row_count"] == 1000
            assert stats["data_size"] == 1024000
            assert stats["index_size"] == 512000
    
    @pytest.mark.unit
    def test_create_index(self, vector_store, mock_collection):
        """Test creating an index on the vector field."""
        # Mock index creation
        mock_collection.create_index.return_value = None
        
        # Create index
        index_params = {
            "index_type": "IVF_FLAT",
            "metric_type": "IP",
            "params": {"nlist": 128}
        }
        
        vector_store.create_index(field_name="embedding", index_params=index_params)
        
        # Verify index creation
        mock_collection.create_index.assert_called_once()
        call_args = mock_collection.create_index.call_args
        assert call_args.kwargs.get("field_name") == "embedding"
    
    @pytest.mark.unit
    def test_load_collection(self, vector_store, mock_collection):
        """Test loading collection into memory."""
        mock_collection.load.return_value = None
        
        vector_store.load_collection()
        
        mock_collection.load.assert_called_once()
    
    @pytest.mark.unit
    def test_release_collection(self, vector_store, mock_collection):
        """Test releasing collection from memory."""
        mock_collection.release.return_value = None
        
        vector_store.release_collection()
        
        mock_collection.release.assert_called_once()
    
    @pytest.mark.unit
    def test_batch_insert_with_chunking(self, vector_store, mock_collection):
        """Test batch insertion with automatic chunking for large datasets."""
        # Create large dataset
        large_embeddings = [[0.1] * 1024 for _ in range(10000)]
        large_metadata = [{"text": f"Doc {i}"} for i in range(10000)]
        
        # Mock insert responses
        mock_collection.insert.return_value = MagicMock(primary_keys=list(range(1000)))
        
        # Insert with chunking
        ids = vector_store.batch_insert(
            embeddings=large_embeddings,
            metadata=large_metadata,
            batch_size=1000
        )
        
        # Should be called 10 times (10000 / 1000)
        assert mock_collection.insert.call_count == 10
        assert len(ids) == 10000
    
    @pytest.mark.unit
    def test_connection_error_handling(self):
        """Test handling of connection errors."""
        with patch('app.models.vector_store.connections.connect', side_effect=Exception("Connection failed")):
            with pytest.raises(Exception, match="Connection failed"):
                VectorStore(
                    collection_name="test",
                    dimension=1024,
                    endpoint="invalid:19530",
                    token="invalid"
                )
    
    @pytest.mark.unit
    def test_search_with_filter(self, vector_store, mock_collection):
        """Test searching with metadata filters."""
        # Mock filtered search results
        mock_results = [
            [
                {"id": 1, "distance": 0.95, "entity": {"text": "Filtered doc", "source": "target.pdf"}}
            ]
        ]
        mock_collection.search.return_value = mock_results
        
        # Search with filter
        query_vector = [0.5] * 1024
        results = vector_store.search_with_filter(
            query_vector=query_vector,
            filter_expr="source == 'target.pdf'",
            top_k=5
        )
        
        # Assertions
        assert len(results) == 1
        assert results[0]["entity"]["source"] == "target.pdf"
        
        # Verify filter was applied
        call_args = mock_collection.search.call_args
        assert "expr" in call_args.kwargs
        assert call_args.kwargs["expr"] == "source == 'target.pdf'"