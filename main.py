from adapter.DataMosApi import DataMosApi

a = DataMosApi()

list_ogrn = [1077757418111, 1027739726233, 1097746129843, 1027739542962, 1027700345012, 1117746464296, 1077761370169, 1057746089169]

b = a.get_all(list_ogrn)
for i in range(len(list_ogrn)):
    print(b[i].name)




