import pandas as pd


class FileLoader:

    def load(self, path):
        if '.csv' in path:
            to_print = "Loading dataset of dimensions {h} x {w}"
            df = pd.read_csv(path)
            print(to_print.format(h=df.shape[0], w=df.shape[1]))
            return df
        else:
            print("Please entre [file.csv].")
            return None

    def display(self, df, n):
        if n >= 0:
            print(df.head(n))
        else:
            n *= -1
            print(df.tail(n))
