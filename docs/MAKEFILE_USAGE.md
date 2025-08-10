# Makefile使用指南

## 快速开始

### 1. 环境准备
```bash
# 复制环境变量模板
cp .env.example .env

# 编辑.env文件，填入你的配置
vi .env

# 安装依赖
make install
```

### 2. 部署应用

#### 完整部署（推荐）
```bash
# 部署所有栈（包含CloudFront 403修复）
make deploy-all
```

#### 分步部署
```bash
# 1. 部署数据栈
make deploy-stack STACK=RAG-Data

# 2. 部署API栈  
make deploy-stack STACK=RAG-API

# 3. 部署Web栈（修复版）
make deploy-web
```

### 3. Web相关命令

#### 部署Web前端
```bash
# 部署Web栈并上传前端文件
make deploy-web

# 验证部署是否成功
make verify-web
```

#### 修复CloudFront 403错误
```bash
# 如果遇到403错误，运行此命令
make fix-cloudfront

# 然后验证修复是否成功
make verify-web
```

## 常用命令

### 部署管理
| 命令 | 说明 |
|------|------|
| `make deploy` | 部署基础栈 |
| `make deploy-all` | 完整部署（包含Web修复） |
| `make deploy-web` | 部署Web栈（修复CloudFront 403） |
| `make fix-cloudfront` | 修复CloudFront 403错误 |
| `make verify-web` | 验证Web部署状态 |
| `make destroy` | 销毁CDK资源 |
| `make destroy-all` | 完全清理所有AWS资源 |

### 测试命令
| 命令 | 说明 |
|------|------|
| `make test` | 运行所有测试 |
| `make test-unit` | 运行单元测试 |
| `make test-integration` | 运行集成测试 |
| `make test-e2e` | 运行端到端测试 |
| `make test-coverage` | 生成覆盖率报告 |

### 开发命令
| 命令 | 说明 |
|------|------|
| `make run-local` | 运行本地API服务器 |
| `make lint` | 运行代码检查 |
| `make format` | 格式化代码 |
| `make clean` | 清理构建产物 |

## CloudFront 403问题解决

### 问题原因
- S3桶权限配置不正确
- CloudFront OAI未正确配置
- 文件不存在或路径错误

### 解决流程
1. **使用Makefile自动修复**
   ```bash
   # 运行修复命令
   make fix-cloudfront
   
   # 验证修复结果
   make verify-web
   ```

2. **重新部署Web栈**
   ```bash
   # 使用修复版Web栈重新部署
   make deploy-web
   ```

3. **验证部署**
   ```bash
   # 检查部署状态
   make verify-web
   
   # 如果显示HTTP 200，说明修复成功
   ```

## 环境变量配置

确保`.env`文件包含以下必要配置：
```bash
# AWS配置
AWS_REGION=us-east-1
AWS_PROFILE=default

# Bedrock配置
BEDROCK_MODEL_ID=amazon.nova-lite-v1:0
EMBEDDING_MODEL_ID=amazon.titan-embed-text-v2:0

# Zilliz配置
ZILLIZ_ENDPOINT=https://your-endpoint.zillizcloud.com
ZILLIZ_TOKEN=your-token

# 部署阶段
STAGE=prod
```

## 故障排除

### CloudFront仍返回403
1. 等待1-2分钟让缓存失效生效
2. 运行 `make fix-cloudfront`
3. 如果问题持续，运行 `make deploy-web` 重新部署

### 部署失败
1. 检查AWS凭证：`aws sts get-caller-identity`
2. 确认区域设置：`echo $AWS_REGION`
3. 查看CDK日志：`make logs`

### 测试失败
1. 确保环境变量正确设置
2. 运行 `make health-check` 检查依赖
3. 查看详细错误：`pytest -vvs`

## 最佳实践

1. **总是先验证环境**
   ```bash
   make show-config
   make health-check
   ```

2. **使用完整部署命令**
   ```bash
   # 推荐使用deploy-all确保所有组件正确部署
   make deploy-all
   ```

3. **部署后验证**
   ```bash
   # 每次部署后都应验证
   make verify-web
   ```

4. **定期清理**
   ```bash
   # 清理构建产物
   make clean
   
   # 销毁不需要的资源
   make destroy
   ```

## 进阶用法

### 并行测试
```bash
# 运行快速测试（跳过慢速测试）
make test-fast

# 监视模式（文件变化时自动测试）
make test-watch
```

### CI/CD集成
```bash
# 运行完整CI流程
make ci

# 带通知的部署
make deploy-notify
```

### Docker部署
```bash
# 构建并运行Docker容器
make docker-run
```

## 支持

如有问题，请查看：
- `docs/CLOUDFRONT_403_FIX.md` - CloudFront 403错误详细解决方案
- `docs/TROUBLESHOOTING.md` - 通用故障排除指南
- GitHub Issues - 提交问题报告