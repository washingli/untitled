# coding=utf-8
import requests
import json

class To_Hbase():
    def json_to_hbase(self,data_csv, namesw):
        pathsw = "C:\\Users\\washingli\\Desktop\\"+namesw+'.json'
        # pathsw=json.dumps(data_csv,ensure_ascii=False)
        # data_csv.to_json(pathsw,orient='records')
        # files=open(pathsw, 'rb')
        # print(len(files.read()))

        file = open(pathsw,'w')
        json.dump(data_csv,file)
        file.close()


        response = requests.post('http://192.168.1.50:32143/upload?user=chenby&destroy=yes&create=yes',
                                 files={'file': open(pathsw, 'rb')})
        # response = requests.post('http://192.168.1.50:8324/upload?user=chenby&create=yes',file={'file':files})
        print(response.status_code)
