import pandas as pd
import os

def transform_data():
    print("Iniciando transformação dos dados...")

    # Define caminhos dos arquivos
    base_dir = os.getcwd()
    raw_path = os.path.join(base_dir, "data/raw/WA_Fn-UseC_-HR-Employee-Attrition.csv")
    processed_dir = os.path.join(base_dir, "data/processed")
    output_file = os.path.join(processed_dir, "dados_transformados.parquet")

    # Garante que a pasta de saída existe
    os.makedirs(processed_dir, exist_ok=True)

    # Carrega os dados brutos
    df = pd.read_csv(raw_path)
    print(f"Dados carregados com {df.shape[0]} linhas e {df.shape[1]} colunas.")

    # Remove colunas irrelevantes
    colunas_remover = ['EmployeeCount', 'Over18', 'StandardHours', 'EmployeeNumber']
    df.drop(columns=colunas_remover, inplace=True, errors='ignore')

    # Remove duplicatas e nulos
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)

    # Padroniza nomes das colunas
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(' ', '_')
        .str.replace('-', '_')
    )

    # Converte colunas de texto para lowercase (evita erros na hora de mapear valores)
    for col in df.select_dtypes(include='object').columns:
        df[col] = df[col].str.lower()

    # Renomeia as colunas para português
    df = df.rename(columns={
        'age': 'idade',
        'attrition': 'rotatividade',
        'business_travel': 'viagem_a_trabalho',
        'daily_rate': 'salario_diario',
        'department': 'departamento',
        'distance_from_home': 'distancia_de_casa',
        'education': 'escolaridade',
        'education_field': 'area_de_formacao',
        'environment_satisfaction': 'satisfacao_ambiente',
        'gender': 'genero',
        'job_involvement': 'envolvimento_trabalho',
        'job_level': 'nivel_trabalho',
        'job_role': 'cargo',
        'job_satisfaction': 'satisfacao_trabalho',
        'marital_status': 'estado_civil',
        'monthly_income': 'salario_mensal',
        'monthly_rate': 'salario_mensal_bruto',
        'num_companies_worked': 'num_empresas_trabalhadas',
        'overtime': 'hora_extra',
        'percent_salary_hike': 'percentual_aumento_salarial',
        'performance_rating': 'avaliacao_desempenho',
        'relationship_satisfaction': 'satisfacao_relacionamento',
        'stock_option_level': 'nivel_opcao_acao',
        'total_working_years': 'anos_experiencia_total',
        'training_times_last_year': 'cursos_ultimo_ano',
        'work_life_balance': 'equilibrio_vida_trabalho',
        'years_at_company': 'anos_na_empresa',
        'years_in_current_role': 'anos_no_cargo_atual',
        'years_since_last_promotion': 'anos_desde_ultima_promocao',
        'years_with_curr_manager': 'anos_com_gerente_atual',
        'hourly_rate': 'salario_hora'
    })

    # Tradução dos valores
    df['rotatividade'] = df['rotatividade'].map({'yes': 'sim', 'no': 'não'})
    df['genero'] = df['genero'].map({'male': 'masculino', 'female': 'feminino'})
    df['hora_extra'] = df['hora_extra'].map({'yes': 'sim', 'no': 'não'})

    df['viagem_a_trabalho'] = df['viagem_a_trabalho'].map({
        'travel_frequently': 'viagem_frequente',
        'travel_rarely': 'viagem_rara',
        'non_travel': 'sem_viagem'
    })

    df['departamento'] = df['departamento'].map({
        'sales': 'vendas',
        'research_&_development': 'pesquisa_e_desenvolvimento',
        'human_resources': 'recursos_humanos'
    })

    df['area_de_formacao'] = df['area_de_formacao'].map({
        'life_sciences': 'ciencias_biologicas',
        'medical': 'medicina',
        'marketing': 'marketing',
        'technical_degree': 'formacao_tecnica',
        'human_resources': 'recursos_humanos',
        'other': 'outra'
    })

    df['cargo'] = df['cargo'].map({
        'sales_executive': 'executivo_de_vendas',
        'research_scientist': 'cientista_de_pesquisa',
        'laboratory_technician': 'tecnico_de_laboratorio',
        'manufacturing_director': 'diretor_de_producao',
        'healthcare_representative': 'representante_saude',
        'manager': 'gerente',
        'sales_representative': 'representante_de_vendas',
        'research_director': 'diretor_de_pesquisa',
        'human_resources': 'recursos_humanos'
    })

    df['estado_civil'] = df['estado_civil'].map({
        'single': 'solteiro',
        'married': 'casado',
        'divorced': 'divorciado'
    })

    # Salva os dados transformados
    df.to_parquet(output_file, index=False)

    print("Transformação concluída!")
    print(f"Arquivo salvo em: {os.path.abspath(output_file)}")

if __name__ == "__main__":
    transform_data()
