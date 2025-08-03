from google.cloud import bigquery
import os

def load_parquet_to_bigquery():
    print("Iniciando carga de dados no BigQuery...")

    # Caminho do arquivo .parquet
    parquet_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../data/processed/dados_transformados.parquet"))

    # Caminho para a chave de serviço
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.abspath(os.path.join(os.path.dirname(__file__), "../chaves/gcp_service_account.json"))

    # IDs atualizados
    project_id = "carbide-eye-466719"
    dataset_id = "datagirls_projetofinal"
    table_id = "dados_transformados"

    client = bigquery.Client(project=project_id)
    table_ref = f"{project_id}.{dataset_id}.{table_id}"

    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.PARQUET,
        autodetect=True,
        write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
    )

    with open(parquet_path, "rb") as source_file:
        load_job = client.load_table_from_file(
            source_file,
            destination=table_ref,
            job_config=job_config,
            location="southamerica-east1"
        )

    load_job.result()  # Aguarda o job terminar
    print(f"Arquivo carregado com sucesso na tabela: {table_ref}")

if __name__ == "__main__":
    load_parquet_to_bigquery()
