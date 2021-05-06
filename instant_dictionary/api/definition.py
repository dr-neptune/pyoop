import pandas as pd


class Definition:
    """
    Takes a term and returns it's definition as a tuple
    """

    def __init__(self, term):
        self.term = term

    def get(self):
        df = pd.read_csv("data/dict_data.csv")
        return tuple(df.loc[df["word"] == self.term]["definition"])
