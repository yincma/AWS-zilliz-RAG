// 主应用程序
let chatManager, documentManager, searchManager;

// 初始化应用
document.addEventListener('DOMContentLoaded', async () => {
    try {
        // 初始化多语言系统
        if (window.i18n) {
            await window.i18n.loadTranslations();
            window.i18n.updateUI();
            
            // 监听语言切换
            const langSelect = document.getElementById('language-select');
            if (langSelect) {
                langSelect.value = window.i18n.currentLang;
                langSelect.addEventListener('change', (e) => {
                    window.i18n.setLanguage(e.target.value);
                    updateDynamicTexts(); // 更新动态文本
                });
            }
        }
        
        // 确保API客户端配置已加载
        if (window.apiClient && window.apiClient.initializeConfig) {
            await window.apiClient.initializeConfig();
            console.log('API configuration loaded successfully');
        }
        
        // 初始化管理器
        chatManager = new ChatManager();
        documentManager = new DocumentManager();
        searchManager = new SearchManager();
        
        // 初始化标签页切换
        initTabNavigation();
        
        // 初始化设置（异步）
        await initSettings();
        
        // 检查服务器连接
        await checkServerConnection();
        
        // 定期检查连接状态
        setInterval(checkServerConnection, 30000);
    } catch (error) {
        console.error('Application initialization error:', error);
        // 显示错误信息给用户
        const statusText = document.getElementById('status-text');
        if (statusText) {
            statusText.textContent = window.i18n ? window.i18n.t('status.error') : 'Error';
        }
    }
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
async function initSettings() {
    const apiUrlInput = document.getElementById('api-url');
    const darkModeInput = document.getElementById('dark-mode');
    const autoScrollInput = document.getElementById('auto-scroll');
    const saveBtn = document.getElementById('save-settings');
    const resetBtn = document.getElementById('reset-settings');
    
    // 加载设置
    await loadSettings();
    
    // 保存设置
    saveBtn.addEventListener('click', () => {
        const settings = {
            apiUrl: apiUrlInput.value,
            darkMode: darkModeInput.checked,
            autoScroll: autoScrollInput.checked,
            temperature: parseFloat(document.getElementById('temperature').value),
            maxTokens: parseInt(document.getElementById('max-tokens').value),
            topK: 5,  // 默认值
            useRag: true  // 默认值
        };
        
        // 验证设置
        const validation = window.configManager.validateSettings(settings);
        if (!validation.valid) {
            alert((window.i18n ? window.i18n.t('common.error') : 'Error') + ':\n' + validation.errors.join('\n'));
            return;
        }
        
        // 使用ConfigManager保存设置
        if (window.configManager.saveSettings(settings)) {
            // 应用设置
            applySettings(settings);
            alert(window.i18n ? window.i18n.t('settings.saveSuccess') : 'Settings saved');
        } else {
            alert(window.i18n ? window.i18n.t('common.error') : 'Save failed');
        }
    });
    
    // 重置设置
    resetBtn.addEventListener('click', async () => {
        if (confirm(window.i18n ? window.i18n.t('settings.resetConfirm') : 'Reset all settings?')) {
            try {
                // 使用ConfigManager重置设置
                await window.configManager.resetToDefaults();
                await loadSettings();
                alert(window.i18n ? window.i18n.t('common.success') : 'Settings reset');
            } catch (error) {
                console.error('Failed to reset settings:', error);
                alert(window.i18n ? window.i18n.t('common.error') : 'Reset failed');
            }
        }
    });
    
    // 深色模式切换
    darkModeInput.addEventListener('change', () => {
        document.body.classList.toggle('dark-mode', darkModeInput.checked);
    });
}

// 加载设置 - 使用ConfigManager统一管理
async function loadSettings() {
    try {
        // 从ConfigManager加载设置，确保配置的一致性
        const settings = await window.configManager.loadSettings();
        
        // 应用设置到界面
        if (document.getElementById('api-url')) {
            document.getElementById('api-url').value = settings.apiUrl || '';
        }
        if (document.getElementById('dark-mode')) {
            document.getElementById('dark-mode').checked = settings.darkMode;
        }
        if (document.getElementById('auto-scroll')) {
            document.getElementById('auto-scroll').checked = settings.autoScroll;
        }
        if (document.getElementById('temperature')) {
            document.getElementById('temperature').value = settings.temperature;
        }
        if (document.getElementById('max-tokens')) {
            document.getElementById('max-tokens').value = settings.maxTokens;
        }
        
        // 显示当前API配置信息（用于调试）
        const apiInfo = await window.configManager.getApiInfo();
        console.log('加载配置:', {
            settings: settings,
            apiInfo: apiInfo
        });
        
        // 应用设置
        applySettings(settings);
    } catch (error) {
        console.error('Failed to load settings:', error);
        // 使用默认配置
        applySettings({
            apiUrl: '',
            darkMode: false,
            autoScroll: true,
            temperature: 0.7,
            maxTokens: 1000
        });
    }
}

// 应用设置
function applySettings(settings) {
    // 注意：API URL由API客户端自动管理，不应在此处手动设置
    // apiClient的baseUrl已经通过动态配置加载
    
    // 应用深色模式
    document.body.classList.toggle('dark-mode', settings.darkMode);
    
    // 存储自动滚动设置（供聊天管理器使用）
    if (window.chatManager) {
        window.chatManager.autoScroll = settings.autoScroll;
    }
}

// 检查服务器连接
async function checkServerConnection() {
    const statusIndicator = document.getElementById('status-indicator');
    const statusText = document.getElementById('status-text');
    
    try {
        const health = await apiClient.checkHealth();
        
        if (health && health.status === 'healthy') {
            statusIndicator.classList.add('connected');
            statusText.textContent = window.i18n ? window.i18n.t('status.connected') : 'Connected';
            
            // 启用聊天输入
            document.getElementById('chat-input').disabled = false;
            document.getElementById('send-btn').disabled = false;
        } else {
            throw new Error('Server unhealthy');
        }
    } catch (error) {
        statusIndicator.classList.remove('connected');
        statusText.textContent = window.i18n ? window.i18n.t('status.disconnected') : 'Disconnected';
        
        // 禁用聊天输入
        document.getElementById('chat-input').disabled = true;
        document.getElementById('send-btn').disabled = true;
    }
}

// 显示加载提示
function showLoading(text) {
    if (!text) {
        text = window.i18n ? window.i18n.t('chat.processing') : 'Processing...';
    }
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
    const lang = window.i18n ? window.i18n.currentLang : 'en';
    const locale = lang === 'zh' ? 'zh-CN' : lang === 'ja' ? 'ja-JP' : 'en-US';
    return new Date(date).toLocaleTimeString(locale, {
        hour: '2-digit',
        minute: '2-digit'
    });
}

// 更新动态文本
function updateDynamicTexts() {
    // 更新速助问题按钮
    const quickActions = document.querySelectorAll('.quick-action');
    quickActions.forEach((btn, index) => {
        const keys = ['quickActions.whatIsRAG', 'quickActions.advantages', 'quickActions.howToUse'];
        if (window.i18n && keys[index]) {
            const text = window.i18n.t(keys[index]);
            btn.innerHTML = btn.innerHTML.replace(/>.*?<\/button>/, `>${text}</button>`);
            btn.dataset.question = text;
        }
    });
}

// 处理错误
function handleError(error, message) {
    if (!message) {
        message = window.i18n ? window.i18n.t('common.error') : 'Operation failed';
    }
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