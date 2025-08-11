// 搜索功能
class SearchManager {
    constructor() {
        this.searchInput = document.getElementById('search-input');
        this.searchBtn = document.getElementById('search-btn');
        this.searchTopK = document.getElementById('search-top-k');
        this.searchResults = document.getElementById('search-results');
        
        this.initEventListeners();
    }

    initEventListeners() {
        // 搜索按钮
        this.searchBtn.addEventListener('click', () => this.performSearch());
        
        // 回车搜索
        this.searchInput.addEventListener('keydown', (e) => {
            if (e.key === 'Enter') {
                this.performSearch();
            }
        });
    }

    async performSearch() {
        const query = this.searchInput.value.trim();
        if (!query) {
            alert('请输入搜索内容');
            return;
        }

        // 显示加载状态
        this.searchResults.innerHTML = '<p class="no-results">搜索中...</p>';

        try {
            const topK = parseInt(this.searchTopK.value) || 10;
            const response = await apiClient.search(query, topK);
            
            if (response.data && response.data.results && response.data.results.length > 0) {
                this.displayResults(response.data.results);
            } else {
                this.searchResults.innerHTML = '<p class="no-results">没有找到相关内容</p>';
            }
        } catch (error) {
            this.searchResults.innerHTML = '<p class="no-results">搜索失败: ' + error.message + '</p>';
        }
    }

    displayResults(results) {
        this.searchResults.innerHTML = '';
        
        results.forEach((result, index) => {
            const resultDiv = document.createElement('div');
            resultDiv.className = 'search-result-item';
            
            const scoreSpan = document.createElement('span');
            scoreSpan.className = 'result-score';
            scoreSpan.textContent = `相似度: ${result.score.toFixed(1)}%`;
            
            const contentDiv = document.createElement('div');
            contentDiv.className = 'result-content';
            contentDiv.textContent = result.content || result.text || '';
            
            const metadataDiv = document.createElement('div');
            metadataDiv.className = 'result-metadata';
            
            if (result.metadata) {
                const source = result.metadata.source || result.metadata.file_name || '';
                const chunkId = result.metadata.chunk_id;
                
                metadataDiv.innerHTML = `
                    <i class="fas fa-file-alt"></i> 
                    ${source} 
                    ${chunkId !== undefined ? `(块 ${chunkId + 1})` : ''}
                `;
            }
            
            resultDiv.appendChild(scoreSpan);
            resultDiv.appendChild(contentDiv);
            if (metadataDiv.innerHTML) {
                resultDiv.appendChild(metadataDiv);
            }
            
            this.searchResults.appendChild(resultDiv);
        });
    }
}