from adapter.DataMosApi import DataMosApi
import pandas as pd


a = DataMosApi()


ogrn = pd.read_excel('./ogrn.xlsx', index_col=None)
list_ogrn = ogrn["ОГРН"].values.tolist()

df = pd.DataFrame({'Название': [], 'ОГРН': [], 'ИНН': [], 'Адрес': [], 'Лицензия': []})

b = a.get_all(list_ogrn)

name_list, inn_list, adress_list, licenses_list, = list(), list(), list(), list()

for i in range(len(list_ogrn)):
    name_list.append(b[i].name)
    inn_list.append(b[i].inn)
    adress_list.append(b[i].adress)
    licenses_list.append(b[i].licenses)

for i in range(len(list_ogrn)):
    df['Название'] = name_list
    df['ОГРН'] = list_ogrn
    df['ИНН'] = inn_list
    df['Адрес'] = adress_list
    df['Лицензия'] = licenses_list


print(df.head())

df.to_excel('./result.xlsx')