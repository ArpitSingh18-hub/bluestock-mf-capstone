from pathlib import Path
import pandas as pd

# =====================================================
# BLUESTOCK MF CAPSTONE
# DAY 2 - DATA CLEANING PIPELINE
# =====================================================

BASE_DIR = Path(__file__).resolve().parent.parent

RAW_DIR = BASE_DIR / "data" / "raw"
PROCESSED_DIR = BASE_DIR / "data" / "processed"

PROCESSED_DIR.mkdir(
    parents=True,
    exist_ok=True
)

print("=" * 60)
print("DATA CLEANING PIPELINE")
print("=" * 60)

summary = []

# =====================================================
# PROCESS ALL CSV FILES
# =====================================================

for file in RAW_DIR.glob("*.csv"):

    print(f"\nProcessing: {file.name}")

    df = pd.read_csv(file)

    original_rows = len(df)

    # -------------------------------
    # Remove duplicates
    # -------------------------------

    duplicates_removed = df.duplicated().sum()

    df = df.drop_duplicates()

    # -------------------------------
    # Missing Value Handling
    # -------------------------------

    missing_before = df.isnull().sum().sum()

    # Numeric columns

    numeric_cols = df.select_dtypes(
        include=["number"]
    ).columns

    for col in numeric_cols:

        df[col] = df[col].fillna(
            df[col].median()
        )

    # Object columns

    object_cols = df.select_dtypes(
        include=["object"]
    ).columns

    for col in object_cols:

        df[col] = df[col].fillna(
            "Unknown"
        )

    missing_after = (
        df.isnull().sum().sum()
    )

    # -------------------------------
    # Date Conversion
    # -------------------------------

    for col in df.columns:

        if "date" in col.lower():

            try:

                df[col] = pd.to_datetime(
                    df[col],
                    errors="coerce"
                )

            except:

                pass

    # -------------------------------
    # Standardize Text
    # -------------------------------

    for col in object_cols:

        df[col] = (
            df[col]
            .astype(str)
            .str.strip()
        )

    # -------------------------------
    # Save Clean File
    # -------------------------------

    output_file = (
        PROCESSED_DIR
        / f"{file.stem}_clean.csv"
    )

    df.to_csv(
        output_file,
        index=False
    )

    summary.append({

        "dataset": file.name,

        "rows": original_rows,

        "duplicates_removed":
        duplicates_removed,

        "missing_before":
        missing_before,

        "missing_after":
        missing_after
    })

    print(
        f"Saved: {output_file.name}"
    )

# =====================================================
# SUMMARY REPORT
# =====================================================

summary_df = pd.DataFrame(summary)

report_file = (
    BASE_DIR
    / "reports"
    / "cleaning_report.md"
)

with open(
    report_file,
    "w",
    encoding="utf-8"
) as f:

    f.write("# Data Cleaning Report\n\n")

    f.write(
        summary_df.to_markdown(
            index=False
        )
    )

print("\nCleaning Completed")
print(report_file)