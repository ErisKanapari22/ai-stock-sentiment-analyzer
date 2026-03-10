# AI Stock Sentiment Analyzer (Python + NLP)

A lightweight **Stock Sentiment Analyzer** that collects stock-related news headlines, performs **sentiment analysis
using VADER**, and produces a **daily sentiment score per ticker** along with a simple **trading-style signal**:
Bullish / Bearish / Neutral.

The project supports two input sources:

- Static CSV files
- Real-time financial news via the **Finnhub API**

Optionally, it generates a **sentiment trend chart** for visualization.

---

## Features

- CSV input (`date`, `ticker`, `text`)
- Optional **real-time financial news via Finnhub API**
- VADER sentiment scoring (`compound` score from -1 to +1)
- Daily aggregation per ticker
- Simple signal rules:
    - Bullish
    - Bearish
    - Neutral
- Optional sentiment trend chart (Matplotlib)
- CLI interface with arguments
- Modular, job-ready code structure

---

## Project Structure

data/ \
raw/ # Sample CSV inputs\
processed/ # Generated daily outputs (ignored by git)\

src/\
io.py # CSV loader\
api_client.py # Finnhub API client\
sentiment.py # VADER sentiment scoring\
scoring.py # Aggregation and signals\
report.py # Report generation\
plot.py # Sentiment visualization\

outputs/ # Generated reports and plots (ignored by git)\

main.py # CLI entrypoint\


---

## Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Using the Finnhub API

To enable real-time financial news, you need a free API key from Finnhub.

### Step 1 — Get an API Key

Create an account at:

https://finnhub.io

Copy your API key from the dashboard.

---

### Step 2 — Create `.env`

Create a file in the project root:\
.env

Add your API key:

⚠️ The `.env` file is ignored by Git to keep your API key secure.

---

## Input Format (CSV)

Example file:\
data/raw/sample_headlines.csv

Required columns:

| Column | Description               |
|--------|---------------------------|
| date   | Format: `YYYY-MM-DD`      |
| ticker | Stock ticker (AAPL, TSLA) |
| text   | Headline or tweet text    |
| source | (optional) News source    |

---

## Run the Analyzer

### Run with CSV input

```bash
python main.py --ticker AAPL
```

## Run with CSV + chart

```bash
python main.py --ticker AAPL --plot
```

## Run using Finnhub API

```bash
python main.py --use-api --ticker AAPL --from-date 2026-03-01 --to-date 2026-03-06
```

## Run with API + chart

```bash
python main.py --use-api --ticker AAPL --from-date 2026-03-01 --to-date 2026-03-06 --plot
```

---

## Output

### Console Output

A table containing:

- date
- ticker
- daily sentiment score
- news count
- signal (Bullish / Bearish / Neutral)

---

### Files Generated

| File                     | Location        | Description                   |
|--------------------------|-----------------|-------------------------------|
| daily_sentiment.csv      | data/processed/ | Aggregated daily sentiment    |
| report.txt               | outputs/        | Text summary report           |
| `<TICKER>_sentiment.png` | outputs/        | Generated when using `--plot` |

---

## Example Pipeline
```bash
News (CSV or API)
↓
Sentiment Analysis (VADER)
↓
Headline Scores
↓
Daily Aggregation
↓
Bullish / Bearish / Neutral Signal
↓
Report + Chart
```

---

## Notes

- This project uses **VADER**, a rule-based sentiment analyzer.
- No model training is required.
- Sentiment thresholds are intentionally conservative to reduce false signals.
- Designed with **clean architecture and modular code**, suitable for portfolio projects.

---

## Quick Check

Run the full pipeline:

```bash
python main.py --use-api --ticker AAPL --plot
```
This will:

Fetch news from Finnhub

Analyze sentiment

Generate a daily signal

Create a sentiment trend chart
