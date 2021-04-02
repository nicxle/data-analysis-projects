import pandas as pd
import matplotlib.pyplot as plt

PATH = r'/Users/nicole/Downloads/AB_NYC_2019.csv'

df = pd.read_csv(PATH)
df_ngbh = df[['neighbourhood', 'latitude', 'longitude', 'price']]
df_lat = df_ngbh.groupby('neighbourhood').mean(['latitude', 'longitude', 'price']).reset_index()
df_final = df_lat.rename(columns = {'neighbourhood' : 'Neighborhood', 'latitude' : 'Avg. Latitude', 'longitude' : 'Avg. Longitude', 'price' : 'Avg. Price'})

# with pd.option_context('display.max_rows', None, 'display.max_columns', None):
#     print(df_final)

landmark_dict = {'Landmark' : ['Times Square', '9/11 Memorial & Museum', 'Central Park', 'The Museum of Modern Art', 'The Statue of Liberty National Monument', 'Empire State Building', 'The Vessel', 'Grand Central Terminal', 'Brooklyn Bridge', 'Broadway'], 'Latitude' : [40.758896, 40.711449, 40.785091, 40.761509, 40.689247, 40.748817, 40.7538, 40.752655, 40.706001, 40.790886], 'Longitude': [-73.98513040, -74.013855, -73.968285, -73.978271, -74.044502, -73.985428, -74.0022, -73.977295, -73.997002, -73.974709]}
df_landmark = pd.DataFrame(data = landmark_dict)

# with pd.option_context('display.max_rows', None, 'display.max_columns', None):
#     print(df_landmark)

plt.figure()
plt.title('NYC Airbnb Locations in Relation to Popular Tourist Attractions')
plt.xlabel('Latitude', fontstyle = 'italic')
plt.ylabel('Longitude', fontstyle = 'italic')
plt.scatter(df_final['Avg. Latitude'], df_final['Avg. Longitude'], s = df_final['Avg. Price'], c = '#e9c7c788', edgecolors= '#ff5a5f', label = 'Airbnb Location')
plt.scatter(df_landmark['Latitude'], df_landmark['Longitude'], c = '#8bd6e088', edgecolors = '#145fd9', s = 100, marker = '*', label = 'Tourist Attraction')
plt.legend(loc = 'lower right', markerscale = .5, fontsize = 'small', labelspacing = 1, borderpad = 1)
plt.show()