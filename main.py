import pandas as pd
from src.io import load_headlines_csv
from src.sentiment import get_vader, score_text


def main():
    df = load_headlines_csv("data/raw/sample_headline.csv")

    sia = get_vader()

    scores = df["text"].apply(lambda t: score_text(t, sia))
    scores_df = pd.json_normalize(scores)

    df_scored = pd.concat([df, scores_df], axis=1)

    print(df_scored[["date", "ticker", "text", "compound"]].head(5))


if __name__ == "__main__":
    main()
