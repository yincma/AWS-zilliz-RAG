#!/usr/bin/env python3
"""
Test runner script for the RAG system.
Executes different test suites and generates reports.
"""

import sys
import os
import subprocess
from pathlib import Path
from typing import List, Optional
import argparse
import json
from datetime import datetime


class TestRunner:
    """Test execution and reporting manager."""
    
    def __init__(self, verbose: bool = False):
        self.verbose = verbose
        self.project_root = Path(__file__).parent.parent
        self.test_dir = self.project_root / "tests"
        self.report_dir = self.project_root / "test-reports"
        self.coverage_dir = self.report_dir / "coverage"
        
        # Ensure directories exist
        self.report_dir.mkdir(exist_ok=True)
        self.coverage_dir.mkdir(exist_ok=True)
    
    def run_unit_tests(self) -> int:
        """Run unit tests."""
        print("\n" + "="*60)
        print("🧪 Running Unit Tests...")
        print("="*60)
        
        cmd = [
            "pytest",
            str(self.test_dir / "unit"),
            "-v" if self.verbose else "-q",
            "-m", "unit",
            "--cov=app",
            "--cov-report=term-missing",
            f"--cov-report=html:{self.coverage_dir}/unit",
            "--cov-report=xml:coverage-unit.xml",
            f"--junit-xml={self.report_dir}/unit-results.xml",
            "--tb=short"
        ]
        
        return self._run_command(cmd)
    
    def run_integration_tests(self) -> int:
        """Run integration tests."""
        print("\n" + "="*60)
        print("🔗 Running Integration Tests...")
        print("="*60)
        
        cmd = [
            "pytest",
            str(self.test_dir / "integration"),
            "-v" if self.verbose else "-q",
            "-m", "integration",
            "--cov=app",
            "--cov-append",
            f"--cov-report=html:{self.coverage_dir}/integration",
            "--cov-report=xml:coverage-integration.xml",
            f"--junit-xml={self.report_dir}/integration-results.xml",
            "--tb=short"
        ]
        
        return self._run_command(cmd)
    
    def run_e2e_tests(self, skip_slow: bool = False) -> int:
        """Run end-to-end tests."""
        print("\n" + "="*60)
        print("🚀 Running End-to-End Tests...")
        print("="*60)
        
        cmd = [
            "pytest",
            str(self.test_dir / "e2e"),
            "-v" if self.verbose else "-q",
            "-m", "e2e" + (" and not slow" if skip_slow else ""),
            "--cov=app",
            "--cov-append",
            f"--cov-report=html:{self.coverage_dir}/e2e",
            "--cov-report=xml:coverage-e2e.xml",
            f"--junit-xml={self.report_dir}/e2e-results.xml",
            "--tb=short"
        ]
        
        return self._run_command(cmd)
    
    def run_all_tests(self, skip_slow: bool = False) -> int:
        """Run all test suites."""
        print("\n" + "="*60)
        print("🎯 Running All Tests...")
        print("="*60)
        
        marks = "not skip_ci"
        if skip_slow:
            marks += " and not slow"
        
        cmd = [
            "pytest",
            str(self.test_dir),
            "-v" if self.verbose else "-q",
            "-m", marks,
            "--cov=app",
            f"--cov-report=html:{self.coverage_dir}/all",
            "--cov-report=xml:coverage.xml",
            "--cov-report=term-missing",
            f"--junit-xml={self.report_dir}/test-results.xml",
            "--tb=short",
            "--color=yes"
        ]
        
        return self._run_command(cmd)
    
    def run_specific_test(self, test_path: str) -> int:
        """Run a specific test file or test case."""
        print(f"\n🎯 Running specific test: {test_path}")
        
        cmd = [
            "pytest",
            test_path,
            "-v",
            "--tb=short",
            "--color=yes"
        ]
        
        return self._run_command(cmd)
    
    def check_coverage(self) -> int:
        """Check if coverage meets minimum requirements."""
        print("\n" + "="*60)
        print("📊 Checking Coverage Requirements...")
        print("="*60)
        
        cmd = [
            "pytest",
            str(self.test_dir),
            "--cov=app",
            "--cov-fail-under=80",
            "--cov-report=term",
            "-q"
        ]
        
        result = self._run_command(cmd)
        
        if result == 0:
            print("✅ Coverage requirement met (≥80%)")
        else:
            print("❌ Coverage below required threshold (80%)")
        
        return result
    
    def generate_report(self) -> None:
        """Generate test report summary."""
        print("\n" + "="*60)
        print("📋 Generating Test Report...")
        print("="*60)
        
        report = {
            "timestamp": datetime.now().isoformat(),
            "test_suites": [],
            "coverage": {}
        }
        
        # Parse XML results if available
        xml_files = [
            "unit-results.xml",
            "integration-results.xml",
            "e2e-results.xml",
            "test-results.xml"
        ]
        
        for xml_file in xml_files:
            xml_path = self.report_dir / xml_file
            if xml_path.exists():
                # Parse and add to report (simplified)
                suite_name = xml_file.replace("-results.xml", "")
                report["test_suites"].append({
                    "name": suite_name,
                    "file": str(xml_file)
                })
        
        # Parse coverage XML if available
        coverage_file = self.project_root / "coverage.xml"
        if coverage_file.exists():
            # Parse coverage (simplified)
            report["coverage"]["file"] = "coverage.xml"
            report["coverage"]["html_report"] = str(self.coverage_dir / "all" / "index.html")
        
        # Save report
        report_file = self.report_dir / "test-report.json"
        with open(report_file, "w") as f:
            json.dump(report, f, indent=2)
        
        print(f"📄 Report saved to: {report_file}")
        print(f"📊 HTML Coverage Report: {self.coverage_dir / 'all' / 'index.html'}")
    
    def _run_command(self, cmd: List[str]) -> int:
        """Execute a command and return exit code."""
        if self.verbose:
            print(f"Executing: {' '.join(cmd)}")
        
        result = subprocess.run(
            cmd,
            cwd=self.project_root,
            capture_output=not self.verbose,
            text=True
        )
        
        if result.returncode != 0 and not self.verbose:
            print(result.stdout)
            print(result.stderr)
        
        return result.returncode
    
    def clean_reports(self) -> None:
        """Clean up old test reports."""
        print("🧹 Cleaning old reports...")
        
        # Remove old XML files
        for xml_file in self.report_dir.glob("*.xml"):
            xml_file.unlink()
        
        # Remove old coverage files
        for cov_file in self.project_root.glob("coverage*.xml"):
            cov_file.unlink()
        
        for cov_file in self.project_root.glob(".coverage*"):
            cov_file.unlink()
        
        print("✅ Old reports cleaned")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description="RAG System Test Runner")
    parser.add_argument(
        "--type",
        choices=["unit", "integration", "e2e", "all"],
        default="all",
        help="Type of tests to run"
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Verbose output"
    )
    parser.add_argument(
        "--skip-slow",
        action="store_true",
        help="Skip slow tests"
    )
    parser.add_argument(
        "--coverage",
        action="store_true",
        help="Check coverage requirements"
    )
    parser.add_argument(
        "--clean",
        action="store_true",
        help="Clean old reports before running"
    )
    parser.add_argument(
        "--test",
        type=str,
        help="Run specific test file or test case"
    )
    parser.add_argument(
        "--report",
        action="store_true",
        help="Generate test report after running"
    )
    
    args = parser.parse_args()
    
    # Initialize test runner
    runner = TestRunner(verbose=args.verbose)
    
    # Clean if requested
    if args.clean:
        runner.clean_reports()
    
    # Run specified tests
    exit_code = 0
    
    if args.test:
        # Run specific test
        exit_code = runner.run_specific_test(args.test)
    elif args.coverage:
        # Check coverage only
        exit_code = runner.check_coverage()
    else:
        # Run test suite
        if args.type == "unit":
            exit_code = runner.run_unit_tests()
        elif args.type == "integration":
            exit_code = runner.run_integration_tests()
        elif args.type == "e2e":
            exit_code = runner.run_e2e_tests(skip_slow=args.skip_slow)
        else:  # all
            exit_code = runner.run_all_tests(skip_slow=args.skip_slow)
    
    # Generate report if requested
    if args.report:
        runner.generate_report()
    
    # Print summary
    print("\n" + "="*60)
    if exit_code == 0:
        print("✅ All tests passed!")
    else:
        print("❌ Some tests failed!")
    print("="*60)
    
    # Play completion sound
    if sys.platform == "darwin":
        os.system("afplay /System/Library/Sounds/Sosumi.aiff")
    
    return exit_code


if __name__ == "__main__":
    sys.exit(main())