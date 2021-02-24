# -*- coding: utf-8 -*-
# coding=utf-8

import json

import requests

import  base64

url = "https://health.foton.com.cn/health-attendance/health/save/fucezhangshidi@foton"
url1 = "https://health.foton.com.cn/health-attendance/health/save/fucelili@foton"

url2 = "https://health.foton.com.cn/health-attendance/health/save/jingguodong@foton"
url3 = "https://health.foton.com.cn/health-attendance/health/save/kangchao3@foton"
url4 = "https://health.foton.com.cn/health-attendance/health/save/wangpengtao2@foton"
url5 = "https://health.foton.com.cn/health-attendance/health/save/bjfcjinlei@foton"
url6 = "https://health.foton.com.cn/health-attendance/health/save/donglulu@foton"
url7 = "https://health.foton.com.cn/health-attendance/health/save/fuceyujianbo@foton"
url8 = "https://health.foton.com.cn/health-attendance/health/save/huxinxin@foton"
url9 = "https://health.foton.com.cn/health-attendance/health/save/fucelixiao@foton"
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


