# coding=utf-8
import codecs

import pandas as pd
import requests


class To_Hbase():
    def json_to_hbase(self, data_csv, namesw):
        # origin = "C:\\Users\\hc\\Desktop\\" + namesw + '.csv'
        target = "C:\\Users\\hc\\Desktop\\" + namesw + '.json'

        # print(data_csv)
        jsonsw = data_csv.to_json()
        print(jsonsw)
        dict_csv = pd.DataFrame({namesw: [jsonsw]})
        print(dict_csv)
        # csv = pd.read_csv(origin)
        dict_csv.to_csv(target, encoding='utf-8', index=False)
        # csv.to_json(target, force_ascii=False)
        file = open(target, 'rb')
        print(len(file.read()))
        # response = requests.post('http://192.168.1.50:8324/upload?user=chenby&create=True&destroy=False',
        #                          files={'file': open(target, 'rb')})
        response = requests.put('http://192.168.1.50:8324/upload?user=chenby&create=yes',
                                files={'file': file})
        file.close()
        print(response.text)