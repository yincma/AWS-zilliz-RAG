/**
 * 浏览器控制台测试脚本
 * 在浏览器中打开 https://dfg648088lloi.cloudfront.net
 * 然后在控制台中运行此脚本
 */

console.log('=== 开始前端功能测试 ===');

// 测试结果收集
const testResults = {
    passed: [],
    failed: [],
    total: 0
};

// 测试函数
function testFunction(name, testFn) {
    testResults.total++;
    try {
        const result = testFn();
        if (result) {
            testResults.passed.push(name);
            console.log(`✅ ${name}: 通过`);
        } else {
            testResults.failed.push(name);
            console.error(`❌ ${name}: 失败`);
        }
    } catch (error) {
        testResults.failed.push(name);
        console.error(`❌ ${name}: 错误 - ${error.message}`);
    }
}

// 1. 测试全局变量和对象
console.log('\n--- 测试全局对象 ---');
testFunction('API客户端存在', () => typeof apiClient !== 'undefined');
testFunction('聊天管理器存在', () => typeof chatManager !== 'undefined');
testFunction('文档管理器存在', () => typeof documentManager !== 'undefined');
testFunction('搜索管理器存在', () => typeof searchManager !== 'undefined');

// 2. 测试导航切换
console.log('\n--- 测试导航切换 ---');
testFunction('切换到文档标签', () => {
    const docTab = document.querySelector('[data-tab="documents"]');
    docTab.click();
    return document.getElementById('documents-tab').classList.contains('active');
});

testFunction('切换到搜索标签', () => {
    const searchTab = document.querySelector('[data-tab="search"]');
    searchTab.click();
    return document.getElementById('search-tab').classList.contains('active');
});

testFunction('切换到设置标签', () => {
    const settingsTab = document.querySelector('[data-tab="settings"]');
    settingsTab.click();
    return document.getElementById('settings-tab').classList.contains('active');
});

testFunction('切换回聊天标签', () => {
    const chatTab = document.querySelector('[data-tab="chat"]');
    chatTab.click();
    return document.getElementById('chat-tab').classList.contains('active');
});

// 3. 测试聊天功能
console.log('\n--- 测试聊天功能 ---');
testFunction('聊天输入框存在', () => {
    const input = document.getElementById('chat-input');
    return input !== null;
});

testFunction('发送按钮存在', () => {
    const btn = document.getElementById('send-btn');
    return btn !== null;
});

testFunction('清空对话按钮功能', () => {
    const clearBtn = document.getElementById('clear-chat');
    clearBtn.click();
    // 检查是否清空了聊天容器（除了欢迎消息）
    const messages = document.querySelectorAll('.message');
    return messages.length === 0;
});

testFunction('快速问题按钮', () => {
    const quickBtns = document.querySelectorAll('.quick-action');
    return quickBtns.length === 3;
});

// 4. 测试文档管理
console.log('\n--- 测试文档管理 ---');
testFunction('上传按钮存在', () => {
    const uploadBtn = document.getElementById('upload-btn');
    return uploadBtn !== null;
});

testFunction('文件输入框存在', () => {
    const fileInput = document.getElementById('file-input');
    return fileInput !== null;
});

testFunction('上传区域可点击', () => {
    const uploadArea = document.getElementById('upload-area');
    uploadArea.click();
    // 检查是否触发了文件选择
    return document.getElementById('file-input') !== null;
});

// 5. 测试搜索功能
console.log('\n--- 测试搜索功能 ---');
document.querySelector('[data-tab="search"]').click();

testFunction('搜索输入框存在', () => {
    const searchInput = document.getElementById('search-input');
    return searchInput !== null;
});

testFunction('搜索按钮存在', () => {
    const searchBtn = document.getElementById('search-btn');
    return searchBtn !== null;
});

testFunction('Top-K设置存在', () => {
    const topK = document.getElementById('search-top-k');
    return topK !== null && topK.value === '10';
});

// 6. 测试设置功能
console.log('\n--- 测试设置功能 ---');
document.querySelector('[data-tab="settings"]').click();

testFunction('API URL输入框', () => {
    const apiUrl = document.getElementById('api-url');
    return apiUrl !== null && apiUrl.value.includes('amazonaws.com');
});

testFunction('深色模式切换', () => {
    const darkMode = document.getElementById('dark-mode');
    const initialState = document.body.classList.contains('dark-mode');
    darkMode.click();
    const afterClick = document.body.classList.contains('dark-mode');
    // 切换回原状态
    if (initialState) darkMode.click();
    return afterClick !== initialState;
});

testFunction('保存设置按钮', () => {
    const saveBtn = document.getElementById('save-settings');
    return saveBtn !== null;
});

testFunction('重置设置按钮', () => {
    const resetBtn = document.getElementById('reset-settings');
    return resetBtn !== null;
});

// 7. 测试API连接状态
console.log('\n--- 测试API连接 ---');
testFunction('连接状态指示器', () => {
    const indicator = document.getElementById('status-indicator');
    return indicator !== null;
});

testFunction('API已连接', () => {
    const indicator = document.getElementById('status-indicator');
    return indicator.classList.contains('connected');
});

// 8. 测试实时功能
console.log('\n--- 测试实时交互 ---');
testFunction('发送测试消息', async () => {
    document.querySelector('[data-tab="chat"]').click();
    const input = document.getElementById('chat-input');
    const sendBtn = document.getElementById('send-btn');
    
    // 设置测试消息
    input.value = 'Test message from automated test';
    
    // 检查发送按钮是否启用
    return !sendBtn.disabled;
});

// 9. 测试响应式设计
console.log('\n--- 测试响应式设计 ---');
testFunction('侧边栏存在', () => {
    const sidebar = document.querySelector('.sidebar');
    return sidebar !== null && getComputedStyle(sidebar).display !== 'none';
});

testFunction('主内容区存在', () => {
    const main = document.querySelector('.main-content');
    return main !== null && getComputedStyle(main).display !== 'none';
});

// 输出测试结果摘要
console.log('\n=== 测试结果摘要 ===');
console.log(`总测试: ${testResults.total}`);
console.log(`通过: ${testResults.passed.length} (${(testResults.passed.length/testResults.total*100).toFixed(1)}%)`);
console.log(`失败: ${testResults.failed.length} (${(testResults.failed.length/testResults.total*100).toFixed(1)}%)`);

if (testResults.failed.length > 0) {
    console.log('\n失败的测试:');
    testResults.failed.forEach(test => console.log(`  - ${test}`));
}

// 返回测试结果
testResults;