import pandas as pd


class Definition:
    def __init__(self, term):
        self.term = term

    def get(self):
        df = pd.read_csv("data/dict_data.csv")
        return tuple(df.loc[df["word"] == self.term]["definition"])


# example
# ex_term = Definition("acid")
# print("---\n", "\n---\n".join(ex_term.get()))
