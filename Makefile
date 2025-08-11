# AWS RAG Application Makefile V2
# 自动化部署，包含所有修复

.PHONY: help install clean deploy destroy test lint synth diff deploy-v2 generate-config update-frontend

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

# 确保CDK使用正确的区域
export CDK_DEFAULT_REGION := $(AWS_REGION)
export AWS_DEFAULT_REGION := $(AWS_REGION)

# 帮助信息
help:
	@echo "AWS RAG Application V2 - 可用命令:"
	@echo ""
	@echo "📦 环境管理:"
	@echo "  make install          - 安装所有依赖"
	@echo "  make clean            - 清理构建产物和缓存"
	@echo ""
	@echo "⚡ Lambda快速部署 (新增):"
	@echo "  make redeploy-lambda      - 快速重新部署Lambda（推荐）"
	@echo "  make test-lambda          - 测试Lambda函数"
	@echo "  make deploy-lambda-direct - 直接部署Lambda函数（21MB优化版）"
	@echo "  make build-lambda-fixed   - 构建修复版Lambda包"
	@echo "  make update-lambda-env    - 更新Lambda环境变量"
	@echo "  make logs-lambda          - 查看Lambda日志"
	@echo ""
	@echo "☁️  部署管理 (推荐):"
	@echo "  make deploy-v2        - 完整部署（使用改进的V2栈）"
	@echo "  make deploy-with-layer - 使用Lambda Layer部署（解决大包问题）"
	@echo "  make update-frontend  - 仅更新前端配置"
	@echo "  make generate-config  - 生成前端API配置"
	@echo ""
	@echo "☁️  部署管理 (传统):"
	@echo "  make deploy           - 部署应用到AWS（原始版本）"
	@echo "  make deploy-web       - 仅部署Web栈"
	@echo "  make deploy-api       - 仅部署API栈"
	@echo "  make destroy          - 销毁所有资源"
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

# 安装依赖
install:
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
	@echo "  - S3 存储桶：cdk-hnb659fds-assets-*"
	@echo "  - IAM 角色：cdk-hnb659fds-*-role"
	@echo "  - SSM 参数：/cdk-bootstrap/hnb659fds/version"
	@echo ""
	@echo "现在可以运行 'make deploy-v2' 部署应用"

# 合成CloudFormation模板
synth:
	@echo "🔧 合成CloudFormation模板..."
	cd infrastructure && \
		AWS_REGION=$(AWS_REGION) \
		AWS_DEFAULT_REGION=$(AWS_REGION) \
		CDK_DEFAULT_REGION=$(AWS_REGION) \
		USE_API_V2=$(USE_API_V2) \
		cdk synth --app "python3 $(CDK_APP)"

# 查看差异
diff:
	@echo "🔍 查看部署差异..."
	cd infrastructure && \
		AWS_REGION=$(AWS_REGION) \
		AWS_DEFAULT_REGION=$(AWS_REGION) \
		CDK_DEFAULT_REGION=$(AWS_REGION) \
		USE_API_V2=$(USE_API_V2) \
		cdk diff --app "python3 $(CDK_APP)"

# 构建Lambda ZIP包（根据USE_LAYER环境变量选择模式）
build-lambda:
	@if [ "$(USE_LAYER)" = "true" ]; then \
		echo "📦 构建Lambda包（Layer模式）..."; \
	else \
		echo "📦 构建Lambda ZIP包（传统模式）..."; \
	fi
	@USE_LAYER=$(USE_LAYER) bash scripts/build_lambda_package.sh
	@if [ "$(USE_LAYER)" = "true" ]; then \
		echo "✅ Lambda Layer包构建完成"; \
	else \
		echo "✅ Lambda ZIP包构建完成"; \
	fi

# CORS Helper在构建时自动从 MVC 位置复制
sync-cors-helper:
	@echo "✅ CORS Helper 已集成到构建流程"

# 快速重新部署Lambda（跳过其他栈）
redeploy-lambda: build-lambda
	@echo "🚀 快速重新部署Lambda函数..."
	cd infrastructure && \
	AWS_REGION=$(AWS_REGION) \
		cdk deploy RAG-API-$(STAGE) \
		--app "python3 app.py" \
		--require-approval never
	@echo "✅ Lambda重新部署完成！"
	@$(MAKE) update-frontend-v2

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

# 构建Lambda包（修复的21MB版本）
build-lambda-fixed:
	@echo "📦 构建修复版Lambda包（21MB优化版）..."
	@echo "  包含pymilvus修复和轻量级stubs"
	@if [ -d lambda_build_temp ]; then \
		echo "清理旧的构建目录..."; \
		rm -rf lambda_build_temp; \
	fi
	@mkdir -p lambda_build_temp/query lambda_build_temp/ingest
	
	# 复制handler文件
	@cp app/controllers/lambda_handlers/query_handler.py lambda_build_temp/query/
	@cp app/controllers/lambda_handlers/ingest_handler.py lambda_build_temp/ingest/
	
	# 使用Docker构建依赖（Linux兼容）
	@echo "🐳 使用Docker构建Linux兼容依赖..."
	@docker run --rm \
		-v $$(pwd):/workspace \
		-w /workspace \
		--platform linux/amd64 \
		python:3.9-slim \
		bash -c "pip install pymilvus grpcio protobuf boto3 python-dotenv -t lambda_build_temp/query/ && \
				pip install pymilvus grpcio protobuf boto3 python-dotenv -t lambda_build_temp/ingest/"
	
	# 复制numpy和pandas stubs
	@cp app/controllers/lambda_handlers/numpy_stub.py lambda_build_temp/query/numpy/__init__.py 2>/dev/null || true
	@cp app/controllers/lambda_handlers/numpy_stub.py lambda_build_temp/ingest/numpy/__init__.py 2>/dev/null || true
	@mkdir -p lambda_build_temp/query/pandas/api lambda_build_temp/ingest/pandas/api
	@cp app/controllers/lambda_handlers/pandas_stub.py lambda_build_temp/query/pandas/__init__.py 2>/dev/null || true
	@cp app/controllers/lambda_handlers/pandas_stub.py lambda_build_temp/ingest/pandas/__init__.py 2>/dev/null || true
	
	# 打包
	@cd lambda_build_temp/query && zip -r ../../zilliz-rag-query.zip . -x "*.pyc" "*__pycache__*" "*.dist-info/*" -q
	@cd lambda_build_temp/ingest && zip -r ../../zilliz-rag-ingest.zip . -x "*.pyc" "*__pycache__*" "*.dist-info/*" -q
	
	@echo "✅ Lambda包构建完成："
	@ls -lh zilliz-rag-*.zip | awk '{print "  " $$9 ": " $$5}'

# 构建Lambda Layer（显式）
build-lambda-layer:
	@echo "📦 构建Lambda Layer包..."
	@USE_LAYER=true bash scripts/build_lambda_package.sh
	@echo "✅ Lambda Layer包构建完成"

# 构建传统Lambda ZIP包（显式）
build-lambda-zip:
	@echo "📦 构建传统Lambda ZIP包..."
	@USE_LAYER=false bash scripts/build_lambda_package.sh
	@echo "✅ Lambda ZIP包构建完成"

# 使用Lambda Layer部署（解决大包问题）
deploy-with-layer:
	@echo "🚀 使用Lambda Layer模式部署..."
	@export USE_LAYER=true && $(MAKE) deploy-v2

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
	
	# 创建环境变量JSON文件
	@echo '{"Variables": {' > env-vars-temp.json
	@echo '  "S3_BUCKET": "rag-documents-375004070918-$(AWS_REGION)",' >> env-vars-temp.json
	@echo '  "ZILLIZ_COLLECTION": "$(ZILLIZ_COLLECTION)",' >> env-vars-temp.json
	@echo '  "AWS_REGION_NAME": "$(AWS_REGION)",' >> env-vars-temp.json
	@echo '  "ZILLIZ_ENDPOINT": "$(ZILLIZ_ENDPOINT)",' >> env-vars-temp.json
	@echo '  "ZILLIZ_TOKEN": "$(ZILLIZ_TOKEN)",' >> env-vars-temp.json
	@echo '  "BEDROCK_MODEL_ID": "$(BEDROCK_MODEL_ID)",' >> env-vars-temp.json
	@echo '  "EMBEDDING_MODEL_ID": "$(EMBEDDING_MODEL_ID)"' >> env-vars-temp.json
	@echo '}}' >> env-vars-temp.json
	
	# 更新Query Lambda环境变量
	@aws lambda update-function-configuration \
		--function-name rag-query-handler \
		--environment file://env-vars-temp.json \
		--region $(AWS_REGION) \
		--output json | jq '{FunctionName, State}' || true
	
	# 更新Ingest Lambda环境变量
	@aws lambda update-function-configuration \
		--function-name rag-ingest-handler \
		--environment file://env-vars-temp.json \
		--region $(AWS_REGION) \
		--output json | jq '{FunctionName, State}' || true
	
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
	@aws logs filter-log-events \
		--log-group-name /aws/lambda/rag-query-handler \
		--start-time $$(date -u -v-5M +%s)000 \
		--region $(AWS_REGION) \
		--query 'events[-10:].message' \
		--output text
	@echo ""
	@echo "如需实时日志，运行："
	@echo "  aws logs tail /aws/lambda/rag-query-handler --follow --region $(AWS_REGION)"

# 完整部署V2（推荐）
deploy-v2: check-env build-lambda
	@echo "🚀 部署RAG应用 V2（包含所有修复）..."
	@echo "  使用API V2: $(USE_API_V2)"
	@echo "  使用Layer模式: $(USE_LAYER)"
	@echo "  阶段: $(STAGE)"
	@echo "  区域: $(AWS_REGION)"
	@echo "  CDK_DEFAULT_REGION: $(CDK_DEFAULT_REGION)"
	
	# 部署所有栈（强制使用.env中的区域配置）
	cd infrastructure && \
		AWS_REGION=$(AWS_REGION) \
		AWS_DEFAULT_REGION=$(AWS_REGION) \
		CDK_DEFAULT_REGION=$(AWS_REGION) \
		USE_API_V2=$(USE_API_V2) \
		USE_LAYER=$(USE_LAYER) \
		BEDROCK_MODEL_ID=$(BEDROCK_MODEL_ID) \
		EMBEDDING_MODEL_ID=$(EMBEDDING_MODEL_ID) \
		ZILLIZ_ENDPOINT=$(ZILLIZ_ENDPOINT) \
		ZILLIZ_TOKEN=$(ZILLIZ_TOKEN) \
		ZILLIZ_COLLECTION=$(ZILLIZ_COLLECTION) \
		cdk deploy --all \
		--app "python3 $(CDK_APP)" \
		--context stage=$(STAGE) \
		--require-approval never
	
	# 生成前端配置
	@$(MAKE) generate-config
	
	# 更新前端
	@$(MAKE) update-frontend
	
	@echo "✅ 部署完成！"
	@echo "📌 访问应用: $$(aws cloudformation describe-stacks --stack-name RAG-Web-$(STAGE) --query 'Stacks[0].Outputs[?OutputKey==`CloudFrontURL`].OutputValue' --output text)"

# 仅部署数据栈
deploy-data:
	@echo "🗄️ 部署数据栈..."
	cd infrastructure && \
		AWS_REGION=$(AWS_REGION) \
		AWS_DEFAULT_REGION=$(AWS_REGION) \
		CDK_DEFAULT_REGION=$(AWS_REGION) \
		USE_API_V2=$(USE_API_V2) \
		cdk deploy RAG-Data-$(STAGE) \
		--app "python3 $(CDK_APP)" \
		--context stage=$(STAGE) \
		--require-approval never

# 仅部署API栈
deploy-api:
	@echo "⚡ 部署API栈 V2..."
	cd infrastructure && \
		AWS_REGION=$(AWS_REGION) \
		AWS_DEFAULT_REGION=$(AWS_REGION) \
		CDK_DEFAULT_REGION=$(AWS_REGION) \
		USE_API_V2=$(USE_API_V2) \
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
		AWS_REGION=$(AWS_REGION) \
		AWS_DEFAULT_REGION=$(AWS_REGION) \
		CDK_DEFAULT_REGION=$(AWS_REGION) \
		USE_API_V2=$(USE_API_V2) \
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

# 更新前端文件（旧版本，保留兼容性）
update-frontend: generate-config
	@echo "📤 更新前端文件到S3..."
	
	# 获取S3桶名称
	$(eval BUCKET_NAME := $(shell aws cloudformation describe-stacks --stack-name RAG-Web-$(STAGE) --query 'Stacks[0].Outputs[?OutputKey==`S3BucketName`].OutputValue' --output text 2>/dev/null || echo ""))
	
	@if [ -z "$(BUCKET_NAME)" ]; then \
		echo "⚠️ 未找到旧栈，尝试新栈..."; \
		$(MAKE) update-frontend-v2; \
	else \
		echo "📦 同步文件到S3: $(BUCKET_NAME)"; \
		aws s3 sync app/views/web/ s3://$(BUCKET_NAME)/ \
			--exclude "*.backup*" \
			--exclude ".git/*" \
			--exclude "*.DS_Store" \
			--cache-control "max-age=3600"; \
		echo "🔄 清除CloudFront缓存..."; \
		DISTRIBUTION_ID=$$(aws cloudformation describe-stacks --stack-name RAG-Web-$(STAGE) --query 'Stacks[0].Outputs[?OutputKey==`CloudFrontDistributionId`].OutputValue' --output text 2>/dev/null || echo ""); \
		if [ -n "$$DISTRIBUTION_ID" ]; then \
			aws cloudfront create-invalidation \
				--distribution-id $$DISTRIBUTION_ID \
				--paths "/*" > /dev/null; \
			echo "✅ CloudFront 缓存已清除"; \
		else \
			echo "⚠️ 未找到 CloudFront Distribution ID，跳过缓存清除"; \
		fi; \
		echo "✅ 前端更新完成"; \
	fi

# 更新前端文件（新版本，用于统一的栈命名）
update-frontend-v2: generate-config
	@echo "📤 更新前端文件到S3..."
	
	# 获取S3桶名称 - 从 Web 栈获取
	$(eval BUCKET_NAME := $(shell aws cloudformation describe-stacks --stack-name RAG-Web-$(STAGE) --query 'Stacks[0].Outputs[?OutputKey==`S3BucketName`].OutputValue' --output text 2>/dev/null || echo ""))
	
	@if [ -z "$(BUCKET_NAME)" ]; then \
		ACCOUNT_ID=$$(aws sts get-caller-identity --query Account --output text); \
		BUCKET_NAME="rag-web-$$ACCOUNT_ID-$(AWS_REGION)"; \
		echo "⚠️ 使用默认桶名: $$BUCKET_NAME"; \
	fi
	
	@if [ -n "$(BUCKET_NAME)" ] && [ -d app/views/web ]; then \
		echo "📦 同步文件到S3: $(BUCKET_NAME)"; \
		aws s3 sync app/views/web/ s3://$(BUCKET_NAME)/ \
			--exclude "*.backup*" \
			--exclude ".git/*" \
			--exclude "*.DS_Store" \
			--cache-control "max-age=3600"; \
		echo "🔄 清除CloudFront缓存..."; \
		DISTRIBUTION_ID=$$(aws cloudformation describe-stacks --stack-name RAG-Web-$(STAGE) --query 'Stacks[0].Outputs[?OutputKey==`CloudFrontDistributionId`].OutputValue' --output text 2>/dev/null || echo ""); \
		if [ -n "$$DISTRIBUTION_ID" ]; then \
			aws cloudfront create-invalidation \
				--distribution-id $$DISTRIBUTION_ID \
				--paths "/*" > /dev/null; \
			echo "✅ CloudFront 缓存已清除"; \
		else \
			echo "⚠️ 未找到 CloudFront Distribution ID"; \
		fi; \
		echo "✅ 前端更新完成 (V2)"; \
	else \
		echo "❌ 无法更新前端：S3桶或前端目录不存在"; \
	fi

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

# 销毁资源
destroy:
	@echo "💥 销毁所有CDK资源..."
	@read -p "确定要销毁所有资源吗？(y/N) " confirm && \
	if [ "$$confirm" = "y" ]; then \
		cd infrastructure && \
		AWS_REGION=$(AWS_REGION) \
		AWS_DEFAULT_REGION=$(AWS_REGION) \
		CDK_DEFAULT_REGION=$(AWS_REGION) \
		cdk destroy --all --app "python3 $(CDK_APP)" --force; \
	else \
		echo "取消销毁"; \
	fi

# 检查环境变量
check-env:
	@echo "🔍 检查环境配置..."
	@if [ -z "$(AWS_REGION)" ]; then \
		echo "❌ AWS_REGION未设置"; \
		exit 1; \
	fi
	@echo "✅ 环境配置正确"

# 传统部署（兼容旧版）
deploy: deploy-v2

# 一键部署和测试
all: clean install deploy-v2 verify-deploy test-api
	@echo "🎉 完整部署和测试完成！"