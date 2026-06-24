# infrastructure/aws_vector_memory.py
import boto3

class AWSVectorMemory:
    def upsert_user_context(self, embedding_vector: list, metadata: dict):
        # Uses OpenSearch or Amazon S3 Vectors for instant recall
        client = boto3.client('opensearch')
        client.index(index="user_memory", body={"vector": embedding_vector, **metadata})
      
