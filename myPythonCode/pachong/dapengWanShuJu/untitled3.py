# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 22:54:00 2018

@author: YL007
"""

url = 'http://api.map.baidu.com/direction/v1?'


cfg = {'mode':'driving', 
       #模式，driving：驾车，walking：步行，transit：公交，riding：骑行
       'origin':'车城温泉花园', #起点
       'destination':'陕西汉德车桥有限公司', #终点
       'origin_region':'西安', #起点所在城市
       'destination_region':'西安', #终点所在城市
       'output':'json', #输出类型，默认xml
       'ak':'NEnbjd3VgNqjjnmGGGbyp5wPo71VxWGy' #密钥
    }
con=""
for i in list(cfg.items()):
  con = con +i[0]+'='+i[1]+'&'
#   print(con)
# print(list(cfg.items())[0][1])
uu = url+con
print(uu)