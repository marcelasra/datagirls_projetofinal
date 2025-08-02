import os

# Define a variável de ambiente ANTES de importar o kaggle
os.environ["KAGGLE_CONFIG_DIR"] = "/opt/airflow/chaves"

from kaggle.api.kaggle_api_extended import KaggleApi

def download_dataset():
    print("Iniciando autenticação com a API do Kaggle...")

    api = KaggleApi()
    api.authenticate()
    print("Autenticação bem-sucedida!")

    # Caminho onde o arquivo será salvo
    dest_path = "/opt/airflow/data/raw"
    os.makedirs(dest_path, exist_ok=True)

    print("Baixando dataset...")
    api.dataset_download_files(
        'pavansubhasht/ibm-hr-analytics-attrition-dataset',
        path=dest_path,
        unzip=True
    )

    print(f"Arquivos extraídos em: {dest_path}")
    arquivos = os.listdir(dest_path)
    for arquivo in arquivos:
        print(f"  - {arquivo}")

if __name__ == "__main__":
    download_dataset()
