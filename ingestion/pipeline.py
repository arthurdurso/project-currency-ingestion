import dlt
import logging
import os
from dlt.destinations import filesystem
from dotenv import load_dotenv
from ingestion.source import freecurrency_source

load_dotenv()

logger = logging.getLogger(__name__)

def build_pipeline() -> dlt.Pipeline:
    """Builds and returns the dlt pipeline configured for MinIO."""
    bucket_url = os.environ["MINIO_BUCKET_URL"]
    
    destination = filesystem(
        bucket_url=bucket_url,
        credentials={
            "aws_access_key_id": os.environ[
                "MINIO_ROOT_USER"
            ],
            "aws_secret_access_key": os.environ[
                "MINIO_ROOT_PASSWORD"
            ],
            "endpoint_url": os.environ[
                "MINIO_ENDPOINT_URL"
            ],
        },
    )

    pipeline = dlt.pipeline(
        pipeline_name="freecurrency_pipeline",
        destination=destination,
        dataset_name="latest", # subfolder inside the bucket
    )
    
    return pipeline


def run_pipeline() -> dict:
    """
    Runs the pipeline and returns a summary with basic matrics.
    
    Returns:
        dict with pipeline_name, rows_loaded and load_id.
    """
    pipeline = build_pipeline()

    source = freecurrency_source()

    logger.info("Starting FreeCurrency -> MinIO Ingestion")
    load_info = pipeline.run(
        source,
        loader_file_format="parquet",
    )

    rows_loaded = sum(
        p.jobs["completed_jobs"].__len__()
        for p in load_info.load_packages
        if p.jobs.get("completed_jobs")
    )

    logger.info(
        "Ingestao Concluida. load_id: %s, load_packages: %d",
        load_info.loads_ids[0] if load_info.loads_ids else None,
        len(load_info.load_packages),
    )

    return {
        "pipeline_name": pipeline.pipeline_name,
        "load_id": load_info.loads_ids[0] if load_info.loads_ids else None,
        "rows_loaded": rows_loaded,
    }

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    result = run_pipeline()
    print(result)

