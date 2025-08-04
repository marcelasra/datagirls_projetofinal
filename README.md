# Projeto Final - Engenharia de Dados | Data Girls 👩🏾‍💻

Este projeto tem como objetivo aplicar os conhecimentos adquiridos no bootcamp de Engenharia de Dados da comunidade [Data Girls](https://www.datagirls.com.br/), utilizando ferramentas modernas para desenvolver um pipeline ETL completo, com orquestração via Apache Airflow, armazenamento no Google Cloud Storage, análise no BigQuery e visualizações com Looker Studio.

## 🔍 Descrição

O projeto utiliza o dataset [IBM HR Analytics Employee Attrition & Performance](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-performance), que trata da rotatividade de funcionários com base em dados de RH. A proposta é extrair, transformar e carregar esses dados em um bucket do GCP e posteriormente no BigQuery, a fim de gerar análises e insights por meio de visualizações.

---

## 🧱 Tecnologias utilizadas

- **Python 3.10** – manipulação e transformação de dados
- **Pandas** – tratamento e tradução dos dados
- **Apache Airflow 2.7.2** – orquestração de tarefas com `docker-compose`
- **Docker Desktop 4.42.1** – containerização e execução local
- **Google Cloud Platform (GCP)** – armazenamento e análise dos dados
  - Google Cloud Storage
  - BigQuery
- **Looker Studio** – visualizações e dashboard interativo

---

## 🗂️ Organização do Projeto

```
datagirls_projetofinal/
├── airflowdocker/
│   ├── dags/
│   │   └── etl_datagirlspfinal.py
│   ├── scripts/
│   │   ├── extract.py
│   │   ├── transform.py
│   │   ├── load.py
│   │   └── load_to_bigquery.py
│   ├── requirements.txt
│   └── docker-compose.yaml
├── data/
│   ├── raw/
│   │   └── WA_Fn-UseC_-HR-Employee-Attrition.csv
│   └── processed/
│       └── dados_transformados.parquet
├── chaves/
│   ├── kaggle.json
│   └── gcp_service_account.json
└── README.md
```

---

## ⚙️ Pipeline ETL

O pipeline é composto por quatro etapas, agendadas para rodar diariamente (`@daily`):

1. **`extract.py`**: Faz o download automático do dataset no Kaggle.
2. **`transform.py`**: Remove colunas irrelevantes, trata nulos e traduz todas as colunas e valores para português.
3. **`load.py`**: Envia os dados transformados (`.parquet`) para o bucket no GCP.
4. **`load_to_bigquery.py`**: Carrega o arquivo `.parquet` do bucket para o BigQuery, dentro do conjunto `carbide-eye-466719-s1.datagirls_projetofinal`.

---

## 🔤 Tradução dos dados

A etapa de transformação inclui:

- Tradução de colunas como `Age` → `idade`, `JobRole` → `cargo`, etc.
- Tradução de valores categóricos como:
  - `BusinessTravel`: `"travel_rarely"` → `"raramente"`, `"travel_frequently"` → `"frequentemente"`, `"non_travel"` → `"não viaja"`
  - `Department`: `"sales"` → `"vendas"`, `"research & development"` → `"pesquisa e desenvolvimento"`
  - `MaritalStatus`: `"single"` → `"solteiro(a)"`, `"married"` → `"casado(a)"`, `"divorced"` → `"divorciado(a)"`
  - `JobRole`, `EducationField`, entre outras, foram todas traduzidas

---

## ☁️ GCP

- **Bucket criado:** `etl_datagirlspfinal`
- **Projeto:** `carbide-eye-466719-s1`
- **Conjunto de dados no BigQuery:** `datagirls_projetofinal`
- **Tabela:** `dados_transformados`

---

## 📊 Dashboard

A etapa de BI está sendo desenvolvida com **Looker Studio**, utilizando a tabela carregada no BigQuery. O dashboard exibirá métricas sobre:

- Rotatividade de funcionários (Attrition)
- Perfil dos colaboradores por área, cargo, tempo de empresa, entre outros

*Link em breve...*

---

## ✅ Status do Projeto

- [x] Configuração do ambiente Docker + Airflow
- [x] Script de extração via API do Kaggle
- [x] Transformação e tradução completa dos dados
- [x] Upload para o bucket no GCP
- [x] Carga no BigQuery
- [ ] Criação do dashboard Looker Studio

---

## 💡 Aprendizados

Durante o desenvolvimento deste projeto, foram consolidados conhecimentos em:

- Orquestração de pipelines com Airflow
- Utilização da Kaggle API
- Manipulação de dados com Pandas
- Integração com GCP (Storage + BigQuery)
- Organização de projeto de dados com boas práticas

---

## 🤝 Agradecimentos

Este projeto foi desenvolvido por **Marcela** durante o bootcamp da [Data Girls](https://www.datagirls.com.br/). Agradecimentos especiais às instrutoras e à comunidade pela partilha de conhecimento e apoio contínuo. 💜

---

## 📝 Licença

Este projeto é apenas para fins educacionais e não possui fins comerciais.