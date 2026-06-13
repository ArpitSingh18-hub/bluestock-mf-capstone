from pathlib import Path
import pandas as pd
import numpy as np

# =====================================================
# BLUESTOCK MF CAPSTONE
# DAY 4 - PERFORMANCE METRICS
# =====================================================

BASE_DIR = Path(__file__).resolve().parent.parent

NAV_PATH = (
    BASE_DIR
    / "data"
    / "processed"
    / "02_nav_history_clean.csv"
)

OUTPUT_PATH = (
    BASE_DIR
    / "data"
    / "processed"
    / "performance_metrics.csv"
)

# -----------------------------------------------------
# ASSUMPTIONS
# -----------------------------------------------------

RISK_FREE_RATE = 0.06

# -----------------------------------------------------
# LOAD NAV DATA
# -----------------------------------------------------

nav = pd.read_csv(NAV_PATH)

nav["date"] = pd.to_datetime(
    nav["date"]
)

# -----------------------------------------------------
# MARKET PROXY
# Average NAV across all schemes
# Used for Beta and Alpha calculations
# -----------------------------------------------------

market_nav = (
    nav
    .groupby("date")["nav"]
    .mean()
    .reset_index()
)

market_nav["market_return"] = (
    market_nav["nav"]
    .pct_change()
)

# -----------------------------------------------------
# STORE RESULTS
# -----------------------------------------------------

results = []

# -----------------------------------------------------
# PROCESS EACH FUND
# -----------------------------------------------------

for fund in nav["amfi_code"].unique():

    df = nav[
        nav["amfi_code"] == fund
    ].copy()

    df = df.sort_values(
        "date"
    )

    if len(df) < 30:
        continue

    # -------------------------------------------------
    # CAGR
    # -------------------------------------------------

    start_nav = df["nav"].iloc[0]

    end_nav = df["nav"].iloc[-1]

    trading_days = len(df)

    cagr = (
        (end_nav / start_nav)
        **
        (252 / trading_days)
        -
        1
    )

    # -------------------------------------------------
    # DAILY RETURNS
    # -------------------------------------------------

    df["daily_return"] = (
        df["nav"]
        .pct_change()
    )

    returns = (
        df["daily_return"]
        .dropna()
    )

    if len(returns) < 20:
        continue

    # -------------------------------------------------
    # VOLATILITY
    # -------------------------------------------------

    volatility = (
        returns.std()
        *
        np.sqrt(252)
    )

    # -------------------------------------------------
    # SHARPE RATIO
    # -------------------------------------------------

    annual_return = (
        returns.mean()
        *
        252
    )

    sharpe = (
        annual_return
        -
        RISK_FREE_RATE
    ) / volatility

    # -------------------------------------------------
    # BETA
    # -------------------------------------------------

    merged = pd.merge(
        df[
            [
                "date",
                "daily_return"
            ]
        ],
        market_nav[
            [
                "date",
                "market_return"
            ]
        ],
        on="date",
        how="inner"
    )

    merged = merged.dropna()

    beta = (
        merged["daily_return"]
        .cov(
            merged["market_return"]
        )
        /
        merged["market_return"]
        .var()
    )

    # -------------------------------------------------
    # ALPHA
    # CAPM APPROACH
    # -------------------------------------------------

    market_return_annual = (
        merged["market_return"]
        .mean()
        *
        252
    )

    expected_return = (
        RISK_FREE_RATE
        +
        beta
        *
        (
            market_return_annual
            -
            RISK_FREE_RATE
        )
    )

    alpha = (
        annual_return
        -
        expected_return
    )

    # -------------------------------------------------
    # VALUE AT RISK (95%)
    # Historical Method
    # -------------------------------------------------

    var95 = np.percentile(
        returns,
        5
    )

    # -------------------------------------------------
    # STORE RESULTS
    # -------------------------------------------------

    results.append(
        [
            fund,
            cagr,
            volatility,
            sharpe,
            beta,
            alpha,
            var95
        ]
    )

# -----------------------------------------------------
# CREATE OUTPUT DATAFRAME
# -----------------------------------------------------

metrics = pd.DataFrame(
    results,
    columns=[
        "amfi_code",
        "cagr",
        "volatility",
        "sharpe_ratio",
        "beta",
        "alpha",
        "var_95"
    ]
)

# -----------------------------------------------------
# SAVE RESULTS
# -----------------------------------------------------

metrics.to_csv(
    OUTPUT_PATH,
    index=False
)

# -----------------------------------------------------
# DISPLAY RESULTS
# -----------------------------------------------------

print("=" * 60)
print("PERFORMANCE METRICS GENERATED")
print("=" * 60)

print(metrics.head())

print(
    f"\nTotal Funds Processed: {len(metrics)}"
)

print(
    f"\nSaved: {OUTPUT_PATH}"
)