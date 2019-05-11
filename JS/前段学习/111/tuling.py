import requests, json

"""
异常码	说明
5000	无解析结果
6000	暂不支持该功能
4000	请求参数格式错误
4001	加密方式错误
4002	无功能权限
4003	该apikey没有可用请求次数
4005	无功能权限
4007	apikey不合法
4100	userid获取失败
4200	上传格式错误
4300	批量操作超过限制
4400	没有上传合法userid
4500	userid申请个数超过限制
4600	输入内容为空
4602	输入文本内容超长(上限150)
7002	上传信息失败
8008	服务器错误
0   	上传成功
========================
参数说明

参数	类型	是否必须	取值范围	说明
intent	-	Y	-	请求意图
results	-	N	-	输出结果集
intent

参数	类型	是否包含	取值范围	说明
code	int	Y	-	输出功能code
intentName	String	N	-	意图名称
actionName	String	N	-	意图动作名称
parameters	Map	N	-	功能相关参数
results

参数	类型	是否包含	取值范围	说明
resultType	String	Y	文本(text);连接(url);音频(voice);视频(video);图片(image);图文(news)	输出类型
values	-	Y	-	输出值
groupType	int	Y	-	‘组’编号:0为独立输出，大于0时可能包含同组相关内容 (如：音频与文本为一组时说明内容一致)
=========================================
"""
def get_response(msg, city='西安', street=None):
    apiurl = 'http://openapi.tuling123.com/openapi/api/v2'
    apikey = '731b13c2c11e4433a11fdeeeed6c84f4'
    miyao = 'b21d2bec8893d8a8'
    userid = '348341'

    dat = {
        "reqType":0,#输入类型:0-文本(默认)、1-图片、2-音频
        "perception": {#输入信息
            "inputText": {
                "text": msg
            },
            "inputImage": {
                "url": "imageUrl"
            },
            "selfInfo": {
                "location": {
                    "city": city,
                    "province": "",
                    "street": street
                }
            }
        },
        "userInfo": {
            "apiKey": apikey,
            "userId": userid
        }
    }
    dat = json.dumps(dat)
    respons = requests.post(apiurl, data = dat).json()
    #print(respons)
    tulingmsg = respons['results'][0]['values']['text']
    return tulingmsg

msg = '晚安'
city = '宝鸡'
print(get_response(msg))