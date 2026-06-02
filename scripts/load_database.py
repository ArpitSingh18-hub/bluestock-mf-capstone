from pathlib import Path
import pandas as pd
import sqlite3

BASE_DIR = Path(__file__).resolve().parent.parent

DB_PATH = (
    BASE_DIR
    / "data"
    / "db"
    / "bluestock_mf.db"
)

SCHEMA_PATH = (
    BASE_DIR
    / "sql"
    / "schema.sql"
)

PROCESSED_DIR = (
    BASE_DIR
    / "data"
    / "processed"
)

print("=" * 60)
print("SQLITE DATA WAREHOUSE LOADER")
print("=" * 60)

conn = sqlite3.connect(DB_PATH)

with open(
    SCHEMA_PATH,
    "r",
    encoding="utf-8"
) as f:

    conn.executescript(f.read())

print("Schema Created")

# ------------------------
# DIM FUND
# ------------------------

fund_df = pd.read_csv(
    PROCESSED_DIR
    / "01_fund_master_clean.csv"
)

dim_fund = fund_df[
    [
        "amfi_code",
        "fund_house",
        "scheme_name",
        "category",
        "sub_category",
        "plan",
        "risk_category",
        "expense_ratio_pct"
    ]
]

dim_fund.to_sql(
    "dim_fund",
    conn,
    if_exists="append",
    index=False
)

print(
    f"dim_fund loaded: {len(dim_fund)} rows"
)

# ------------------------
# FACT NAV
# ------------------------

nav_df = pd.read_csv(
    PROCESSED_DIR
    / "02_nav_history_clean.csv"
)

nav_df.columns = [
    "amfi_code",
    "nav_date",
    "nav"
]

nav_df.to_sql(
    "fact_nav",
    conn,
    if_exists="append",
    index=False
)

print(
    f"fact_nav loaded: {len(nav_df)} rows"
)

# ------------------------
# FACT PERFORMANCE
# ------------------------

perf_df = pd.read_csv(
    PROCESSED_DIR
    / "07_scheme_performance_clean.csv"
)

fact_perf = perf_df[
    [
        "amfi_code",
        "return_1yr_pct",
        "return_3yr_pct",
        "return_5yr_pct",
        "alpha",
        "beta",
        "sharpe_ratio"
    ]
]

fact_perf.to_sql(
    "fact_performance",
    conn,
    if_exists="append",
    index=False
)

print(
    f"fact_performance loaded: {len(fact_perf)} rows"
)

# ------------------------
# FACT TRANSACTIONS
# ------------------------

txn_df = pd.read_csv(
    PROCESSED_DIR
    / "08_investor_transactions_clean.csv"
)

fact_txn = txn_df[
    [
        "investor_id",
        "transaction_date",
        "amfi_code",
        "amount_inr",
        "state",
        "city"
    ]
]

fact_txn.to_sql(
    "fact_transactions",
    conn,
    if_exists="append",
    index=False
)

print(
    f"fact_transactions loaded: {len(fact_txn)} rows"
)

cursor = conn.cursor()

tables = cursor.execute(
    """
    SELECT name
    FROM sqlite_master
    WHERE type='table';
    """
).fetchall()

print("\nTables Created")

for t in tables:
    print(t[0])

conn.close()

print("\nDatabase Build Complete")
print(DB_PATH)