# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 21:50:15 2018

@author: YL007
"""

import requests

url = 'http://api.map.baidu.com/direction/v1'
#api参数
cfg = {'mode':'driving', 
       #模式，driving：驾车，walking：步行，transit：公交，riding：骑行
       'origin':'车城温泉花园', #起点
       'destination':'陕西汉德车桥有限公司', #终点
       'origin_region':'西安', #起点所在城市
       'destination_region':'西安', #终点所在城市
       'output':'json', #输出类型，默认xml
       'ak':'NEnbjd3VgNqjjnmGGGbyp5wPo71VxWGy' #密钥
    }

r = requests.get(url, cfg)
r_js = r.json()
#返回js数据

routes = r_js['result']['routes'][0]
dis = routes['distance']
time = routes['duration']

#以下打开文件，写字段名
f_path = "D:\\myCode\\myPythonCode\\dapengWanShuJu\\result.txt"
f = open(f_path, 'w')
f.write('lng,lat\n')

steps = routes['steps']
for step in steps:
  path = step['path']
  points = path.split(';')
  for point in points:
    lng = point.split(',')[0]
    lat = point.split(',')[1]
    f.writelines(str(lng)+','+str(lat)+'\n')
f.close()
    