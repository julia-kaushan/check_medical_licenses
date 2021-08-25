from adapter.DataMosApi import DataMosApi
from excel.Excel import Excel


excel = Excel()
list_ogrn = excel.read('ogrn.xlsx', "ОГРН")
print(list_ogrn)

api = DataMosApi()
list_org = api.get_all(list_ogrn)
print(list_org)

excel.build('result.xlsx', list_org)
