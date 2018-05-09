'''
2018年5月8日

https://kyfw.12306.cn/otn/login/init
'''
import requests,config
#用到cookie保持
session = requests.Session()
#第一步，下载验证码图片
captcha_url = 'https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand&0.4579646842093128'
response = session.get(captcha_url)
img_content = response.content

with open('captcha.jpg','wb') as f:
    f.write(img_content)

#检验验证码
check_captcha_api = 'https://kyfw.12306.cn/passport/captcha/captcha-check'
code = input('请输入验证码的坐标 >>>:')
data = {
    'answer':code.split(' '),
    'login_site':'E',
    'rand':'sjrand'
}
check_response = session.post(url = check_captcha_api, data = data)
print(check_response.text)

#登录
login_api= 'https://kyfw.12306.cn/passport/web/login'
login_data = {
    'appid':'otn',
    'password':config.password,
    'username':config.username
}
login_respose = session.post(login_api, login_data)
print(login_respose)