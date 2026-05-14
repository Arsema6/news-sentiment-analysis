import pandas as pd
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[1] / "data" / "raw"

def load_news(csv_name: str = "raw_analyst_ratings.csv") -> pd.DataFrame:
    path = DATA_DIR / csv_name
    df = pd.read_csv(path, parse_dates=["date"]) if path.exists() else pd.DataFrame()
    return df

def load_stock(csv_name: str) -> pd.DataFrame:
    path = DATA_DIR / csv_name
    df = pd.read_csv(path, parse_dates=["Date"]) if path.exists() else pd.DataFrame()
    return df
