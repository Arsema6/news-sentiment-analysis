"""Run the full analysis pipeline: sentiment scoring, indicator computation, correlations, and save outputs."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

from src.data_loader import load_news, load_stock
from src.sentiment import apply_vader, aggregate_daily_sentiment
from src.indicators import compute_returns


def run():
    out = Path("outputs")
    out.mkdir(exist_ok=True)

    news = load_news()
    if news.empty:
        print('News dataset not found at data/raw/raw_analyst_ratings.csv')
        return

    print('Applying VADER sentiment...')
    news = apply_vader(news, 'headline')
    daily = aggregate_daily_sentiment(news, 'date', 'stock')

    p = Path('data/raw')
    results = []
    for f in sorted(p.glob('*.csv')):
        if f.name == 'raw_analyst_ratings.csv':
            continue
        stock = f.stem
        print('Processing', stock)
        df = load_stock(f.name)
        if df.empty:
            print(f'Stock file {f.name} empty or missing')
            continue
        df = df.sort_values('Date').set_index('Date')
        df['Daily_Return'] = compute_returns(df, 'Adj Close')
        df = df.reset_index()
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce').dt.date
        stock_daily = daily[daily['stock'] == stock].copy()
        stock_daily['date'] = pd.to_datetime(stock_daily['date'], errors='coerce').dt.date
        merged = stock_daily.merge(df[['Date','Daily_Return']], left_on='date', right_on='Date')
        merged.dropna(subset=['avg_sentiment','Daily_Return'], inplace=True)
        if len(merged) >= 5:
            corr, pval = pearsonr(merged['avg_sentiment'], merged['Daily_Return'])
        else:
            corr, pval = None, None
        results.append({'stock': stock, 'n': len(merged), 'corr': corr, 'p': pval})
        if corr is not None:
            plt.figure()
            plt.scatter(merged['avg_sentiment'], merged['Daily_Return'])
            plt.title(f'{stock} r={corr:.3f}')
            plt.xlabel('avg_sentiment')
            plt.ylabel('Daily_Return')
            plt.savefig(out / f'{stock}_sentiment_return.png')
            plt.close()

    import csv
    with open(out / 'correlations.csv', 'w', newline='') as fh:
        writer = csv.DictWriter(fh, fieldnames=['stock','n','corr','p'])
        writer.writeheader()
        writer.writerows(results)
    print('Pipeline complete — outputs/correlations.csv created')


if __name__ == '__main__':
    run()
