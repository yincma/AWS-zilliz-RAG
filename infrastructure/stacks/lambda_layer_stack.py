"""
Lambda Layer Stack for large dependencies
Separates heavy dependencies from main Lambda code
"""

from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_s3 as s3,
    RemovalPolicy,
    Duration,
    Size
)
from constructs import Construct
import subprocess
import os
import shutil
import tempfile

class LambdaLayerStack(Stack):
    """Create Lambda Layers for heavy dependencies"""
    
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        
        # Create Lambda Layer for LangChain dependencies
        self.langchain_layer = self._create_langchain_layer()
        
        # Create Lambda Layer for data processing (if needed later)
        # self.data_layer = self._create_data_layer()
    
    def _create_langchain_layer(self) -> _lambda.LayerVersion:
        """Create a Lambda layer with LangChain dependencies"""
        
        # Build layer in temp directory
        build_dir = tempfile.mkdtemp()
        layer_dir = os.path.join(build_dir, "python")
        os.makedirs(layer_dir)
        
        # Install minimal dependencies for layer
        requirements = """
langchain-core>=0.1.0
langchain-aws>=0.1.0
pydantic>=2.0.0
        """
        
        req_file = os.path.join(build_dir, "requirements.txt")
        with open(req_file, "w") as f:
            f.write(requirements)
        
        # Install packages
        subprocess.run([
            "pip3", "install",
            "-r", req_file,
            "-t", layer_dir,
            "--no-cache-dir",
            "--quiet",
            "--no-deps"  # Don't install sub-dependencies
        ], check=False)
        
        # Clean up unnecessary files
        for root, dirs, files in os.walk(layer_dir):
            # Remove __pycache__
            if "__pycache__" in dirs:
                shutil.rmtree(os.path.join(root, "__pycache__"))
            # Remove .pyc files
            for file in files:
                if file.endswith(('.pyc', '.pyo', '.pyi')):
                    os.remove(os.path.join(root, file))
        
        # Create layer
        layer = _lambda.LayerVersion(
            self, "LangChainLayer",
            code=_lambda.Code.from_asset(build_dir),
            compatible_runtimes=[
                _lambda.Runtime.PYTHON_3_9,
                _lambda.Runtime.PYTHON_3_10,
                _lambda.Runtime.PYTHON_3_11
            ],
            description="LangChain core dependencies for RAG",
            removal_policy=RemovalPolicy.DESTROY
        )
        
        # Clean up temp directory
        try:
            shutil.rmtree(build_dir)
        except:
            pass
        
        return layer
    
    def _create_data_layer(self) -> _lambda.LayerVersion:
        """Create a Lambda layer for data processing libraries (optional)"""
        # This can be implemented if numpy/pandas are needed
        pass