from os import getenv

import pandas as pd
from dotenv import load_dotenv

load_dotenv()
with open("./query.sql") as q:
    query_sql = q.read()

sheet_id = getenv("sheet_id")
gid = getenv("gid")

url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid={gid}"

df = (
    pd.read_csv(url, skiprows=3, header=0)
    .dropna(how="all")["COD PROD."]
    .dropna()
    .astype(int)
)

code_list = df.tolist()
first_metad_query = query_sql[:1135]
second_metad_query = query_sql[1135:]

for code in code_list:
    if code_list.index(code) == len(code_list) - 1:
        first_metad_query += str(code)
        break
    first_metad_query += str(code) + ","

full_query = first_metad_query + second_metad_query
