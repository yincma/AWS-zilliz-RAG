# AWS RAG Application Makefile
# 提供标准化的部署和管理命令

.PHONY: help install clean deploy destroy test lint check synth diff test-unit test-integration test-e2e test-coverage test-report

# 默认目标
help:
	@echo "AWS RAG Application - 可用命令:"
	@echo ""
	@echo "📦 环境管理:"
	@echo "  make install      - 安装所有依赖"
	@echo "  make clean        - 清理构建产物和缓存"
	@echo "  make kill-cdk     - 终止所有CDK进程"
	@echo ""
	@echo "🧪 测试命令:"
	@echo "  make test         - 运行所有测试"
	@echo "  make test-unit    - 运行单元测试"
	@echo "  make test-integration - 运行集成测试"
	@echo "  make test-e2e     - 运行端到端测试"
	@echo "  make test-coverage - 生成覆盖率报告"
	@echo "  make test-report  - 生成测试报告"
	@echo "  make test-ui      - 运行UI测试"
	@echo ""
	@echo "🔍 代码质量:"
	@echo "  make lint         - 运行代码检查"
	@echo "  make type-check   - 运行类型检查"
	@echo "  make format       - 格式化代码"
	@echo ""
	@echo "☁️  部署管理:"
	@echo "  make deploy       - 部署应用到AWS"
	@echo "  make destroy      - 销毁CDK管理的资源"
	@echo "  make destroy-all  - 完全清理所有AWS资源"
	@echo "  make synth        - 合成CDK模板"
	@echo "  make diff         - 查看栈差异"
	@echo "  make logs         - 查看Lambda日志"
	@echo ""
	@echo "🐳 Docker:"
	@echo "  make docker-build - 构建Docker镜像"
	@echo "  make docker-run   - 运行Docker容器"
	@echo "  make run-local    - 运行本地API服务器"
	@echo ""

# 环境变量检查
check-env:
ifndef ZILLIZ_ENDPOINT
	$(error ZILLIZ_ENDPOINT未设置)
endif
ifndef ZILLIZ_TOKEN
	$(error ZILLIZ_TOKEN未设置)
endif

# 安装依赖
install:
	@echo "安装Python依赖..."
	pip3 install -r requirements.txt
	pip3 install -r requirements-dev.txt
	@echo "安装测试依赖..."
	pip3 install -r tests/requirements-test.txt
	@echo "安装CDK..."
	npm install -g aws-cdk@latest
	cd infrastructure && pip3 install -r requirements.txt
	@echo "✅ 依赖安装完成"

# 清理
clean: kill-cdk
	@echo "清理构建产物..."
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	rm -rf infrastructure/cdk.out
	rm -rf htmlcov coverage.xml .coverage* coverage-*.xml
	rm -rf test-reports/
	rm -f /tmp/rag-deploy.lock
	@echo "✅ 清理完成"

# 终止CDK进程
kill-cdk:
	@echo "检查并终止CDK进程..."
	@ps aux | grep -E "(cdk|aws-cdk)" | grep -v grep | awk '{print $$2}' | xargs -r kill -9 2>/dev/null || true
	@docker ps -a | grep -E "(cdk|sam)" | awk '{print $$1}' | xargs -r docker stop 2>/dev/null || true
	@docker ps -a | grep -E "(cdk|sam)" | awk '{print $$1}' | xargs -r docker rm 2>/dev/null || true
	@echo "✅ CDK进程已清理"

# 代码检查
lint:
	@echo "运行代码格式化检查..."
	black --check app/ tests/
	isort --check-only app/ tests/
	flake8 app/ tests/
	@echo "✅ 代码检查通过"

# 代码格式化
format:
	@echo "格式化代码..."
	black app/ tests/
	isort app/ tests/
	@echo "✅ 代码格式化完成"

# 类型检查
type-check:
	@echo "运行类型检查..."
	mypy app/
	@echo "✅ 类型检查通过"

# 运行所有测试
test:
	@echo "运行所有测试..."
	pytest tests/ -v
	@echo "✅ 测试完成"

# 运行单元测试
test-unit:
	@echo "运行单元测试..."
	pytest tests/unit -v -m unit
	@echo "✅ 单元测试完成"

# 运行集成测试
test-integration:
	@echo "运行集成测试..."
	@chmod +x run_integration_tests.sh
	./run_integration_tests.sh
	@echo "✅ 集成测试完成"

# 运行端到端测试
test-e2e:
	@echo "运行端到端测试..."
	pytest tests/e2e -v -m e2e --tb=short
	@echo "✅ E2E测试完成"

# 运行UI测试
test-ui:
	@echo "运行UI测试..."
	@if [ -f "tests/run_ui_tests.sh" ]; then \
		chmod +x tests/run_ui_tests.sh && ./tests/run_ui_tests.sh; \
	else \
		pytest tests/test_ui*.py -v; \
	fi
	@echo "✅ UI测试完成"

# 生成覆盖率报告
test-coverage:
	@echo "生成测试覆盖率报告..."
	pytest tests/ --cov=app --cov-report=html:htmlcov --cov-report=term --cov-report=xml
	@echo "✅ 覆盖率报告已生成"
	@echo "📊 HTML报告: htmlcov/index.html"

# 生成测试报告
test-report:
	@echo "生成综合测试报告..."
	@python generate_test_report.py
	@echo "✅ 测试报告已生成"

# 快速测试（跳过慢速测试）
test-fast:
	@echo "运行快速测试（跳过慢速测试）..."
	pytest tests/ -v -m "not slow"
	@echo "✅ 快速测试完成"

# 测试监视模式
test-watch:
	@echo "启动测试监视模式..."
	pytest-watch tests/ -- -v

# CDK相关命令
STAGE ?= dev
AWS_REGION ?= us-east-1

# 合成模板
synth: clean
	@echo "合成CDK模板 (stage=$(STAGE))..."
	cd infrastructure && npx cdk synth --context stage=$(STAGE)
	@echo "✅ 模板合成完成"

# 查看差异
diff:
	@echo "查看栈差异 (stage=$(STAGE))..."
	cd infrastructure && npx cdk diff --context stage=$(STAGE)

# 打包Lambda函数
package-lambda:
	@echo "打包Lambda函数..."
	@rm -rf lambda_deployment.zip
	@cd lambda_functions && \
		pip3 install -r requirements.txt -t . --quiet && \
		zip -r ../lambda_deployment.zip . -x "*.pyc" -x "__pycache__/*" > /dev/null
	@echo "✅ Lambda函数打包完成 (lambda_deployment.zip)"

# 部署前端到S3
deploy-frontend:
	@echo "部署前端到S3..."
	@if [ -z "$${WEB_BUCKET}" ]; then \
		echo "❌ WEB_BUCKET环境变量未设置"; \
		exit 1; \
	fi
	@aws s3 sync app/views/web/static s3://$${WEB_BUCKET}/ --delete
	@aws s3 cp app/views/web/templates/index.html s3://$${WEB_BUCKET}/
	@echo "✅ 前端部署完成"

# 部署
deploy: check-env clean package-lambda
	@echo "开始部署 (stage=$(STAGE))..."
	@echo "正在检查并清理CDK进程..."
	@ps aux | grep -E "(cdk|aws-cdk)" | grep -v grep | awk '{print $$2}' | xargs -r kill -9 2>/dev/null || true
	@rm -rf infrastructure/cdk.out
	@echo ""
	@echo "1. 安装CDK依赖..."
	@cd infrastructure && pip3 install -r requirements.txt --quiet
	@echo ""
	@echo "2. 引导CDK环境..."
	@cd infrastructure && AWS_REGION=$(AWS_REGION) npx cdk bootstrap aws://$$(aws sts get-caller-identity --query Account --output text)/$(AWS_REGION) \
		--context stage=$(STAGE) || true
	@echo ""
	@echo "3. 合成CloudFormation模板..."
	@cd infrastructure && npx cdk synth --context stage=$(STAGE)
	@echo ""
	@echo "4. 显示要部署的栈..."
	@cd infrastructure && npx cdk list --context stage=$(STAGE)
	@echo ""
	@read -p "确认部署? (y/n): " confirm && [ "$$confirm" = "y" ]
	@echo ""
	@echo "5. 开始部署栈..."
	@cd infrastructure && npx cdk deploy --all \
		--context stage=$(STAGE) \
		--require-approval never \
		--concurrency 1 \
		--parameters RAG-API-$(STAGE):BedrockModelId=$${BEDROCK_MODEL_ID:-amazon.nova-lite-v1:0} \
		--parameters RAG-API-$(STAGE):EmbeddingModelId=$${EMBEDDING_MODEL_ID:-amazon.titan-embed-text-v2:0} \
		--parameters RAG-API-$(STAGE):ZillizEndpoint=$(ZILLIZ_ENDPOINT) \
		--parameters RAG-API-$(STAGE):ZillizToken=$(ZILLIZ_TOKEN)
	@echo ""
	@echo "6. 部署前端（如果WEB_BUCKET已设置）..."
	@if [ -n "$${WEB_BUCKET}" ]; then \
		$(MAKE) deploy-frontend; \
	else \
		echo "跳过前端部署（WEB_BUCKET未设置）"; \
	fi
	@echo "✅ 部署完成"
	@echo ""
	@echo "部署信息："
	@echo "  API端点: 请查看CDK输出"
	@if [ -n "$${WEB_BUCKET}" ]; then \
		echo "  前端URL: https://$${WEB_BUCKET}.s3.amazonaws.com/index.html"; \
	fi

# 快速部署（跳过确认）
deploy-fast: check-env clean
	@echo "快速部署模式 (stage=$(STAGE))..."
	cd infrastructure && \
	npx cdk deploy --all \
		--context stage=$(STAGE) \
		--require-approval never \
		--concurrency 1 \
		--parameters RAG-API-$(STAGE):BedrockModelId=$${BEDROCK_MODEL_ID:-amazon.nova-lite-v1:0} \
		--parameters RAG-API-$(STAGE):EmbeddingModelId=$${EMBEDDING_MODEL_ID:-amazon.titan-embed-text-v2:0} \
		--parameters RAG-API-$(STAGE):ZillizEndpoint=$(ZILLIZ_ENDPOINT) \
		--parameters RAG-API-$(STAGE):ZillizToken=$(ZILLIZ_TOKEN)
	@echo "✅ 快速部署完成"

# 销毁资源（CDK管理的资源）
destroy:
	@echo "⚠️  警告: 即将销毁所有AWS资源 (stage=$(STAGE))"
	@read -p "确认销毁? (输入'yes'确认): " confirm && [ "$$confirm" = "yes" ]
	cd infrastructure && npx cdk destroy --all --context stage=$(STAGE) --force
	@echo "✅ CDK资源已销毁"
	@echo ""
	@echo "⚠️  注意: 某些资源可能需要手动清理"
	@echo "  运行 'make destroy-all' 进行完整清理"

# 完全销毁所有资源（包括CDK未管理的）
destroy-all:
	@echo "🚨 警告: 即将完全清理所有AWS资源！"
	@echo "这将删除："
	@echo "  - 所有CloudFormation栈"
	@echo "  - 所有S3存储桶及内容"
	@echo "  - 所有Lambda函数"
	@echo "  - 所有API Gateway"
	@echo "  - 相关IAM角色和策略"
	@echo ""
	@read -p "确认完全销毁? (输入'DELETE ALL'确认): " confirm && [ "$$confirm" = "DELETE ALL" ]
	@chmod +x cleanup_aws_resources.sh
	@./cleanup_aws_resources.sh
	@echo "✅ 所有资源已完全清理"

# 部署单个栈
deploy-stack:
	@echo "部署单个栈 (stack=$(STACK), stage=$(STAGE))..."
	cd infrastructure && npx cdk deploy $(STACK)-$(STAGE) \
		--context stage=$(STAGE) \
		--require-approval never
	@echo "✅ 栈部署完成"

# 查看日志
logs:
	@echo "查看Lambda日志 (stage=$(STAGE))..."
	aws logs tail /aws/lambda/RAG-Query-$(STAGE) --follow

# 运行本地API
run-local:
	@echo "启动本地API服务器..."
	cd app && python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000

# 构建Docker镜像
docker-build:
	@echo "构建Docker镜像..."
	docker build -t rag-app:latest .
	@echo "✅ Docker镜像构建完成"

# 运行Docker容器
docker-run: docker-build
	@echo "运行Docker容器..."
	docker run -p 8000:8000 \
		-e AWS_REGION=$${AWS_REGION:-us-east-1} \
		-e ZILLIZ_ENDPOINT=$(ZILLIZ_ENDPOINT) \
		-e ZILLIZ_TOKEN=$(ZILLIZ_TOKEN) \
		--rm rag-app:latest

# 完整的CI/CD流程
ci: clean install lint type-check test test-coverage
	@echo "✅ CI检查全部通过"

# 部署前准备
prepare: check-env clean synth
	@echo "✅ 部署准备完成"

# 显示当前配置
show-config:
	@echo "当前配置:"
	@echo "  STAGE: $(STAGE)"
	@echo "  AWS_REGION: $${AWS_REGION:-us-east-1}"
	@echo "  BEDROCK_MODEL_ID: $${BEDROCK_MODEL_ID:-amazon.nova-lite-v1:0}"
	@echo "  EMBEDDING_MODEL_ID: $${EMBEDDING_MODEL_ID:-amazon.titan-embed-text-v2:0}"
	@echo "  ZILLIZ_ENDPOINT: $${ZILLIZ_ENDPOINT:0:20}..."

# 开发环境设置
dev-setup: install
	@echo "设置开发环境..."
	@cp .env.example .env 2>/dev/null || true
	@echo "请编辑 .env 文件配置必要的环境变量"
	@echo "✅ 开发环境设置完成"

# 检查项目健康状态
health-check:
	@echo "检查项目健康状态..."
	@python -c "import app; print('✅ App模块可导入')"
	@python -c "import boto3; print('✅ AWS SDK已安装')"
	@python -c "import langchain; print('✅ LangChain已安装')"
	@python -c "import pymilvus; print('✅ Milvus客户端已安装')"
	@echo "✅ 项目健康检查通过"

# 启动所有服务
start-all: docker-run
	@echo "✅ 所有服务已启动"

# 停止所有服务
stop-all:
	@echo "停止所有服务..."
	@docker stop $$(docker ps -q) 2>/dev/null || true
	@pkill -f "uvicorn" 2>/dev/null || true
	@echo "✅ 所有服务已停止"

# 显示项目信息
info:
	@echo "AWS-Zilliz-RAG 项目信息"
	@echo "========================"
	@echo "项目路径: $$(pwd)"
	@echo "Python版本: $$(python3 --version)"
	@echo "Pytest版本: $$(pytest --version | head -1)"
	@echo "AWS CLI版本: $$(aws --version)"
	@echo "CDK版本: $$(cdk --version)"
	@echo ""
	@echo "测试统计:"
	@echo "  单元测试: $$(find tests/unit -name "test_*.py" | wc -l) 个文件"
	@echo "  集成测试: $$(find tests/integration -name "test_*.py" | wc -l) 个文件"
	@echo "  E2E测试: $$(find tests/e2e -name "test_*.py" | wc -l) 个文件"
	@echo ""
	@echo "代码统计:"
	@echo "  Python文件: $$(find app -name "*.py" | wc -l) 个"
	@echo "  代码行数: $$(find app -name "*.py" -exec wc -l {} + | tail -1 | awk '{print $$1}') 行"

# 完成提示音
notify:
	@afplay /System/Library/Sounds/Sosumi.aiff

# 带通知的部署
deploy-notify: deploy notify
	@echo "✅ 部署完成并已发送通知"

# 带通知的测试
test-notify: test notify
	@echo "✅ 测试完成并已发送通知"