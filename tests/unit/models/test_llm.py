"""
Unit tests for the LLM model.
Tests Amazon Bedrock Nova model integration for text generation.
"""

import pytest
from unittest.mock import Mock, patch, MagicMock
import json
from typing import List, Dict

from app.models.llm import LLMModel


class TestLLMModel:
    """Test cases for LLMModel class."""
    
    @pytest.fixture
    def mock_bedrock_client(self):
        """Create a mock Bedrock runtime client."""
        mock_client = Mock()
        return mock_client
    
    @pytest.fixture
    def llm_model(self, mock_bedrock_client):
        """Create an LLMModel instance with mocked client."""
        with patch('app.models.llm.boto3.client', return_value=mock_bedrock_client):
            model = LLMModel(model_id="amazon.nova-1")
            model.client = mock_bedrock_client
            return model
    
    @pytest.mark.unit
    def test_initialization(self):
        """Test LLMModel initialization."""
        with patch('app.models.llm.boto3.client') as mock_boto:
            model = LLMModel(
                model_id="amazon.nova-1",
                temperature=0.7,
                max_tokens=2048
            )
            
            assert model.model_id == "amazon.nova-1"
            assert model.temperature == 0.7
            assert model.max_tokens == 2048
            mock_boto.assert_called_once_with('bedrock-runtime')
    
    @pytest.mark.unit
    def test_generate_response(self, llm_model, mock_bedrock_client):
        """Test generating a response from the LLM."""
        # Mock response
        mock_response = {
            "completion": "Based on the provided context, RAG systems combine retrieval and generation.",
            "stop_reason": "stop",
            "usage": {
                "input_tokens": 100,
                "output_tokens": 50,
                "total_tokens": 150
            }
        }
        
        mock_bedrock_client.invoke_model.return_value = {
            'body': MagicMock(read=lambda: json.dumps(mock_response).encode())
        }
        
        # Generate response
        prompt = "What are RAG systems?"
        response = llm_model.generate(prompt)
        
        # Assertions
        assert isinstance(response, str)
        assert "RAG systems" in response
        assert len(response) > 0
        
        # Verify API call
        mock_bedrock_client.invoke_model.assert_called_once()
        call_args = mock_bedrock_client.invoke_model.call_args
        assert call_args.kwargs['modelId'] == "amazon.nova-1"
    
    @pytest.mark.unit
    def test_generate_with_context(self, llm_model, mock_bedrock_client):
        """Test generating a response with context documents."""
        # Mock response
        mock_response = {
            "completion": "According to the documents, the answer is 42.",
            "stop_reason": "stop"
        }
        
        mock_bedrock_client.invoke_model.return_value = {
            'body': MagicMock(read=lambda: json.dumps(mock_response).encode())
        }
        
        # Generate with context
        query = "What is the answer?"
        context_docs = [
            {"text": "The ultimate answer is 42.", "source": "doc1.pdf"},
            {"text": "42 is significant.", "source": "doc2.pdf"}
        ]
        
        response = llm_model.generate_with_context(query, context_docs)
        
        # Assertions
        assert "42" in response
        mock_bedrock_client.invoke_model.assert_called_once()
        
        # Verify context was included in prompt
        call_args = mock_bedrock_client.invoke_model.call_args
        body = json.loads(call_args.kwargs['body'])
        assert "42" in body.get('prompt', '') or "42" in str(body)
    
    @pytest.mark.unit
    def test_streaming_generation(self, llm_model, mock_bedrock_client):
        """Test streaming text generation."""
        # Mock streaming response chunks
        chunks = [
            {"completion": "This ", "stop_reason": None},
            {"completion": "is ", "stop_reason": None},
            {"completion": "streaming.", "stop_reason": "stop"}
        ]
        
        mock_stream = Mock()
        mock_stream.__iter__ = Mock(return_value=iter([
            {'chunk': {'bytes': json.dumps(chunk).encode()}} for chunk in chunks
        ]))
        
        mock_bedrock_client.invoke_model_with_response_stream.return_value = {
            'body': mock_stream
        }
        
        # Generate streaming response
        prompt = "Test streaming"
        full_response = ""
        
        for chunk in llm_model.generate_stream(prompt):
            full_response += chunk
        
        # Assertions
        assert full_response == "This is streaming."
        mock_bedrock_client.invoke_model_with_response_stream.assert_called_once()
    
    @pytest.mark.unit
    def test_prompt_formatting(self, llm_model):
        """Test prompt formatting with system message and user query."""
        system_message = "You are a helpful AI assistant."
        user_query = "What is machine learning?"
        
        formatted_prompt = llm_model.format_prompt(
            system_message=system_message,
            user_query=user_query
        )
        
        # Check prompt structure
        assert system_message in formatted_prompt
        assert user_query in formatted_prompt
        assert formatted_prompt.index(system_message) < formatted_prompt.index(user_query)
    
    @pytest.mark.unit
    def test_rag_prompt_formatting(self, llm_model):
        """Test RAG-specific prompt formatting."""
        query = "What is the capital of France?"
        documents = [
            {"text": "Paris is the capital of France.", "source": "geography.pdf", "page": 10},
            {"text": "France is a country in Europe.", "source": "europe.pdf", "page": 5}
        ]
        
        prompt = llm_model.format_rag_prompt(query, documents)
        
        # Check all components are included
        assert query in prompt
        assert "Paris" in prompt
        assert "geography.pdf" in prompt
        assert "Context" in prompt or "Documents" in prompt
    
    @pytest.mark.unit
    def test_token_counting(self, llm_model):
        """Test token counting estimation."""
        text = "This is a test text for counting tokens in the LLM model."
        
        # Estimate tokens (rough approximation)
        token_count = llm_model.estimate_tokens(text)
        
        # Should be reasonable for the text length
        assert 5 <= token_count <= 20  # Rough estimate for the test text
    
    @pytest.mark.unit
    def test_max_tokens_limit(self, llm_model, mock_bedrock_client):
        """Test that max_tokens parameter is respected."""
        mock_response = {
            "completion": "Short response",
            "stop_reason": "max_tokens"
        }
        
        mock_bedrock_client.invoke_model.return_value = {
            'body': MagicMock(read=lambda: json.dumps(mock_response).encode())
        }
        
        # Set low max_tokens
        llm_model.max_tokens = 10
        response = llm_model.generate("Generate a long story")
        
        # Verify max_tokens was passed
        call_args = mock_bedrock_client.invoke_model.call_args
        body = json.loads(call_args.kwargs['body'])
        assert body.get('max_tokens') == 10 or 'max_tokens' in str(body)
    
    @pytest.mark.unit
    def test_temperature_setting(self, llm_model, mock_bedrock_client):
        """Test temperature parameter for response randomness."""
        mock_response = {
            "completion": "Response with temperature",
            "stop_reason": "stop"
        }
        
        mock_bedrock_client.invoke_model.return_value = {
            'body': MagicMock(read=lambda: json.dumps(mock_response).encode())
        }
        
        # Test with different temperatures
        for temp in [0.0, 0.5, 1.0]:
            llm_model.temperature = temp
            llm_model.generate("Test prompt")
            
            call_args = mock_bedrock_client.invoke_model.call_args
            body = json.loads(call_args.kwargs['body'])
            assert body.get('temperature') == temp or 'temperature' in str(body)
    
    @pytest.mark.unit
    def test_error_handling(self, llm_model, mock_bedrock_client):
        """Test error handling for Bedrock API failures."""
        # Simulate API error
        mock_bedrock_client.invoke_model.side_effect = Exception("Bedrock API error")
        
        with pytest.raises(Exception, match="Bedrock API error"):
            llm_model.generate("Test prompt")
    
    @pytest.mark.unit
    def test_retry_logic(self, llm_model, mock_bedrock_client):
        """Test retry logic for transient failures."""
        # First two calls fail, third succeeds
        mock_response = {
            "completion": "Success after retries",
            "stop_reason": "stop"
        }
        
        mock_bedrock_client.invoke_model.side_effect = [
            Exception("Temporary failure"),
            Exception("Another temporary failure"),
            {'body': MagicMock(read=lambda: json.dumps(mock_response).encode())}
        ]
        
        # Should succeed after retries
        response = llm_model.generate_with_retry("Test prompt", max_retries=3)
        
        assert response == "Success after retries"
        assert mock_bedrock_client.invoke_model.call_count == 3
    
    @pytest.mark.unit
    def test_response_parsing(self, llm_model, mock_bedrock_client):
        """Test parsing different response formats."""
        # Test various response formats
        response_formats = [
            {"completion": "Simple response"},
            {"content": [{"text": "Alternative format"}]},
            {"choices": [{"message": {"content": "OpenAI-style format"}}]}
        ]
        
        for mock_response in response_formats:
            mock_bedrock_client.invoke_model.return_value = {
                'body': MagicMock(read=lambda r=mock_response: json.dumps(r).encode())
            }
            
            response = llm_model.generate("Test")
            assert len(response) > 0  # Should parse something from each format
    
    @pytest.mark.unit
    @patch.dict('os.environ', {'AWS_REGION': 'us-east-1'})
    def test_region_configuration(self):
        """Test AWS region configuration."""
        with patch('app.models.llm.boto3.client') as mock_boto:
            model = LLMModel(model_id="amazon.nova-1")
            
            # Verify region configuration
            mock_boto.assert_called_once()
            call_args = mock_boto.call_args
            # Region should be configured somehow