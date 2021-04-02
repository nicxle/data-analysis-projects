repeat = True

while repeat == True:

    import pandas as pd

    PATH = r'/Users/nicole/Downloads/California_Counties.csv'

    df = pd.read_csv(PATH)

    name_list = df.loc[:, 'Name'].values.tolist()
    lat_list = df.loc[:, 'Latitude'].values.tolist()
    long_list = df.loc[:, 'Longitude'].values.tolist()

    lat_dict = {name_list[i]: lat_list[i] for i in range(len(name_list))}
    long_dict = {name_list[i]: long_list[i] for i in range(len(name_list))}

    def out(name, value):
        print('\n{0} County\'s {1}: {2}'.format(county, name, value.get(county)))


    county = input('\nWhat county are you looking for?: ')

    if county in name_list:
        out('latitude', lat_dict)
        out('longitude', long_dict)
        
        answer = True

        while answer == True:
            answer = input('\nWould you like to look for another county?: ')
            if answer == 'yes':
                repeat = True
            elif answer == 'no':
                repeat = False 
            else:
                print('\nNot a valid input. Please try again.')
                answer = True
                
    else:
        print('\nNot a valid input. Please try again.')
        repeat = True