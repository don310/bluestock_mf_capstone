import pandas as pd
from pathlib import Path

data_path = Path("data/raw")

files = [
    "01_fund_master.csv",
    "02_nav_history.csv"
]

for file in files:
    try:
        df = pd.read_csv(data_path / file)

        print("\n" + "="*50)
        print(file)
        print("="*50)

        print("Shape:")
        print(df.shape)

        print("\nColumns:")
        print(df.dtypes)

        print("\nHead:")
        print(df.head())

    except Exception as e:
        print(f"Error in {file}: {e}")