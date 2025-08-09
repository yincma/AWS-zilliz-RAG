// 主应用程序
let chatManager, documentManager, searchManager;

// 初始化应用
document.addEventListener('DOMContentLoaded', () => {
    // 初始化管理器
    chatManager = new ChatManager();
    documentManager = new DocumentManager();
    searchManager = new SearchManager();
    
    // 初始化标签页切换
    initTabNavigation();
    
    // 初始化设置
    initSettings();
    
    // 检查服务器连接
    checkServerConnection();
    
    // 定期检查连接状态
    setInterval(checkServerConnection, 30000);
});

// 标签页切换
function initTabNavigation() {
    const navItems = document.querySelectorAll('.nav-item');
    const tabContents = document.querySelectorAll('.tab-content');
    
    navItems.forEach(item => {
        item.addEventListener('click', () => {
            const targetTab = item.dataset.tab;
            
            // 更新导航状态
            navItems.forEach(nav => nav.classList.remove('active'));
            item.classList.add('active');
            
            // 切换内容
            tabContents.forEach(content => {
                content.classList.remove('active');
                if (content.id === `${targetTab}-tab`) {
                    content.classList.add('active');
                }
            });
            
            // 特定标签的初始化
            if (targetTab === 'documents') {
                documentManager.updateStats();
            }
        });
    });
}

// 设置功能
function initSettings() {
    const apiUrlInput = document.getElementById('api-url');
    const darkModeInput = document.getElementById('dark-mode');
    const autoScrollInput = document.getElementById('auto-scroll');
    const saveBtn = document.getElementById('save-settings');
    const resetBtn = document.getElementById('reset-settings');
    
    // 加载设置
    loadSettings();
    
    // 保存设置
    saveBtn.addEventListener('click', () => {
        const settings = {
            apiUrl: apiUrlInput.value,
            darkMode: darkModeInput.checked,
            autoScroll: autoScrollInput.checked,
            temperature: document.getElementById('temperature').value,
            maxTokens: document.getElementById('max-tokens').value
        };
        
        localStorage.setItem('ragSettings', JSON.stringify(settings));
        
        // 应用设置
        applySettings(settings);
        
        alert('设置已保存');
    });
    
    // 重置设置
    resetBtn.addEventListener('click', () => {
        if (confirm('确定要重置所有设置吗？')) {
            localStorage.removeItem('ragSettings');
            loadSettings();
            alert('设置已重置');
        }
    });
    
    // 深色模式切换
    darkModeInput.addEventListener('change', () => {
        document.body.classList.toggle('dark-mode', darkModeInput.checked);
    });
}

// 加载设置
function loadSettings() {
    const defaultSettings = {
        apiUrl: 'http://localhost:8000',
        darkMode: false,
        autoScroll: true,
        temperature: 0.7,
        maxTokens: 1000
    };
    
    const savedSettings = localStorage.getItem('ragSettings');
    const settings = savedSettings ? JSON.parse(savedSettings) : defaultSettings;
    
    // 应用设置到界面
    document.getElementById('api-url').value = settings.apiUrl;
    document.getElementById('dark-mode').checked = settings.darkMode;
    document.getElementById('auto-scroll').checked = settings.autoScroll;
    document.getElementById('temperature').value = settings.temperature;
    document.getElementById('max-tokens').value = settings.maxTokens;
    
    // 应用设置
    applySettings(settings);
}

// 应用设置
function applySettings(settings) {
    // 更新API客户端URL
    apiClient.baseUrl = settings.apiUrl;
    
    // 应用深色模式
    document.body.classList.toggle('dark-mode', settings.darkMode);
}

// 检查服务器连接
async function checkServerConnection() {
    const statusIndicator = document.getElementById('status-indicator');
    const statusText = document.getElementById('status-text');
    
    try {
        const health = await apiClient.checkHealth();
        
        if (health && health.status === 'healthy') {
            statusIndicator.classList.add('connected');
            statusText.textContent = '已连接';
            
            // 启用聊天输入
            document.getElementById('chat-input').disabled = false;
            document.getElementById('send-btn').disabled = false;
        } else {
            throw new Error('Server unhealthy');
        }
    } catch (error) {
        statusIndicator.classList.remove('connected');
        statusText.textContent = '未连接';
        
        // 禁用聊天输入
        document.getElementById('chat-input').disabled = true;
        document.getElementById('send-btn').disabled = true;
    }
}

// 显示加载提示
function showLoading(text = '处理中...') {
    const overlay = document.getElementById('loading-overlay');
    const loadingText = document.getElementById('loading-text');
    
    loadingText.textContent = text;
    overlay.classList.add('active');
}

// 隐藏加载提示
function hideLoading() {
    const overlay = document.getElementById('loading-overlay');
    overlay.classList.remove('active');
}

// 格式化时间
function formatTime(date) {
    return new Date(date).toLocaleTimeString('zh-CN', {
        hour: '2-digit',
        minute: '2-digit'
    });
}

// 处理错误
function handleError(error, message = '操作失败') {
    console.error(error);
    alert(message + ': ' + error.message);
}

// 防抖函数
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// 节流函数
function throttle(func, limit) {
    let inThrottle;
    return function(...args) {
        if (!inThrottle) {
            func.apply(this, args);
            inThrottle = true;
            setTimeout(() => inThrottle = false, limit);
        }
    };
}