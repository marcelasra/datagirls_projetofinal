import pandas as pd
import os

def transform_data():
    print("Iniciando transformação dos dados...")

    #Define caminhos dos arquivos
    base_dir = os.path.dirname(os.path.abspath(__file__))
    raw_path = os.path.abspath(os.path.join(base_dir, "../data/raw/WA_Fn-UseC_-HR-Employee-Attrition.csv"))
    processed_dir = os.path.abspath(os.path.join(base_dir, "../data/processed"))
    output_file = os.path.join(processed_dir, "dados_transformados.parquet")

    #Garante que a pasta de saída existe
    os.makedirs(processed_dir, exist_ok=True)

    #Carrega os dados brutos
    df = pd.read_csv(raw_path)
    print(f"Dados carregados com {df.shape[0]} linhas e {df.shape[1]} colunas.")

    #Remove colunas irrelevantes
    colunas_remover = ['EmployeeCount', 'Over18', 'StandardHours', 'EmployeeNumber']
    df.drop(columns=colunas_remover, inplace=True, errors='ignore')

    #Remove duplicatas e nulos
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)

    #Mapeamento de valores
    df['Attrition'] = df['Attrition'].map({'Yes': 'Sim', 'No': 'Não'})
    df['Gender'] = df['Gender'].map({'Male': 'Masculino', 'Female': 'Feminino'})
    df['OverTime'] = df['OverTime'].map({'Yes': 'Sim', 'No': 'Não'})
    
    df['BusinessTravel'] = df['BusinessTravel'].map({
        'Travel_Frequently': 'Viagem Frequente',
        'Travel_Rarely': 'Viagem Rara',
        'Non-Travel': 'Sem Viagem'
    })

    df['Department'] = df['Department'].map({
        'Sales': 'Vendas',
        'Research & Development': 'Pesquisa e Desenvolvimento',
        'Human Resources': 'Recursos Humanos'
    })
    
    df['EducationField'] = df['EducationField'].map({
        'Life Sciences': 'Ciências Biológicas',
        'Medical': 'Medicina',
        'Marketing': 'Marketing',
        'Technical Degree': 'Formação Técnica',
        'Human Resources': 'Recursos Humanos',
        'Other': 'Outra'
    })

    df['JobRole'] = df['JobRole'].map({
        'Sales Executive': 'Executivo de Vendas',
        'Research Scientist': 'Cientista de Pesquisa',
        'Laboratory Technician': 'Técnico de Laboratório',
        'Manufacturing Director': 'Diretor de Produção',
        'Healthcare Representative': 'Representante de Saúde',
        'Manager': 'Gerente',
        'Sales Representative': 'Representante de Vendas',
        'Research Director': 'Diretor de Pesquisa',
        'Human Resources': 'Recursos Humanos'
    })

    df['MaritalStatus'] = df['MaritalStatus'].map({
        'Single': 'Solteiro',
        'Married': 'Casado',
        'Divorced': 'Divorciado'
    })

    #Mapeamento para colunas numéricas categorizadas
    df['Education'] = df['Education'].map({1: 'Abaixo da Faculdade', 2: 'Faculdade', 3: 'Bacharelado', 4: 'Mestrado', 5: 'Doutorado'})
    df['EnvironmentSatisfaction'] = df['EnvironmentSatisfaction'].map({1: 'Muito Baixo', 2: 'Baixo', 3: 'Médio', 4: 'Alto'})
    df['JobInvolvement'] = df['JobInvolvement'].map({1: 'Muito Baixo', 2: 'Baixo', 3: 'Médio', 4: 'Alto'})
    df['JobSatisfaction'] = df['JobSatisfaction'].map({1: 'Muito Baixo', 2: 'Baixo', 3: 'Médio', 4: 'Alto'})
    df['PerformanceRating'] = df['PerformanceRating'].map({3: 'Ótimo', 4: 'Excelente'})
    df['RelationshipSatisfaction'] = df['RelationshipSatisfaction'].map({1: 'Muito Baixo', 2: 'Baixo', 3: 'Médio', 4: 'Alto'})
    df['WorkLifeBalance'] = df['WorkLifeBalance'].map({1: 'Muito Baixo', 2: 'Baixo', 3: 'Médio', 4: 'Alto'})
    
    #Renomear as colunas para português
    df.rename(columns={
        'Age': 'Idade',
        'Attrition': 'Rotatividade',
        'BusinessTravel': 'ViagemATrabalho',
        'DailyRate': 'SalarioDiario',
        'Department': 'Departamento',
        'DistanceFromHome': 'DistanciaDeCasa',
        'Education': 'Escolaridade',
        'EducationField': 'AreaDeFormacao',
        'EnvironmentSatisfaction': 'SatisfacaoAmbiente',
        'Gender': 'Genero',
        'HourlyRate': 'SalarioHora',
        'JobInvolvement': 'EnvolvimentoTrabalho',
        'JobLevel': 'NivelTrabalho',
        'JobRole': 'Cargo',
        'JobSatisfaction': 'SatisfacaoTrabalho',
        'MaritalStatus': 'EstadoCivil',
        'MonthlyIncome': 'SalarioMensal',
        'MonthlyRate': 'SalarioMensalBruto',
        'NumCompaniesWorked': 'NumEmpresasTrabalhadas',
        'OverTime': 'HoraExtra',
        'PercentSalaryHike': 'PercentualAumentoSalarial',
        'PerformanceRating': 'AvaliacaoDesempenho',
        'RelationshipSatisfaction': 'SatisfacaoRelacionamento',
        'StockOptionLevel': 'NivelOpcaoAcao',
        'TotalWorkingYears': 'AnosExperienciaTotal',
        'TrainingTimesLastYear': 'CursosUltimoAno',
        'WorkLifeBalance': 'EquilibrioVidaTrabalho',
        'YearsAtCompany': 'AnosNaEmpresa',
        'YearsInCurrentRole': 'AnosNoCargoAtual',
        'YearsSinceLastPromotion': 'AnosDesdeUltimaPromocao',
        'YearsWithCurrManager': 'AnosComGerenteAtual'
    }, inplace=True)
    
    #Salvando os dados transformados
    df.to_parquet(output_file, index=False)

    print("Transformação concluída!")
    print(f"Arquivo salvo em: {os.path.abspath(output_file)}")

if __name__ == "__main__":
    transform_data()