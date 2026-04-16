# 💱 Currency Data Ingestion Pipeline

> Exchange rate data ingestion pipeline orchestrated with Apache Airflow, efficient Parquet storage, and a fully containerized environment.

---

## 📌 About the Project

The **Currency Data Ingestion Pipeline** is a data engineering project that automates the extraction of exchange rate data from the [FreeCurrency API](https://freecurrencyapi.com/), orchestrates execution with **Apache Airflow**, and stores data in **Parquet** format on **MinIO** — an S3-compatible object storage.

The project simulates a real Data Engineering workflow with orchestration, versioning, and efficient storage, serving as a best-practices reference for data ingestion pipelines.

---

## 🏗️ Architecture

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

## 🚀 Tech Stack

| Technology | Role |
|---|---|
| **Python 3.13** | Main language |
| **Apache Airflow** | Pipeline orchestration |
| **dlt** | Data ingestion and loading |
| **MinIO (S3-compatible)** | Data Lake / object storage |
| **Docker & Docker Compose** | Environment containerization |
| **Poetry** | Dependency management |
| **Parquet** | Efficient columnar storage format |

---

## ⚙️ Getting Started

### Prerequisites

- [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/) installed
- API key from [FreeCurrency API](https://freecurrencyapi.com/)

### 1. Clone the repository

```bash
git clone https://github.com/your-username/currency-data-ingestion-pipeline.git
cd currency-data-ingestion-pipeline
```

### 2. Set up environment variables

Create a `.env` file at the project root based on the example below:

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

Also configure the `.dlt/secrets.toml` file with your FreeCurrency API key:

```toml
[sources.freecurrency]
api_key = "your_api_key_here"
```

> 💡 Use `.dlt/example-secrets.toml` as a reference.

### 3. Build and start the environment

```bash
docker compose up --build
```

### 4. Access the interfaces

| Service | URL | Default credentials |
|---|---|---|
| **Airflow** | http://localhost:8080 | `airflow` / `airflow` |
| **MinIO** | http://localhost:9001 | defined in `.env` |

### 5. Run the pipeline

In Airflow, enable and manually trigger the DAG:

```
freecurrency_hourly_ingestion
```

---

## 📂 Project Structure

```
project-currency-inge.../
├── .dlt/
│   ├── example-secrets.toml               # Secrets configuration example
│   └── secrets.toml                       # dlt secrets (not versioned)
├── dags/
│   └── currency_ingestion_dag.py          # Main Airflow DAG
├── ingestion/
│   ├── __init__.py
│   ├── pipeline.py                        # dlt pipeline setup and execution
│   └── source.py                          # Data source definition (FreeCurrency API)
├── scripts/                               # Helper scripts
├── .dockerignore
├── .env                                   # Environment variables (not versioned)
├── .env.example                           # Environment variables example
├── .gitignore
├── .python-version                        # Project Python version
├── docker-compose.yml                     # Container orchestration
├── Dockerfile
├── poetry.lock                            # Dependency lock file
├── pyproject.toml                         # Dependencies via Poetry
└── README.md
```

---

## 📊 How Data is Stored

After each DAG execution, data is automatically stored in MinIO:

```
s3://currency-raw/
  └── latest/
      └── _dlt_loads/
            └── <timestamp>_exchange_rates.parquet
```

- Each run generates a new file with an **ingestion timestamp**
- **Parquet** format ensures efficient compression and fast reads
- The structure simulates a **raw layer Data Lake**

---

## ✨ Highlights

- ✅ **Real orchestration** with Apache Airflow (DAGs, scheduling, retries)
- ✅ **Data Lake simulation** with S3-compatible MinIO
- ✅ **Parquet format** for efficient storage and analytical reads
- ✅ **100% containerized environment** with Docker Compose
- ✅ **Dependency management** with Poetry
- ✅ **Data Engineering best practices** applied end-to-end

---

## 📄 License

This project does not yet have a defined license. Feel free to reach out for more information.

---

<p align="center">
  Built with 🛠️ and Data Engineering best practices
</p>
