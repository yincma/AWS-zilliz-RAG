/**
 * 配置管理器 - 统一的配置管理中心
 * 所有配置都从这里读取，确保单一数据源
 */

class ConfigManager {
    constructor() {
        // 配置版本，用于检测配置是否需要更新
        this.CONFIG_VERSION = '1.0.0';
        this.STORAGE_KEY = 'ragSettings';
        this.VERSION_KEY = 'ragSettingsVersion';
    }

    /**
     * 获取默认配置
     * 异步获取配置，支持动态加载
     */
    async getDefaultSettings() {
        // 确保API客户端配置已加载
        if (window.apiClient && window.apiClient.ensureConfigLoaded) {
            await window.apiClient.ensureConfigLoaded();
        }
        
        return {
            // API配置从动态加载的配置获取
            apiUrl: window.apiClient ? window.apiClient.baseUrl : '',
            
            // UI设置
            darkMode: false,
            autoScroll: true,
            
            // 模型参数
            temperature: 0.7,
            maxTokens: 1000,
            topK: 5,
            useRag: true
        };
    }

    /**
     * 加载设置
     * 智能处理版本更新和配置迁移
     */
    async loadSettings() {
        const savedVersion = localStorage.getItem(this.VERSION_KEY);
        const savedSettings = localStorage.getItem(this.STORAGE_KEY);
        
        // 如果没有保存的设置或版本不匹配，使用默认设置
        if (!savedSettings || savedVersion !== this.CONFIG_VERSION) {
            console.log('配置版本更新或首次加载，使用默认设置');
            return await this.resetToDefaults();
        }
        
        try {
            const settings = JSON.parse(savedSettings);
            
            // 确保API客户端配置已加载
            if (window.apiClient && window.apiClient.ensureConfigLoaded) {
                await window.apiClient.ensureConfigLoaded();
            }
            
            // 验证API URL是否需要更新
            const currentApiUrl = window.apiClient ? window.apiClient.baseUrl : '';
            if (settings.apiUrl !== currentApiUrl && currentApiUrl) {
                console.log(`API URL已更新: ${settings.apiUrl} -> ${currentApiUrl}`);
                settings.apiUrl = currentApiUrl;
                this.saveSettings(settings);
            }
            
            return settings;
        } catch (error) {
            console.error('加载设置失败:', error);
            return await this.resetToDefaults();
        }
    }

    /**
     * 保存设置
     */
    saveSettings(settings) {
        try {
            localStorage.setItem(this.STORAGE_KEY, JSON.stringify(settings));
            localStorage.setItem(this.VERSION_KEY, this.CONFIG_VERSION);
            return true;
        } catch (error) {
            console.error('保存设置失败:', error);
            return false;
        }
    }

    /**
     * 重置为默认设置
     */
    async resetToDefaults() {
        const defaults = await this.getDefaultSettings();
        this.saveSettings(defaults);
        return defaults;
    }

    /**
     * 清除所有设置
     */
    clearSettings() {
        localStorage.removeItem(this.STORAGE_KEY);
        localStorage.removeItem(this.VERSION_KEY);
    }

    /**
     * 验证设置的有效性
     */
    validateSettings(settings) {
        const errors = [];
        
        // 验证API URL
        if (!settings.apiUrl || typeof settings.apiUrl !== 'string') {
            errors.push('API URL无效');
        }
        
        // 验证温度参数
        if (settings.temperature < 0 || settings.temperature > 1) {
            errors.push('温度参数必须在0-1之间');
        }
        
        // 验证最大token数
        if (settings.maxTokens < 1 || settings.maxTokens > 100000) {
            errors.push('最大Token数无效');
        }
        
        // 验证topK
        if (settings.topK < 1 || settings.topK > 100) {
            errors.push('TopK必须在1-100之间');
        }
        
        return {
            valid: errors.length === 0,
            errors: errors
        };
    }

    /**
     * 获取当前API配置信息
     */
    async getApiInfo() {
        // 确保API客户端配置已加载
        if (window.apiClient && window.apiClient.ensureConfigLoaded) {
            await window.apiClient.ensureConfigLoaded();
        }
        
        const baseUrl = window.apiClient ? window.apiClient.baseUrl : '';
        
        return {
            currentUrl: baseUrl,
            environment: window.location.hostname === 'localhost' ? 'development' : 'production',
            endpoints: {
                health: `${baseUrl}/health`,
                query: `${baseUrl}/query`,
                documents: `${baseUrl}/documents`,
                stats: `${baseUrl}/stats`,
                search: `${baseUrl}/search`
            },
            configSource: window.apiClient ? (window.apiClient.configSource || 'unknown') : 'not-loaded',
            configLoaded: window.apiClient ? window.apiClient.configLoaded : false
        };
    }

    /**
     * 迁移旧配置（用于版本升级）
     */
    async migrateOldSettings(oldSettings) {
        const newSettings = await this.getDefaultSettings();
        
        // 保留用户的UI偏好
        if (oldSettings.darkMode !== undefined) {
            newSettings.darkMode = oldSettings.darkMode;
        }
        if (oldSettings.autoScroll !== undefined) {
            newSettings.autoScroll = oldSettings.autoScroll;
        }
        
        // 保留有效的模型参数
        if (oldSettings.temperature >= 0 && oldSettings.temperature <= 1) {
            newSettings.temperature = oldSettings.temperature;
        }
        if (oldSettings.maxTokens > 0 && oldSettings.maxTokens <= 100000) {
            newSettings.maxTokens = oldSettings.maxTokens;
        }
        
        // API URL始终使用当前配置
        if (window.apiClient && window.apiClient.baseUrl) {
            newSettings.apiUrl = window.apiClient.baseUrl;
        }
        
        return newSettings;
    }
}

// 创建全局配置管理器实例
window.configManager = new ConfigManager();

// 异步初始化和调试输出
(async function() {
    try {
        const apiInfo = await window.configManager.getApiInfo();
        console.log('ConfigManager initialized:', {
            version: window.configManager.CONFIG_VERSION,
            apiInfo: apiInfo
        });
    } catch (error) {
        console.error('ConfigManager initialization error:', error);
    }
})();