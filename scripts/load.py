import os
from google.cloud import storage

def upload_to_gcs():
    print("Iniciando upload para o Google Cloud Storage...")

    # Caminho local para o .parquet
    base_dir = os.path.dirname(os.path.abspath(__file__))
    local_file = os.path.abspath(os.path.join(base_dir, "../data/processed/dados_transformados.parquet"))

    # Nome do bucket e destino no GCS
    bucket_name = "etl_datagirlspfinal"
    destination_blob = "dados/dados_transformados.parquet"

    # Caminho para a chave de serviço
    chave_path = os.path.abspath(os.path.join(base_dir, "../chaves/gcp_service_account.json"))
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = chave_path

    # Inicializa o cliente do GCS
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(destination_blob)

    # Faz o upload
    blob.upload_from_filename(local_file)
    print(f"Upload concluído! Arquivo disponível em: gs://{bucket_name}/{destination_blob}")

if __name__ == "__main__":
    upload_to_gcs()
