# Pipeline script for ingesting from FreeCurrency API using DLT


import dlt
from ingestion.source import freecurrency_source

pipeline = dlt.pipeline(
    pipeline_name="freecurrency_pipeline",
    destination="filesystem",   # salva em disco local
    dataset_name="latest",
)

source = freecurrency_source(api_key=dlt.secrets.value)
load_info = pipeline.run(source, loader_file_format="parquet")
print(load_info)