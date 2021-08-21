import requests

api_url = 'https://data.mos.ru/api/rows/getresultwithcount'

params = {
    'datasetId': '1189',
    'search': '',
    'filters[0].Key': 'OGRN',
    'filters[0].Value': '1077757418111',
    'sortField': 'Number',
    'sortOrder': 'ASC',
    'versionNumber': '2',
    'releaseNumber': '546'
}

res = requests.get(api_url, params=params)

result = res.json()
count = result['Count']

org_information = {
    'Название организации': result['Result'][0]['Cells']['LicenseHolderName'],
    'ИНН организации': result['Result'][0]['Cells']['INN'],
    'ОГРН организации': result['Result'][0]['Cells']['OGRN'],
    'Адрес организации': result['Result'][0]['Cells']['Address']
}

license_inf = []
for i in range(count):
    license_inf.append({'id': (i+1),
                        'Номер лицензии': result['Result'][i]['Cells']['License'],
                        'Дата выдачи лицензии': result['Result'][i]['Cells']['RegistrationDate'],
                        'Вид деятельности': result['Result'][i]['Cells']['PermissionList']
    })

print(org_information, license_inf)

