import pandas as pd

def apply_vader(df: pd.DataFrame, text_col: str = "headline") -> pd.DataFrame:
    try:
        from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
    except Exception:
        raise
    analyzer = SentimentIntensityAnalyzer()
    scores = df[text_col].fillna("").apply(analyzer.polarity_scores)
    scores_df = pd.DataFrame(list(scores))
    return pd.concat([df.reset_index(drop=True), scores_df], axis=1)

def aggregate_daily_sentiment(df: pd.DataFrame, date_col: str = "date", symbol_col: str = "stock") -> pd.DataFrame:
    df = df.copy()
    df[date_col] = pd.to_datetime(df[date_col], errors="coerce", utc=True).dt.date
    df = df.dropna(subset=[date_col, symbol_col, "compound"])
    grouped = df.groupby([symbol_col, date_col])["compound"].mean().reset_index()
    grouped.rename(columns={"compound": "avg_sentiment"}, inplace=True)
    return grouped
