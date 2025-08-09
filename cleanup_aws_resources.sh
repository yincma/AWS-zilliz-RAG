#!/bin/bash

# AWS Resources Cleanup Script
# This script thoroughly cleans up all AWS resources created by the RAG application

set -e

echo "🧹 AWS Resources Complete Cleanup Script"
echo "========================================"
echo ""

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Get AWS account ID and region
ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
AWS_REGION=${AWS_REGION:-us-east-1}

echo "📍 AWS Account: $ACCOUNT_ID"
echo "📍 AWS Region: $AWS_REGION"
echo ""

# Confirmation
echo -e "${YELLOW}⚠️  WARNING: This will delete ALL resources related to the RAG application${NC}"
echo "This includes:"
echo "  - CloudFormation stacks"
echo "  - S3 buckets and their contents"
echo "  - Lambda functions"
echo "  - API Gateway"
echo "  - CloudFront distributions"
echo "  - IAM roles and policies"
echo ""
read -p "Are you sure you want to continue? Type 'yes' to confirm: " confirmation

if [ "$confirmation" != "yes" ]; then
    echo "Cleanup cancelled."
    exit 0
fi

echo ""
echo "Starting cleanup process..."
echo ""

# Function to delete S3 bucket with all contents
delete_s3_bucket() {
    local bucket=$1
    echo "  Deleting S3 bucket: $bucket"
    
    # First, delete all objects including versions
    aws s3api list-object-versions --bucket "$bucket" --output json 2>/dev/null | \
    jq -r '.Versions[] | "--key \"\(.Key)\" --version-id \(.VersionId)"' | \
    while read -r line; do
        eval "aws s3api delete-object --bucket \"$bucket\" $line" 2>/dev/null || true
    done
    
    # Delete all delete markers
    aws s3api list-object-versions --bucket "$bucket" --output json 2>/dev/null | \
    jq -r '.DeleteMarkers[] | "--key \"\(.Key)\" --version-id \(.VersionId)"' | \
    while read -r line; do
        eval "aws s3api delete-object --bucket \"$bucket\" $line" 2>/dev/null || true
    done
    
    # Empty the bucket (for any remaining objects)
    aws s3 rm "s3://$bucket" --recursive 2>/dev/null || true
    
    # Delete the bucket
    aws s3api delete-bucket --bucket "$bucket" 2>/dev/null || true
    
    echo -e "    ${GREEN}✓${NC} Bucket $bucket deleted"
}

# Step 1: Delete CloudFormation Stacks
echo "1️⃣  Deleting CloudFormation Stacks..."
echo "-----------------------------------"

# List all stacks with RAG prefix
STACKS=$(aws cloudformation list-stacks \
    --stack-status-filter CREATE_COMPLETE UPDATE_COMPLETE ROLLBACK_COMPLETE UPDATE_ROLLBACK_COMPLETE \
    --query "StackSummaries[?contains(StackName, 'RAG') || contains(StackName, 'rag')].StackName" \
    --output text)

if [ -n "$STACKS" ]; then
    for stack in $STACKS; do
        echo "  Deleting stack: $stack"
        aws cloudformation delete-stack --stack-name "$stack" 2>/dev/null || true
        
        # Wait for stack deletion
        echo "  Waiting for stack deletion..."
        aws cloudformation wait stack-delete-complete --stack-name "$stack" 2>/dev/null || true
        echo -e "    ${GREEN}✓${NC} Stack $stack deleted"
    done
else
    echo "  No RAG stacks found"
fi
echo ""

# Step 2: Delete S3 Buckets
echo "2️⃣  Deleting S3 Buckets..."
echo "------------------------"

# Find and delete RAG-related buckets
BUCKETS=$(aws s3 ls | awk '{print $3}' | grep -E "(rag|RAG|cdk-.*-assets-$ACCOUNT_ID)" || true)

if [ -n "$BUCKETS" ]; then
    for bucket in $BUCKETS; do
        delete_s3_bucket "$bucket"
    done
else
    echo "  No RAG buckets found"
fi
echo ""

# Step 3: Delete Lambda Functions
echo "3️⃣  Deleting Lambda Functions..."
echo "------------------------------"

# Find and delete RAG-related Lambda functions
FUNCTIONS=$(aws lambda list-functions \
    --query "Functions[?contains(FunctionName, 'rag') || contains(FunctionName, 'RAG')].FunctionName" \
    --output text)

if [ -n "$FUNCTIONS" ]; then
    for func in $FUNCTIONS; do
        echo "  Deleting function: $func"
        aws lambda delete-function --function-name "$func" 2>/dev/null || true
        echo -e "    ${GREEN}✓${NC} Function $func deleted"
    done
else
    echo "  No RAG Lambda functions found"
fi
echo ""

# Step 4: Delete API Gateway APIs
echo "4️⃣  Deleting API Gateway APIs..."
echo "------------------------------"

# REST APIs
REST_APIS=$(aws apigateway get-rest-apis \
    --query "items[?contains(name, 'rag') || contains(name, 'RAG')].id" \
    --output text 2>/dev/null || true)

if [ -n "$REST_APIS" ]; then
    for api in $REST_APIS; do
        echo "  Deleting REST API: $api"
        aws apigateway delete-rest-api --rest-api-id "$api" 2>/dev/null || true
        echo -e "    ${GREEN}✓${NC} REST API $api deleted"
    done
fi

# HTTP APIs
HTTP_APIS=$(aws apigatewayv2 get-apis \
    --query "Items[?contains(Name, 'rag') || contains(Name, 'RAG')].ApiId" \
    --output text 2>/dev/null || true)

if [ -n "$HTTP_APIS" ]; then
    for api in $HTTP_APIS; do
        echo "  Deleting HTTP API: $api"
        aws apigatewayv2 delete-api --api-id "$api" 2>/dev/null || true
        echo -e "    ${GREEN}✓${NC} HTTP API $api deleted"
    done
else
    echo "  No RAG APIs found"
fi
echo ""

# Step 5: Delete CloudFront Distributions
echo "5️⃣  Deleting CloudFront Distributions..."
echo "--------------------------------------"

DISTRIBUTIONS=$(aws cloudfront list-distributions \
    --query "DistributionList.Items[?contains(Comment, 'RAG') || contains(Comment, 'rag')].Id" \
    --output text 2>/dev/null || true)

if [ -n "$DISTRIBUTIONS" ]; then
    for dist in $DISTRIBUTIONS; do
        echo "  Disabling distribution: $dist"
        
        # Get the distribution config
        ETAG=$(aws cloudfront get-distribution-config --id "$dist" --query "ETag" --output text)
        aws cloudfront get-distribution-config --id "$dist" --query "DistributionConfig" > /tmp/dist-config.json
        
        # Disable the distribution
        jq '.Enabled = false' /tmp/dist-config.json > /tmp/dist-config-disabled.json
        aws cloudfront update-distribution --id "$dist" --distribution-config file:///tmp/dist-config-disabled.json --if-match "$ETAG" 2>/dev/null || true
        
        echo "  Waiting for distribution to be disabled..."
        aws cloudfront wait distribution-deployed --id "$dist" 2>/dev/null || true
        
        # Delete the distribution
        ETAG=$(aws cloudfront get-distribution-config --id "$dist" --query "ETag" --output text)
        aws cloudfront delete-distribution --id "$dist" --if-match "$ETAG" 2>/dev/null || true
        echo -e "    ${GREEN}✓${NC} Distribution $dist deleted"
    done
else
    echo "  No RAG CloudFront distributions found"
fi
echo ""

# Step 6: Delete IAM Roles and Policies
echo "6️⃣  Cleaning IAM Roles and Policies..."
echo "------------------------------------"

# Find and delete RAG-related IAM roles
ROLES=$(aws iam list-roles \
    --query "Roles[?contains(RoleName, 'rag') || contains(RoleName, 'RAG')].RoleName" \
    --output text)

if [ -n "$ROLES" ]; then
    for role in $ROLES; do
        echo "  Processing role: $role"
        
        # Detach managed policies
        POLICIES=$(aws iam list-attached-role-policies --role-name "$role" \
            --query "AttachedPolicies[*].PolicyArn" --output text)
        
        for policy in $POLICIES; do
            aws iam detach-role-policy --role-name "$role" --policy-arn "$policy" 2>/dev/null || true
        done
        
        # Delete inline policies
        INLINE_POLICIES=$(aws iam list-role-policies --role-name "$role" \
            --query "PolicyNames[]" --output text)
        
        for policy in $INLINE_POLICIES; do
            aws iam delete-role-policy --role-name "$role" --policy-name "$policy" 2>/dev/null || true
        done
        
        # Delete the role
        aws iam delete-role --role-name "$role" 2>/dev/null || true
        echo -e "    ${GREEN}✓${NC} Role $role deleted"
    done
else
    echo "  No RAG IAM roles found"
fi
echo ""

# Step 7: Delete CDK Bootstrap Stack (optional)
echo "7️⃣  CDK Bootstrap Stack..."
echo "------------------------"
echo "CDKToolkit stack found. This is the CDK bootstrap stack."
read -p "Do you want to delete the CDK bootstrap stack? (y/n): " delete_cdk

if [ "$delete_cdk" = "y" ]; then
    echo "  Deleting CDKToolkit stack..."
    
    # First empty the CDK bucket
    CDK_BUCKET=$(aws cloudformation describe-stacks --stack-name CDKToolkit \
        --query "Stacks[0].Outputs[?OutputKey=='BucketName'].OutputValue" \
        --output text 2>/dev/null || true)
    
    if [ -n "$CDK_BUCKET" ]; then
        delete_s3_bucket "$CDK_BUCKET"
    fi
    
    # Delete the stack
    aws cloudformation delete-stack --stack-name CDKToolkit 2>/dev/null || true
    aws cloudformation wait stack-delete-complete --stack-name CDKToolkit 2>/dev/null || true
    echo -e "    ${GREEN}✓${NC} CDKToolkit stack deleted"
else
    echo "  Keeping CDKToolkit stack"
fi
echo ""

# Step 8: Final Verification
echo "8️⃣  Verification..."
echo "-----------------"

# Check for remaining resources
REMAINING_STACKS=$(aws cloudformation list-stacks \
    --stack-status-filter CREATE_COMPLETE UPDATE_COMPLETE \
    --query "StackSummaries[?contains(StackName, 'RAG') || contains(StackName, 'rag')].StackName" \
    --output text)

REMAINING_BUCKETS=$(aws s3 ls | awk '{print $3}' | grep -E "(rag|RAG)" || true)

REMAINING_FUNCTIONS=$(aws lambda list-functions \
    --query "Functions[?contains(FunctionName, 'rag') || contains(FunctionName, 'RAG')].FunctionName" \
    --output text)

if [ -z "$REMAINING_STACKS" ] && [ -z "$REMAINING_BUCKETS" ] && [ -z "$REMAINING_FUNCTIONS" ]; then
    echo -e "${GREEN}✅ All RAG resources have been successfully deleted!${NC}"
else
    echo -e "${YELLOW}⚠️  Some resources may still exist:${NC}"
    [ -n "$REMAINING_STACKS" ] && echo "  - Stacks: $REMAINING_STACKS"
    [ -n "$REMAINING_BUCKETS" ] && echo "  - Buckets: $REMAINING_BUCKETS"
    [ -n "$REMAINING_FUNCTIONS" ] && echo "  - Functions: $REMAINING_FUNCTIONS"
fi

echo ""
echo "🎉 Cleanup process completed!"
echo ""

# Clean up temp files
rm -f /tmp/dist-config.json /tmp/dist-config-disabled.json 2>/dev/null || true

# Play completion sound
afplay /System/Library/Sounds/Sosumi.aiff 2>/dev/null || true