#!/bin/bash

# Quick AWS Resources Cleanup
# Deletes S3 buckets and Lambda functions without waiting

echo "🧹 Quick AWS Cleanup"
echo "==================="
echo ""

# Delete S3 buckets
echo "Deleting S3 buckets..."
aws s3 ls | grep -E "(rag|RAG)" | awk '{print $3}' | while read bucket; do
    echo "  Deleting bucket: $bucket"
    aws s3 rb "s3://$bucket" --force 2>/dev/null || true
done

# Delete Lambda functions  
echo "Deleting Lambda functions..."
aws lambda list-functions --query "Functions[*].FunctionName" --output text | grep -i rag | while read func; do
    echo "  Deleting function: $func"
    aws lambda delete-function --function-name "$func" 2>/dev/null || true
done

echo "✅ Quick cleanup completed!"
echo ""
echo "Note: CloudFront distributions may take time to delete."
echo "Check AWS Console for remaining resources."

afplay /System/Library/Sounds/Sosumi.aiff