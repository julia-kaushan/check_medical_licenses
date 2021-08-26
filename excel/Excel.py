import pandas as pd
from io import BytesIO


class Excel:
    def __init__(self, excel_binary):
        self.df = pd.DataFrame({'Название': [], 'ОГРН': [], 'ИНН': [], 'Адрес': [], 'Лицензия': []})
        self.excel_binary = excel_binary



    def read(self, column_name):
        ogrn = pd.read_excel(self.excel_binary)
        list_ogrn = ogrn[column_name].values.tolist()
        return list_ogrn


    def build(self, list_org):
        org = list_org
        for org in list(map(lambda org: {"Название": org.name,
                                         'ОГРН': org.ogrn,
                                         'ИНН': org.inn,
                                         'Адрес': org.adress,
                                         'Лицензия': org.licenses}, list_org)):
            self.df = self.df.append(org, ignore_index=True)
        bio = BytesIO()
        writer = pd.ExcelWriter(bio, engine="xlsxwriter")
        self.df.to_excel(writer, sheet_name="Sheet1")
        writer.save()
        bio.seek(0)
        return bio


