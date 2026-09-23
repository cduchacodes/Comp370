# This is a sample Python script.
import pandas as pd
import numpy as np

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def first_step():
    df = pd.read_csv("IRAhandle_tweets_1.csv")

    #only look at first 10000 tweets
    df = df.head(10000)

    #only tweets in Engligh
    df = df[df["language"] == "English"]

    #remove tweets with ?
    df = df[~df["content"].str.contains("?", na=False, regex=False)]

    #df.to_csv("Filtered_IRAhandle_tweets_1.tsv", sep='\t', index=False)
    return df


def second_step(df):
    #df = pd.read_csv("Filtered_IRAhandle_tweets_1.tsv", sep='\t')
    df["trump_mention"] = np.where(df["content"].str.contains(r"\bTrump\b"), "True", "False")
    #keep only the right columns
    df = df[['tweet_id', 'publish_date', 'content', 'trump_mention']]
    df.to_csv("dataset.tsv", sep='\t', index=False)


    #results
    columns = ['results', 'value']
    row_data = [['frac-trump-mentions', round((df['trump_mention'] == "True").sum()/len(df), 3)]]
    (pd.DataFrame(row_data, columns=columns)).to_csv("results.tsv", sep='\t', index=False)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    df = first_step()
    second_step(df)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
