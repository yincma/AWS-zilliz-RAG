#!/usr/bin/env python3
"""Document Ingestion Processing Flow Diagram"""

from diagrams import Diagram, Cluster, Edge
from diagrams.aws.compute import Lambda
from diagrams.aws.storage import S3
from diagrams.aws.ml import Bedrock
from diagrams.custom import Custom
from diagrams.onprem.client import User
from diagrams.generic.storage import Storage
from diagrams.onprem.compute import Server

with Diagram("Document Ingestion Flow", filename="../images/document_ingestion", show=False, direction="TB"):
    user = User("User")
    
    with Cluster("Document Upload"):
        upload = Storage("Document Upload")
        s3_storage = S3("S3 Storage")
        trigger = Lambda("Ingestion Trigger")
    
    with Cluster("Document Processing"):
        # Document processing runs in Lambda
        parse = Lambda("Document Parsing")
        chunk = Lambda("Text Chunking")
        clean = Lambda("Text Cleaning")
    
    with Cluster("Vectorization Processing"):
        batch_embed = Bedrock("Batch Vectorization\n(Titan)")
        # Vector optimization runs in Lambda
        optimize = Lambda("Vector Optimization")
    
    with Cluster("Storage Update"):
        # Use custom Zilliz icon
        store_vectors = Custom("Store Vectors\n(Zilliz)", "../images/Zilliz.jpeg")
        cache_s3 = S3("Cache to S3")
        # Metadata update runs in Lambda
        update_meta = Lambda("Update Metadata")
    
    complete = Server("Completion Notification")
    
    # Processing flow
    user >> upload >> s3_storage >> trigger
    trigger >> parse >> chunk >> clean
    clean >> batch_embed >> optimize
    optimize >> [store_vectors, cache_s3]
    store_vectors >> update_meta >> complete
    cache_s3 >> update_meta