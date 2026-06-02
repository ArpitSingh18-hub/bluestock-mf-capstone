from pathlib import Path
from datetime import datetime
import time
import requests
import pandas as pd

# ==========================================================
# BLUESTOCK MF CAPSTONE PROJECT
# DAY 1 - TASK 4
# LIVE NAV INGESTION PIPELINE
# ==========================================================


class LiveNAVFetcher:

    def __init__(self, amfi_code: str):

        self.amfi_code = str(amfi_code)

        self.api_url = (
            f"https://api.mfapi.in/mf/{self.amfi_code}"
        )

        self.base_dir = (
            Path(__file__)
            .resolve()
            .parent
            .parent
        )

        self.raw_dir = (
            self.base_dir
            / "data"
            / "raw"
        )

        self.report_dir = (
            self.base_dir
            / "reports"
        )

        self.raw_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        self.report_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        self.output_file = (
            self.raw_dir
            / f"{self.amfi_code}_live_nav.csv"
        )

        self.validation_report = (
            self.report_dir
            / "api_validation_report.md"
        )

    # ======================================================
    # API REQUEST
    # ======================================================

    def fetch_data(self):

        print("\nFetching Live NAV Data...")

        try:

            response = requests.get(
                self.api_url,
                timeout=30
            )

            response.raise_for_status()

            print(
                "API Connection Successful"
            )

            return response.json()

        except requests.exceptions.RequestException as e:

            print(
                f"API Request Failed: {e}"
            )

            return None

    # ======================================================
    # EXTRACT META DATA
    # ======================================================

    def extract_meta(self, data):

        meta = data.get(
            "meta",
            {}
        )

        return {

            "scheme_code":
            meta.get("scheme_code"),

            "scheme_name":
            meta.get("scheme_name"),

            "fund_house":
            meta.get("fund_house"),

            "scheme_type":
            meta.get("scheme_type"),

            "scheme_category":
            meta.get("scheme_category"),
        }

    # ======================================================
    # EXTRACT LATEST NAV
    # ======================================================

    def extract_latest_nav(self, data):

        nav_records = data.get(
            "data",
            []
        )

        if len(nav_records) == 0:

            raise ValueError(
                "No NAV data returned."
            )

        latest = nav_records[0]

        return {

            "latest_nav":
            latest.get("nav"),

            "nav_date":
            latest.get("date")
        }

    # ======================================================
    # CREATE DATAFRAME
    # ======================================================

    def create_dataframe(
        self,
        meta,
        nav_data
    ):

        record = {

            **meta,

            **nav_data,

            "api_fetch_timestamp":
            datetime.now()
        }

        return pd.DataFrame(
            [record]
        )

    # ======================================================
    # MASTER DATA VALIDATION
    # ======================================================

    def validate_master_data(
        self,
        meta
    ):

        expected_scheme = (
            "HDFC Top 100 Fund - Direct Plan - Growth"
        )

        api_scheme = (
            meta["scheme_name"]
        )

        print("\n" + "=" * 60)
        print(
            "MASTER DATA VALIDATION"
        )
        print("=" * 60)

        print(
            f"AMFI Code          : "
            f"{self.amfi_code}"
        )

        print(
            f"Expected Scheme    : "
            f"{expected_scheme}"
        )

        print(
            f"API Returned       : "
            f"{api_scheme}"
        )

        if (
            expected_scheme.lower()
            ==
            api_scheme.lower()
        ):

            status = "PASS"

            print(
                "Validation Status  : PASS"
            )

        else:

            status = "WARNING"

            print(
                "Validation Status  : WARNING"
            )

            print(
                "\nObservation:"
            )

            print(
                "API metadata differs "
                "from project master dataset."
            )

            print(
                "Project dataset is "
                "treated as source of truth."
            )

        self.generate_validation_report(
            expected_scheme,
            api_scheme,
            status
        )

    # ======================================================
    # REPORT GENERATION
    # ======================================================

    def generate_validation_report(
        self,
        expected_scheme,
        api_scheme,
        status
    ):

        with open(
            self.validation_report,
            "w",
            encoding="utf-8"
        ) as f:

            f.write(
                "# API Validation Report\n\n"
            )

            f.write(
                f"Date: "
                f"{datetime.now()}\n\n"
            )

            f.write(
                f"AMFI Code: "
                f"{self.amfi_code}\n\n"
            )

            f.write(
                f"Expected Scheme:\n"
                f"{expected_scheme}\n\n"
            )

            f.write(
                f"API Returned:\n"
                f"{api_scheme}\n\n"
            )

            f.write(
                f"Validation Status: "
                f"{status}\n\n"
            )

            if status == "WARNING":

                f.write(
                    "Observation:\n"
                )

                f.write(
                    "The live API metadata "
                    "does not match the "
                    "project master dataset.\n\n"
                )

                f.write(
                    "The project dataset "
                    "will be treated as "
                    "the authoritative "
                    "source of truth."
                )

    # ======================================================
    # DATA QUALITY CHECK
    # ======================================================

    def quality_check(
        self,
        df
    ):

        print("\n" + "=" * 60)
        print(
            "DATA QUALITY SUMMARY"
        )
        print("=" * 60)

        print(
            f"Rows Loaded       : "
            f"{len(df)}"
        )

        print(
            f"Columns Loaded    : "
            f"{len(df.columns)}"
        )

        print(
            f"Missing Values    : "
            f"{df.isnull().sum().sum()}"
        )

        print(
            f"Duplicate Rows    : "
            f"{df.duplicated().sum()}"
        )

    # ======================================================
    # SAVE CSV
    # ======================================================

    def save_csv(
        self,
        df
    ):

        df.to_csv(
            self.output_file,
            index=False
        )

        print("\nCSV Saved Successfully")

        print(
            self.output_file
        )

    # ======================================================
    # MAIN PIPELINE
    # ======================================================

    def run(self):

        start_time = time.time()

        print("=" * 60)
        print(
            "BLUESTOCK MF CAPSTONE"
        )
        print(
            "LIVE NAV INGESTION PIPELINE"
        )
        print("=" * 60)

        data = self.fetch_data()

        if data is None:

            return

        meta = self.extract_meta(
            data
        )

        nav_data = (
            self.extract_latest_nav(
                data
            )
        )

        df = self.create_dataframe(
            meta,
            nav_data
        )

        print(
            "\nLATEST NAV RECORD"
        )

        print(df)

        self.validate_master_data(
            meta
        )

        self.quality_check(df)

        self.save_csv(df)

        end_time = time.time()

        runtime = round(
            end_time - start_time,
            2
        )

        print("\n" + "=" * 60)

        print(
            f"Pipeline Runtime : "
            f"{runtime} sec"
        )

        print(
            "Pipeline Completed Successfully"
        )

        print("=" * 60)


# ==========================================================
# ENTRY POINT
# ==========================================================

if __name__ == "__main__":

    AMFI_CODE = "125497"

    pipeline = LiveNAVFetcher(
        AMFI_CODE
    )

    pipeline.run()