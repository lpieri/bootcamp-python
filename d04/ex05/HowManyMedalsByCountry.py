import pandas as pd


def howManyMedalsByCountry(df, country):
    df_country = df.loc[lambda df: df['Team'] == country]
    years_list = df_country['Year'].drop_duplicates().sort_values()
    dic = dict()
    for key, year in years_list.items():
        df_year = df_country.loc[lambda df: df['Year'] == year]
        df_year = df_year.drop_duplicates(subset=['Event', 'Medal'])
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
