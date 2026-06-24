from google.cloud import bigquery
import json


class BigQueryProcessor:
    def __init__(self, project_id="t3l3pathy-analytics"):
        self.client = bigquery.Client(project=project_id)

    def run_pattern_analysis(self, user_id: str):
        """
        Executes a query to identify long-term cognitive patterns
        across millions of rows of historical telemetry data.
        """
        query = f"""
            SELECT 
                AVG(somatic_arousal_index) as avg_stress,
                COUNT(*) as event_count
            FROM `t3l3pathy_analytics.user_telemetry`
            WHERE user_id = '{user_id}'
            GROUP BY event_type
        """
        query_job = self.client.query(query)
        return [dict(row) for row in query_job]
