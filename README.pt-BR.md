# 💱 Currency Data Ingestion Pipeline

> Pipeline de ingestão de dados de câmbio com orquestração via Apache Airflow, armazenamento eficiente em Parquet e ambiente totalmente containerizado.

---

## 📌 Sobre o Projeto

O **Currency Data Ingestion Pipeline** é um projeto de engenharia de dados que automatiza a extração de dados de câmbio a partir da [FreeCurrency API](https://freecurrencyapi.com/), orquestra a execução com **Apache Airflow** e armazena os dados em formato **Parquet** no **MinIO** — um storage S3-compatible.

O projeto simula um fluxo real de Data Engineering com orquestração, versionamento e armazenamento eficiente, servindo como referência de boas práticas para pipelines de ingestão de dados.

---

## 🏗️ Arquitetura

```
FreeCurrency API
      │
      ▼
  Apache Airflow  ──►  dlt (Data Load Tool)
      │
      ▼
   MinIO (S3)
  └── currency-raw/
        └── latest/
              └── *.parquet
```

---

## 🚀 Tecnologias

| Tecnologia | Função |
|---|---|
| **Python 3.13** | Linguagem principal |
| **Apache Airflow** | Orquestração de pipelines |
| **dlt** | Ingestão e transformação de dados |
| **MinIO (S3-compatible)** | Data Lake / armazenamento de objetos |
| **Docker & Docker Compose** | Containerização do ambiente |
| **Poetry** | Gerenciamento de dependências |
| **Parquet** | Formato de armazenamento colunar eficiente |

---

## ⚙️ Como Rodar o Projeto

### Pré-requisitos

- [Docker](https://www.docker.com/) e [Docker Compose](https://docs.docker.com/compose/) instalados
- Chave de API da [FreeCurrency API](https://freecurrencyapi.com/)

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/currency-data-ingestion-pipeline.git
cd currency-data-ingestion-pipeline
```

### 2. Configure as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto com base no exemplo abaixo:

```env
# FreeCurrency API
FREECURRENCY_API_KEY=your_api_key_here

# MinIO
MINIO_ROOT_USER=minioadmin
MINIO_ROOT_PASSWORD=minioadmin
MINIO_ENDPOINT=http://minio:9000
MINIO_BUCKET=currency-raw

# Airflow
AIRFLOW_UID=50000
AIRFLOW__CORE__FERNET_KEY=your_fernet_key_here
```

Configure também o arquivo `.dlt/secrets.toml` com sua chave da FreeCurrency API:

```toml
[sources.freecurrency]
api_key = "your_api_key_here"
```

> 💡 Use o arquivo `.dlt/example-secrets.toml` como referência.

### 3. Suba o ambiente

```bash
docker compose up --build
```

### 4. Acesse as interfaces

| Serviço | URL | Credenciais padrão |
|---|---|---|
| **Airflow** | http://localhost:8080 | `airflow` / `airflow` |
| **MinIO** | http://localhost:9001 | definidas no `.env` |

### 5. Execute o pipeline

No Airflow, ative e execute manualmente a DAG:

```
freecurrency_hourly_ingestion
```

---

## 📂 Estrutura do Projeto

```
project-currency-inge.../
├── .dlt/
│   ├── example-secrets.toml               # Exemplo de configuração de secrets
│   └── secrets.toml                       # Secrets do dlt (não versionado)
├── dags/
│   └── currency_ingestion_dag.py          # DAG principal do Airflow
├── ingestion/
│   ├── __init__.py
│   ├── pipeline.py                        # Configuração e execução do pipeline dlt
│   └── source.py                          # Definição da fonte de dados (FreeCurrency API)
├── scripts/                               # Scripts auxiliares
├── .dockerignore
├── .env                                   # Variáveis de ambiente (não versionado)
├── .env.example                           # Exemplo de variáveis de ambiente
├── .gitignore
├── .python-version                        # Versão do Python do projeto
├── docker-compose.yml                     # Orquestração dos containers
├── Dockerfile
├── poetry.lock                            # Lock de dependências
├── pyproject.toml                         # Dependências via Poetry
└── README.md
```

---

## 📊 Como os Dados São Armazenados

Após cada execução da DAG, os dados são armazenados automaticamente no MinIO:

```
s3://currency-raw/
  └── latest/
      └── _dlt_loads/
            └── <timestamp>_exchange_rates.parquet
```

- Cada execução gera um novo arquivo com **timestamp de ingestão**
- O formato **Parquet** garante compressão eficiente e leitura rápida
- A estrutura simula um **Data Lake** de camada raw

---

## ✨ Destaques

- ✅ **Orquestração real** com Apache Airflow (DAGs, agendamento, retries)
- ✅ **Simulação de Data Lake** com MinIO S3-compatible
- ✅ **Formato Parquet** para eficiência de armazenamento e leitura analítica
- ✅ **Ambiente 100% containerizado** com Docker Compose
- ✅ **Gerenciamento de dependências** com Poetry
- ✅ **Boas práticas de Data Engineering** aplicadas do início ao fim

---

## 📄 Licença

Este projeto ainda não possui uma licença definida. Entre em contato para mais informações.

---

<p align="center">
  Feito com 🛠️ e boas práticas de Data Engineering
</p>
