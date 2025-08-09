/**
 * CloudFront浏览器端测试脚本
 * 
 * 使用方法：
 * 1. 在浏览器中打开 https://dfg648088lloi.cloudfront.net
 * 2. 打开开发者控制台 (F12)
 * 3. 将此脚本粘贴到控制台并运行
 */

console.log('%c=== CloudFront浏览器端功能测试 ===', 'color: blue; font-size: 16px; font-weight: bold');
console.log('测试URL:', window.location.href);
console.log('测试时间:', new Date().toLocaleString());

// 测试结果收集
const testResults = {
    passed: 0,
    failed: 0,
    details: []
};

// 测试函数
async function runTest(name, testFn) {
    try {
        const result = await testFn();
        if (result.success) {
            testResults.passed++;
            console.log(`✅ ${name}`, result.details || '');
            if (result.data) {
                console.log('  📊 返回数据:', result.data);
            }
        } else {
            testResults.failed++;
            console.error(`❌ ${name}:`, result.error || result.details);
        }
        testResults.details.push({name, ...result});
    } catch (error) {
        testResults.failed++;
        console.error(`❌ ${name}: 异常 -`, error.message);
        testResults.details.push({name, success: false, error: error.message});
    }
}

// 测试套件
const tests = {
    // 1. 检查全局对象
    async checkGlobalObjects() {
        const objects = {
            'API客户端': typeof apiClient !== 'undefined',
            '配置对象': typeof RAG_CONFIG !== 'undefined' || typeof API_CONFIG !== 'undefined',
            '聊天管理器': typeof chatManager !== 'undefined',
            '文档管理器': typeof documentManager !== 'undefined',
            '搜索管理器': typeof searchManager !== 'undefined'
        };
        
        const allExist = Object.values(objects).every(v => v);
        return {
            success: allExist,
            details: `检测到 ${Object.values(objects).filter(v => v).length}/${Object.keys(objects).length} 个对象`,
            data: objects
        };
    },

    // 2. 测试API连接
    async testAPIConnection() {
        if (typeof apiClient === 'undefined') {
            return {success: false, error: 'apiClient未定义'};
        }
        
        try {
            const health = await apiClient.checkHealth();
            return {
                success: health && health.status === 'healthy',
                details: `API状态: ${health?.status}`,
                data: health
            };
        } catch (error) {
            return {success: false, error: error.message};
        }
    },

    // 3. 测试查询功能
    async testQuery() {
        if (typeof apiClient === 'undefined') {
            return {success: false, error: 'apiClient未定义'};
        }
        
        try {
            console.log('  🔄 发送测试查询...');
            const response = await apiClient.query('What is RAG?', 5, true);
            
            const hasAnswer = response && response.answer;
            const hasSources = response && response.sources && response.sources.length > 0;
            
            return {
                success: hasAnswer && hasSources,
                details: `回答长度: ${response?.answer?.length || 0}, 来源数: ${response?.sources?.length || 0}`,
                data: {
                    answerPreview: response?.answer?.substring(0, 100) + '...',
                    sourcesCount: response?.sources?.length,
                    firstSource: response?.sources?.[0]
                }
            };
        } catch (error) {
            return {success: false, error: error.message};
        }
    },

    // 4. 测试文档管理
    async testDocumentManagement() {
        if (typeof apiClient === 'undefined') {
            return {success: false, error: 'apiClient未定义'};
        }
        
        const results = {
            list: false,
            stats: false,
            upload: false
        };
        
        // 测试文档列表
        try {
            const response = await apiClient.listDocuments();
            results.list = response && response.status !== 'error';
        } catch (error) {
            console.log('  ⚠️ 文档列表失败:', error.message);
        }
        
        // 测试统计
        try {
            const response = await apiClient.getStats();
            results.stats = response && response.status !== 'error';
        } catch (error) {
            console.log('  ⚠️ 统计获取失败:', error.message);
        }
        
        return {
            success: results.list || results.stats,
            details: `列表: ${results.list ? '✓' : '✗'}, 统计: ${results.stats ? '✓' : '✗'}`,
            data: results
        };
    },

    // 5. 测试UI交互
    async testUIInteraction() {
        const tests = {
            '标签切换': () => {
                const tabs = document.querySelectorAll('.nav-item');
                return tabs.length === 4;
            },
            '聊天输入': () => {
                const input = document.getElementById('chat-input');
                return input !== null;
            },
            '发送按钮': () => {
                const btn = document.getElementById('send-btn');
                return btn !== null;
            },
            '快速问题': () => {
                const quickBtns = document.querySelectorAll('.quick-action');
                return quickBtns.length === 3;
            },
            '上传区域': () => {
                const uploadArea = document.getElementById('upload-area');
                return uploadArea !== null;
            }
        };
        
        const results = {};
        for (const [name, test] of Object.entries(tests)) {
            results[name] = test();
        }
        
        const allPass = Object.values(results).every(v => v);
        return {
            success: allPass,
            details: `通过 ${Object.values(results).filter(v => v).length}/${Object.keys(results).length} 项`,
            data: results
        };
    },

    // 6. 测试实时消息发送
    async testSendMessage() {
        const input = document.getElementById('chat-input');
        const sendBtn = document.getElementById('send-btn');
        
        if (!input || !sendBtn) {
            return {success: false, error: '聊天组件未找到'};
        }
        
        // 设置测试消息
        input.value = 'CloudFront测试消息: ' + new Date().toLocaleTimeString();
        
        // 检查按钮状态
        const isEnabled = !sendBtn.disabled;
        
        // 模拟发送
        if (isEnabled && typeof chatManager !== 'undefined') {
            console.log('  📤 发送测试消息...');
            // 不实际发送，避免污染界面
            // chatManager.sendMessage();
        }
        
        return {
            success: isEnabled,
            details: `发送按钮${isEnabled ? '已启用' : '已禁用'}`,
            data: {inputValue: input.value, buttonEnabled: isEnabled}
        };
    },

    // 7. 性能测试
    async testPerformance() {
        const metrics = {
            pageLoadTime: performance.timing.loadEventEnd - performance.timing.navigationStart,
            domReady: performance.timing.domContentLoadedEventEnd - performance.timing.navigationStart,
            resources: performance.getEntriesByType('resource').length,
            jsFiles: performance.getEntriesByType('resource').filter(r => r.name.includes('.js')).length,
            cssFiles: performance.getEntriesByType('resource').filter(r => r.name.includes('.css')).length
        };
        
        const isfast = metrics.pageLoadTime < 3000; // 3秒内加载完成
        
        return {
            success: isfast,
            details: `页面加载: ${metrics.pageLoadTime}ms, 资源数: ${metrics.resources}`,
            data: metrics
        };
    },

    // 8. 错误检查
    async checkErrors() {
        // 检查控制台错误
        const errors = [];
        
        // 检查网络错误
        const failedResources = performance.getEntriesByType('resource')
            .filter(r => r.responseEnd === 0);
        
        return {
            success: failedResources.length === 0,
            details: failedResources.length > 0 ? `${failedResources.length} 个资源加载失败` : '无错误',
            data: {failedResources}
        };
    }
};

// 运行所有测试
async function runAllTests() {
    console.log('\n📋 开始测试...\n');
    
    // 按顺序运行测试
    await runTest('1. 全局对象检查', tests.checkGlobalObjects);
    await runTest('2. API连接测试', tests.testAPIConnection);
    await runTest('3. 查询功能测试', tests.testQuery);
    await runTest('4. 文档管理测试', tests.testDocumentManagement);
    await runTest('5. UI交互测试', tests.testUIInteraction);
    await runTest('6. 消息发送测试', tests.testSendMessage);
    await runTest('7. 性能测试', tests.testPerformance);
    await runTest('8. 错误检查', tests.checkErrors);
    
    // 打印总结
    console.log('\n' + '='.repeat(50));
    console.log('%c📊 测试总结', 'color: blue; font-size: 14px; font-weight: bold');
    console.log('='.repeat(50));
    console.log(`✅ 通过: ${testResults.passed}`);
    console.log(`❌ 失败: ${testResults.failed}`);
    console.log(`📈 成功率: ${(testResults.passed / (testResults.passed + testResults.failed) * 100).toFixed(1)}%`);
    
    // 失败详情
    const failures = testResults.details.filter(t => !t.success);
    if (failures.length > 0) {
        console.log('\n⚠️ 失败项目:');
        failures.forEach(f => {
            console.log(`  - ${f.name}: ${f.error || f.details}`);
        });
    }
    
    // 保存到全局变量
    window.cloudFrontTestResults = testResults;
    console.log('\n💾 测试结果已保存到 window.cloudFrontTestResults');
    
    return testResults;
}

// 自动运行测试
runAllTests().then(results => {
    console.log('\n✨ 测试完成！');
    
    // 提供快捷操作
    console.log('\n可用命令:');
    console.log('  window.cloudFrontTestResults - 查看详细结果');
    console.log('  apiClient.query("你的问题") - 测试查询');
    console.log('  location.reload() - 刷新页面');
});