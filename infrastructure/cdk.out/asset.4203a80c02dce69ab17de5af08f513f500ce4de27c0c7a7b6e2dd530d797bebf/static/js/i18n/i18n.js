// 多语言管理器
class I18nManager {
    constructor() {
        this.currentLang = 'en'; // 默认英文
        this.translations = {};
        this.observers = [];
    }
    
    async loadTranslations() {
        // 直接加载所有翻译文件
        try {
            const [enModule, zhModule, jaModule] = await Promise.all([
                import('./translations/en.js'),
                import('./translations/zh.js'),
                import('./translations/ja.js')
            ]);
            
            this.translations = {
                en: enModule.default,
                zh: zhModule.default,
                ja: jaModule.default
            };
            
            console.log('Translations loaded successfully');
        } catch (error) {
            console.error('Failed to load translations:', error);
        }
    }
    
    setLanguage(lang) {
        if (!this.translations[lang]) {
            console.warn(`Language ${lang} not found, using English`);
            lang = 'en';
        }
        
        this.currentLang = lang;
        document.documentElement.lang = lang;
        this.updateUI();
        this.notifyObservers();
    }
    
    t(key, params = {}) {
        const keys = key.split('.');
        let value = this.translations[this.currentLang];
        
        for (const k of keys) {
            value = value?.[k];
        }
        
        // 如果找不到翻译，返回key本身
        if (!value) {
            console.warn(`Translation not found for key: ${key}`);
            return key;
        }
        
        // 替换参数 {param}
        if (typeof value === 'string') {
            return value.replace(/\{(\w+)\}/g, (match, param) => params[param] || match);
        }
        
        return value;
    }
    
    updateUI() {
        // 更新所有带有 data-i18n 属性的元素
        document.querySelectorAll('[data-i18n]').forEach(elem => {
            const key = elem.getAttribute('data-i18n');
            
            if (elem.tagName === 'INPUT' || elem.tagName === 'TEXTAREA') {
                elem.placeholder = this.t(key);
            } else {
                elem.textContent = this.t(key);
            }
        });
        
        // 更新HTML title
        document.title = this.t('app.title');
    }
    
    // 注册观察者，用于响应语言变化
    subscribe(callback) {
        this.observers.push(callback);
    }
    
    notifyObservers() {
        this.observers.forEach(callback => callback(this.currentLang));
    }
    
    getCurrentLanguage() {
        return this.currentLang;
    }
}

// 创建全局实例
window.i18n = new I18nManager();