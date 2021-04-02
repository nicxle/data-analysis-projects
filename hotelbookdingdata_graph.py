import pandas as pd
import matplotlib.pyplot as plt

PATH = r'/Users/nicole/Downloads/hotel_bookings.csv'

df = pd.read_csv(PATH)
df_filter = df[df['is_canceled'] == 0]
df_data = df_filter[['hotel', 'arrival_date_month', 'stays_in_weekend_nights', 'stays_in_week_nights']].rename(columns = {'hotel' : 'Hotel', 'arrival_date_month' : 'Arrival Month', 'stays_in_weekend_nights' : 'Nights Booked (E)', 'stays_in_week_nights' : 'Nights Booked (W)' })
df_data['Hotel'] = df_data['Hotel'].str.split('Hotel', expand = True)
df_hotel_data = df_data.groupby(['Hotel']).count()
df_hotel = df_hotel_data.drop(columns = ['Nights Booked (E)', 'Nights Booked (W)']).rename(columns = {'Hotel' : 'Hotel Type', 'Arrival Month' : 'Total Bookings'}).sort_values(by = ['Total Bookings'], ascending = False).reset_index()
df_month_data = df_data.replace(to_replace = ['January','February','March','April','May','June','July','August','September','October','November','December'], value = ['Jan.','Feb.','Mar.','Apr.','May','Jun.','Jul.','Aug.','Sept.','Oct.','Nov.','Dec.']).groupby('Arrival Month').count()
df_month = df_month_data.drop(columns = ['Nights Booked (E)', 'Nights Booked (W)']).rename(columns = {'Hotel' : 'Total Bookings'}).sort_values(by = ['Total Bookings'], ascending = False).reset_index()
df_weekend_data = df_data.groupby(['Nights Booked (E)']).count()
df_weekend = df_weekend_data.drop(columns = ['Arrival Month', 'Nights Booked (W)']).rename(columns = {'Hotel' : 'Total Bookings'}).sort_values(by = ['Total Bookings'], ascending = False).reset_index()
df_week_data = df_data.groupby(['Nights Booked (W)']).count()
df_week = df_week_data.drop(columns = ['Arrival Month', 'Nights Booked (E)']).rename(columns = {'Hotel' : 'Total Bookings'}).sort_values(by = ['Total Bookings'], ascending = False).reset_index()

print('\nHotel Booking Stats - Most Popular')
print('\nHotel Type: {0}'.format(df_hotel.at[0, 'Hotel']))
print('Month: {0}'.format(df_month.at[0, 'Arrival Month']))
print('Weeknights Booked: {0}'.format(df_week.at[0, 'Nights Booked (W)']))
print('Weekend Nights Booked: {0}'.format(df_weekend.at[1, 'Nights Booked (E)']))

plt.figure()
plt.suptitle('Hotel Booking Data', weight = 'bold', fontsize = 25)
plt.subplot(221)
plt.bar(df_hotel['Hotel'], df_hotel['Total Bookings'], color = '#e6a3a3')
plt.title('per Hotel Type', weight = 'semibold', fontsize = 10)
plt.subplot(222)
plt.bar(df_month['Arrival Month'], df_month['Total Bookings'], color = '#b0eda4')
plt.xticks(fontsize = 7)
plt.title('per Arrival Month', weight = 'semibold', fontsize = 10)
plt.subplot(223)
plt.bar(df_weekend['Nights Booked (E)'], df_weekend['Total Bookings'], color = '#a4e0ed')
plt.xticks(ticks = range(df_weekend['Nights Booked (E)'].max() + 1))
plt.xlabel('Num. of Nights')
plt.title('per Weekend Nights Booked', weight = 'semibold', fontsize = 10)
plt.subplot(224)
plt.bar(df_week['Nights Booked (W)'], df_week['Total Bookings'], color = '#d8a2e8')
plt.xticks(ticks = range(df_week['Nights Booked (W)'].max() + 1), fontsize = 3)
plt.xlabel('Num. of Nights')
plt.title('per Week Nights Booked', weight = 'semibold', fontsize = 10)
plt.show()