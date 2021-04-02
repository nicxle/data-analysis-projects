import pandas as pd

PATH = r'/Users/nicole/Downloads/AB_NYC_2019.csv'

df = pd.read_csv(PATH)

df_info = df[['neighbourhood', 'price']]
df_mean = df_info.groupby('neighbourhood').mean()
df_count = df_info.groupby('neighbourhood').count()
df_merged = df_mean.merge(df_count, on = 'neighbourhood', suffixes = ['_mean', '_count'])
df_reset = df_merged.reset_index()
df_renamed = df_reset.rename(columns = {'neighbourhood' : 'Neighborhood', 'price_mean' : 'Average Price', 'price_count' : 'Total Listings'})
df_fix = df_renamed.loc[df_renamed['Total Listings'] > 16].sort_values(by = 'Average Price', ascending = False)
df_final = df_fix.reset_index(drop = True)

with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print(df_final)


print('\nOn average, the most expensive place to stay in NYC is {0}. Out of {1} listings, the average price per night is ${2}.'.format(df_final.at[0, 'Neighborhood'], df_final.at[0, 'Total Listings'], round(df_final.at[0, 'Average Price'], 2)))
print('\nOn average, the least expensive place to stay in NYC is {0}. Out of {1} listings, the average price per night is ${2}.'.format(df_final.at[143, 'Neighborhood'], df_final.at[143, 'Total Listings'], round(df_final.at[143, 'Average Price'], 2)))

df_final.to_excel('100daysofpython_day28.xlsx')