import pandas as pd
import matplotlib.pyplot as plt

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

plt.title('NYC Airbnb Average Price per Night by Neighborhood')
plt.ylabel('Dollars', fontsize = 8)
plt.scatter(df_final['Neighborhood'], df_final['Average Price'], c = '#ff5a5f', s = 1.5)
plt.xticks(rotation = 90, fontsize = 3)
plt.show()