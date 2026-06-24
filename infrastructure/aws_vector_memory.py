import boto3
import json
from datetime import datetime

class AWSVectorMemory:
    def __init__(self, index_name="t3l3pathy_context"):
        self.client = boto3.client('opensearch', region_name='us-east-1')
        self.index = index_name

    def upsert_memory(self, session_id: str, semantic_payload: dict, embedding: list):
        """
        Stores interaction data in AWS OpenSearch as a vector.
        """
        document = {
            "session_id": session_id,
            "timestamp": datetime.utcnow().isoformat(),
            "context_data": json.dumps(semantic_payload),
            "vector_field": embedding  # The 768-dim vector from Gemini
        }
        
        response = self.client.index(
            index=self.index,
            body=document
        )
        return response

    def recall_memory(self, query_embedding: list, top_k=5):
        """
        Performs a K-Nearest Neighbor (KNN) search to find the 
        most relevant past context for the current thought.
        """
        search_query = {
            "size": top_k,
            "query": {
                "knn": {
                    "vector_field": {
                        "vector": query_embedding,
                        "k": top_k
                    }
                }
            }
        }
        return self.client.search(index=self.index, body=search_query)
