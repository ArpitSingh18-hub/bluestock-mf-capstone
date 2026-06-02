from pathlib import Path
from datetime import datetime
import requests
import pandas as pd
import time

# ======================================================
# BLUESTOCK MF CAPSTONE
# DAY 1 TASK 5
# MULTIPLE NAV INGESTION PIPELINE
# ======================================================

AMFI_CODES = [
    "119551",
    "120503",
    "118632",
    "119092",
    "120841"
]

# ======================================================
# PATHS
# ======================================================

BASE_DIR = Path(__file__).resolve().parent.parent

RAW_DIR = BASE_DIR / "data" / "raw"

API_DIR = RAW_DIR / "api_nav"

REPORT_DIR = BASE_DIR / "reports"

API_DIR.mkdir(
    parents=True,
    exist_ok=True
)

REPORT_DIR.mkdir(
    parents=True,
    exist_ok=True
)

COMBINED_FILE = (
    RAW_DIR
    / "combined_live_nav.csv"
)

REPORT_FILE = (
    REPORT_DIR
    / "multiple_nav_fetch_report.md"
)

# ======================================================
# PIPELINE START
# ======================================================

start_time = time.time()

print("=" * 60)
print("MULTIPLE NAV INGESTION PIPELINE")
print("=" * 60)

master_data = []

success_count = 0

failure_count = 0

# ======================================================
# PROCESS EACH FUND
# ======================================================

for code in AMFI_CODES:

    print(f"\nFetching AMFI Code: {code}")

    try:

        url = (
            f"https://api.mfapi.in/mf/{code}"
        )

        response = requests.get(
            url,
            timeout=20
        )

        response.raise_for_status()

        data = response.json()

        meta = data["meta"]

        latest = data["data"][0]

        record = {

            "amfi_code":
            meta.get("scheme_code"),

            "scheme_name":
            meta.get("scheme_name"),

            "fund_house":
            meta.get("fund_house"),

            "scheme_type":
            meta.get("scheme_type"),

            "scheme_category":
            meta.get("scheme_category"),

            "latest_nav":
            latest.get("nav"),

            "nav_date":
            latest.get("date"),

            "api_fetch_timestamp":
            datetime.now()
        }

        # ------------------------------------------
        # Individual CSV
        # ------------------------------------------

        df = pd.DataFrame(
            [record]
        )

        output_file = (
            API_DIR
            / f"{code}.csv"
        )

        df.to_csv(
            output_file,
            index=False
        )

        print(
            f"Saved: {code}.csv"
        )

        master_data.append(
            record
        )

        success_count += 1

    except Exception as e:

        print(
            f"Failed: {code}"
        )

        print(e)

        failure_count += 1

# ======================================================
# COMBINED DATASET
# ======================================================

combined_df = pd.DataFrame(
    master_data
)

combined_df.to_csv(
    COMBINED_FILE,
    index=False
)

# ======================================================
# DATA QUALITY SUMMARY
# ======================================================

rows = len(combined_df)

columns = len(combined_df.columns)

missing_values = (
    combined_df
    .isnull()
    .sum()
    .sum()
)

duplicates = (
    combined_df
    .duplicated()
    .sum()
)

# ======================================================
# REPORT
# ======================================================

runtime = round(
    time.time() - start_time,
    2
)

with open(
    REPORT_FILE,
    "w",
    encoding="utf-8"
) as f:

    f.write(
        "# Multiple NAV Fetch Report\n\n"
    )

    f.write(
        f"Execution Date: "
        f"{datetime.now()}\n\n"
    )

    f.write(
        "## Summary\n\n"
    )

    f.write(
        f"Funds Requested: "
        f"{len(AMFI_CODES)}\n\n"
    )

    f.write(
        f"Successful Fetches: "
        f"{success_count}\n\n"
    )

    f.write(
        f"Failed Fetches: "
        f"{failure_count}\n\n"
    )

    f.write(
        "## Data Quality\n\n"
    )

    f.write(
        f"Rows: {rows}\n\n"
    )

    f.write(
        f"Columns: {columns}\n\n"
    )

    f.write(
        f"Missing Values: "
        f"{missing_values}\n\n"
    )

    f.write(
        f"Duplicate Rows: "
        f"{duplicates}\n\n"
    )

    f.write(
        f"Runtime: "
        f"{runtime} seconds\n"
    )

# ======================================================
# FINAL SUMMARY
# ======================================================

print("\n" + "=" * 60)

print("PIPELINE SUMMARY")

print("=" * 60)

print(
    f"Funds Processed : "
    f"{success_count}"
)

print(
    f"Failed Requests : "
    f"{failure_count}"
)

print(
    f"Combined Rows   : "
    f"{rows}"
)

print(
    f"Missing Values  : "
    f"{missing_values}"
)

print(
    f"Duplicates      : "
    f"{duplicates}"
)

print(
    f"Runtime         : "
    f"{runtime} sec"
)

print("\nCombined CSV Saved")

print(COMBINED_FILE)

print("\nReport Generated")

print(REPORT_FILE)

print("\nTask 5 Completed Successfully")