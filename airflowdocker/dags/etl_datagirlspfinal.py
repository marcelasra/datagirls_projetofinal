from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys
import os

sys.path.append("/opt/airflow/scripts")

from extract import download_dataset
from transform import transform_data
from load import upload_to_gcs
from load_to_bigquery import load_parquet_to_bigquery

# Define a DAG
with DAG(
    dag_id="etl_datagirlspfinal",
    start_date=datetime(2023, 1, 1),
    schedule_interval="@daily",
    catchup=False,
    tags=["ibm_hr", "datagirls"],
    description="Pipeline ETL com dados de RH da IBM para o projeto final Data Girls"
) as dag:

    t1 = PythonOperator(
        task_id="extract",
        python_callable=download_dataset
    )

    t2 = PythonOperator(
        task_id="transform",
        python_callable=transform_data
    )

    t3 = PythonOperator(
        task_id="load",
        python_callable=upload_to_gcs
    )

    t4 = PythonOperator(
        task_id="load_to_bigquery",
        python_callable=load_parquet_to_bigquery
    )

    # Define a ordem: extract → transform → load → bigquery
    t1 >> t2 >> t3 >> t4
