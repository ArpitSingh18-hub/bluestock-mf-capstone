from pathlib import Path
import pandas as pd

from sqlalchemy import (
    create_engine,
    text
)

# ============================================================
# PATHS
# ============================================================

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

# ============================================================
# DATABASE ENGINE
# ============================================================

print("=" * 60)
print("SQLITE DATA WAREHOUSE LOADER")
print("=" * 60)

engine = create_engine(
    f"sqlite:///{DB_PATH}"
)

# ============================================================
# CREATE SCHEMA
# ============================================================

with open(
    SCHEMA_PATH,
    "r",
    encoding="utf-8"
) as f:

    schema_sql = f.read()

with engine.begin() as conn:

    for statement in schema_sql.split(";"):

        statement = statement.strip()

        if statement:
            conn.execute(text(statement))

print("Schema Created")

# ============================================================
# DIM FUND
# ============================================================

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
    engine,
    if_exists="append",
    index=False
)

print(
    f"dim_fund loaded: {len(dim_fund)} rows"
)

# ============================================================
# FACT NAV
# ============================================================

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
    engine,
    if_exists="append",
    index=False
)

print(
    f"fact_nav loaded: {len(nav_df)} rows"
)

# ============================================================
# FACT PERFORMANCE
# ============================================================

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
    engine,
    if_exists="append",
    index=False
)

print(
    f"fact_performance loaded: {len(fact_perf)} rows"
)

# ============================================================
# FACT TRANSACTIONS
# ============================================================

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
    engine,
    if_exists="append",
    index=False
)

print(
    f"fact_transactions loaded: {len(fact_txn)} rows"
)

# ============================================================
# VERIFY TABLES
# ============================================================

tables = pd.read_sql(
    """
    SELECT name
    FROM sqlite_master
    WHERE type='table'
    ORDER BY name
    """,
    engine
)

print("\nTables Created")

for table in tables["name"]:
    print(table)

# ============================================================
# RECORD COUNTS
# ============================================================

print("\nRow Counts")

for table in [
    "dim_fund",
    "fact_nav",
    "fact_performance",
    "fact_transactions"
]:

    count = pd.read_sql(
        f"""
        SELECT COUNT(*) AS total_rows
        FROM {table}
        """,
        engine
    )

    print(
        f"{table}: {count.iloc[0]['total_rows']} rows"
    )

# ============================================================
# CLEANUP
# ============================================================

engine.dispose()

print("\nDatabase Build Complete")
print(DB_PATH)