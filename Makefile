# AWS RAG Application Makefile
# 自动化部署，包含所有修复

.PHONY: help install clean deploy destroy test lint synth diff generate-config update-frontend \
	check-tools check-env bootstrap build-lambda build-lambda-fixed build-lambda-zip \
	deploy-lambda-direct update-lambda-env list-lambda logs-lambda \
	deploy-data deploy-api deploy-web _update_frontend_common \
	fix-cors fix-cloudfront verify-deploy test-api test-ui all redeploy-lambda test-lambda sync-cors-helper \
	build-container push-container deploy-container clean-ecr update-lambda deploy-quick check-ecr-image \
	clean-logs destroy-force clean-all

# 设置默认目标
.DEFAULT_GOAL := help

# 从.env文件加载环境变量（如果存在）
-include .env
export

# 变量定义（.env中的值会覆盖这些默认值）
STAGE ?= prod
# 强制使用.env中的AWS_REGION，如果没有则使用默认值
ifndef AWS_REGION
  AWS_REGION := us-east-1
endif
USE_API_V2 ?= true
# 注意：有两个CDK应用
# - app.py: 创建 RagApiStackV2 栈（当前使用）
# - app_v2.py: 创建 RAG-API-prod 栈（备用）
CDK_APP := app_v2.py

# 动态获取的值（避免硬编码）
ACCOUNT_ID ?= $(shell aws sts get-caller-identity --query Account --output text 2>/dev/null)
CDK_BOOTSTRAP_QUALIFIER ?= hnb659fds
OS_TYPE := $(shell uname -s)

# S3桶名称模板（使用变量而非硬编码）
S3_BUCKET_DOCUMENTS ?= rag-documents-$(ACCOUNT_ID)-$(AWS_REGION)
S3_BUCKET_WEB ?= rag-web-$(ACCOUNT_ID)-$(AWS_REGION)

# ECR容器镜像配置
ECR_REPOSITORY_NAME ?= rag-lambda-query
ECR_IMAGE_TAG ?= latest
ECR_IMAGE_URI := $(ACCOUNT_ID).dkr.ecr.$(AWS_REGION).amazonaws.com/$(ECR_REPOSITORY_NAME):$(ECR_IMAGE_TAG)
LAMBDA_FUNCTION_NAME ?= RAG-API-prod-QueryFunctionBDF4DE5B-fefZmPcq2NrF

# 确保CDK使用正确的区域
export CDK_DEFAULT_REGION := $(AWS_REGION)
export AWS_DEFAULT_REGION := $(AWS_REGION)

# 通用AWS环境变量设置
define SET_AWS_ENV
	AWS_REGION=$(AWS_REGION) \
	AWS_DEFAULT_REGION=$(AWS_REGION) \
	CDK_DEFAULT_REGION=$(AWS_REGION)
endef

# 通用CDK环境变量设置
define SET_CDK_ENV
	$(SET_AWS_ENV) \
	USE_API_V2=$(USE_API_V2) \
	STAGE=$(STAGE)
endef

# 帮助信息
help:
	@echo "AWS RAG Application - 可用命令:"
	@echo ""
	@echo "📦 环境管理:"
	@echo "  make install          - 安装所有依赖"
	@echo "  make clean            - 清理构建产物和缓存"
	@echo ""
	@echo "🐳 容器镜像部署 (推荐):"
	@echo "  make deploy-container     - 构建并部署容器镜像到Lambda（一键部署）"
	@echo "  make build-container      - 构建Docker容器镜像"
	@echo "  make push-container       - 推送镜像到ECR"
	@echo "  make update-lambda        - 快速更新Lambda代码（仅重新构建和部署容器）"
	@echo "  make test-lambda          - 测试Lambda函数"
	@echo "  make logs-lambda          - 查看Lambda日志"
	@echo "  make clean-ecr            - 清理ECR仓库"
	@echo ""
	@echo "⚡ Lambda ZIP部署 (已弃用):"
	@echo "  make redeploy-lambda      - 快速重新部署Lambda（ZIP方式）"
	@echo "  make deploy-lambda-direct - 直接部署Lambda函数（21MB优化版）"
	@echo "  make build-lambda-fixed   - 构建修复版Lambda包"
	@echo "  make update-lambda-env    - 更新Lambda环境变量"
	@echo ""
	@echo "☁️  部署管理:"
	@echo "  make deploy           - 完整部署应用到AWS（自动构建镜像）"
	@echo "  make deploy-quick     - 快速部署（跳过镜像构建如果已存在）"
	@echo "  make deploy-web       - 仅部署Web栈"
	@echo "  make deploy-api       - 仅部署API栈"
	@echo "  make update-frontend  - 仅更新前端配置"
	@echo "  make generate-config  - 生成前端API配置"
	@echo "  make destroy          - 销毁所有资源（智能清理）"
	@echo "  make destroy-force    - 强制销毁所有资源（跳过确认）"
	@echo "  make clean-logs       - 清理CloudWatch日志组"
	@echo "  make clean-all        - 清理所有AWS和本地资源"
	@echo ""
	@echo "🔍 CDK操作:"
	@echo "  make synth            - 合成CloudFormation模板"
	@echo "  make diff             - 查看部署差异"
	@echo "  make bootstrap        - 初始化CDK环境"
	@echo ""
	@echo "🧪 测试命令:"
	@echo "  make test             - 运行所有测试"
	@echo "  make test-api         - 测试API端点"
	@echo "  make test-ui          - 测试UI功能"
	@echo "  make test-lambda      - 测试Lambda函数（新增）"
	@echo ""
	@echo "🔧 修复命令:"
	@echo "  make fix-cors         - 修复CORS问题"
	@echo "  make fix-cloudfront   - 修复CloudFront配置"
	@echo "  make verify-deploy    - 验证部署状态"

# 检查必要工具
check-tools:
	@echo "🔍 检查必要工具..."
	@which aws >/dev/null 2>&1 || { echo "❌ 需要安装 AWS CLI"; exit 1; }
	@which jq >/dev/null 2>&1 || { echo "❌ 需要安装 jq"; exit 1; }
	@which python3 >/dev/null 2>&1 || { echo "❌ 需要安装 Python3"; exit 1; }
	@which npm >/dev/null 2>&1 || { echo "⚠️  建议安装 npm (用于CDK)"; }
	@which docker >/dev/null 2>&1 || { echo "⚠️  建议安装 Docker (用于Lambda构建)"; }
	@echo "✅ 工具检查完成"

# 安装依赖
install: check-tools
	@echo "📦 安装依赖..."
	pip install -r requirements.txt
	pip install -r requirements-dev.txt
	cd infrastructure && pip install -r requirements.txt
	npm install -g aws-cdk
	@echo "✅ 依赖安装完成"

# 清理
clean:
	@echo "🧹 清理构建产物..."
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	rm -rf infrastructure/cdk.out
	rm -rf .pytest_cache
	rm -rf htmlcov
	@echo "✅ 清理完成"

# CDK Bootstrap
bootstrap:
	@echo "🚀 初始化CDK Bootstrap..."
	@echo "  区域: $(AWS_REGION)"
	$(eval ACCOUNT_ID := $(shell aws sts get-caller-identity --query Account --output text))
	@echo "  账号: $(ACCOUNT_ID)"
	@echo ""
	@cd infrastructure && \
		CDK_DEFAULT_REGION=$(AWS_REGION) \
		CDK_DEFAULT_ACCOUNT=$(ACCOUNT_ID) \
		AWS_DEFAULT_REGION=$(AWS_REGION) \
		npx cdk bootstrap aws://$(ACCOUNT_ID)/$(AWS_REGION) \
		--app "echo '{}'" \
		--cloudformation-execution-policies 'arn:aws:iam::aws:policy/AdministratorAccess'
	@echo ""
	@echo "✅ CDK Bootstrap 完成！"
	@echo ""
	@echo "Bootstrap 已创建："
	@echo "  - S3 存储桶：cdk-$(CDK_BOOTSTRAP_QUALIFIER)-assets-*"
	@echo "  - IAM 角色：cdk-$(CDK_BOOTSTRAP_QUALIFIER)-*-role"
	@echo "  - SSM 参数：/cdk-bootstrap/$(CDK_BOOTSTRAP_QUALIFIER)/version"
	@echo ""
	@echo "现在可以运行 'make deploy' 部署应用"

# 合成CloudFormation模板
synth:
	@echo "🔧 合成CloudFormation模板..."
	cd infrastructure && \
		$(SET_CDK_ENV) \
		cdk synth --app "python3 $(CDK_APP)"

# 查看差异
diff:
	@echo "🔍 查看部署差异..."
	cd infrastructure && \
		$(SET_CDK_ENV) \
		cdk diff --app "python3 $(CDK_APP)"

# 构建Lambda ZIP包
build-lambda:
	@echo "📦 构建Lambda ZIP包..."
	@bash scripts/build_lambda_package.sh
	@echo "✅ Lambda ZIP包构建完成"

# CORS Helper在构建时自动从 MVC 位置复制
sync-cors-helper:
	@echo "✅ CORS Helper 已集成到构建流程"

# 快速重新部署Lambda（跳过其他栈）
redeploy-lambda: build-lambda
	@echo "🚀 快速重新部署Lambda函数..."
	cd infrastructure && \
		$(SET_AWS_ENV) \
		cdk deploy RAG-API-$(STAGE) \
		--app "python3 app.py" \
		--require-approval never
	@echo "✅ Lambda重新部署完成！"
	@$(MAKE) update-frontend

# 测试Lambda函数
test-lambda:
	@echo "🧪 测试Lambda函数..."
	@FUNCTION_NAME=$$(aws lambda list-functions --region $(AWS_REGION) \
		--query 'Functions[?contains(FunctionName, `RAG-API-$(STAGE)-QueryFunction`)].[FunctionName]' \
		--output text | head -1); \
	if [ -z "$$FUNCTION_NAME" ]; then \
		echo "❌ 找不到Lambda函数"; \
		exit 1; \
	fi; \
	echo "  函数名: $$FUNCTION_NAME"; \
	echo '{"query":"test Zilliz connection","top_k":5,"use_rag":true}' | base64 > /tmp/payload.txt; \
	aws lambda invoke \
		--function-name $$FUNCTION_NAME \
		--payload file:///tmp/payload.txt \
		--region $(AWS_REGION) \
		/tmp/response.json > /dev/null 2>&1; \
	echo "  响应:"; \
	cat /tmp/response.json | jq '.body' | jq -r . | jq '.sources[0]' | head -10; \
	rm -f /tmp/payload.txt /tmp/response.json

# 构建Lambda包（修复的Linux兼容版本）
build-lambda-fixed:
	@echo "📦 构建Linux兼容的Lambda包..."
	@echo "  强制使用Docker确保Linux兼容性"
	
	# 检查Docker
	@if ! which docker >/dev/null 2>&1; then \
		echo "❌ Docker未安装！请安装Docker:"; \
		echo "  macOS: brew install --cask docker"; \
		echo "  Linux: curl -fsSL https://get.docker.com | sh"; \
		exit 1; \
	fi
	@if ! docker info >/dev/null 2>&1; then \
		echo "❌ Docker daemon未运行！请启动Docker Desktop"; \
		exit 1; \
	fi
	
	# 清理旧的构建目录
	@if [ -d lambda_build_temp ]; then \
		echo "🧹 清理旧的构建目录..."; \
		rm -rf lambda_build_temp; \
	fi
	@mkdir -p lambda_build_temp/query lambda_build_temp/ingest
	
	# 复制handler文件
	@echo "📋 复制Lambda handler文件..."
	@cp app/controllers/lambda_handlers/query_handler_v2.py lambda_build_temp/query/query_handler.py
	@cp app/controllers/lambda_handlers/ingest_handler.py lambda_build_temp/ingest/
	@cp app/controllers/lambda_handlers/cors_helper.py lambda_build_temp/query/ 2>/dev/null || true
	@cp app/controllers/lambda_handlers/cors_helper.py lambda_build_temp/ingest/ 2>/dev/null || true
	
	# 复制app模块
	@echo "📋 复制app模块..."
	@for dir in query ingest; do \
		mkdir -p lambda_build_temp/$$dir/app/models; \
		mkdir -p lambda_build_temp/$$dir/app/controllers; \
		cp -r app/models/*.py lambda_build_temp/$$dir/app/models/ 2>/dev/null || true; \
		touch lambda_build_temp/$$dir/app/__init__.py; \
		touch lambda_build_temp/$$dir/app/models/__init__.py; \
	done
	
	# 使用Docker构建依赖（Linux兼容）
	@echo "🐳 使用Docker构建Linux兼容依赖..."
	@docker run --rm \
		-v $$(pwd):/workspace \
		-w /workspace \
		--platform linux/amd64 \
		python:3.9-slim \
		bash -c "pip install --no-cache-dir \
			'numpy<2.0,>=1.19.0' \
			'pandas<2.0.0' \
			'pymilvus>=2.3.0' \
			'grpcio>=1.48.0' \
			'protobuf>=3.20.0' \
			'boto3>=1.34.0' \
			'python-dotenv>=1.0.0' \
			'pydantic>=2.6.1' \
			'pydantic-settings>=2.2.1' \
			'ujson>=5.0.0' \
			-t lambda_build_temp/query/ --upgrade && \
		pip install --no-cache-dir \
			'numpy<2.0,>=1.19.0' \
			'pandas<2.0.0' \
			'pymilvus>=2.3.0' \
			'grpcio>=1.48.0' \
			'protobuf>=3.20.0' \
			'boto3>=1.34.0' \
			'python-dotenv>=1.0.0' \
			'pydantic>=2.6.1' \
			'pydantic-settings>=2.2.1' \
			'ujson>=5.0.0' \
			-t lambda_build_temp/ingest/ --upgrade"
	
	# 清理不必要的文件
	@echo "🧹 清理不必要的文件..."
	@find lambda_build_temp -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	@find lambda_build_temp -type d -name "*.dist-info" ! -name "pymilvus*" -exec rm -rf {} + 2>/dev/null || true
	@find lambda_build_temp -type f -name "*.pyc" -delete 2>/dev/null || true
	
	# 打包
	@echo "📦 创建ZIP包..."
	@cd lambda_build_temp/query && zip -r ../../zilliz-rag-query.zip . -x "*.pyc" "*__pycache__*" -q
	@cd lambda_build_temp/ingest && zip -r ../../zilliz-rag-ingest.zip . -x "*.pyc" "*__pycache__*" -q
	
	@echo "✅ Lambda包构建完成："
	@ls -lh zilliz-rag-*.zip | awk '{print "  " $$9 ": " $$5}'

# 构建Lambda ZIP包
build-lambda-zip:
	@echo "📦 构建Lambda ZIP包..."
	@bash scripts/build_lambda_package.sh
	@echo "✅ Lambda ZIP包构建完成"

# 直接部署Lambda函数（不通过CDK）
deploy-lambda-direct: build-lambda-fixed
	@echo "🚀 直接部署Lambda函数到AWS..."
	@echo "  区域: $(AWS_REGION)"
	
	# 检查Lambda函数是否存在
	@if aws lambda get-function --function-name rag-query-handler --region $(AWS_REGION) >/dev/null 2>&1; then \
		echo "📦 更新Query Lambda函数..."; \
		aws lambda update-function-code \
			--function-name rag-query-handler \
			--zip-file fileb://zilliz-rag-query.zip \
			--region $(AWS_REGION) \
			--output json | jq '{FunctionName, LastModified, CodeSize}'; \
	else \
		echo "❌ Lambda函数不存在，请先使用CDK部署基础架构"; \
		exit 1; \
	fi
	
	@if aws lambda get-function --function-name rag-ingest-handler --region $(AWS_REGION) >/dev/null 2>&1; then \
		echo "📦 更新Ingest Lambda函数..."; \
		aws lambda update-function-code \
			--function-name rag-ingest-handler \
			--zip-file fileb://zilliz-rag-ingest.zip \
			--region $(AWS_REGION) \
			--output json | jq '{FunctionName, LastModified, CodeSize}'; \
	else \
		echo "❌ Lambda函数不存在，请先使用CDK部署基础架构"; \
		exit 1; \
	fi
	
	# 更新环境变量
	@$(MAKE) update-lambda-env
	
	@echo "✅ Lambda函数部署完成！"

# 更新Lambda环境变量
update-lambda-env:
	@echo "🔧 更新Lambda环境变量..."
	
	# 验证敏感变量存在
	@if [ -z "$(ZILLIZ_TOKEN)" ]; then \
		echo "❌ ZILLIZ_TOKEN 未设置"; \
		exit 1; \
	fi
	
	# 创建环境变量JSON（使用临时文件避免命令行暴露）
	@cat > env-vars-temp.json <<-EOF
	{
	  "Variables": {
	    "S3_BUCKET": "$(S3_BUCKET_DOCUMENTS)",
	    "ZILLIZ_COLLECTION": "$(ZILLIZ_COLLECTION)",
	    "AWS_REGION_NAME": "$(AWS_REGION)",
	    "ZILLIZ_ENDPOINT": "$(ZILLIZ_ENDPOINT)",
	    "ZILLIZ_TOKEN": "$(ZILLIZ_TOKEN)",
	    "BEDROCK_MODEL_ID": "$(BEDROCK_MODEL_ID)",
	    "EMBEDDING_MODEL_ID": "$(EMBEDDING_MODEL_ID)"
	  }
	}
	EOF
	
	# 设置文件权限（仅用户可读）
	@chmod 600 env-vars-temp.json
	
	# 更新Query Lambda环境变量
	@aws lambda update-function-configuration \
		--function-name rag-query-handler \
		--environment file://env-vars-temp.json \
		--region $(AWS_REGION) \
		--output json 2>/dev/null | jq '{FunctionName, State}' || \
		echo "⚠️  Query Lambda配置更新可能失败"
	
	# 更新Ingest Lambda环境变量
	@aws lambda update-function-configuration \
		--function-name rag-ingest-handler \
		--environment file://env-vars-temp.json \
		--region $(AWS_REGION) \
		--output json 2>/dev/null | jq '{FunctionName, State}' || \
		echo "⚠️  Ingest Lambda配置更新可能失败"
	
	# 安全删除临时文件
	@rm -f env-vars-temp.json
	@echo "✅ 环境变量更新完成"

# 查看Lambda函数列表
list-lambda:
	@echo "📋 列出所有Lambda函数..."
	@aws lambda list-functions --region $(AWS_REGION) \
		--query 'Functions[?contains(FunctionName, `RAG-API-$(STAGE)`)].[FunctionName,LastModified,CodeSize]' \
		--output table

# 查看Lambda日志
logs-lambda:
	@echo "📋 查看Lambda日志..."
	@echo "Query Lambda最近日志："
	@if [ "$(OS_TYPE)" = "Darwin" ]; then \
		START_TIME=$$(date -u -v-5M +%s)000; \
	else \
		START_TIME=$$(date -u -d '5 minutes ago' +%s)000; \
	fi; \
	aws logs filter-log-events \
		--log-group-name /aws/lambda/rag-query-handler \
		--start-time $$START_TIME \
		--region $(AWS_REGION) \
		--query 'events[-10:].message' \
		--output text
	@echo ""
	@echo "如需实时日志，运行："
	@echo "  aws logs tail /aws/lambda/rag-query-handler --follow --region $(AWS_REGION)"

# 构建容器镜像
build-container:
	@echo "🐳 构建Docker容器镜像..."
	@echo "  平台: linux/amd64"
	@echo "  镜像标签: $(ECR_IMAGE_TAG)"
	
	# 检查Docker
	@if ! which docker >/dev/null 2>&1; then \
		echo "❌ Docker未安装！请安装Docker:"; \
		echo "  macOS: brew install --cask docker"; \
		echo "  Linux: curl -fsSL https://get.docker.com | sh"; \
		exit 1; \
	fi
	@if ! docker info >/dev/null 2>&1; then \
		echo "❌ Docker daemon未运行！请启动Docker Desktop"; \
		exit 1; \
	fi
	
	# 构建镜像
	@docker buildx build \
		--platform linux/amd64 \
		--provenance=false \
		-t $(ECR_REPOSITORY_NAME):$(ECR_IMAGE_TAG) \
		-f Dockerfile.lambda \
		.
	@echo "✅ Docker镜像构建完成"

# 推送容器镜像到ECR
push-container: build-container
	@echo "📤 推送Docker镜像到ECR..."
	
	# 创建ECR仓库（如果不存在）
	@aws ecr describe-repositories --repository-names $(ECR_REPOSITORY_NAME) --region $(AWS_REGION) >/dev/null 2>&1 || \
		aws ecr create-repository \
			--repository-name $(ECR_REPOSITORY_NAME) \
			--region $(AWS_REGION) \
			--image-scanning-configuration scanOnPush=true \
			--image-tag-mutability MUTABLE
	
	# 登录到ECR
	@aws ecr get-login-password --region $(AWS_REGION) | \
		docker login --username AWS --password-stdin \
		$(ACCOUNT_ID).dkr.ecr.$(AWS_REGION).amazonaws.com
	
	# 标记并推送镜像
	@docker tag $(ECR_REPOSITORY_NAME):$(ECR_IMAGE_TAG) $(ECR_IMAGE_URI)
	@docker push $(ECR_IMAGE_URI)
	@echo "✅ 镜像推送成功: $(ECR_IMAGE_URI)"

# 一键部署容器镜像到Lambda（推荐）
deploy-container: push-container
	@echo "🚀 部署容器镜像到Lambda..."
	
	# 检查Lambda函数是否存在
	@if aws lambda get-function --function-name $(LAMBDA_FUNCTION_NAME) --region $(AWS_REGION) >/dev/null 2>&1; then \
		echo "📦 更新Lambda函数镜像..."; \
		aws lambda update-function-code \
			--function-name $(LAMBDA_FUNCTION_NAME) \
			--image-uri $(ECR_IMAGE_URI) \
			--region $(AWS_REGION) \
			--output json | jq '{FunctionName, LastUpdateStatus, State}'; \
		echo "⏳ 等待Lambda更新完成..."; \
		aws lambda wait function-updated \
			--function-name $(LAMBDA_FUNCTION_NAME) \
			--region $(AWS_REGION); \
		echo "✅ Lambda函数更新完成！"; \
	else \
		echo "❌ Lambda函数不存在: $(LAMBDA_FUNCTION_NAME)"; \
		echo "请先运行 'make deploy' 创建基础架构"; \
		exit 1; \
	fi
	
	# 测试API
	@echo "🧪 测试API健康检查..."
	@curl -s https://9j0pdvhnya.execute-api.us-east-1.amazonaws.com/prod/health | python3 -m json.tool || true
	@echo ""
	@echo "✅ 容器镜像部署完成！"
	@echo "  镜像URI: $(ECR_IMAGE_URI)"
	@echo "  Lambda函数: $(LAMBDA_FUNCTION_NAME)"

# 清理ECR仓库
clean-ecr:
	@echo "🧹 清理ECR仓库..."
	@read -p "确定要删除ECR仓库 $(ECR_REPOSITORY_NAME) 吗？(y/N) " confirm && \
	if [ "$$confirm" = "y" ]; then \
		aws ecr delete-repository \
			--repository-name $(ECR_REPOSITORY_NAME) \
			--region $(AWS_REGION) \
			--force && \
		echo "✅ ECR仓库已删除"; \
	else \
		echo "取消删除"; \
	fi

# 快速更新Lambda（仅重新构建和部署容器）
update-lambda: deploy-container
	@echo "✅ Lambda函数快速更新完成！"

# 检查ECR镜像是否存在
check-ecr-image:
	@aws ecr describe-images \
		--repository-name $(ECR_REPOSITORY_NAME) \
		--image-ids imageTag=$(ECR_IMAGE_TAG) \
		--region $(AWS_REGION) >/dev/null 2>&1 && echo "true" || echo "false"

# 快速部署（跳过镜像构建如果已存在）
deploy-quick: check-env
	@echo "🚀 快速部署RAG应用..."
	@echo "  检查ECR镜像是否存在..."
	
	@if [ "$$($(MAKE) -s check-ecr-image)" = "false" ]; then \
		echo "  ❌ 镜像不存在，需要构建"; \
		$(MAKE) build-container; \
		$(MAKE) push-container; \
	else \
		echo "  ✅ 镜像已存在，跳过构建"; \
	fi
	
	# 部署CDK栈
	@echo ""
	@echo "☁️  部署CDK栈..."
	cd infrastructure && \
		AWS_REGION=$(AWS_REGION) \
		AWS_DEFAULT_REGION=$(AWS_REGION) \
		CDK_DEFAULT_REGION=$(AWS_REGION) \
		USE_API_V2=$(USE_API_V2) \
		BEDROCK_MODEL_ID=$(BEDROCK_MODEL_ID) \
		EMBEDDING_MODEL_ID=$(EMBEDDING_MODEL_ID) \
		ZILLIZ_ENDPOINT=$(ZILLIZ_ENDPOINT) \
		ZILLIZ_TOKEN=$(ZILLIZ_TOKEN) \
		ZILLIZ_COLLECTION=$(ZILLIZ_COLLECTION) \
		cdk deploy --all \
		--app "python3 $(CDK_APP)" \
		--context stage=$(STAGE) \
		--require-approval never
	
	@$(MAKE) generate-config
	@$(MAKE) update-frontend
	
	@echo ""
	@echo "✅ 快速部署完成！"

# 完整部署（使用容器镜像）
deploy: check-env
	@echo "🚀 部署RAG应用（容器镜像版本）..."
	@echo "  使用API V2: $(USE_API_V2)"
	@echo "  阶段: $(STAGE)"
	@echo "  区域: $(AWS_REGION)"
	@echo "  部署方式: Docker容器镜像"
	
	# 先构建并推送容器镜像到ECR（确保镜像存在）
	@echo ""
	@echo "📦 步骤1: 构建并推送容器镜像..."
	@$(MAKE) build-container
	@$(MAKE) push-container
	
	# 部署CDK栈
	@echo ""
	@echo "☁️  步骤2: 部署CDK栈..."
	cd infrastructure && \
		AWS_REGION=$(AWS_REGION) \
		AWS_DEFAULT_REGION=$(AWS_REGION) \
		CDK_DEFAULT_REGION=$(AWS_REGION) \
		USE_API_V2=$(USE_API_V2) \
		BEDROCK_MODEL_ID=$(BEDROCK_MODEL_ID) \
		EMBEDDING_MODEL_ID=$(EMBEDDING_MODEL_ID) \
		ZILLIZ_ENDPOINT=$(ZILLIZ_ENDPOINT) \
		ZILLIZ_TOKEN=$(ZILLIZ_TOKEN) \
		ZILLIZ_COLLECTION=$(ZILLIZ_COLLECTION) \
		cdk deploy --all \
		--app "python3 $(CDK_APP)" \
		--context stage=$(STAGE) \
		--require-approval never
	
	# 更新Lambda函数为最新镜像
	@echo ""
	@echo "🔄 步骤3: 更新Lambda函数..."
	@$(MAKE) deploy-container
	
	# 生成前端配置
	@echo ""
	@echo "⚙️  步骤4: 生成前端配置..."
	@$(MAKE) generate-config
	
	# 更新前端
	@echo ""
	@echo "🌐 步骤5: 更新前端..."
	@$(MAKE) update-frontend
	
	@echo ""
	@echo "✅ 部署完成！"
	@echo "📌 访问应用: $$(aws cloudformation describe-stacks --stack-name RAG-Web-$(STAGE) --query 'Stacks[0].Outputs[?OutputKey==`CloudFrontURL`].OutputValue' --output text 2>/dev/null || echo '正在获取URL...')"

# 仅部署数据栈
deploy-data:
	@echo "🗄️ 部署数据栈..."
	cd infrastructure && \
		$(SET_CDK_ENV) \
		cdk deploy RAG-Data-$(STAGE) \
		--app "python3 $(CDK_APP)" \
		--context stage=$(STAGE) \
		--require-approval never

# 仅部署API栈
deploy-api:
	@echo "⚡ 部署API栈..."
	cd infrastructure && \
		$(SET_CDK_ENV) \
		cdk deploy RAG-API-$(STAGE) \
		--app "python3 $(CDK_APP)" \
		--context stage=$(STAGE) \
		--require-approval never
	
	# 生成新的前端配置
	@$(MAKE) generate-config

# 仅部署Web栈
deploy-web:
	@echo "🌐 部署Web栈..."
	cd infrastructure && \
		$(SET_CDK_ENV) \
		cdk deploy RAG-Web-$(STAGE) \
		--app "python3 $(CDK_APP)" \
		--context stage=$(STAGE) \
		--require-approval never

# 生成前端配置
generate-config:
	@echo "⚙️ 生成前端API配置..."
	@echo "  使用 RAG-API-$(STAGE) 栈"
	export CDK_STACK_NAME=RAG-API-$(STAGE) && \
	STAGE=$(STAGE) python3 scripts/generate_frontend_config.py

# 通用前端更新函数
_update_frontend_common:
	@echo "📤 更新前端文件到S3..."
	$(eval BUCKET_NAME := $(shell aws cloudformation describe-stacks \
		--stack-name RAG-Web-$(STAGE) \
		--query 'Stacks[0].Outputs[?OutputKey==`S3BucketName`].OutputValue' \
		--output text 2>/dev/null || echo "$(S3_BUCKET_WEB)"))
	
	@if [ -n "$(BUCKET_NAME)" ] && [ -d app/views/web ]; then \
		echo "📦 同步文件到S3: $(BUCKET_NAME)"; \
		aws s3 sync app/views/web/ s3://$(BUCKET_NAME)/ \
			--exclude "*.backup*" \
			--exclude ".git/*" \
			--exclude "*.DS_Store" \
			--cache-control "max-age=3600"; \
		echo "🔄 清除CloudFront缓存..."; \
		DISTRIBUTION_ID=$$(aws cloudformation describe-stacks \
			--stack-name RAG-Web-$(STAGE) \
			--query 'Stacks[0].Outputs[?OutputKey==`CloudFrontDistributionId`].OutputValue' \
			--output text 2>/dev/null); \
		if [ -n "$$DISTRIBUTION_ID" ]; then \
			aws cloudfront create-invalidation \
				--distribution-id $$DISTRIBUTION_ID \
				--paths "/*" > /dev/null; \
			echo "✅ CloudFront 缓存已清除"; \
		else \
			echo "⚠️  未找到 CloudFront Distribution ID"; \
		fi; \
		echo "✅ 前端更新完成"; \
	else \
		echo "❌ 无法更新前端：S3桶或前端目录不存在"; \
	fi

# 更新前端文件
update-frontend: generate-config _update_frontend_common

# 修复CORS问题
fix-cors:
	@echo "🔧 修复CORS配置..."
	@$(MAKE) deploy-api
	@$(MAKE) update-frontend
	@echo "✅ CORS修复完成"

# 修复CloudFront
fix-cloudfront:
	@echo "🔧 修复CloudFront配置..."
	# 重新生成前端配置
	@$(MAKE) generate-config
	# 更新前端文件
	@$(MAKE) update-frontend
	# 验证配置
	@echo "📋 验证配置..."
	@if [ -f app/views/web/config.json ]; then \
		echo "✅ config.json已生成"; \
		cat app/views/web/config.json | head -5; \
	fi
	@echo "✅ CloudFront修复完成"

# 验证部署
verify-deploy:
	@echo "🔍 验证部署状态..."
	
	# 检查栈状态
	@echo "\n📊 栈状态:"
	@aws cloudformation list-stacks \
		--stack-status-filter CREATE_COMPLETE UPDATE_COMPLETE \
		--query "StackSummaries[?contains(StackName, 'RAG-')].{Name:StackName,Status:StackStatus}" \
		--output table
	
	# 获取端点
	@echo "\n🔗 端点:"
	@echo "  API: $$(aws cloudformation describe-stacks --stack-name RAG-API-$(STAGE) --query 'Stacks[0].Outputs[?OutputKey==`ApiUrl`].OutputValue' --output text)"
	@echo "  Web: $$(aws cloudformation describe-stacks --stack-name RAG-Web-$(STAGE) --query 'Stacks[0].Outputs[?OutputKey==`CloudFrontURL`].OutputValue' --output text)"
	
	# 测试健康检查
	@echo "\n💓 健康检查:"
	$(eval API_URL := $(shell aws cloudformation describe-stacks --stack-name RAG-API-$(STAGE) --query 'Stacks[0].Outputs[?OutputKey==`ApiUrl`].OutputValue' --output text))
	@curl -s $(API_URL)health | python -m json.tool || echo "  ⚠️ API健康检查失败"

# 测试API
test-api:
	@echo "🧪 测试API端点..."
	$(eval API_URL := $(shell aws cloudformation describe-stacks --stack-name RAG-API-$(STAGE) --query 'Stacks[0].Outputs[?OutputKey==`ApiUrl`].OutputValue' --output text))
	
	@echo "测试健康检查..."
	@curl -X GET $(API_URL)health
	
	@echo "\n测试查询端点..."
	@curl -X POST $(API_URL)query \
		-H "Content-Type: application/json" \
		-d '{"query": "测试查询", "top_k": 5}'

# 测试UI
test-ui:
	@echo "🧪 测试UI功能..."
	python3 tests/test_ui_functionality.py

# 销毁资源 - 增强版本，确保完全清理
destroy:
	@echo "💥 销毁所有AWS资源..."
	@read -p "确定要销毁所有资源吗？(y/N) " confirm && \
	if [ "$$confirm" = "y" ]; then \
		echo ""; \
		echo "📋 开始清理AWS资源..."; \
		echo "======================="; \
		echo ""; \
		echo "1️⃣ 清理S3存储桶内容..." && \
		for bucket in $$(aws s3api list-buckets --query "Buckets[?contains(Name, 'rag-')].Name" --output text); do \
			echo "  清空S3桶: $$bucket" && \
			aws s3api put-bucket-versioning --bucket $$bucket --versioning-configuration Status=Suspended 2>/dev/null || true && \
			aws s3api delete-objects --bucket $$bucket \
				--delete "$$(aws s3api list-object-versions --bucket $$bucket --output json \
				--query '{Objects: Versions[].{Key:Key,VersionId:VersionId}}')" 2>/dev/null || true && \
			aws s3 rm s3://$$bucket --recursive 2>/dev/null || true && \
			aws s3api delete-bucket --bucket $$bucket --region $(AWS_REGION) 2>/dev/null || true; \
		done; \
		echo "  ✅ S3清理完成"; \
		echo ""; \
		echo "2️⃣ 清理ECR仓库..." && \
		for repo in $$(aws ecr describe-repositories --query "repositories[?contains(repositoryName, 'rag-')].repositoryName" --output text 2>/dev/null); do \
			echo "  删除ECR仓库: $$repo" && \
			aws ecr delete-repository --repository-name $$repo --region $(AWS_REGION) --force 2>/dev/null || true; \
		done; \
		echo "  ✅ ECR清理完成"; \
		echo ""; \
		echo "3️⃣ 删除CloudFormation栈（按照正确顺序）..." && \
		echo "  处理删除失败的栈..." && \
		for stack in $$(aws cloudformation list-stacks \
			--stack-status-filter DELETE_FAILED \
			--query "StackSummaries[?contains(StackName, 'RAG-')].StackName" \
			--output text --region $(AWS_REGION)); do \
			echo "    重试删除失败的栈: $$stack" && \
			aws cloudformation delete-stack --stack-name $$stack --region $(AWS_REGION) 2>/dev/null || true; \
		done; \
		echo "  删除Web栈..." && \
		aws cloudformation delete-stack --stack-name RAG-Web-$(STAGE) --region $(AWS_REGION) 2>/dev/null || true && \
		echo "  删除API栈..." && \
		aws cloudformation delete-stack --stack-name RAG-API-$(STAGE) --region $(AWS_REGION) 2>/dev/null || true && \
		echo "  删除Data栈..." && \
		aws cloudformation delete-stack --stack-name RAG-Data-$(STAGE) --region $(AWS_REGION) 2>/dev/null || true && \
		echo "  ⏳ 等待栈删除完成..." && \
		for i in $$(seq 1 24); do \
			remaining=$$(aws cloudformation list-stacks \
				--stack-status-filter DELETE_IN_PROGRESS DELETE_FAILED \
				--query "StackSummaries[?contains(StackName, 'RAG-')].StackName" \
				--output text --region $(AWS_REGION) 2>/dev/null | wc -w); \
			if [ "$$remaining" -eq 0 ]; then \
				echo "  ✅ CloudFormation栈清理完成"; \
				break; \
			else \
				echo "  ⏳ 还有 $$remaining 个栈正在处理，等待10秒... ($$i/24)" && \
				sleep 10; \
			fi; \
		done; \
		echo ""; \
		echo "4️⃣ 清理CloudWatch日志组..." && \
		for log_group in $$(aws logs describe-log-groups \
			--query "logGroups[?contains(logGroupName, 'RAG-') || contains(logGroupName, 'rag-')].logGroupName" \
			--output text --region $(AWS_REGION)); do \
			echo "  删除日志组: $$log_group" && \
			aws logs delete-log-group --log-group-name "$$log_group" --region $(AWS_REGION) 2>/dev/null || true; \
		done; \
		echo "  ✅ CloudWatch日志组清理完成"; \
		echo ""; \
		echo "5️⃣ 使用CDK destroy作为备份清理..." && \
		cd infrastructure && \
		$(SET_AWS_ENV) \
		cdk destroy --all --app "python3 $(CDK_APP)" --force 2>/dev/null || true && \
		cd .. && \
		echo "  ✅ CDK清理完成"; \
		echo ""; \
		echo "6️⃣ 清理本地资源..." && \
		docker rmi $(ECR_REPOSITORY_NAME):$(ECR_IMAGE_TAG) 2>/dev/null || true && \
		docker rmi $(ECR_IMAGE_URI) 2>/dev/null || true && \
		rm -rf lambda_build_temp && \
		rm -rf zilliz-rag-*.zip && \
		rm -rf infrastructure/cdk.out && \
		echo "  ✅ 本地资源清理完成"; \
		echo ""; \
		echo "======================="; \
		echo "✅ 🎉 所有资源清理完成！"; \
		echo ""; \
		read -p "是否要清理CDK Bootstrap资源？(y/N) " confirm_bootstrap && \
		if [ "$$confirm_bootstrap" = "y" ]; then \
			echo "7️⃣ 清理CDK Bootstrap资源..." && \
			for bucket in $$(aws s3api list-buckets --query "Buckets[?contains(Name, 'cdk-')].Name" --output text); do \
				echo "  清空CDK Bootstrap S3桶: $$bucket" && \
				aws s3 rm s3://$$bucket --recursive 2>/dev/null || true && \
				aws s3api delete-bucket --bucket $$bucket --region $(AWS_REGION) 2>/dev/null || true; \
			done && \
			aws cloudformation delete-stack --stack-name CDKToolkit --region $(AWS_REGION) 2>/dev/null || true && \
			echo "  ✅ CDK Bootstrap清理完成"; \
		fi; \
	else \
		echo "❌ 取消销毁操作"; \
	fi

# 检查环境变量
check-env:
	@echo "🔍 检查环境配置..."
	@if [ -z "$(AWS_REGION)" ]; then \
		echo "❌ AWS_REGION未设置"; \
		exit 1; \
	fi
	@if [ -f .env ]; then \
		chmod 600 .env; \
		echo "✅ .env文件权限已设置为600"; \
	fi
	@if [ -z "$(ZILLIZ_TOKEN)" ] || [ -z "$(ZILLIZ_ENDPOINT)" ]; then \
		echo "⚠️  Zilliz配置可能不完整"; \
	fi
	@echo "✅ 环境配置检查完成"

# 一键部署和测试（使用容器镜像）
all: clean install deploy verify-deploy test-api
	@echo "🎉 完整部署和测试完成！"
	@echo "  部署方式: Docker容器镜像"
	@echo "  镜像URI: $(ECR_IMAGE_URI)"

# 清理CloudWatch日志组
clean-logs:
	@echo "🧹 清理CloudWatch日志组..."
	@echo "  正在搜索RAG相关的日志组..."
	@LOG_COUNT=$$(aws logs describe-log-groups \
		--query "logGroups[?contains(logGroupName, 'RAG-') || contains(logGroupName, 'rag-')].logGroupName" \
		--output text --region $(AWS_REGION) 2>/dev/null | wc -w); \
	if [ "$$LOG_COUNT" -gt 0 ]; then \
		echo "  发现 $$LOG_COUNT 个日志组"; \
		read -p "确定要删除这些日志组吗？(y/N) " confirm && \
		if [ "$$confirm" = "y" ]; then \
			for log_group in $$(aws logs describe-log-groups \
				--query "logGroups[?contains(logGroupName, 'RAG-') || contains(logGroupName, 'rag-')].logGroupName" \
				--output text --region $(AWS_REGION)); do \
				echo "  删除: $$log_group" && \
				aws logs delete-log-group --log-group-name "$$log_group" --region $(AWS_REGION) 2>/dev/null || true; \
			done; \
			echo "✅ CloudWatch日志组清理完成"; \
		else \
			echo "❌ 取消清理操作"; \
		fi; \
	else \
		echo "  没有发现需要清理的日志组"; \
	fi

# 强制销毁（跳过确认）
destroy-force:
	@echo "💥 强制销毁所有AWS资源（无需确认）..."
	@echo ""; \
	echo "📋 开始强制清理AWS资源..."; \
	echo "======================="; \
	echo ""; \
	echo "1️⃣ 清理S3存储桶..." && \
	for bucket in $$(aws s3api list-buckets --query "Buckets[?contains(Name, 'rag-')].Name" --output text); do \
		echo "  强制清空S3桶: $$bucket" && \
		aws s3api put-bucket-versioning --bucket $$bucket --versioning-configuration Status=Suspended 2>/dev/null || true && \
		aws s3 rm s3://$$bucket --recursive --force 2>/dev/null || true && \
		aws s3api delete-bucket --bucket $$bucket --region $(AWS_REGION) 2>/dev/null || true; \
	done; \
	echo "  ✅ S3清理完成"; \
	echo ""; \
	echo "2️⃣ 清理ECR仓库..." && \
	for repo in $$(aws ecr describe-repositories --query "repositories[?contains(repositoryName, 'rag-')].repositoryName" --output text 2>/dev/null); do \
		echo "  删除ECR仓库: $$repo" && \
		aws ecr delete-repository --repository-name $$repo --region $(AWS_REGION) --force 2>/dev/null || true; \
	done; \
	echo "  ✅ ECR清理完成"; \
	echo ""; \
	echo "3️⃣ 处理删除失败的栈（跳过资源保留）..." && \
	for stack in $$(aws cloudformation list-stacks \
		--stack-status-filter DELETE_FAILED \
		--query "StackSummaries[?contains(StackName, 'RAG-')].StackName" \
		--output text --region $(AWS_REGION)); do \
		echo "  处理删除失败的栈: $$stack" && \
		echo "  获取失败的资源..." && \
		FAILED_RESOURCES=$$(aws cloudformation list-stack-resources \
			--stack-name $$stack \
			--query "StackResourceSummaries[?ResourceStatus=='DELETE_FAILED'].LogicalResourceId" \
			--output text --region $(AWS_REGION) 2>/dev/null) && \
		if [ -n "$$FAILED_RESOURCES" ]; then \
			echo "  跳过失败的资源并删除栈..." && \
			aws cloudformation delete-stack \
				--stack-name $$stack \
				--retain-resources $$FAILED_RESOURCES \
				--region $(AWS_REGION) 2>/dev/null || \
			aws cloudformation delete-stack \
				--stack-name $$stack \
				--region $(AWS_REGION) 2>/dev/null || true; \
		else \
			aws cloudformation delete-stack --stack-name $$stack --region $(AWS_REGION) 2>/dev/null || true; \
		fi; \
	done; \
	echo "  删除所有栈..." && \
	for stack in $$(aws cloudformation list-stacks \
		--stack-status-filter CREATE_COMPLETE UPDATE_COMPLETE \
		--query "StackSummaries[?contains(StackName, 'RAG-')].StackName" \
		--output text --region $(AWS_REGION)); do \
		echo "  强制删除栈: $$stack" && \
		aws cloudformation delete-stack --stack-name $$stack --region $(AWS_REGION) 2>/dev/null || true; \
	done; \
	echo "  ⏳ 等待栈删除..." && \
	for i in $$(seq 1 12); do \
		remaining=$$(aws cloudformation list-stacks \
			--stack-status-filter DELETE_IN_PROGRESS DELETE_FAILED \
			--query "StackSummaries[?contains(StackName, 'RAG-')].StackName" \
			--output text --region $(AWS_REGION) 2>/dev/null | wc -w); \
		if [ "$$remaining" -eq 0 ]; then \
			echo "  ✅ CloudFormation栈清理完成"; \
			break; \
		else \
			echo "  ⏳ 还有 $$remaining 个栈正在处理... ($$i/12)" && \
			sleep 10; \
		fi; \
	done; \
	echo ""; \
	echo "4️⃣ 清理CloudWatch日志组..." && \
	for log_group in $$(aws logs describe-log-groups \
		--query "logGroups[?contains(logGroupName, 'RAG-') || contains(logGroupName, 'rag-')].logGroupName" \
		--output text --region $(AWS_REGION)); do \
		aws logs delete-log-group --log-group-name "$$log_group" --region $(AWS_REGION) 2>/dev/null || true; \
	done; \
	echo "  ✅ CloudWatch日志组清理完成"; \
	echo ""; \
	echo "5️⃣ 清理本地资源..." && \
	docker rmi $(ECR_REPOSITORY_NAME):$(ECR_IMAGE_TAG) 2>/dev/null || true && \
	docker rmi $(ECR_IMAGE_URI) 2>/dev/null || true && \
	rm -rf lambda_build_temp && \
	rm -rf zilliz-rag-*.zip && \
	rm -rf infrastructure/cdk.out && \
	echo "  ✅ 本地资源清理完成"; \
	echo ""; \
	echo "======================="; \
	echo "✅ 🎉 强制清理完成！"; \
	echo ""

# 清理所有资源（包括CDK Bootstrap）
clean-all: destroy-force
	@echo "🧹 清理所有资源（包括CDK Bootstrap）..."
	@echo "清理CDK Bootstrap资源..." && \
	for bucket in $$(aws s3api list-buckets --query "Buckets[?contains(Name, 'cdk-')].Name" --output text); do \
		echo "  清空CDK Bootstrap S3桶: $$bucket" && \
		aws s3 rm s3://$$bucket --recursive --force 2>/dev/null || true && \
		aws s3api delete-bucket --bucket $$bucket --region $(AWS_REGION) 2>/dev/null || true; \
	done && \
	aws cloudformation delete-stack --stack-name CDKToolkit --region $(AWS_REGION) 2>/dev/null || true && \
	echo "✅ 所有资源清理完成（包括CDK Bootstrap）"