# AI Stock Sentiment Analyzer (Python + NLP)

A lightweight **Stock Sentiment Analyzer** that reads stock-related headlines (CSV),
runs **VADER sentiment analysis**, aggregates a **daily sentiment score per ticker**,
and outputs a simple trading-style signal: **Bullish / Bearish / Neutral**.
Optionally, it generates a sentiment trend chart.

## Features
- CSV input (date, ticker, text)
- VADER sentiment scoring (`compound` from -1 to +1)
- Daily aggregation per ticker (mean score + news count)
- Simple signal rules (Bullish/Bearish/Neutral)
- Optional trend chart (Matplotlib)
- Clean, modular code structure (job-ready)

## Project Structure
- data/processed/ # Generated daily outputs (ignored by git)
- src/ # Core logic (io, sentiment, scoring, report, plot)
- outputs/ # Generated report/plots (ignored by git)
- main.py # CLI entrypoint

## Setup
```bash
pip install -r requirements.txt
```

## 📄 Input Format (CSV)

Example file: `data/raw/sample_headlines.csv`

Required columns:

| Column | Description |
|--------|-------------|
| `date` | Format: YYYY-MM-DD |
| `ticker` | Stock ticker (e.g., AAPL, TSLA) |
| `text` | Headline or tweet text |
| `source` | *(optional)* News source |

## ▶️ Run the Analyzer

### Run without plot:
```bash
python main.py --ticker AAPL
```
### Run with plot:
```bash
python main.py --ticker AAPL --plot
```

## 📤 Output

### Console
A daily sentiment table with aggregated scores and trading‑style signals.

### Files Generated

| File | Location | Description |
|------|----------|-------------|
| `daily_sentiment.csv` | `data/processed/` | Aggregated daily sentiment |
| `report.txt` | `outputs/` | Text summary report |
| `<TICKER>_sentiment.png` | `outputs/` | Generated when using `--plot` |

## 📝 Notes

- This project uses **VADER**, a rule‑based sentiment analyzer — no model training required.
- Sentiment thresholds are intentionally conservative to reduce false trading signals.
- Designed for clarity, modularity, and real‑world job‑ready structure.

## 🔍 Quick Check

Run:

```bash
python main.py --ticker AAPL --plot