import pandas as pd
import os

def transform_data():
    print("Iniciando transformação dos dados...")

    base_dir = os.path.dirname(os.path.abspath(__file__))
    raw_path = os.path.join(base_dir, "../data/raw/WA_Fn-UseC_-HR-Employee-Attrition.csv")
    processed_dir = os.path.join(base_dir, "../data/processed")
    output_file = os.path.join(processed_dir, "dados_transformados.parquet")

    # Garante que a pasta de saída existe
    os.makedirs(processed_dir, exist_ok=True)

    # Carrega os dados brutos
    df = pd.read_csv(raw_path)
    print(f"Dados carregados com {df.shape[0]} linhas e {df.shape[1]} colunas.")

    # Remoção de colunas irrelevantes
    colunas_remover = ['EmployeeCount', 'Over18', 'StandardHours', 'EmployeeNumber']
    df.drop(columns=colunas_remover, inplace=True, errors='ignore')

    # Remove duplicatas e nulos
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)

    # Padroniza nomes
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(' ', '_')
        .str.replace('-', '_')
    )

    # Colunas texto para lowercase
    for col in df.select_dtypes(include='object').columns:
        df[col] = df[col].str.lower()

    # Salva em parquet
    df.to_parquet(output_file, index=False)

    print(f"Transformação concluída!")
    print(f"Arquivo salvo em: {os.path.abspath(output_file)}")

if __name__ == "__main__":
    transform_data()
