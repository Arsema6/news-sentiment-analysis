import pandas as pd


def _price_series(df: pd.DataFrame, column: str = "Adj Close") -> pd.Series:
    if column in df.columns:
        return df[column]
    if "Close" in df.columns:
        return df["Close"]
    raise KeyError(f"Neither '{column}' nor 'Close' exists in the dataframe")


def compute_sma(df: pd.DataFrame, column: str = "Adj Close", window: int = 20) -> pd.Series:
    return _price_series(df, column).rolling(window=window, min_periods=1).mean()


def compute_ema(df: pd.DataFrame, column: str = "Adj Close", span: int = 20) -> pd.Series:
    return _price_series(df, column).ewm(span=span, adjust=False).mean()


def compute_returns(df: pd.DataFrame, column: str = "Adj Close") -> pd.Series:
    return _price_series(df, column).pct_change() * 100


def compute_rsi(df: pd.DataFrame, column: str = "Adj Close", window: int = 14) -> pd.Series:
    delta = _price_series(df, column).diff()
    up = delta.clip(lower=0)
    down = -1 * delta.clip(upper=0)
    ma_up = up.rolling(window=window, min_periods=1).mean()
    ma_down = down.rolling(window=window, min_periods=1).mean()
    rs = ma_up / (ma_down + 1e-9)
    rsi = 100 - (100 / (1 + rs))
    return rsi
