import sqlite3
import pandas as pd

conn=sqlite3.connect("data/db/bluestock_mf.db")

df=pd.read_sql(
"SELECT * FROM dim_fund LIMIT 5",
conn)

print(df.columns.tolist())

df=pd.read_sql(
"SELECT * FROM fact_nav LIMIT 5",
conn)

print(df.columns.tolist())