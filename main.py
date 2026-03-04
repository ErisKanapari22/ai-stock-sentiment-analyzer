from src.io import load_headlines_csv

def main():
    df = load_headlines_csv("data/raw/sample_headline.csv")
    print("Rows: ", len(df))
    print(df.head(3))

if __name__ == "__main__":
    main()