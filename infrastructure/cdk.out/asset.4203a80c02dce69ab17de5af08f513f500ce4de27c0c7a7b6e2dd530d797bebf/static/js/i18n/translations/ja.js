// 日本語翻訳
export default {
    app: {
        title: 'AWS Zilliz RAG - インテリジェントQ&Aシステム',
        version: 'v0.1.0'
    },
    nav: {
        chat: 'チャット',
        documents: 'ドキュメント管理',
        search: 'ベクトル検索',
        settings: '設定'
    },
    status: {
        connected: '接続済み',
        disconnected: '未接続',
        connecting: '接続中...',
        error: '接続エラー'
    },
    chat: {
        title: 'インテリジェントQ&Aアシスタント',
        clearChat: 'チャットをクリア',
        welcome: 'RAGインテリジェントQ&Aシステムへようこそ',
        welcomeDesc: 'アップロードされたドキュメントに基づいて質問に答えることができます',
        inputPlaceholder: '質問を入力してください...',
        send: '送信',
        sending: '送信中...',
        showSources: 'ソースを表示',
        hideSources: 'ソースを非表示',
        thinking: '考え中...',
        error: 'エラーが発生しました',
        noAnswer: '答えが見つかりません',
        topK: 'トップK',
        sources: 'ソース',
        similarity: '類似度',
        processing: '処理中...'
    },
    documents: {
        title: 'ドキュメント管理',
        upload: 'ドキュメントをアップロード',
        dragDrop: 'ファイルをここにドラッグ&ドロップまたはクリックして参照',
        supportedFormats: 'サポート形式：PDF、TXT、MD、DOCX',
        uploadSuccess: 'アップロード成功',
        uploadFailed: 'アップロード失敗',
        deleteConfirm: 'このドキュメントを削除してもよろしいですか？',
        processing: '処理中...',
        fileName: 'ファイル名',
        fileSize: 'サイズ',
        uploadTime: 'アップロード時刻',
        actions: 'アクション',
        delete: '削除',
        view: '表示',
        noDocuments: 'まだドキュメントがアップロードされていません',
        uploadFromS3: 'S3からアップロード',
        s3Key: 'S3キー',
        s3Keys: 'S3キー（1行に1つ）',
        batchUpload: 'バッチアップロード'
    },
    search: {
        title: 'ベクトル検索',
        placeholder: '検索キーワードを入力...',
        topK: 'トップK結果',
        search: '検索',
        searching: '検索中...',
        similarity: '類似度スコア',
        noResults: '結果が見つかりません',
        resultCount: '{count}件の結果が見つかりました',
        content: 'コンテンツ',
        metadata: 'メタデータ'
    },
    settings: {
        title: '設定',
        language: '言語',
        model: 'モデル設定',
        interface: 'インターフェース設定',
        darkMode: 'ダークモード',
        autoScroll: '最新メッセージに自動スクロール',
        temperature: '温度',
        maxTokens: '最大トークン数',
        save: '設定を保存',
        reset: 'デフォルトに戻す',
        saveSuccess: '設定が正常に保存されました',
        resetConfirm: 'すべての設定をデフォルトに戻してもよろしいですか？'
    },
    quickActions: {
        whatIsRAG: 'RAGとは何ですか？',
        advantages: 'RAGの利点は何ですか？',
        howToUse: 'このシステムの使い方は？'
    },
    common: {
        loading: '読み込み中...',
        error: 'エラー',
        success: '成功',
        warning: '警告',
        info: '情報',
        confirm: '確認',
        cancel: 'キャンセル',
        yes: 'はい',
        no: 'いいえ',
        ok: 'OK',
        close: '閉じる',
        retry: 'リトライ',
        refresh: '更新'
    }
};