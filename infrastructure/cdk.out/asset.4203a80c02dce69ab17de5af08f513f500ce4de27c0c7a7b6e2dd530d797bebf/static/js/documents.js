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

        const allowedTypes = ['.txt', '.pdf', '.md', '.json'];
        let validFiles = [];
        
        for (let file of files) {
            const ext = file.name.substring(file.name.lastIndexOf('.')).toLowerCase();
            if (!allowedTypes.includes(ext)) {
                alert(`不支持的文件类型: ${file.name}\n支持的格式: ${allowedTypes.join(', ')}`);
                continue;
            }
            
            // 限制文件大小（5MB）
            if (file.size > 5 * 1024 * 1024) {
                alert(`文件太大: ${file.name} (最大5MB)`);
                continue;
            }
            
            validFiles.push(file);
        }

        if (validFiles.length === 0) return;

        // 显示加载状态
        showLoading('正在上传文档...');

        try {
            // 逐个上传文件
            let successCount = 0;
            for (let file of validFiles) {
                const reader = new FileReader();
                
                await new Promise((resolve, reject) => {
                    reader.onload = async (e) => {
                        try {
                            // 准备上传数据
                            const uploadData = {
                                filename: file.name,
                                content: e.target.result,
                                content_type: file.type || 'text/plain',
                                size: file.size
                            };
                            
                            // 调用API上传文档
                            const response = await apiClient.uploadDocument(uploadData);
                            
                            if (response && response.status === 'success') {
                                successCount++;
                                console.log(`✅ 成功上传: ${file.name}`);
                            } else {
                                console.error(`❌ 上传失败: ${file.name}`, response);
                            }
                            resolve();
                        } catch (error) {
                            console.error(`上传 ${file.name} 失败:`, error);
                            reject(error);
                        }
                    };
                    
                    reader.onerror = reject;
                    
                    // 根据文件类型选择读取方式
                    const ext = file.name.substring(file.name.lastIndexOf('.')).toLowerCase();
                    if (file.type.startsWith('text/') || ext === '.json' || ext === '.md' || ext === '.txt') {
                        reader.readAsText(file);
                    } else {
                        reader.readAsDataURL(file);
                    }
                });
            }
            
            if (successCount > 0) {
                alert(`成功上传 ${successCount}/${validFiles.length} 个文档`);
                this.loadDocuments();
                this.updateStats();
            } else {
                alert('所有文档上传失败');
            }
        } catch (error) {
            console.error('上传失败:', error);
            alert('上传失败: ' + (error.message || '未知错误'));
        } finally {
            hideLoading();
            // 清空文件输入
            this.fileInput.value = '';
        }

        // 清空文件选择
        this.fileInput.value = '';
    }

    async loadDocuments() {
        try {
            const response = await apiClient.listDocuments();
            
            // 修复：API返回的是 response.documents，不是 response.data
            if (response.documents && response.documents.length > 0) {
                this.displayDocuments(response.documents);
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
            
            // 修复：直接使用response的属性，不是response.data
            if (response) {
                // 只更新向量维度和集合名称（文档总数和向量数量已从界面移除）
                const dimensionElement = document.getElementById('stat-dimension');
                const collectionElement = document.getElementById('stat-collection');
                
                if (dimensionElement) {
                    dimensionElement.textContent = response.dimension || 0;
                }
                if (collectionElement) {
                    collectionElement.textContent = response.collection || '-';
                }
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