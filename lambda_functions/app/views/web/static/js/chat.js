// 聊天功能
class ChatManager {
    constructor() {
        this.chatContainer = document.getElementById('chat-container');
        this.chatInput = document.getElementById('chat-input');
        this.sendBtn = document.getElementById('send-btn');
        this.clearBtn = document.getElementById('clear-chat');
        this.topKInput = document.getElementById('top-k');
        this.showSourcesInput = document.getElementById('show-sources');
        
        this.initEventListeners();
        this.initQuickActions();
    }

    initEventListeners() {
        // 发送按钮
        this.sendBtn.addEventListener('click', () => this.sendMessage());
        
        // 输入框事件
        this.chatInput.addEventListener('input', () => {
            this.adjustTextareaHeight();
            this.sendBtn.disabled = !this.chatInput.value.trim();
        });
        
        // 回车发送
        this.chatInput.addEventListener('keydown', (e) => {
            if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                if (this.chatInput.value.trim()) {
                    this.sendMessage();
                }
            }
        });
        
        // 清空对话
        this.clearBtn.addEventListener('click', () => this.clearChat());
    }

    initQuickActions() {
        document.querySelectorAll('.quick-action').forEach(btn => {
            btn.addEventListener('click', () => {
                const question = btn.dataset.question;
                this.chatInput.value = question;
                this.sendBtn.disabled = false;
                this.sendMessage();
            });
        });
    }

    adjustTextareaHeight() {
        this.chatInput.style.height = 'auto';
        this.chatInput.style.height = Math.min(this.chatInput.scrollHeight, 120) + 'px';
    }

    async sendMessage() {
        const question = this.chatInput.value.trim();
        if (!question) return;

        // 清空输入框
        this.chatInput.value = '';
        this.sendBtn.disabled = true;
        this.adjustTextareaHeight();

        // 移除欢迎消息
        const welcomeMessage = this.chatContainer.querySelector('.welcome-message');
        if (welcomeMessage) {
            welcomeMessage.remove();
        }

        // 添加用户消息
        this.addMessage(question, 'user');

        // 显示加载状态
        const loadingMessage = this.addMessage('正在思考...', 'assistant', true);

        try {
            // 调用API
            const topK = parseInt(this.topKInput.value) || 5;
            const response = await apiClient.query(question, topK);

            // 移除加载消息
            loadingMessage.remove();

            // 显示回答
            if (response.answer) {
                const answerElement = this.addMessage(response.answer, 'assistant');
                
                // 显示引用源
                if (this.showSourcesInput.checked && response.sources && response.sources.length > 0) {
                    this.addSources(answerElement, response.sources, response.confidence);
                }
            } else {
                this.addMessage('抱歉，无法生成答案。请检查系统是否正常运行。', 'assistant');
            }
        } catch (error) {
            // 移除加载消息
            loadingMessage.remove();
            
            // 显示错误消息
            this.addMessage('发生错误：' + error.message, 'assistant');
        }

        // 滚动到底部
        this.scrollToBottom();
    }

    addMessage(text, type, isLoading = false) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${type}`;
        
        const avatarDiv = document.createElement('div');
        avatarDiv.className = 'message-avatar';
        avatarDiv.innerHTML = type === 'user' 
            ? '<i class="fas fa-user"></i>' 
            : '<i class="fas fa-robot"></i>';
        
        const contentDiv = document.createElement('div');
        contentDiv.className = 'message-content';
        
        const textDiv = document.createElement('div');
        textDiv.className = 'message-text';
        
        if (isLoading) {
            textDiv.innerHTML = '<i class="fas fa-spinner fa-spin"></i> ' + text;
        } else {
            textDiv.textContent = text;
        }
        
        const timeDiv = document.createElement('div');
        timeDiv.className = 'message-time';
        timeDiv.textContent = new Date().toLocaleTimeString();
        
        contentDiv.appendChild(textDiv);
        contentDiv.appendChild(timeDiv);
        
        messageDiv.appendChild(avatarDiv);
        messageDiv.appendChild(contentDiv);
        
        this.chatContainer.appendChild(messageDiv);
        
        return messageDiv;
    }

    addSources(messageElement, sources, confidence) {
        const contentDiv = messageElement.querySelector('.message-content');
        
        const sourcesDiv = document.createElement('div');
        sourcesDiv.className = 'message-sources';
        
        const headerDiv = document.createElement('div');
        headerDiv.innerHTML = `<strong>引用源 (置信度: ${(confidence * 100).toFixed(1)}%)</strong>`;
        sourcesDiv.appendChild(headerDiv);
        
        sources.forEach((source, index) => {
            const sourceDiv = document.createElement('div');
            sourceDiv.className = 'source-item';
            
            const sourceHeader = document.createElement('div');
            sourceHeader.className = 'source-header';
            
            const sourceTitle = document.createElement('span');
            sourceTitle.className = 'source-title';
            sourceTitle.textContent = source.metadata?.source || `来源 ${index + 1}`;
            
            const sourceScore = document.createElement('span');
            sourceScore.className = 'source-score';
            sourceScore.textContent = `相似度: ${(source.score * 100).toFixed(1)}%`;
            
            sourceHeader.appendChild(sourceTitle);
            sourceHeader.appendChild(sourceScore);
            
            const sourceContent = document.createElement('div');
            sourceContent.className = 'source-content';
            sourceContent.textContent = source.text.substring(0, 200) + '...';
            
            sourceDiv.appendChild(sourceHeader);
            sourceDiv.appendChild(sourceContent);
            
            sourcesDiv.appendChild(sourceDiv);
        });
        
        contentDiv.appendChild(sourcesDiv);
    }

    clearChat() {
        this.chatContainer.innerHTML = `
            <div class="welcome-message">
                <div class="welcome-icon">
                    <i class="fas fa-robot fa-3x"></i>
                </div>
                <h2>欢迎使用RAG智能问答系统</h2>
                <p>我可以基于已上传的文档回答您的问题</p>
                <div class="quick-actions">
                    <button class="quick-action" data-question="什么是RAG？">
                        <i class="fas fa-question-circle"></i> 什么是RAG？
                    </button>
                    <button class="quick-action" data-question="RAG有哪些优势？">
                        <i class="fas fa-star"></i> RAG有哪些优势？
                    </button>
                    <button class="quick-action" data-question="如何使用这个系统？">
                        <i class="fas fa-info-circle"></i> 如何使用？
                    </button>
                </div>
            </div>
        `;
        this.initQuickActions();
    }

    scrollToBottom() {
        const autoScroll = document.getElementById('auto-scroll');
        if (autoScroll && autoScroll.checked) {
            this.chatContainer.scrollTop = this.chatContainer.scrollHeight;
        }
    }
}