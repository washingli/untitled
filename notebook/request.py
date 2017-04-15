import requests
url = 'https://gw.cloud.sinocbd.com/api/test/show'
multiple_files ={"date":"sd"}
r = requests.post(url, data=multiple_files,verify=False)
print(r.text)
print(r.status_code)