# -*- coding: utf-8 -*-
# coding=utf-8

import json

import requests

import  base64

url = "aHR0cDovLzEwLjEwNS4xMS4yMjo4MTMzL2hlYWx0aC9zYXZlL2Z1Y2V6aGFuZ3NoaWRpQGZvdG9u"
url = base64.b64decode(url).decode("utf-8")

url1 = "aHR0cDovLzEwLjEwNS4xMS4yMjo4MTMzL2hlYWx0aC9zYXZlL2Z1Y2VsaWxpQGZvdG9u"
url1 = base64.b64decode(url1).decode("utf-8")

url2 = "http://10.105.11.22:8133/health/save/jingguodong@foton"
url3 = "http://10.105.11.22:8133/health/save/kangchao3@foton"
url4 = "http://10.105.11.22:8133/health/save/wangpengtao2@foton"
url5 = "http://10.105.11.22:8133/health/save/bjfcjinlei@foton"
url6 = "http://10.105.11.22:8133/health/save/donglulu@foton"
url7 = "http://10.105.11.22:8133/health/save/fuceyujianbo@foton"
url8 = "http://10.105.11.22:8133/health/save/huxinxin@foton"
url9 = "http://10.105.11.22:8133/health/save/fucelixiao@foton"
values={"province":"北京","city":"北京市","addressType":"整租房","temperature":"36.7","dayNum":"","contactHbPerplr":"无接触","toWh":"未去过/路过武汉","familySymptom":"无症状","remarks":"","otherDesc":"","backDate":"2020-02-12","jtgj":"自驾/步行","bc":"","addressOther":"","hbOther":"","familyOther":None,"lj":"是","ljOther":"","workStatus":"到岗上班","workOther":"","returnCountry":"未出国","returnCountryRemarks":"","provinceId":"110000","symptom":"无症状"}
values_json=json.dumps(values)
headers = {'content-type': 'application/json'}
req = requests.post(url,data=values_json,headers=headers)
req1 = requests.post(url1,data=values_json,headers=headers)
req1 = requests.post(url2,data=values_json,headers=headers)
req1 = requests.post(url3,data=values_json,headers=headers)
req1 = requests.post(url4,data=values_json,headers=headers)
req1 = requests.post(url5,data=values_json,headers=headers)
req1 = requests.post(url6,data=values_json,headers=headers)
req1 = requests.post(url7,data=values_json,headers=headers)
req1 = requests.post(url8,data=values_json,headers=headers)
req1 = requests.post(url9,data=values_json,headers=headers)
change = req.json()
new_req = json.dumps(change, ensure_ascii=False)
print(new_req)

