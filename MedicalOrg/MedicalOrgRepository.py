from xml.etree import ElementTree
from accounts.SqlConnection import SqlConnetion
from models.MedicalOrg import MedicalOrg


class MedicalOrgRepository:
    def __init__(self):
        self.db = SqlConnetion(database='medical_org')

    def xmlparser_tobase(self):
        tree = ElementTree.parse("Base1.xml")
        root = tree.getroot()
        add_org = ("INSERT INTO medical_org.medical_org "
                   "(name, adress, OGRN, INN, license_num, license_date, termination ) "
                   "VALUES (%(name)s, %(adress)s, %(OGRN)s, %(INN)s, %(license_num)s, %(license_date)s, %(termination)s)")
        for child in root:
            date = {"name": child[3].text,
                    "adress": child[7].text,
                    "OGRN": child[8].text,
                    "INN": child[9].text,
                    "license_num": child[11].text,
                    "license_date": child[12].text,
                    "termination": 1 if child[19].text else 0}
            self.db.execute(add_org, date)

    def get_info_org(self, ogrn):
        query = ("SELECT * FROM medical_org.medical_org WHERE OGRN=%(OGRN)s AND termination=0")
        OGRN = {'OGRN': ogrn}
        result = self.db.execute(query, OGRN)
        resultORG = MedicalOrg(ogrn)
        for i in result:
            resultORG.name = i[1]
            resultORG.inn = i[4]
            resultORG.adress = i[2]
            resultORG.licenses.append(i[5])
        return resultORG

    def get_all(self, list_ogrn):
        list_org = list()
        for ogrn in list_ogrn:
            list_org.append(self.get_info_org(ogrn))
        return list_org
