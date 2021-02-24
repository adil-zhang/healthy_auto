# -*- coding: utf-8 -*-
# coding=utf-8


import json

import requests

#人员名单
name = ['fucezhangshidi','fucelili','bjfcjinlei','donglulu','fuceyujianbo','fucelixiao','huxinxin']
#请求内容转json
values={"province":"北京","city":"北京市","addressType":"整租房","temperature":"36.7","dayNum":"","contactHbPerplr":"无接触","toWh":"未去过/路过武汉","familySymptom":"无症状","remarks":"","otherDesc":"","backDate":"2020-02-12","jtgj":"自驾/步行","bc":"","addressOther":"","hbOther":"","familyOther":None,"lj":"是","ljOther":"","workStatus":"到岗上班","workOther":"","returnCountry":"未出国","returnCountryRemarks":"","provinceId":"110000","symptom":"无症状"}
values_json=json.dumps(values)
#请求头
headers = {'content-type': 'application/json'}

#人太多了，写个循环
for name in name:
    url='https://health.foton.com.cn/health-attendance/health/save/'+name+'@foton'
    req = requests.post(url,data=values_json,headers=headers)