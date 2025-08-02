# 📊 Projeto ETL – DataGirls Projeto Final

Pipeline completo de engenharia de dados desenvolvido com foco em automação, transformação e visualização dos dados de RH da IBM. O objetivo é monitorar métricas de rotatividade e fornecer insights valiosos para a área de Recursos Humanos.

## 📁 Estrutura do Projeto

```
├── airflowdocker/
│   ├── dags/
│   │   └── etl_datagirlspfinal.py
│   ├── scripts/
│   │   ├── extract.py
│   │   ├── transform.py
│   │   └── load.py
│   ├── docker-compose.yaml
│   └── requirements.txt
├── data/
│   ├── raw/
│   └── processed/
├── chaves/
│   ├── kaggle.json
│   └── gcp_service_account.json
```

## 🚀 Tecnologias Utilizadas

- **Apache Airflow** v2.7.2
- **Docker** + Docker Compose
- **Python** v3.10
- **Pandas** e **PyArrow**
- **Kaggle API**
- **Google Cloud Storage (GCS)**
- **BigQuery (planejado)**
- **Power BI ou Looker Studio (para visualização)**

## ⚙️ Execução do Pipeline

### Pré-requisitos

- Docker + Docker Compose
- Conta no [Kaggle](https://www.kaggle.com/) e chave `kaggle.json`
- Conta e bucket criado no GCP

### Passo a passo

1. Clone o repositório:
   ```bash
   git clone https://github.com/seuusuario/datagirls_projetofinal.git
   cd datagirls_projetofinal/airflowdocker
   ```

2. Execute:
   ```bash
   docker compose up --build
   ```

3. Acesse o Airflow via [http://localhost:8080](http://localhost:8080)  
   Usuário padrão: `airflow`  
   Senha: `airflow`

4. Inicie manualmente a DAG `etl_datagirlspfinal`.

## 🧠 Lógica do ETL

### Extração (`extract.py`)
- A API do Kaggle baixa o dataset de RH da IBM.
- Os dados são descompactados e salvos em `data/raw`.

### Transformação (`transform.py`)
- Remoção de colunas irrelevantes como `EmployeeCount`, `Over18`, `StandardHours`.
- Padronização dos nomes das colunas (`snake_case`).
- Conversão para `lowercase`.
- Remoção de nulos e duplicados.
- Dados transformados são salvos em `.parquet` em `data/processed`.

### Carga (`load.py`)
- O arquivo `dados_transformados.parquet` é enviado para o bucket `etl_datagirlspfinal` no GCS.
- O script utiliza a conta de serviço do GCP via `google-cloud-storage`.

## ☁️ Integrações Finais (em desenvolvimento)

- Os dados carregados no GCS serão ingeridos no **BigQuery**.
- As visualizações serão criadas via **Looker Studio** (gratuito) ou **Power BI**.

## ❓Perguntas Norteadoras de Negócio

1. **Como a empresa pode monitorar a rotatividade de funcionários semanalmente?**  
   → Com execução diária da DAG e integração com o BI, é possível gerar dashboards semanais com base nas saídas registradas.

2. **Quais informações devem ser atualizadas em tempo real ou periodicamente?**  
   → Neste projeto, a periodicidade ideal é diária, suficiente para detectar tendências de rotatividade com agilidade.

3. **Como garantir que os dados estejam prontos para análises de forma confiável?**  
   → A transformação remove ruídos, padroniza nomes e garante consistência estrutural, além de exportar para um formato leve (.parquet).

4. **É possível criar um modelo incremental com essa base?**  
   → Sim, adaptando a lógica de extração para controlar modificações e utilizando marcas temporais (timestamps).

## 📌 Observações

- O pipeline é modular e preparado para escala.
- A DAG `etl_datagirlspfinal` pode ser ajustada para ingestões mais frequentes ou acionadas por eventos.

## 🙏 Agradecimentos

Este projeto foi desenvolvido por Marcela como parte do bootcamp de Engenharia de Dados promovido pela **comunidade Data Girls**.  
Agradecimentos especiais às instrutoras e colegas que contribuíram ao longo do processo.