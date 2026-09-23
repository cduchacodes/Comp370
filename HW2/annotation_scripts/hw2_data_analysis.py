import pandas as pd


if __name__ == '__main__':
    df = pd.read_csv("annotated_block.csv")
    print(sum(df['addressee'] == df['actual addressee'])/30)
