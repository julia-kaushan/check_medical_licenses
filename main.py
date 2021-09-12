from adapter.DataMosApi import DataMosApi
from excel.Excel import Excel
from accounts.AccountRepository import AccountRepository
from MedicalOrg.MedicalOrgRepository import MedicalOrgRepository
import os

# excel = Excel()
# list_ogrn = excel.read('ogrn.xlsx', "ОГРН")
# print(list_ogrn)
#
# api = DataMosApi()
# list_org = api.get_all(list_ogrn)
# print(list_org)
#
# excel.build('result.xlsx', list_org)

# a = AccountRepository()
# b = a.register('555@yandex.ru')
# print(b.__dict__)

a = MedicalOrgRepository()
a.xmlparser_tobase()
