from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys
import os

# Adiciona o diretório dos scripts ao path do Python
sys.path.append("/opt/airflow/scripts")

# Importa as funções dos seus scripts
from extract import download_dataset
from transform import transform_data
from load import upload_to_gcs

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

    # Define a ordem: extract → transform → load
    t1 >> t2 >> t3
