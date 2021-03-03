# -*- coding: utf-8 -*-
# coding=utf-8


import json

import requests
import argparse

def gethead():

    # 请求内容转json
    values = {"province": "北京", "city": "北京市", "addressType": "整租房", "temperature": "36.7", "dayNum": "", "contactHbPerplr": "无接触", "toWh": "未去过/路过武汉", "familySymptom": "无症状", "remarks": "", "otherDesc": "", "backDate": "2020-02-12",
              "jtgj": "自驾/步行", "bc": "", "addressOther": "", "hbOther": "", "familyOther": None, "lj": "是", "ljOther": "", "workStatus": "到岗上班", "workOther": "", "returnCountry": "未出国", "returnCountryRemarks": "", "provinceId": "110000", "symptom": "无症状"}
    values_json = json.dumps(values)
# 请求头
    headers = {'content-type': 'application/json'}


def getarg():
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", dest="name", nargs='*', help="your name list")
    args = parser.parse_args()
    
    return {
        'name': args.name
    }


if __name__ == '__main__':

    info=getarg()
    name=info['name']
    head=gethead()
    for name in name:
        url = 'https://health.foton.com.cn/health-attendance/health/save/'+name+'@foton'
        req = requests.post(url, data=head.values_json, headers=head.headers)
        print(name + '今日打卡成功！')
    
    
