import pandas as pd
from pathlib import Path

Project_Root = Path(__file__).resolve().parents[1]
DATA_DIR = Project_Root / "data" / "raw"


def inspect_csv(file_name):
    file_path = DATA_DIR / file_name
    df = pd.read_csv(file_path)

    print("=" * 80)
    print(f"File: {file_path}")

    print("\nShape:")
    print(df.shape)

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nFirst 5 rows:")
    print(df.head())

    print("\nData types:")
    print(df.dtypes)

    print("\nMissing values:")
    print(df.isna().sum())

    hidden_missing = (df == "\\N").sum()
    print(hidden_missing[hidden_missing > 0].sort_values(ascending=False))

    print("\nBasic statistics:")
    print(df.describe())

    print("\nDuplicated rows:")
    print(df.duplicated().sum())


inspect_csv("results.csv")
inspect_csv("races.csv")
inspect_csv("drivers.csv")
inspect_csv("constructors.csv")
inspect_csv("circuits.csv")
inspect_csv("status.csv")
