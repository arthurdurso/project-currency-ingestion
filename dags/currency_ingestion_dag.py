"""
Hourly DAG to ingest currency data from FreeCurrencyAPI and saving it to MinIO in Parquet format.

Schedule: Every hour at minute 0 (cron: 0 * * * *)
Retry: 3 attempts with a delay of 5 minutes.
"""

from __future__ import annotations

import logging
from datetime import datetime, timedelta
from airflow.sdk import dag, task

logger = logging.getLogger(__name__)

DEFAULT_ARGS = {
    "owner": "durso",
    "retries": 3,
    "retry_delay": timedelta(minutes=5),
    "retry_exponential_backoff": False,
    "email_on_failure": False,
    "email_on_retry": False,
}

@dag(
    dag_id="freecurrency_hourly_ingestion",
    description="Ingestão horária das cotações FreeCurrency API → MinIO (Parquet).",
    schedule="0 * * * *",
    start_date=datetime(2025, 1, 1),
    catchup=False,
    max_active_runs=1,
    default_args=DEFAULT_ARGS,
    tags=["ingestion", "currency", "dlt", "minio"],
)
def currency_ingestion_dat() -> None:
    @task(task_id="run_dlt_pipeline")
    def run_dlt_pipeline() -> dict:
        """
        Executes the dlt pipeline.
        Returns a dict with basic metrics for XCom.
        """
        # Import inside the task to ensure PYTHONPATH is resolved
        # in the Airflow worker context.
        from ingestion.pipeline import run_pipeline

        result = run_pipeline()
        logger.info("Pipeline completed: %s", result)
        return result
    
    run_dlt_pipeline()


currency_ingestion_dat()