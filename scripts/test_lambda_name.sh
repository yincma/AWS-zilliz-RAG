#!/bin/bash
# 测试脚本：验证Lambda函数名动态获取

echo "🔍 测试Lambda函数名动态获取..."
echo "================================"

# 设置变量
STAGE=${STAGE:-prod}
AWS_REGION=${AWS_REGION:-us-east-1}

echo "环境配置:"
echo "  STAGE: $STAGE"
echo "  AWS_REGION: $AWS_REGION"
echo ""

# 方法1: 从CloudFormation栈输出获取
echo "方法1: CloudFormation栈输出"
echo "----------------------------"
LAMBDA_NAME_FROM_STACK=$(aws cloudformation describe-stacks \
    --stack-name RAG-API-${STAGE} \
    --query 'Stacks[0].Outputs[?OutputKey==`QueryFunctionName`].OutputValue' \
    --output text --region ${AWS_REGION} 2>/dev/null)

if [ -n "$LAMBDA_NAME_FROM_STACK" ]; then
    echo "✅ 成功获取: $LAMBDA_NAME_FROM_STACK"
else
    echo "❌ 无法从栈输出获取（栈可能未部署或未更新）"
fi
echo ""

# 方法2: 使用模式匹配查找
echo "方法2: 模式匹配查找"
echo "-------------------"
LAMBDA_NAME_FROM_PATTERN=$(aws lambda list-functions --region ${AWS_REGION} \
    --query 'Functions[?contains(FunctionName, `RAG-API-'${STAGE}'-QueryFunction`)].[FunctionName]' \
    --output text 2>/dev/null | head -1)

if [ -n "$LAMBDA_NAME_FROM_PATTERN" ]; then
    echo "✅ 成功获取: $LAMBDA_NAME_FROM_PATTERN"
else
    echo "❌ 未找到匹配的Lambda函数"
fi
echo ""

# 最终决策
echo "最终决策"
echo "--------"
FINAL_LAMBDA_NAME=${LAMBDA_NAME_FROM_STACK:-$LAMBDA_NAME_FROM_PATTERN}

if [ -n "$FINAL_LAMBDA_NAME" ]; then
    echo "✅ 将使用Lambda函数: $FINAL_LAMBDA_NAME"
    
    # 验证函数是否存在
    if aws lambda get-function --function-name $FINAL_LAMBDA_NAME --region ${AWS_REGION} >/dev/null 2>&1; then
        echo "✅ Lambda函数存在且可访问"
    else
        echo "⚠️  Lambda函数名获取成功但函数不可访问"
    fi
else
    echo "❌ 无法获取Lambda函数名"
    echo "   请确保："
    echo "   1. RAG-API-${STAGE} 栈已部署"
    echo "   2. AWS凭证配置正确"
    echo "   3. 区域设置正确: ${AWS_REGION}"
fi

echo ""
echo "================================"
echo "测试完成"