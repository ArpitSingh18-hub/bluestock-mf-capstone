from pathlib import Path
import pandas as pd

# =====================================================
# BLUESTOCK MF CAPSTONE
# DAY 2 - DATA CLEANING PIPELINE
# =====================================================

BASE_DIR = Path(__file__).resolve().parent.parent

RAW_DIR = (
    BASE_DIR
    / "data"
    / "raw"
)

PROCESSED_DIR = (
    BASE_DIR
    / "data"
    / "processed"
)

REPORTS_DIR = (
    BASE_DIR
    / "reports"
)

PROCESSED_DIR.mkdir(
    parents=True,
    exist_ok=True
)

REPORTS_DIR.mkdir(
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

    # -------------------------------------------------
    # REMOVE DUPLICATES
    # -------------------------------------------------

    duplicates_removed = df.duplicated().sum()

    df = df.drop_duplicates()

    # -------------------------------------------------
    # MISSING VALUE HANDLING
    # -------------------------------------------------

    missing_before = (
        df.isnull()
        .sum()
        .sum()
    )

    numeric_cols = df.select_dtypes(
        include=["number"]
    ).columns

    for col in numeric_cols:

        df[col] = df[col].fillna(
            df[col].median()
        )

    object_cols = df.select_dtypes(
        include=["object"]
    ).columns

    for col in object_cols:

        df[col] = df[col].fillna(
            "Unknown"
        )

    # -------------------------------------------------
    # DATE CONVERSION
    # -------------------------------------------------

    date_cols = []

    for col in df.columns:

        if "date" in col.lower():

            try:

                df[col] = pd.to_datetime(
                    df[col],
                    errors="coerce"
                )

                date_cols.append(col)

            except Exception:
                pass

    # -------------------------------------------------
    # TEXT STANDARDIZATION
    # -------------------------------------------------

    object_cols = df.select_dtypes(
        include=["object"]
    ).columns

    for col in object_cols:

        df[col] = (
            df[col]
            .astype(str)
            .str.strip()
            .str.replace(
                r"\s+",
                " ",
                regex=True
            )
        )

    # -------------------------------------------------
    # NAV DATA SPECIAL HANDLING
    # WEEKENDS + HOLIDAYS
    # -------------------------------------------------

    if (
        "nav" in df.columns
        and
        len(date_cols) > 0
    ):

        date_col = date_cols[0]

        try:

            df = df.sort_values(
                date_col
            )

            if "amfi_code" in df.columns:

                cleaned_groups = []

                for scheme in df["amfi_code"].unique():

                    temp = df[
                        df["amfi_code"] == scheme
                    ].copy()

                    temp = (
                        temp
                        .set_index(date_col)
                    )

                    full_dates = pd.date_range(
                        start=temp.index.min(),
                        end=temp.index.max(),
                        freq="D"
                    )

                    temp = temp.reindex(
                        full_dates
                    )

                    temp["nav"] = (
                        temp["nav"]
                        .ffill()
                    )

                    temp["amfi_code"] = (
                        temp["amfi_code"]
                        .ffill()
                    )

                    temp = (
                        temp
                        .reset_index()
                    )

                    temp.rename(
                        columns={
                            "index": date_col
                        },
                        inplace=True
                    )

                    cleaned_groups.append(
                        temp
                    )

                df = pd.concat(
                    cleaned_groups,
                    ignore_index=True
                )

        except Exception as e:

            print(
                f"Weekend handling skipped: {e}"
            )

    # -------------------------------------------------
    # FINAL MISSING CHECK
    # -------------------------------------------------

    missing_after = (
        df.isnull()
        .sum()
        .sum()
    )

    # -------------------------------------------------
    # SAVE CLEAN FILE
    # -------------------------------------------------

    output_file = (
        PROCESSED_DIR
        / f"{file.stem}_clean.csv"
    )

    df.to_csv(
        output_file,
        index=False
    )

    summary.append({

        "dataset":
        file.name,

        "rows":
        original_rows,

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
# CLEANING REPORT
# =====================================================

summary_df = pd.DataFrame(
    summary
)

report_file = (
    REPORTS_DIR
    / "cleaning_report.md"
)

with open(
    report_file,
    "w",
    encoding="utf-8"
) as f:

    f.write(
        "# Data Cleaning Report\n\n"
    )

    f.write(
        "## Summary\n\n"
    )

    f.write(
        summary_df.to_markdown(
            index=False
        )
    )

    f.write(
        "\n\n## Cleaning Steps Applied\n"
    )

    f.write(
        """
1. Duplicate removal

2. Missing value treatment
   - Numeric columns → Median
   - Text columns → 'Unknown'

3. Date conversion

4. Text standardization

5. Weekend/Holiday NAV handling
   - Reindexed to full date range
   - Forward-filled NAV values

6. Exported cleaned datasets
"""
    )

print("\nCleaning Completed")

print(
    f"Report Saved: {report_file}"
)