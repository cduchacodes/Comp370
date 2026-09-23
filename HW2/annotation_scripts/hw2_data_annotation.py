# This is a sample Python script.
import pandas as pd


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    df = pd.read_csv("cleaned_dialog.csv")
    df['addressee'] = df['speaker'].shift(-1)
    df.to_csv("annotated_dialog.csv", index=False)
    df = df.head(40).tail(30)
    df.to_csv("annotated_block.csv", index=False)




# See PyCharm help at https://www.jetbrains.com/help/pycharm/

