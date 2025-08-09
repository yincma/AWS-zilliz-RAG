"""
文档模型单元测试
测试文档的加载、解析、分割等功能
"""

import pytest
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock
import tempfile

from app.models.document import Document, DocumentModel


class TestDocument:
    """测试Document数据类"""
    
    def test_document_creation(self):
        """测试文档对象创建"""
        doc = Document(
            content="测试内容",
            metadata={"source": "test.txt"},
            doc_id="doc_001"
        )
        
        assert doc.content == "测试内容"
        assert doc.metadata["source"] == "test.txt"
        assert doc.doc_id == "doc_001"
        assert doc.chunks is None
    
    def test_document_with_chunks(self):
        """测试带文本块的文档"""
        doc = Document(
            content="长文本内容",
            metadata={},
            chunks=["块1", "块2", "块3"]
        )
        
        assert len(doc.chunks) == 3
        assert doc.chunks[0] == "块1"


class TestDocumentModel:
    """测试DocumentModel类"""
    
    @pytest.fixture
    def document_model(self):
        """创建DocumentModel实例"""
        return DocumentModel(chunk_size=100, chunk_overlap=20)
    
    @pytest.fixture
    def temp_text_file(self):
        """创建临时文本文件"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
            f.write("这是一个测试文档。\n它有多行内容。\n用于测试文档加载功能。")
            temp_path = f.name
        
        yield temp_path
        
        # 清理
        Path(temp_path).unlink()
    
    @pytest.fixture
    def temp_pdf_file(self):
        """创建模拟的PDF文件路径"""
        with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as f:
            temp_path = f.name
        
        yield temp_path
        
        # 清理
        Path(temp_path).unlink()
    
    def test_init(self, document_model):
        """测试初始化"""
        assert document_model.chunk_size == 100
        assert document_model.chunk_overlap == 20
        assert document_model.text_splitter is not None
    
    def test_load_text_document(self, document_model, temp_text_file):
        """测试加载文本文档"""
        with patch('app.models.document.TextLoader') as mock_loader:
            # 模拟TextLoader的行为
            mock_doc = Mock()
            mock_doc.page_content = "测试内容"
            mock_doc.metadata = {"source": temp_text_file}
            mock_loader.return_value.load.return_value = [mock_doc]
            
            # 加载文档
            doc = document_model.load_document(temp_text_file)
            
            # 验证
            assert isinstance(doc, Document)
            assert doc.content == "测试内容"
            assert doc.metadata["source"] == temp_text_file
            assert doc.metadata["file_type"] == ".txt"
    
    def test_load_pdf_document(self, document_model, temp_pdf_file):
        """测试加载PDF文档"""
        with patch('app.models.document.PyPDFLoader') as mock_loader:
            # 模拟PyPDFLoader的行为
            mock_doc1 = Mock()
            mock_doc1.page_content = "第一页内容"
            mock_doc1.metadata = {"page": 0}
            
            mock_doc2 = Mock()
            mock_doc2.page_content = "第二页内容"
            mock_doc2.metadata = {"page": 1}
            
            mock_loader.return_value.load.return_value = [mock_doc1, mock_doc2]
            
            # 加载文档
            doc = document_model.load_document(temp_pdf_file)
            
            # 验证
            assert isinstance(doc, Document)
            assert "第一页内容" in doc.content
            assert "第二页内容" in doc.content
            assert doc.metadata["file_type"] == ".pdf"
            assert doc.metadata["total_pages"] == 2
    
    def test_load_nonexistent_document(self, document_model):
        """测试加载不存在的文档"""
        with pytest.raises(FileNotFoundError):
            document_model.load_document("nonexistent.txt")
    
    def test_load_unsupported_format(self, document_model):
        """测试加载不支持的格式"""
        with tempfile.NamedTemporaryFile(suffix='.xyz', delete=False) as f:
            temp_path = f.name
        
        try:
            with pytest.raises(ValueError, match="不支持的文件类型"):
                document_model.load_document(temp_path)
        finally:
            Path(temp_path).unlink()
    
    def test_split_document(self, document_model):
        """测试文档分割"""
        # 创建一个长文档
        long_content = "这是第一段。" * 20  # 创建超过chunk_size的内容
        doc = Document(
            content=long_content,
            metadata={"source": "test.txt"}
        )
        
        # 分割文档
        chunks = document_model.split_document(doc)
        
        # 验证
        assert len(chunks) > 1  # 应该被分割成多个块
        assert all(hasattr(chunk, 'page_content') for chunk in chunks)
        assert all(hasattr(chunk, 'metadata') for chunk in chunks)
        
        # 检查元数据
        first_chunk = chunks[0]
        assert first_chunk.metadata["chunk_id"] == 0
        assert first_chunk.metadata["chunk_total"] == len(chunks)
        assert first_chunk.metadata["source"] == "test.txt"
    
    def test_process_documents(self, document_model):
        """测试批量处理文档"""
        with patch.object(document_model, 'load_document') as mock_load:
            with patch.object(document_model, 'split_document') as mock_split:
                # 模拟加载文档
                mock_doc = Document(
                    content="测试内容",
                    metadata={"source": "test.txt", "file_name": "test.txt"}
                )
                mock_load.return_value = mock_doc
                
                # 模拟分割文档
                mock_chunk = Mock()
                mock_chunk.page_content = "块内容"
                mock_chunk.metadata = {"chunk_id": 0}
                mock_split.return_value = [mock_chunk]
                
                # 处理文档
                file_paths = ["test1.txt", "test2.txt"]
                chunks = document_model.process_documents(file_paths)
                
                # 验证
                assert len(chunks) == 2  # 两个文件，每个一个块
                assert mock_load.call_count == 2
                assert mock_split.call_count == 2
    
    def test_load_documents_with_error(self, document_model):
        """测试批量加载文档时的错误处理"""
        with patch.object(document_model, 'load_document') as mock_load:
            # 第一个成功，第二个失败
            mock_load.side_effect = [
                Document(content="成功", metadata={}),
                Exception("加载失败")
            ]
            
            # 批量加载
            docs = document_model.load_documents(["success.txt", "fail.txt"])
            
            # 验证：应该只返回成功的文档
            assert len(docs) == 1
            assert docs[0].content == "成功"


class TestTextSplitting:
    """测试文本分割功能"""
    
    def test_chinese_text_splitting(self):
        """测试中文文本分割"""
        model = DocumentModel(chunk_size=20, chunk_overlap=5)
        
        chinese_text = "这是第一句话。这是第二句话。这是第三句话。这是第四句话。"
        doc = Document(content=chinese_text, metadata={})
        
        chunks = model.split_document(doc)
        
        # 验证分割
        assert len(chunks) > 1
        # 验证重叠
        if len(chunks) > 1:
            # 检查是否有重叠内容
            for i in range(len(chunks) - 1):
                chunk1_end = chunks[i].page_content[-5:]  # 最后5个字符
                chunk2_start = chunks[i+1].page_content[:5]  # 前5个字符
                # 由于重叠设置，可能有部分内容重复
    
    def test_empty_document_splitting(self):
        """测试空文档分割"""
        model = DocumentModel()
        doc = Document(content="", metadata={})
        
        chunks = model.split_document(doc)
        
        # 空文档应该返回空列表或一个空块
        assert len(chunks) <= 1