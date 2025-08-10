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
	@echo "☁️  部署管理 (推荐):"
	@echo "  make deploy-v2        - 完整部署（使用改进的V2栈）"
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
		cdk synth --app "python $(CDK_APP)"

# 查看差异
diff:
	@echo "🔍 查看部署差异..."
	cd infrastructure && \
		AWS_REGION=$(AWS_REGION) \
		AWS_DEFAULT_REGION=$(AWS_REGION) \
		CDK_DEFAULT_REGION=$(AWS_REGION) \
		USE_API_V2=$(USE_API_V2) \
		cdk diff --app "python $(CDK_APP)"

# 完整部署V2（推荐）
deploy-v2: check-env
	@echo "🚀 部署RAG应用 V2（包含所有修复）..."
	@echo "  使用API V2: $(USE_API_V2)"
	@echo "  阶段: $(STAGE)"
	@echo "  区域: $(AWS_REGION)"
	@echo "  CDK_DEFAULT_REGION: $(CDK_DEFAULT_REGION)"
	
	# 部署所有栈（强制使用.env中的区域配置）
	cd infrastructure && \
		AWS_REGION=$(AWS_REGION) \
		AWS_DEFAULT_REGION=$(AWS_REGION) \
		CDK_DEFAULT_REGION=$(AWS_REGION) \
		USE_API_V2=$(USE_API_V2) \
		cdk deploy --all \
		--app "python $(CDK_APP)" \
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
		--app "python $(CDK_APP)" \
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
		--app "python $(CDK_APP)" \
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
		--app "python $(CDK_APP)" \
		--context stage=$(STAGE) \
		--require-approval never

# 生成前端配置
generate-config:
	@echo "⚙️ 生成前端API配置..."
	STAGE=$(STAGE) python scripts/generate_frontend_config.py

# 更新前端文件
update-frontend: generate-config
	@echo "📤 更新前端文件到S3..."
	
	# 获取S3桶名称
	$(eval BUCKET_NAME := $(shell aws cloudformation describe-stacks \
		--stack-name RAG-Web-$(STAGE) \
		--query 'Stacks[0].Outputs[?OutputKey==`S3BucketName`].OutputValue' \
		--output text))
	
	# 同步文件到S3
	aws s3 sync app/views/web/ s3://$(BUCKET_NAME)/ \
		--exclude "*.backup*" \
		--exclude ".git/*" \
		--exclude "*.DS_Store" \
		--cache-control "max-age=3600"
	
	# 清除CloudFront缓存
	$(eval DISTRIBUTION_ID := $(shell aws cloudformation describe-stacks \
		--stack-name RAG-Web-$(STAGE) \
		--query 'Stacks[0].Outputs[?OutputKey==`CloudFrontDistributionId`].OutputValue' \
		--output text))
	
	aws cloudfront create-invalidation \
		--distribution-id $(DISTRIBUTION_ID) \
		--paths "/*" > /dev/null
	
	@echo "✅ 前端更新完成"

# 修复CORS问题
fix-cors:
	@echo "🔧 修复CORS配置..."
	@$(MAKE) deploy-api
	@$(MAKE) update-frontend
	@echo "✅ CORS修复完成"

# 修复CloudFront
fix-cloudfront:
	@echo "🔧 修复CloudFront配置..."
	@$(MAKE) deploy-web
	@$(MAKE) update-frontend
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
	python tests/test_ui_functionality.py

# 销毁资源
destroy:
	@echo "💥 销毁所有CDK资源..."
	@read -p "确定要销毁所有资源吗？(y/N) " confirm && \
	if [ "$$confirm" = "y" ]; then \
		cd infrastructure && \
		AWS_REGION=$(AWS_REGION) \
		AWS_DEFAULT_REGION=$(AWS_REGION) \
		CDK_DEFAULT_REGION=$(AWS_REGION) \
		cdk destroy --all --app "python $(CDK_APP)" --force; \
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