from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent

file_path = (
    BASE_DIR
    / "data"
    / "raw"
    / "01_fund_master.csv"
)

df = pd.read_csv(file_path)

print("="*60)
print("FUND MASTER ANALYSIS")
print("="*60)

print("\nDataset Shape")
print(df.shape)

print("\nTotal Fund Houses")
print(df["fund_house"].nunique())

print("\nFund Houses")
print(sorted(df["fund_house"].unique()))

print("\nTotal Categories")
print(df["category"].nunique())

print("\nCategories")
print(sorted(df["category"].unique()))

print("\nTotal Sub Categories")
print(df["sub_category"].nunique())

print("\nRisk Categories")
print(df["risk_category"].value_counts())

print("\nPlan Types")
print(df["plan"].value_counts())

print("\nExpense Ratio Summary")
print(df["expense_ratio_pct"].describe())

print("\nTop 5 Highest Expense Ratio Funds")

print(
    df[
        [
            "scheme_name",
            "expense_ratio_pct"
        ]
    ]
    .sort_values(
        "expense_ratio_pct",
        ascending=False
    )
    .head(5)
)