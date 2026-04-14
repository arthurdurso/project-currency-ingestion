import logging
import os

import dlt
from dlt.destinations import filesystem
from ingestion.source import freecurrency_source

logger = logging.getLogger(__name__)

def build_pipeline() -> dlt.Pipeline:
    """Builds and returns the dlt pipeline configured for MinIO."""
    bucket_url = os.environ["DESTINATION__FILESYSTEM__BUCKET_UFRL"]

    pipeline = filesystem(
        bucket_url=bucket_url,
        credentials={
            "aws_access_key_id": os.environ[
                "DESTINATION__FILESYSTEM__CREDENTIALS__AWS_ACCESS_KEY_ID"
            ],
            "aws_secret_access_key": os.environ[
                "DESTINATION__FILESYSTEM__CREDENTIALS__AWS_SECRET_ACCESS_KEY"
            ],
            "endpoint_url": os.environ[
                "DESTINATION__FILESYSTEM__CREDENTIALS__ENDPOINT_URL"
            ],
        },
    )

    pipeline = dlt.pipeline(
        pipeline_name="freecurrency_pipeline",
        destination=pipeline,
        dataset_name="latest", # subfolder inside the bucket
    )
    
    return pipeline
