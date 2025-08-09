"""
Unit tests for the Embedding model.
Tests Amazon Titan Multimodal Embeddings G1 integration.
"""

import pytest
from unittest.mock import Mock, patch, MagicMock
import numpy as np
from typing import List

from app.models.embedding import EmbeddingModel


class TestEmbeddingModel:
    """Test cases for EmbeddingModel class."""
    
    @pytest.fixture
    def mock_bedrock_client(self):
        """Create a mock Bedrock runtime client."""
        mock_client = Mock()
        return mock_client
    
    @pytest.fixture
    def embedding_model(self, mock_bedrock_client):
        """Create an EmbeddingModel instance with mocked client."""
        with patch('app.models.embedding.boto3.client', return_value=mock_bedrock_client):
            model = EmbeddingModel(model_id="amazon.titan-embed-image-v1")
            model.client = mock_bedrock_client
            return model
    
    @pytest.mark.unit
    def test_initialization(self):
        """Test EmbeddingModel initialization."""
        with patch('app.models.embedding.boto3.client') as mock_boto:
            model = EmbeddingModel(model_id="amazon.titan-embed-image-v1")
            
            assert model.model_id == "amazon.titan-embed-image-v1"
            assert model.dimension == 1024  # Titan embedding dimension
            mock_boto.assert_called_once_with('bedrock-runtime')
    
    @pytest.mark.unit
    def test_generate_single_embedding(self, embedding_model, mock_bedrock_client):
        """Test generating a single text embedding."""
        # Mock response
        mock_response = {
            'embedding': [0.1] * 1024  # Titan uses 1024 dimensions
        }
        mock_bedrock_client.invoke_model.return_value = {
            'body': MagicMock(read=lambda: str(mock_response).encode())
        }
        
        # Generate embedding
        text = "This is a test document about RAG systems."
        embedding = embedding_model.generate_embedding(text)
        
        # Assertions
        assert isinstance(embedding, list)
        assert len(embedding) == 1024
        assert all(isinstance(x, float) for x in embedding)
        
        # Verify API call
        mock_bedrock_client.invoke_model.assert_called_once()
        call_args = mock_bedrock_client.invoke_model.call_args
        assert call_args.kwargs['modelId'] == "amazon.titan-embed-image-v1"
    
    @pytest.mark.unit
    def test_generate_batch_embeddings(self, embedding_model, mock_bedrock_client):
        """Test generating embeddings for multiple texts."""
        # Mock response for each text
        mock_response = {
            'embedding': [0.2] * 1024
        }
        mock_bedrock_client.invoke_model.return_value = {
            'body': MagicMock(read=lambda: str(mock_response).encode())
        }
        
        # Generate batch embeddings
        texts = [
            "First document about machine learning",
            "Second document about vector databases",
            "Third document about AWS services"
        ]
        embeddings = embedding_model.generate_batch_embeddings(texts)
        
        # Assertions
        assert isinstance(embeddings, list)
        assert len(embeddings) == 3
        assert all(len(emb) == 1024 for emb in embeddings)
        
        # Verify multiple API calls
        assert mock_bedrock_client.invoke_model.call_count == 3
    
    @pytest.mark.unit
    def test_empty_text_handling(self, embedding_model):
        """Test handling of empty text input."""
        with pytest.raises(ValueError, match="Input text cannot be empty"):
            embedding_model.generate_embedding("")
    
    @pytest.mark.unit
    def test_long_text_truncation(self, embedding_model, mock_bedrock_client):
        """Test that long texts are properly truncated."""
        # Mock response
        mock_response = {
            'embedding': [0.3] * 1024
        }
        mock_bedrock_client.invoke_model.return_value = {
            'body': MagicMock(read=lambda: str(mock_response).encode())
        }
        
        # Generate embedding for very long text
        long_text = "This is a very long document. " * 1000  # ~6000 tokens
        embedding = embedding_model.generate_embedding(long_text)
        
        # Should still return valid embedding
        assert len(embedding) == 1024
        
        # Verify text was truncated in the request
        call_args = mock_bedrock_client.invoke_model.call_args
        body = call_args.kwargs.get('body')
        assert body is not None
    
    @pytest.mark.unit
    def test_bedrock_error_handling(self, embedding_model, mock_bedrock_client):
        """Test error handling for Bedrock API failures."""
        # Simulate Bedrock error
        mock_bedrock_client.invoke_model.side_effect = Exception("Bedrock API error")
        
        with pytest.raises(Exception, match="Bedrock API error"):
            embedding_model.generate_embedding("Test text")
    
    @pytest.mark.unit
    def test_normalize_embeddings(self, embedding_model):
        """Test embedding normalization."""
        # Create unnormalized embedding
        embedding = [3.0, 4.0, 0.0]  # Magnitude = 5
        
        normalized = embedding_model.normalize_embedding(embedding)
        
        # Check normalization
        assert len(normalized) == 3
        assert abs(normalized[0] - 0.6) < 0.001
        assert abs(normalized[1] - 0.8) < 0.001
        assert abs(normalized[2] - 0.0) < 0.001
        
        # Check magnitude is 1
        magnitude = np.linalg.norm(normalized)
        assert abs(magnitude - 1.0) < 0.001
    
    @pytest.mark.unit
    def test_similarity_calculation(self, embedding_model):
        """Test cosine similarity calculation between embeddings."""
        # Create test embeddings
        emb1 = [1.0, 0.0, 0.0]
        emb2 = [1.0, 0.0, 0.0]  # Same as emb1
        emb3 = [0.0, 1.0, 0.0]  # Orthogonal to emb1
        emb4 = [-1.0, 0.0, 0.0]  # Opposite to emb1
        
        # Test similarities
        assert embedding_model.cosine_similarity(emb1, emb2) == pytest.approx(1.0)
        assert embedding_model.cosine_similarity(emb1, emb3) == pytest.approx(0.0)
        assert embedding_model.cosine_similarity(emb1, emb4) == pytest.approx(-1.0)
    
    @pytest.mark.unit
    @patch.dict('os.environ', {'AWS_REGION': 'us-west-2'})
    def test_region_configuration(self):
        """Test that AWS region is properly configured."""
        with patch('app.models.embedding.boto3.client') as mock_boto:
            model = EmbeddingModel(model_id="amazon.titan-embed-image-v1")
            
            # Verify region was passed to boto3
            mock_boto.assert_called_once()
            call_args = mock_boto.call_args
            assert 'region_name' in call_args.kwargs or call_args.kwargs == {'region_name': 'us-west-2'}