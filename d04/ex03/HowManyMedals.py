import pandas as pd


def howManyMedals(df, name):
    df_filter = df.loc[lambda df: df['Name'] == name]
    years_list = df_filter['Year'].drop_duplicates()
    dic = dict()
    for key, year in years_list.items():
        df_year = df_filter.loc[lambda df: df['Year'] == year]
        golden = 0
        silver = 0
        bronze = 0
        medals_count = df_year['Medal'].count()
        medals = df_year['Medal']
        if medals_count > 0:
            for key, medal in medals.items():
                if medal == 'Gold':
                    golden += 1
                if medal == 'Silver':
                    silver += 1
                if medal == 'Bronze':
                    bronze += 1
        dic[year] = {"G": golden, "S": silver, "B": bronze}
    return dic
