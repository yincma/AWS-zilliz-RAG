// 文档管理功能
class DocumentManager {
    constructor() {
        this.uploadArea = document.getElementById('upload-area');
        this.fileInput = document.getElementById('file-input');
        this.uploadBtn = document.getElementById('upload-btn');
        this.documentsContainer = document.getElementById('documents-container');
        
        this.initEventListeners();
        this.loadDocuments();
        this.updateStats();
    }

    initEventListeners() {
        // 上传按钮
        this.uploadBtn.addEventListener('click', () => {
            this.fileInput.click();
        });

        // 点击上传区域
        this.uploadArea.addEventListener('click', () => {
            this.fileInput.click();
        });

        // 文件选择
        this.fileInput.addEventListener('change', (e) => {
            this.handleFileSelect(e.target.files);
        });

        // 拖拽上传
        this.uploadArea.addEventListener('dragover', (e) => {
            e.preventDefault();
            this.uploadArea.classList.add('dragover');
        });

        this.uploadArea.addEventListener('dragleave', () => {
            this.uploadArea.classList.remove('dragover');
        });

        this.uploadArea.addEventListener('drop', (e) => {
            e.preventDefault();
            this.uploadArea.classList.remove('dragover');
            this.handleFileSelect(e.dataTransfer.files);
        });
    }

    async handleFileSelect(files) {
        if (files.length === 0) return;

        const filePaths = [];
        const allowedTypes = ['.txt', '.pdf', '.md'];
        
        for (let file of files) {
            const ext = file.name.substring(file.name.lastIndexOf('.'));
            if (!allowedTypes.includes(ext)) {
                alert(`不支持的文件类型: ${file.name}`);
                continue;
            }
            
            // 在实际应用中，这里需要先上传文件到服务器
            // 这里简化处理，假设文件已经在服务器上
            filePaths.push(`uploaded/${file.name}`);
        }

        if (filePaths.length === 0) return;

        // 显示加载状态
        showLoading('正在上传文档...');

        try {
            // 调用API摄入文档
            const response = await apiClient.ingestDocuments(filePaths);
            
            if (response.status === 'success') {
                alert(`成功处理 ${response.files_processed} 个文档`);
                this.loadDocuments();
                this.updateStats();
            } else {
                alert('文档处理失败');
            }
        } catch (error) {
            alert('上传失败: ' + error.message);
        } finally {
            hideLoading();
        }

        // 清空文件选择
        this.fileInput.value = '';
    }

    async loadDocuments() {
        try {
            const response = await apiClient.listDocuments();
            
            if (response.data && response.data.length > 0) {
                this.displayDocuments(response.data);
            } else {
                this.documentsContainer.innerHTML = '<p class="no-documents">暂无文档</p>';
            }
        } catch (error) {
            console.error('Failed to load documents:', error);
            this.documentsContainer.innerHTML = '<p class="no-documents">加载文档失败</p>';
        }
    }

    displayDocuments(documents) {
        this.documentsContainer.innerHTML = '';
        
        documents.forEach(doc => {
            const docDiv = document.createElement('div');
            docDiv.className = 'document-item';
            
            docDiv.innerHTML = `
                <div class="document-info">
                    <i class="fas fa-file-alt document-icon"></i>
                    <div>
                        <div class="document-name">${doc.name}</div>
                        <div class="document-size">${this.formatFileSize(doc.size)}</div>
                    </div>
                </div>
                <div class="document-actions">
                    <button class="btn-icon" onclick="documentManager.deleteDocument('${doc.name}')" title="删除">
                        <i class="fas fa-trash"></i>
                    </button>
                </div>
            `;
            
            this.documentsContainer.appendChild(docDiv);
        });
    }

    async deleteDocument(filename) {
        if (!confirm(`确定删除文档 "${filename}" 吗？`)) return;

        showLoading('正在删除...');

        try {
            const response = await apiClient.deleteDocument(filename);
            
            if (response.status === 'success') {
                alert('删除成功');
                this.loadDocuments();
                this.updateStats();
            } else {
                alert('删除失败');
            }
        } catch (error) {
            alert('删除失败: ' + error.message);
        } finally {
            hideLoading();
        }
    }

    async updateStats() {
        try {
            const response = await apiClient.getStats();
            
            if (response.data) {
                document.getElementById('stat-docs').textContent = response.data.num_entities || 0;
                document.getElementById('stat-vectors').textContent = response.data.num_entities || 0;
                document.getElementById('stat-dimension').textContent = response.data.dimension || 0;
                document.getElementById('stat-collection').textContent = response.data.name || '-';
            }
        } catch (error) {
            console.error('Failed to update stats:', error);
        }
    }

    formatFileSize(bytes) {
        if (!bytes) return '0 B';
        
        const k = 1024;
        const sizes = ['B', 'KB', 'MB', 'GB'];
        const i = Math.floor(Math.log(bytes) / Math.log(k));
        
        return Math.round(bytes / Math.pow(k, i) * 100) / 100 + ' ' + sizes[i];
    }
}

// 注意：由于浏览器安全限制，实际的文件上传需要额外的处理
// 这里提供一个简化的示例，实际应用中需要：
// 1. 使用FormData上传文件到服务器
// 2. 服务器保存文件后返回文件路径
// 3. 使用文件路径调用摄入API