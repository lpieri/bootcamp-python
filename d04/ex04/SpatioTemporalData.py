import pandas as pd


class SpatioTemporalData:

    def __init__(self, df):
        self.df = df

    def when(self, location):
        df_city = self.df.loc[lambda df: df['City'] == location]
        df_filter = df_city.filter(items=['Year', 'City'])
        df_simple = df_filter.drop_duplicates()
        year = df_simple['Year'].values
        return list(year)

    def where(self, date):
        df_year = self.df.loc[lambda df: df['Year'] == date]
        df_filter = df_year.filter(items=['Year', 'City'])
        df_simple = df_filter.drop_duplicates()
        city = df_simple['City'].values
        return list(city)
