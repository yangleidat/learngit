# coding: utf-8

import requests, json
from aip import AipSpeech

appId = '11063361'
apiKey = 'S9XOU2PDMLo9cFh9LRdw08EU'
secretKey = '31f2ca52d9b4ba558188cbd9de09b9d0'

a = AipSpeech(appId, apiKey, secretKey)

def get_token():
    '''获取token'''
    baidu_server = "https://aip.baidubce.com/oauth/2.0/token?" #获取token的地址
    grant_type = "client_credentials" #固定值
    client_id = 'S9XOU2PDMLo9cFh9LRdw08EU' #apiKEY
    client_secret = '31f2ca52d9b4ba558188cbd9de09b9d0' #secrenKEY
    #组合url
    url = "%sgrant_type=%s&client_id=%s&client_secret=%s"%(baidu_server, grant_type, client_id, client_secret)
    res = requests.post(url)
    token = json.loads(res.text)["access_token"]
    print(token)
    return token

def get_file_content(filepath):
    '''获取文件对象'''
    with open(filepath, 'rb') as fp:
        return fp.read()

token = get_token()
file = r'D:\myCode\myPythonCode\API\baidu\yuyin2wenzi\public\output.raw'
speech = get_file_content(file)
result = a.asr(speech, 'pcm', 16000, {'dev_pid':'1536', 'cuid':'yangleidat', 'token':token})
# print('\n'+result['result'][0])
print(result)