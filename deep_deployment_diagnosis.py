#!/usr/bin/env python3
"""
Deep Deployment Diagnosis Tool for AWS RAG Application
This script performs comprehensive analysis of deployment issues
"""

import os
import sys
import json
import subprocess
from pathlib import Path
from typing import Dict, List, Tuple, Optional
import boto3
from botocore.exceptions import ClientError, NoCredentialsError

class DeploymentDiagnostics:
    """Comprehensive deployment diagnostics tool"""
    
    def __init__(self):
        self.base_path = Path(__file__).parent
        self.infrastructure_path = self.base_path / "infrastructure"
        self.issues = []
        self.warnings = []
        self.recommendations = []
        self.critical_errors = []
        
    def print_section(self, title: str, emoji: str = "📋"):
        """Print formatted section header"""
        print(f"\n{'='*60}")
        print(f"{emoji} {title}")
        print('='*60)
        
    def run_command(self, command: str, cwd: Optional[Path] = None) -> Tuple[bool, str, str]:
        """Run shell command and return success, stdout, stderr"""
        try:
            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True,
                cwd=cwd or self.base_path
            )
            return result.returncode == 0, result.stdout, result.stderr
        except Exception as e:
            return False, "", str(e)
    
    def check_aws_credentials(self) -> bool:
        """Check AWS credentials configuration"""
        self.print_section("AWS Credentials Check", "🔑")
        
        try:
            # Check environment variables
            env_vars = {
                'AWS_REGION': os.environ.get('AWS_REGION'),
                'AWS_ACCESS_KEY_ID': os.environ.get('AWS_ACCESS_KEY_ID'),
                'AWS_SECRET_ACCESS_KEY': os.environ.get('AWS_SECRET_ACCESS_KEY')
            }
            
            print("Environment Variables:")
            for key, value in env_vars.items():
                if value:
                    masked = value[:4] + '****' if 'KEY' in key or 'SECRET' in key else value
                    print(f"  ✅ {key}: {masked}")
                else:
                    print(f"  ❌ {key}: Not set")
                    if key == 'AWS_REGION':
                        self.warnings.append(f"{key} not set, will use default region")
                    else:
                        self.issues.append(f"{key} not set")
            
            # Test AWS connectivity
            try:
                sts = boto3.client('sts')
                identity = sts.get_caller_identity()
                print(f"\n✅ AWS Connection Successful:")
                print(f"  Account: {identity['Account']}")
                print(f"  UserID: {identity['UserId']}")
                print(f"  ARN: {identity['Arn']}")
                return True
            except NoCredentialsError:
                self.critical_errors.append("No AWS credentials found")
                print("❌ AWS credentials not configured properly")
                return False
            except ClientError as e:
                self.critical_errors.append(f"AWS connection error: {e}")
                print(f"❌ AWS connection failed: {e}")
                return False
                
        except Exception as e:
            self.issues.append(f"Credential check failed: {e}")
            print(f"❌ Error checking credentials: {e}")
            return False
    
    def check_cdk_bootstrap(self) -> bool:
        """Check CDK bootstrap status"""
        self.print_section("CDK Bootstrap Check", "🔨")
        
        try:
            # Get current region
            region = os.environ.get('AWS_REGION', 'us-east-1')
            
            # Check bootstrap stack
            cfn = boto3.client('cloudformation', region_name=region)
            try:
                response = cfn.describe_stacks(StackName='CDKToolkit')
                stack = response['Stacks'][0]
                print(f"✅ CDK Bootstrap Stack Found:")
                print(f"  Status: {stack['StackStatus']}")
                print(f"  Region: {region}")
                
                # Check bootstrap version
                outputs = {o['OutputKey']: o['OutputValue'] for o in stack.get('Outputs', [])}
                if 'BootstrapVersion' in outputs:
                    print(f"  Bootstrap Version: {outputs['BootstrapVersion']}")
                    
                return stack['StackStatus'] in ['CREATE_COMPLETE', 'UPDATE_COMPLETE']
                
            except ClientError as e:
                if 'does not exist' in str(e):
                    self.critical_errors.append(f"CDK not bootstrapped in region {region}")
                    print(f"❌ CDK not bootstrapped in region {region}")
                    print(f"   Run: cdk bootstrap aws://ACCOUNT/{region}")
                    return False
                raise
                
        except Exception as e:
            self.issues.append(f"Bootstrap check failed: {e}")
            print(f"❌ Error checking bootstrap: {e}")
            return False
    
    def check_project_structure(self) -> bool:
        """Check project structure and dependencies"""
        self.print_section("Project Structure Check", "📁")
        
        critical_files = [
            ('infrastructure/app.py', 'CDK entry point'),
            ('infrastructure/cdk.json', 'CDK configuration'),
            ('infrastructure/requirements.txt', 'Python dependencies'),
            ('infrastructure/stacks/web_stack.py', 'Web stack definition'),
            ('infrastructure/stacks/api_stack.py', 'API stack definition'),
            ('infrastructure/stacks/data_stack.py', 'Data stack definition'),
        ]
        
        all_exist = True
        for file_path, description in critical_files:
            full_path = self.base_path / file_path
            if full_path.exists():
                print(f"✅ {description}: {file_path}")
            else:
                print(f"❌ Missing {description}: {file_path}")
                self.critical_errors.append(f"Missing file: {file_path}")
                all_exist = False
                
        return all_exist
    
    def check_lambda_functions(self) -> bool:
        """Check Lambda function handlers"""
        self.print_section("Lambda Functions Check", "⚡")
        
        handlers = [
            'lambda_functions/query_handler.py',
            'lambda_functions/ingest_handler.py',
            'lambda_functions/stats_handler.py',
        ]
        
        all_valid = True
        for handler_path in handlers:
            full_path = self.base_path / handler_path
            if full_path.exists():
                # Check if handler function exists
                content = full_path.read_text()
                if 'def handler(' in content or 'def lambda_handler(' in content:
                    print(f"✅ {handler_path}: Valid handler found")
                else:
                    print(f"⚠️ {handler_path}: Handler function might be missing")
                    self.warnings.append(f"Handler function not found in {handler_path}")
            else:
                print(f"❌ Missing handler: {handler_path}")
                self.issues.append(f"Missing Lambda handler: {handler_path}")
                all_valid = False
                
        return all_valid
    
    def check_dependencies(self) -> bool:
        """Check Python dependencies"""
        self.print_section("Dependencies Check", "📦")
        
        try:
            # Check main requirements
            req_file = self.base_path / "requirements.txt"
            if req_file.exists():
                with open(req_file) as f:
                    requirements = f.read().splitlines()
                
                critical_deps = ['boto3', 'langchain', 'langchain-aws', 'pymilvus']
                for dep in critical_deps:
                    if any(dep in req for req in requirements):
                        print(f"✅ {dep}: Found in requirements")
                    else:
                        print(f"⚠️ {dep}: Not found in requirements")
                        self.warnings.append(f"Dependency {dep} might be missing")
            else:
                self.issues.append("requirements.txt not found")
                return False
                
            # Check CDK dependencies
            cdk_req = self.infrastructure_path / "requirements.txt"
            if cdk_req.exists():
                print("\n✅ CDK requirements.txt found")
            else:
                self.issues.append("CDK requirements.txt not found")
                
            return True
            
        except Exception as e:
            self.issues.append(f"Dependency check failed: {e}")
            return False
    
    def check_cdk_synth(self) -> bool:
        """Check CDK synthesis"""
        self.print_section("CDK Synthesis Check", "🔧")
        
        print("Running CDK synth (this may take a moment)...")
        success, stdout, stderr = self.run_command(
            "npx cdk synth --quiet",
            cwd=self.infrastructure_path
        )
        
        if success:
            print("✅ CDK synthesis successful")
            
            # Check generated templates
            cdk_out = self.infrastructure_path / "cdk.out"
            if cdk_out.exists():
                templates = list(cdk_out.glob("*.template.json"))
                print(f"  Generated {len(templates)} CloudFormation templates:")
                for template in templates:
                    print(f"    - {template.name}")
            return True
        else:
            print("❌ CDK synthesis failed")
            if stderr:
                print(f"Error: {stderr[:500]}")  # Print first 500 chars of error
                self.critical_errors.append(f"CDK synth error: {stderr[:200]}")
            return False
    
    def check_deployment_status(self) -> bool:
        """Check current deployment status"""
        self.print_section("Deployment Status Check", "🚀")
        
        try:
            region = os.environ.get('AWS_REGION', 'us-east-1')
            cfn = boto3.client('cloudformation', region_name=region)
            
            # List all stacks
            response = cfn.list_stacks(
                StackStatusFilter=[
                    'CREATE_COMPLETE', 'UPDATE_COMPLETE', 'CREATE_FAILED',
                    'ROLLBACK_COMPLETE', 'UPDATE_ROLLBACK_COMPLETE'
                ]
            )
            
            rag_stacks = [s for s in response['StackSummaries'] 
                         if 'RAG' in s['StackName']]
            
            if rag_stacks:
                print(f"Found {len(rag_stacks)} RAG-related stacks:")
                for stack in rag_stacks:
                    status_emoji = "✅" if "COMPLETE" in stack['StackStatus'] and "ROLLBACK" not in stack['StackStatus'] else "❌"
                    print(f"  {status_emoji} {stack['StackName']}: {stack['StackStatus']}")
                    
                    if "FAILED" in stack['StackStatus'] or "ROLLBACK" in stack['StackStatus']:
                        # Get failure reason
                        try:
                            events = cfn.describe_stack_events(StackName=stack['StackName'])
                            failed_events = [e for e in events['StackEvents'] 
                                           if 'FAILED' in e.get('ResourceStatus', '')]
                            if failed_events:
                                print(f"      Failure reason: {failed_events[0].get('ResourceStatusReason', 'Unknown')[:100]}")
                                self.issues.append(f"Stack {stack['StackName']} failed: {failed_events[0].get('ResourceStatusReason', '')[:100]}")
                        except:
                            pass
            else:
                print("No RAG stacks found in this region")
                self.warnings.append("No existing deployments found")
                
            return True
            
        except Exception as e:
            self.issues.append(f"Deployment status check failed: {e}")
            print(f"❌ Error checking deployment: {e}")
            return False
    
    def analyze_environment(self) -> bool:
        """Analyze environment configuration"""
        self.print_section("Environment Analysis", "🌍")
        
        # Check .env file
        env_file = self.base_path / ".env"
        if env_file.exists():
            print("✅ .env file found")
            
            # Load and check critical variables
            with open(env_file) as f:
                env_content = f.read()
                
            critical_vars = [
                'AWS_REGION',
                'BEDROCK_MODEL_ID',
                'EMBEDDING_MODEL_ID',
                'ZILLIZ_ENDPOINT',
                'ZILLIZ_TOKEN'
            ]
            
            for var in critical_vars:
                if var in env_content:
                    print(f"  ✅ {var}: Configured")
                else:
                    print(f"  ❌ {var}: Not configured")
                    self.issues.append(f"Missing environment variable: {var}")
        else:
            print("⚠️ .env file not found")
            self.warnings.append(".env file not found - using environment variables")
            
        return True
    
    def generate_recommendations(self):
        """Generate recommendations based on findings"""
        self.print_section("Recommendations", "💡")
        
        if self.critical_errors:
            print("\n🚨 CRITICAL ISSUES TO FIX FIRST:")
            for error in self.critical_errors:
                print(f"  1. {error}")
                
        if not any('bootstrap' in e.lower() for e in self.critical_errors):
            if 'CDK not bootstrapped' in str(self.critical_errors):
                print("\n📌 Fix CDK Bootstrap:")
                print("   aws sts get-caller-identity  # Verify credentials")
                print("   cdk bootstrap aws://ACCOUNT/REGION")
                
        if self.issues:
            print("\n⚠️ Issues to address:")
            for issue in self.issues:
                print(f"  - {issue}")
                
        if self.warnings:
            print("\n📝 Warnings (non-critical):")
            for warning in self.warnings:
                print(f"  - {warning}")
                
        # Provide deployment commands
        print("\n🚀 Deployment Commands (run in order):")
        print("   1. cd infrastructure")
        print("   2. pip install -r requirements.txt")
        print("   3. cdk bootstrap  # If not already done")
        print("   4. cdk synth  # Verify synthesis")
        print("   5. cdk deploy --all --require-approval never")
        
    def run_full_diagnosis(self):
        """Run complete diagnostic suite"""
        print("\n" + "="*60)
        print("🔬 AWS RAG DEPLOYMENT DEEP DIAGNOSIS")
        print("="*60)
        
        # Run all checks
        checks = [
            ("AWS Credentials", self.check_aws_credentials),
            ("CDK Bootstrap", self.check_cdk_bootstrap),
            ("Project Structure", self.check_project_structure),
            ("Lambda Functions", self.check_lambda_functions),
            ("Dependencies", self.check_dependencies),
            ("Environment", self.analyze_environment),
            ("CDK Synthesis", self.check_cdk_synth),
            ("Deployment Status", self.check_deployment_status),
        ]
        
        results = {}
        for name, check_func in checks:
            try:
                results[name] = check_func()
            except Exception as e:
                print(f"\n❌ {name} check failed with error: {e}")
                results[name] = False
                
        # Generate final report
        self.print_section("Diagnosis Summary", "📊")
        
        total_checks = len(results)
        passed_checks = sum(1 for v in results.values() if v)
        
        print(f"\nChecks Passed: {passed_checks}/{total_checks}")
        
        for check, passed in results.items():
            status = "✅ PASS" if passed else "❌ FAIL"
            print(f"  {status}: {check}")
            
        # Generate recommendations
        self.generate_recommendations()
        
        # Overall status
        print("\n" + "="*60)
        if self.critical_errors:
            print("❌ DEPLOYMENT BLOCKED: Critical issues detected")
            print("   Please fix the critical issues listed above")
        elif passed_checks == total_checks:
            print("✅ READY TO DEPLOY: All checks passed")
            print("   Run: cd infrastructure && cdk deploy --all")
        else:
            print("⚠️ DEPLOYMENT POSSIBLE: Some issues detected")
            print("   Review and fix issues before deployment")
        print("="*60)

if __name__ == "__main__":
    diagnostics = DeploymentDiagnostics()
    diagnostics.run_full_diagnosis()