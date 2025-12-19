from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.google.cloud.operators.bigquery import BigQueryInsertJobOperator
from datetime import datetime
import pandas as pd
from google.oauth2 import service_account
from google.cloud import bigquery

# --- CONFIGURATION ---
PROJECT_ID = "Project-ID-Here" 
DATASET_ID = "exercise_17_dataset"
TABLE_ID = "transformed_data"
KEY_PATH = "/opt/airflow/google_keys.json"

def extract_and_transform_in_python():
    # 1. Create credentials object from your file
    credentials = service_account.Credentials.from_service_account_file(KEY_PATH)
    
    # 2. Initialize Client for extraction
    client = bigquery.Client(credentials=credentials, project=PROJECT_ID)
    
    # 3. Query Public Data
    query = """
        SELECT name, gender, SUM(number) as total
        FROM `bigquery-public-data.usa_names.usa_1910_2013`
        WHERE state = 'NY'
        GROUP BY name, gender
        ORDER BY total DESC
        LIMIT 100
    """
    query_job = client.query(query)
    df = query_job.to_dataframe()
    
    # 4. Transform Logic
    df['name'] = df['name'].str.upper()
    
    # 5. Load back to BigQuery
    client.create_dataset(DATASET_ID, exists_ok=True)
    table_ref = f"{DATASET_ID}.{TABLE_ID}"
    
    # Passing credentials here prevents the browser-popup error
    df.to_gbq(
        destination_table=table_ref, 
        project_id=PROJECT_ID, 
        if_exists='replace',
        credentials=credentials
    )

# --- DAG DEFINITION ---
with DAG(
    dag_id='bigquery_etl_pipeline',
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False
) as dag:

    # TASK 1: Extract/Transform in Python environment
    python_etl = PythonOperator(
        task_id='python_transform_and_upload',
        python_callable=extract_and_transform_in_python
    )

    # TASK 2: SQL transformation inside BigQuery
    # This uses the connection defined in your .env file
    internal_bq_transform = BigQueryInsertJobOperator(
        task_id='internal_bq_transform',
        gcp_conn_id='google_cloud_default', 
        configuration={
            "query": {
                "query": f"""
                    CREATE OR REPLACE TABLE `{PROJECT_ID}.{DATASET_ID}.final_summary` AS 
                    SELECT name, total 
                    FROM `{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}` 
                    WHERE total > 1000
                """,
                "useLegacySql": False,
            }
        }
    )

    # Dependencies
    python_etl >> internal_bq_transform