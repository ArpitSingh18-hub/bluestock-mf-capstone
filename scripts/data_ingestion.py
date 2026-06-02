from pathlib import Path
import pandas as pd
import os

BASE_DIR = Path(__file__).resolve().parent.parent

folder = BASE_DIR / "data" / "raw"

print(f"Reading files from: {folder}")

for file in os.listdir(folder):

    if file.endswith(".csv"):

        file_path = folder / file

        df = pd.read_csv(file_path)

        print("\n" + "="*60)
        print(file)
        print("Shape:", df.shape)
        print("Columns:", list(df.columns))
        print("Missing Values:")
        print(df.isnull().sum())
        print("Duplicates:", df.duplicated().sum())