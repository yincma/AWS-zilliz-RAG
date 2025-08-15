// 中文翻译
export default {
    app: {
        title: 'AWS Zilliz RAG - 智能问答系统',
        version: 'v0.1.0'
    },
    nav: {
        chat: '对话',
        documents: '文档管理',
        search: '向量搜索',
        settings: '设置'
    },
    status: {
        connected: '已连接',
        disconnected: '未连接',
        connecting: '连接中...',
        error: '连接错误'
    },
    chat: {
        title: '智能问答助手',
        clearChat: '清空对话',
        welcome: '欢迎使用RAG智能问答系统',
        welcomeDesc: '我可以基于已上传的文档回答您的问题',
        inputPlaceholder: '输入您的问题...',
        send: '发送',
        sending: '发送中...',
        showSources: '显示来源',
        hideSources: '隐藏来源',
        thinking: '思考中...',
        error: '发生错误',
        noAnswer: '未找到答案',
        topK: 'Top K',
        sources: '来源',
        similarity: '相似度',
        processing: '处理中...'
    },
    documents: {
        title: '文档管理',
        upload: '上传文档',
        dragDrop: '拖拽文件到此处或点击浏览',
        supportedFormats: '支持格式：PDF、TXT、MD、DOCX',
        uploadSuccess: '上传成功',
        uploadFailed: '上传失败',
        deleteConfirm: '确定要删除此文档吗？',
        processing: '处理中...',
        fileName: '文件名',
        fileSize: '大小',
        uploadTime: '上传时间',
        actions: '操作',
        delete: '删除',
        view: '查看',
        noDocuments: '暂无上传的文档',
        uploadFromS3: '从S3上传',
        s3Key: 'S3键值',
        s3Keys: 'S3键值（每行一个）',
        batchUpload: '批量上传'
    },
    search: {
        title: '向量搜索',
        placeholder: '输入搜索关键词...',
        topK: 'Top K 结果数',
        search: '搜索',
        searching: '搜索中...',
        similarity: '相似度分数',
        noResults: '未找到结果',
        resultCount: '找到 {count} 个结果',
        content: '内容',
        metadata: '元数据'
    },
    settings: {
        title: '设置',
        language: '语言',
        model: '模型设置',
        interface: '界面设置',
        darkMode: '深色模式',
        autoScroll: '自动滚动到最新消息',
        temperature: '温度',
        maxTokens: '最大令牌数',
        save: '保存设置',
        reset: '重置默认',
        saveSuccess: '设置保存成功',
        resetConfirm: '确定要重置所有设置为默认值吗？'
    },
    quickActions: {
        whatIsRAG: '什么是RAG？',
        advantages: 'RAG有哪些优势？',
        howToUse: '如何使用这个系统？'
    },
    common: {
        loading: '加载中...',
        error: '错误',
        success: '成功',
        warning: '警告',
        info: '信息',
        confirm: '确认',
        cancel: '取消',
        yes: '是',
        no: '否',
        ok: '确定',
        close: '关闭',
        retry: '重试',
        refresh: '刷新'
    }
};