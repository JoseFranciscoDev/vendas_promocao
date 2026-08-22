import os

import pandas as pd
from dotenv import load_dotenv

load_dotenv()

# sheet_id = os.getenv("sheet_id")
# gid = os.getenv("gid")

# url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid={gid}"

# df = (
#     pd.read_csv(url, skiprows=3, header=0)
#     .dropna(how="all")["COD PROD."]
#     .dropna()
#     .astype(int)
# )

# codes_list = df.tolist()

query = os.getenv("query_sql")
print(query)
