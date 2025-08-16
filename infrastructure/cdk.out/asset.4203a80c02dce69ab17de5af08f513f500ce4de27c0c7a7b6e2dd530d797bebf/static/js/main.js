// RAG系统前端主JavaScript文件

// API配置
const API_BASE_URL = window.RAG_CONFIG ? window.RAG_CONFIG.API_BASE_URL : 
    (window.location.hostname === 'localhost' ? 'http://localhost:8000' : '/api');

// 全局状态
let currentFiles = [];
let isLoading = false;

// DOM元素
const elements = {
    queryInput: document.getElementById('queryInput'),
    queryBtn: document.getElementById('queryBtn'),
    topK: document.getElementById('topK'),
    answerSection: document.getElementById('answerSection'),
    answerContent: document.getElementById('answerContent'),
    confidenceBar: document.getElementById('confidenceBar'),
    confidenceFill: document.getElementById('confidenceFill'),
    confidenceValue: document.getElementById('confidenceValue'),
    sourcesSection: document.getElementById('sourcesSection'),
    sourcesList: document.getElementById('sourcesList'),
    uploadArea: document.getElementById('uploadArea'),
    fileInput: document.getElementById('fileInput'),
    fileList: document.getElementById('fileList'),
    uploadBtn: document.getElementById('uploadBtn'),
    s3Key: document.getElementById('s3Key'),
    s3IngestBtn: document.getElementById('s3IngestBtn'),
    s3Keys: document.getElementById('s3Keys'),
    s3BatchIngestBtn: document.getElementById('s3BatchIngestBtn'),
    statsContainer: document.getElementById('statsContainer'),
    refreshStatsBtn: document.getElementById('refreshStatsBtn'),
    clearKBBtn: document.getElementById('clearKBBtn'),
    toast: document.getElementById('toast')
};

// 初始化
document.addEventListener('DOMContentLoaded', () => {
    initEventListeners();
    loadStats();
});

// 事件监听器
function initEventListeners() {
    // 查询功能
    elements.queryBtn.addEventListener('click', handleQuery);
    elements.queryInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter' && e.shiftKey === false) {
            e.preventDefault();
            handleQuery();
        }
    });

    // 文件上传
    elements.uploadArea.addEventListener('click', () => elements.fileInput.click());
    elements.uploadArea.addEventListener('dragover', handleDragOver);
    elements.uploadArea.addEventListener('dragleave', handleDragLeave);
    elements.uploadArea.addEventListener('drop', handleDrop);
    elements.fileInput.addEventListener('change', handleFileSelect);
    elements.uploadBtn.addEventListener('click', handleUpload);

    // S3文档
    elements.s3IngestBtn.addEventListener('click', handleS3Ingest);
    elements.s3BatchIngestBtn.addEventListener('click', handleS3BatchIngest);

    // 系统管理
    elements.refreshStatsBtn.addEventListener('click', loadStats);
    elements.clearKBBtn.addEventListener('click', handleClearKB);

    // Tab切换
    document.querySelectorAll('.tab').forEach(tab => {
        tab.addEventListener('click', (e) => {
            switchTab(e.target.dataset.tab);
        });
    });
}

// 查询处理
async function handleQuery() {
    const query = elements.queryInput.value.trim();
    if (!query) {
        showToast('请输入查询内容', 'error');
        return;
    }

    if (isLoading) return;
    
    setLoading(true);
    hideResults();

    try {
        const response = await fetch(`${API_BASE_URL}/query`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                query: query,
                top_k: parseInt(elements.topK.value)
            })
        });

        const data = await response.json();

        if (response.ok && data.status === 'success') {
            displayResults(data);
        } else {
            throw new Error(data.error || '查询失败');
        }
    } catch (error) {
        console.error('Query error:', error);
        showToast(error.message, 'error');
    } finally {
        setLoading(false);
    }
}

// 显示查询结果
function displayResults(data) {
    // 显示答案
    elements.answerContent.textContent = data.answer;
    elements.answerSection.style.display = 'block';

    // 显示置信度
    if (data.confidence !== undefined) {
        const confidence = Math.round(data.confidence * 100);
        elements.confidenceFill.style.width = `${confidence}%`;
        elements.confidenceValue.textContent = `${confidence}%`;
        elements.confidenceBar.style.display = 'flex';
    }

    // 显示来源文档
    if (data.sources && data.sources.length > 0) {
        displaySources(data.sources);
    }
}

// 显示来源文档
function displaySources(sources) {
    elements.sourcesList.innerHTML = '';
    
    sources.forEach((source, index) => {
        const sourceItem = document.createElement('div');
        sourceItem.className = 'source-item';
        
        const score = Math.round(source.score * 100) / 100;
        const metadata = source.metadata || {};
        
        sourceItem.innerHTML = `
            <div class="source-header">
                <span class="source-title">来源 ${index + 1}</span>
                <span class="source-score">相关度: ${score}</span>
            </div>
            <div class="source-text">${source.text}</div>
            ${metadata.file_name ? `
                <div class="source-metadata">
                    文件: ${metadata.file_name}
                    ${metadata.page ? ` | 页码: ${metadata.page}` : ''}
                    ${metadata.chunk_index !== undefined ? ` | 块: ${metadata.chunk_index}` : ''}
                </div>
            ` : ''}
        `;
        
        elements.sourcesList.appendChild(sourceItem);
    });
    
    elements.sourcesSection.style.display = 'block';
}

// 文件处理
function handleDragOver(e) {
    e.preventDefault();
    elements.uploadArea.classList.add('dragover');
}

function handleDragLeave(e) {
    e.preventDefault();
    elements.uploadArea.classList.remove('dragover');
}

function handleDrop(e) {
    e.preventDefault();
    elements.uploadArea.classList.remove('dragover');
    
    const files = Array.from(e.dataTransfer.files);
    processFiles(files);
}

function handleFileSelect(e) {
    const files = Array.from(e.target.files);
    processFiles(files);
}

function processFiles(files) {
    const validFiles = files.filter(file => {
        const ext = file.name.split('.').pop().toLowerCase();
        return ['pdf', 'txt', 'md', 'markdown'].includes(ext);
    });

    if (validFiles.length === 0) {
        showToast('请选择支持的文件格式（PDF, TXT, Markdown）', 'error');
        return;
    }

    currentFiles = validFiles;
    displayFileList();
    elements.uploadBtn.style.display = 'block';
}

function displayFileList() {
    elements.fileList.innerHTML = '';
    
    currentFiles.forEach((file, index) => {
        const fileItem = document.createElement('div');
        fileItem.className = 'file-item';
        
        const size = formatFileSize(file.size);
        
        fileItem.innerHTML = `
            <span class="file-name">${file.name}</span>
            <span class="file-size">${size}</span>
            <button onclick="removeFile(${index})" class="btn-icon">×</button>
        `;
        
        elements.fileList.appendChild(fileItem);
    });
}

// 文件上传
async function handleUpload() {
    if (currentFiles.length === 0) return;

    setLoading(true);
    
    try {
        // 这里需要实现文件上传逻辑
        // 可以先上传到S3，然后调用摄入API
        showToast('文件上传功能需要配置S3存储', 'info');
    } catch (error) {
        console.error('Upload error:', error);
        showToast(error.message, 'error');
    } finally {
        setLoading(false);
    }
}

// S3文档摄入
async function handleS3Ingest() {
    const s3Key = elements.s3Key.value.trim();
    if (!s3Key) {
        showToast('请输入S3对象键', 'error');
        return;
    }

    await ingestS3Documents([s3Key]);
}

async function handleS3BatchIngest() {
    const s3Keys = elements.s3Keys.value
        .split('\n')
        .map(key => key.trim())
        .filter(key => key);
    
    if (s3Keys.length === 0) {
        showToast('请输入S3对象键', 'error');
        return;
    }

    await ingestS3Documents(s3Keys);
}

async function ingestS3Documents(s3Keys) {
    setLoading(true);
    
    try {
        const response = await fetch(`${API_BASE_URL}/documents`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                operation: 's3_ingest',
                s3_keys: s3Keys
            })
        });

        const data = await response.json();

        if (response.ok && data.status === 'success') {
            showToast(`成功摄入 ${data.chunks_created} 个文档块`, 'success');
            elements.s3Key.value = '';
            elements.s3Keys.value = '';
            loadStats();
        } else {
            throw new Error(data.error || '摄入失败');
        }
    } catch (error) {
        console.error('Ingest error:', error);
        showToast(error.message, 'error');
    } finally {
        setLoading(false);
    }
}

// 加载统计信息
async function loadStats() {
    try {
        const response = await fetch(`${API_BASE_URL}/documents`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                operation: 'stats'
            })
        });

        const data = await response.json();

        if (response.ok) {
            displayStats(data);
        }
    } catch (error) {
        console.error('Stats error:', error);
        elements.statsContainer.innerHTML = '<p>无法加载统计信息</p>';
    }
}

function displayStats(stats) {
    const vectorStore = stats.vector_store || {};
    
    elements.statsContainer.innerHTML = `
        <div class="stat-item">
            <span class="stat-label">集合名称</span>
            <span class="stat-value">${vectorStore.name || '-'}</span>
        </div>
        <div class="stat-item">
            <span class="stat-label">文档数量</span>
            <span class="stat-value">${vectorStore.num_entities || 0}</span>
        </div>
        <div class="stat-item">
            <span class="stat-label">向量维度</span>
            <span class="stat-value">${vectorStore.dimension || '-'}</span>
        </div>
        <div class="stat-item">
            <span class="stat-label">Embedding模型</span>
            <span class="stat-value">${stats.embedding_model || '-'}</span>
        </div>
        <div class="stat-item">
            <span class="stat-label">LLM模型</span>
            <span class="stat-value">${stats.llm_model || '-'}</span>
        </div>
    `;
}

// 清空知识库
async function handleClearKB() {
    if (!confirm('确定要清空知识库吗？此操作不可恢复。')) {
        return;
    }

    setLoading(true);
    
    try {
        const response = await fetch(`${API_BASE_URL}/documents`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                operation: 'clear'
            })
        });

        const data = await response.json();

        if (response.ok && data.status === 'success') {
            showToast('知识库已清空', 'success');
            loadStats();
        } else {
            throw new Error(data.error || '清空失败');
        }
    } catch (error) {
        console.error('Clear error:', error);
        showToast(error.message, 'error');
    } finally {
        setLoading(false);
    }
}

// 工具函数
function setLoading(loading) {
    isLoading = loading;
    
    if (loading) {
        elements.queryBtn.disabled = true;
        elements.queryBtn.querySelector('.btn-text').style.display = 'none';
        elements.queryBtn.querySelector('.loader').style.display = 'inline-block';
    } else {
        elements.queryBtn.disabled = false;
        elements.queryBtn.querySelector('.btn-text').style.display = 'inline';
        elements.queryBtn.querySelector('.loader').style.display = 'none';
    }
}

function hideResults() {
    elements.answerSection.style.display = 'none';
    elements.sourcesSection.style.display = 'none';
}

function switchTab(tabName) {
    document.querySelectorAll('.tab').forEach(tab => {
        tab.classList.toggle('active', tab.dataset.tab === tabName);
    });
    
    document.querySelectorAll('.tab-content').forEach(content => {
        content.classList.toggle('active', content.id === tabName);
    });
}

function showToast(message, type = 'info') {
    elements.toast.textContent = message;
    elements.toast.className = `toast show ${type}`;
    
    setTimeout(() => {
        elements.toast.classList.remove('show');
    }, 3000);
}

function formatFileSize(bytes) {
    if (bytes === 0) return '0 Bytes';
    
    const k = 1024;
    const sizes = ['Bytes', 'KB', 'MB', 'GB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    
    return Math.round(bytes / Math.pow(k, i) * 100) / 100 + ' ' + sizes[i];
}

function removeFile(index) {
    currentFiles.splice(index, 1);
    displayFileList();
    
    if (currentFiles.length === 0) {
        elements.uploadBtn.style.display = 'none';
    }
}

// 导出函数供HTML使用
window.removeFile = removeFile;