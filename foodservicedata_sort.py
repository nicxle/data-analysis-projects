import pandas as pd
pd.options.mode.chained_assignment = None

PATH = r'/Users/nicole/Downloads/FoodServiceData_23_0.csv'

df = pd.read_csv(PATH) 
df_grades = (df.loc[df['Grade']== 'C'])


df_grades['EstablishmentName'] = df_grades['EstablishmentName'].str.split(' #', expand = True)
df_list = (df_grades.loc[:, 'EstablishmentName']).values.tolist()
# print(df_list)


def frequency(x_list):
    list_dict = dict()
    for i in x_list:
        if i in list_dict:
            list_dict[i] += 1
        else:
            list_dict[i] = 1
    list_dict = {key:value for key, value in list_dict.items()}
    return list_dict


list_dict = frequency(df_list)

highest_freq = max(list_dict, key=list_dict.get)
highest_freq_list = []

for key, value in list_dict.items():
    if value == list_dict[highest_freq]:
        highest_freq_list.append(key)

print('{0} is the food service establishment with the greatest number ({1}) of \'C\' grades.'.format(highest_freq_list, list_dict[highest_freq]))