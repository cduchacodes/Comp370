
# This is a sample Python script.
import pandas as pd

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    df = pd.read_csv("clean_dialog.csv")
    df = df[["title", "pony", "dialog"]]
    df.columns = ["episode", "speaker", "content"]
    df['content'] = df['content'].str.replace(r"\[.*?\]", "", regex=True)
    df['content'] = df['content'].str.replace(r"\<.*?\>", "", regex=True)
    df.to_csv("cleaned_dialog.csv", index=False)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
