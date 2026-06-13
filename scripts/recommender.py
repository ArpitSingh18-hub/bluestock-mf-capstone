# =====================================================
# BLUESTOCK MF CAPSTONE
# FUND RECOMMENDER SYSTEM
# =====================================================

import pandas as pd
from pathlib import Path

# ==========================================
# PATHS
# ==========================================

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = (
    BASE_DIR
    / "data"
    / "processed"
    / "07_scheme_performance_clean.csv"
)

# ==========================================
# LOAD DATA
# ==========================================

df = pd.read_csv(DATA_PATH)

# ==========================================
# USER INPUT
# ==========================================

print("=" * 60)
print("BLUESTOCK FUND RECOMMENDER")
print("=" * 60)

print("\nAvailable Risk Levels:")

print("1. Low")
print("2. Moderate")
print("3. High")
print("4. Very High")
print("5. Moderately High")

risk = input(
    "\nEnter Risk Appetite: "
).strip()

# ==========================================
# FILTER
# ==========================================

filtered = df[
    df["risk_grade"].str.lower()
    ==
    risk.lower()
]

# ==========================================
# CHECK
# ==========================================

if filtered.empty:

    print("\nNo matching funds found.")

else:

    recommendations = (

        filtered

        .sort_values(

            "sharpe_ratio",

            ascending=False

        )

        .head(3)

    )

    print("\n")
    print("=" * 60)
    print("TOP 3 RECOMMENDED FUNDS")
    print("=" * 60)

    print(

        recommendations[
            [
                "scheme_name",
                "fund_house",
                "category",
                "risk_grade",
                "sharpe_ratio",
                "return_5yr_pct",
                "aum_crore"
            ]
        ]

        .to_string(index=False)

    )

print("\nDone.")