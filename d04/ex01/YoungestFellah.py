import pandas as pd


def youngestFellah(df, year):
    df_filter = df.loc[lambda df: df['Year'] == year]
    df_f = df_filter[lambda df: df['Sex'] == 'F']
    df_m = df_filter[lambda df: df['Sex'] == 'M']
    dic = {'f': df_f['Age'].min(), 'm': df_m['Age'].min()}
    return dic
