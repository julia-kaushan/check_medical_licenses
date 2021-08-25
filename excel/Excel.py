import pandas as pd


class Excel:
    def __init__(self):
        self.df = pd.DataFrame({'Название': [], 'ОГРН': [], 'ИНН': [], 'Адрес': [], 'Лицензия': []})


    def read(self, name_file, column_name):
        ogrn = pd.read_excel(name_file)
        list_ogrn = ogrn[column_name].values.tolist()
        return list_ogrn


    def build(self, name_file: str, list_org):
        org = list_org
        for org in list(map(lambda org: {"Название": org.name,
                                         'ОГРН': org.ogrn,
                                         'ИНН': org.inn,
                                         'Адрес': org.adress,
                                         'Лицензия': org.licenses}, list_org)):
            self.df = self.df.append(org, ignore_index=True)
        print(self.df)
        self.df.to_excel(name_file)

