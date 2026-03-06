import pandas as pd
from src.io import load_headlines_csv
from src.sentiment import get_vader, score_text
from src.scoring import label_from_compound, daily_sentiment
from src.report import build_daily_report


def main():
    df = load_headlines_csv("data/raw/sample_headline.csv")

    sia = get_vader()

    scores = df["text"].apply(lambda t: score_text(t, sia))
    scores_df = pd.json_normalize(scores)

    df_scored = pd.concat([df, scores_df], axis=1)

    df_scored["sentiment"] = df_scored["compound"].apply(label_from_compound)
    df_daily = daily_sentiment(df_scored)

    df_report = build_daily_report(df_daily)

    print(df_scored[["date", "ticker", "text", "compound", "sentiment"]].head(5))

    print("\nDaily sentiment score: ")
    print(df_daily)

    print("\nFinal report: (Daily Score + Signal) ")
    print(df_report)


if __name__ == "__main__":
    main()
