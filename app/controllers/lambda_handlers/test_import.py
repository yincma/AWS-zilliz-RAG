"""测试Lambda中的import问题"""
import json
import sys
import os

def handler(event, context):
    """测试handler"""
    
    response = {
        "python_path": sys.path,
        "current_dir": os.getcwd(),
        "list_dir": os.listdir("/var/task"),
        "pymilvus_check": None,
        "import_error": None
    }
    
    # 测试pymilvus导入
    try:
        import pymilvus
        response["pymilvus_check"] = f"pymilvus version: {pymilvus.__version__}"
        response["pymilvus_path"] = pymilvus.__file__
    except ImportError as e:
        response["import_error"] = str(e)
        
    # 尝试更详细的导入
    try:
        from pymilvus import connections
        response["connections_import"] = "Success"
    except Exception as e:
        response["connections_error"] = str(e)
    
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps(response, indent=2)
    }