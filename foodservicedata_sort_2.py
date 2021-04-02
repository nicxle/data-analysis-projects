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

highest_freq = sorted(list_dict, key=list_dict.get, reverse = True)[:3]
highest_freq_list = []
sep = ', '

def change(y):
    y = sorted(y, reverse = True)
    return y 


for key, value in list_dict.items():
    if key in highest_freq:
        highest_freq_list.append(value)

print('{0} are the food service establishments with the greatest frequency of \'C\' grades. \nThey appear {1} times, respectively.'.format(sep.join(highest_freq), sep.join(str(i) for i in change(highest_freq_list))))