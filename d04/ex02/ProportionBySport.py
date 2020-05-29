import pandas as pd


def proportionBySport(df, year, sport, gender):
    df_filter = df.loc[lambda df: df['Year'] == year]
    df_gender = df_filter.loc[lambda df: df['Sex'] == gender]
    df_simple = df_gender.drop_duplicates(subset='Name')
    df_sport = df_simple.loc[lambda df: df['Sport'] == sport]
    among = df_sport.shape[0] / df_simple.shape[0]
    return among
