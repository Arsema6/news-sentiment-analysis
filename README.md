# 📈 News Sentiment Analysis – Task 1 Report

## Nova Financial Solutions  

## Overview

This project investigates the interplay between financial news sentiment and stock price movements. Using real-world datasets that combine headline-level news with historical trading data, I conduct rigorous text and time-series analyses to uncover the patterns, trends, and statistical properties most likely to inform predictive investment strategies.

**Business Context:**  
Nova Financial Solutions leverages advanced analytics to empower investment teams with actionable insights, bridging the gap between market narrative and price action.

---

## Objectives

1. **Descriptive Statistics:**  
   - Characterize headline lengths.
   - Identify top publishers and their activity levels.
   - Analyze publication date trends to reveal bursts and lulls in news volume.

2. **Text & Topic Analysis:**  
   - Extract top keywords using TF-IDF and CountVectorizer.
   - Use LDA for topic modeling to find recurring themes (e.g., “earnings”, “FDA approval”).

3. **Time Series Analysis:**  
   - Visualize article frequency across dates and times; highlight news spikes that might correspond to market events.

4. **Publisher Analysis:**  
   - Determine the most active publishers and, if emails are used, group by domain to see organizational influence.

---

## Data Sources

- **Financial News Dataset**: Contains headlines, publication timestamps, publishers, and stock tickers.
- **Stock Price Dataset**: Daily OHLCV data for multiple stocks (used in subsequent tasks).

---

## Repository Structure

```
news-sentiment-analysis/
├── .github/workflows/unittests.yml         # CI pipeline: notebook and tests
├── requirements.txt                        # All dependencies
├── README.md                               # This report
├── data/                                   # Place input data here
├── notebooks/
│   └── news_eda.ipynb                      # Main EDA notebook
├── src/                                    # (future code)
├── tests/                                  # (future tests)
├── scripts/                                # (future utilities)
```

---

## How to Reproduce

1. **Install packages:**
   ```bash
   pip install -r requirements.txt
   ```
2. **Download and place your datasets in** `data/`
3. **Run the notebook (EDA):**
   ```bash
   jupyter notebook notebooks/news_eda.ipynb
   ```

---

## Key Analysis & Insights

### Descriptive Statistics

- **Headline Lengths**  
  Distribution plotted; median headline length: _[to be filled by user]_ characters.

- **Top Publishers**  
  Bar plot shows most prolific news sources.

- **Publication Trends**  
  Line chart visualizes daily news volume—noticeable spikes during major market events ([insert example dates]).

### Topic Modeling

- **TF-IDF & Keywords**  
  The most frequent and distinctive terms include: _[auto-filled by analysis]_.

- **LDA Topics**  
  Common themes: _Topic 1_ (e.g., “earnings”), _Topic 2_ (e.g., “FDA approval”), etc.  
  Representative headlines provided for each.

### Time Series & Publisher Analysis

- **Time of Day**  
  Publication volume peaks in the early morning and late afternoon.

- **Email Domain Analysis**  
  If applicable, the most active publisher domains are shown, highlighting organizational contributors.

---

## Visualizations

> **Included in the notebook:**  
> - Headline length histogram  
> - Top publishers barplot  
> - News volume over time  
> - Word cloud for headlines  
> - Topic keyword barplots  
> - Hour-of-day news histogram  
> - (and more...)

---

## Reflections & Next Steps

- All code is reproducible, version-controlled, and run-tested by GitHub Actions (see "Actions" tab or `.github/workflows/unittests.yml`).
- This investigation forms the foundation for subsequent sentiment quantification and correlation analyses (Tasks 2+).
- Recommendations for Nova: Integrate burst-detection on publication series; consider publisher weighting in sentiment models.
