# Parquet Reader Script

from pathlib import Path
import pandas as pd

base_path = Path("local_data") / "latest" / "latest_rates"

df = pd.read_parquet(base_path)

pivot = df.pivot(
    index="extracted_at",
    columns="target_currency",
    values="rate"
).sort_index()

print(pivot)