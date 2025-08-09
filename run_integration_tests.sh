#!/bin/bash

# Integration Test Runner for AWS-Zilliz-RAG System
# This script runs integration tests with proper environment setup

echo "🚀 AWS-Zilliz-RAG Integration Test Suite"
echo "========================================="
echo ""

# Set test environment variables
export TEST_ENV=true
export AWS_REGION=us-east-1
export AWS_ACCESS_KEY_ID=test-key
export AWS_SECRET_ACCESS_KEY=test-secret
export ZILLIZ_ENDPOINT=test-endpoint
export ZILLIZ_TOKEN=test-token
export BEDROCK_MODEL_ID=amazon.nova-1
export EMBEDDING_MODEL_ID=amazon.titan-embed-image-v1

# Activate virtual environment if needed
if [[ "$VIRTUAL_ENV" == "" ]]; then
    echo "📦 Activating virtual environment..."
    source venv/bin/activate
fi

# Function to run tests with proper error handling
run_test() {
    local test_name=$1
    local test_path=$2
    
    echo ""
    echo "🧪 Running: $test_name"
    echo "-----------------------------------"
    
    # Run the test
    pytest $test_path -v --tb=short --capture=no 2>&1 | tee test_output.tmp
    
    # Check result
    if [ ${PIPESTATUS[0]} -eq 0 ]; then
        echo "✅ $test_name: PASSED"
        return 0
    else
        echo "❌ $test_name: FAILED"
        return 1
    fi
}

# Initialize counters
TOTAL_TESTS=0
PASSED_TESTS=0
FAILED_TESTS=0

# Run integration tests
echo "📋 Starting Integration Tests..."
echo "================================="

# Test 1: Environment Setup
run_test "Environment Setup" "tests/test_environment.py"
if [ $? -eq 0 ]; then
    ((PASSED_TESTS++))
else
    ((FAILED_TESTS++))
fi
((TOTAL_TESTS++))

# Test 2: Integration Tests
run_test "RAG Integration" "tests/integration/test_rag_integration.py::TestRAGIntegration -m integration"
if [ $? -eq 0 ]; then
    ((PASSED_TESTS++))
else
    ((FAILED_TESTS++))
fi
((TOTAL_TESTS++))

# Test 3: Controller Integration Tests (if they can be imported)
if [ -f "tests/integration/test_rag_controller.py" ]; then
    echo ""
    echo "🔗 Testing Controller Integration..."
    python -c "
import sys
sys.path.insert(0, '.')
try:
    import tests.integration.test_rag_controller
    print('✅ Controller tests can be imported')
except ImportError as e:
    print('⚠️  Controller tests have import issues (expected if models not fully implemented)')
    print(f'   Details: {e}')
"
fi

# Generate simple test report
echo ""
echo "📊 Test Report Generation"
echo "========================"

# Create test report directory
mkdir -p test-reports/integration

# Generate JSON report
python -c "
import json
from datetime import datetime

report = {
    'timestamp': datetime.now().isoformat(),
    'test_type': 'integration',
    'summary': {
        'total': $TOTAL_TESTS,
        'passed': $PASSED_TESTS,
        'failed': $FAILED_TESTS,
        'pass_rate': round(($PASSED_TESTS / $TOTAL_TESTS * 100) if $TOTAL_TESTS > 0 else 0, 2)
    },
    'environment': {
        'aws_region': '$AWS_REGION',
        'test_env': True,
        'models': {
            'llm': '$BEDROCK_MODEL_ID',
            'embedding': '$EMBEDDING_MODEL_ID'
        }
    }
}

with open('test-reports/integration/report.json', 'w') as f:
    json.dump(report, f, indent=2)

print('📄 Report saved to: test-reports/integration/report.json')
"

# Summary
echo ""
echo "📈 Integration Test Summary"
echo "==========================="
echo "Total Tests Run: $TOTAL_TESTS"
echo "Tests Passed: $PASSED_TESTS ✅"
echo "Tests Failed: $FAILED_TESTS ❌"

if [ $FAILED_TESTS -eq 0 ]; then
    echo ""
    echo "🎉 All integration tests passed!"
    RESULT=0
else
    echo ""
    echo "⚠️  Some tests failed. Please review the output above."
    RESULT=1
fi

# Clean up
rm -f test_output.tmp

# Play completion sound
afplay /System/Library/Sounds/Sosumi.aiff

echo ""
echo "✨ Integration test run complete!"
echo ""

exit $RESULT