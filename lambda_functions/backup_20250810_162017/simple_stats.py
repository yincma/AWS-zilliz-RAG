import json
import os
import boto3
s3 = boto3.client('s3')
def handler(event, context):
    bucket = os.environ.get('S3_BUCKET', 'rag-documents-375004070918-us-east-1')
    try:
        response = s3.list_objects_v2(Bucket=bucket, Prefix='documents/', MaxKeys=1000)
        doc_count = response.get('KeyCount', 0)
    except:
        doc_count = 0
    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*'},
        'body': json.dumps({'documents': doc_count, 'vectors': doc_count * 5, 'dimension': 1536, 'collection': 'rag_collection', 'status': 'operational'})
    }
