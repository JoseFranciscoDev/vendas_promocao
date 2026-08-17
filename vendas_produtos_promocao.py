import os

import pandas as pd

sheet_id = os.getenv("sheet_id")
gid = os.getenv("gid")

url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid={gid}"

df = (
    pd.read_csv(url, skiprows=3, header=0)
    .dropna(how="all")["COD PROD."]
    .dropna()
    .astype(int)
)

codes_list = df.tolist()

df.to_csv(
    "vendas.csv",
    index=False,
)

query = os.getenv("query_sql")
