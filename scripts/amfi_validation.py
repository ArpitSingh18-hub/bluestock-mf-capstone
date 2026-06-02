from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent

fund_master = pd.read_csv(
    BASE_DIR
    / "data"
    / "raw"
    / "01_fund_master.csv"
)

nav_history = pd.read_csv(
    BASE_DIR
    / "data"
    / "raw"
    / "02_nav_history.csv"
)

fund_codes = set(
    fund_master["amfi_code"]
)

nav_codes = set(
    nav_history["amfi_code"]
)

missing_codes = (
    fund_codes - nav_codes
)

print("="*60)
print("AMFI VALIDATION REPORT")
print("="*60)

print(
    f"Fund Master Codes: "
    f"{len(fund_codes)}"
)

print(
    f"NAV History Codes: "
    f"{len(nav_codes)}"
)

print(
    f"Missing Codes: "
    f"{len(missing_codes)}"
)

if len(missing_codes) == 0:

    print(
        "\nPASS"
    )

    print(
        "All AMFI codes exist "
        "in NAV history."
    )

else:

    print(
        "\nWARNING"
    )

    print(
        missing_codes
    )