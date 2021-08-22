import requests
from models.MedicalOrg import MedicalOrg

class DataMosApi:

    API = 'https://data.mos.ru/api/rows/getresultwithcount'

    params = {
        'datasetId': '1189',
        'search': '',
        'filters[0].Key': 'OGRN',
        'filters[0].Value': None,
        'sortField': 'Number',
        'sortOrder': 'ASC',
        'versionNumber': '2',
        'releaseNumber': '546'
    }

    def get(self, ogrn):
        org = MedicalOrg(ogrn)
        self.params['filters[0].Value'] = ogrn
        try:
            response = requests.get(self.API, params=self.params)
            if response.status_code != 200:
                raise requests.exceptions.ConnectionError
            res = response.json()
            count = res['Count']
            # мы не можем определить, является ли лицензия действующей
            if count > 10:
                count = 10
            org.name = res['Result'][0]['Cells']['LicenseHolderName']
            org.inn = res['Result'][0]['Cells']['INN']
            org.adress = res['Result'][0]['Cells']['Address']
            for i in range(count):
                org.licenses.append({'id': (i + 1),
                                     'Номер лицензии': res['Result'][i]['Cells']['License'],
                                     'Дата выдачи лицензии': res['Result'][i]['Cells']['RegistrationDate'],
                                     'Вид деятельности': res['Result'][i]['Cells']['PermissionList']
                                     })
            return org
        except requests.exceptions.ConnectionError as err:
            print('Сервер не доступен', err)


    def get_all(self, list_ogrn):
        list_org = []
        for ogrn in list_ogrn:
            list_org.append(self.get(ogrn))
        return list_org