# Pipeline script for ingesting from FreeCurrency API using DLT

import dlt
from dlt.destinations import filesystem
from ingestion.source import freecurrency_source
from pathlib import Path


local_destination = filesystem(
        bucket_url=Path("local_data").resolve().as_uri()
    )
pipeline = dlt.pipeline(
    pipeline_name="freecurrency_pipeline",
    destination=local_destination,   # salva em disco local
    dataset_name="latest",
)

source = freecurrency_source(api_key=dlt.secrets.value)
load_info = pipeline.run(source, loader_file_format="parquet")
print(load_info)