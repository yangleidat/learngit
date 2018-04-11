import requests, json, os, base64
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
	# print(token)
	return token

def get_word(token):
	#组合参数
		#设置参数
	FORMAT = 'wav'
	CUID = 'yangleidat'
	DEV_PID = '1536'
		#读取文件并转码
	file = r'D:\myCode\myPythonCode\API\baidu\yuyin2wenzi\Calling_001.wav'
	with open(file, 'rb') as f:
		speech = base64.b64encode(f.read()).decode('utf8')
		# speech1 = f.read()
	size = os.path.getsize(file)
	headers = {'Content-Type':'application/json'}
	apiurl = "https://vop.baidu.com/server_api"
	set_data = {
		'format':FORMAT,
		'rate':16000,
		'dev_pid':DEV_PID,
		'channel':1,
		'token':get_token,
		'cuid':CUID,
		'len':size,
		'speech':speech
	}
	# a.asr(set_data)
	req = requests.post(apiurl, json.dumps(set_data), headers)
	result = json.loads(req.text)
	print(result)
	res = result['uesult'][0]
	print(res)

token = get_token()
res = get_word(token)