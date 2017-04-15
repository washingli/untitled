# coding=utf-8
import pandas as pd
import numpy as np
import requests
import json

response = requests.put('http://192.168.1.50:8324/all?table=S1_QianChengWuYou')
print(response.text)
data = json.loads(response.text)
# print(data)
read_csvsw = pd.DataFrame(data)
print(read_csvsw)



