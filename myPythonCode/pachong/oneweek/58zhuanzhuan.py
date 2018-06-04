'''
2018年5月14日
一周爬虫作业
爬取http://bj.58.com/pingbandiannao/0/中来自转转用户的发布的信息
'''
import requests, time
from bs4 import BeautifulSoup

url = 'http://bj.58.com/pingbandiannao/0/'
zz_url = 'http://zhuanzhuan.58.com/detail/995983547028078602z.shtml?fullCate=5%2C38484%2C23094&fullLocal=1&from=pc&metric=null'

def get_zz_list(url):
    '''
    :param url: 列表页URL
    :return: 由{名字，URL}组成的列表
    '''
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    data_list = soup.select('div#main > div#infolist > div.infocon > table.tbimg > tbody > tr.zzinfo ')
    zhua_list = []
    for i in data_list:
        if len(i.select('td.tc > div > p > span') ) > 0 :
            zhua_list.append(i)
    zz_list = []
    for i in zhua_list:
        a = i.select('td.t > a')[0].get('href')
        b = i.select('td.t > a')[0].text
        zz_list.append({'zz_name':b, 'zz_url':a})
    return zz_list

def get_info(zz_url):
    time.sleep(5)
    wb_data = requests.get(zz_url)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    title = soup.select('body > div.content > div > div.box_left > div.info_lubotu.clearfix > div.box_left_top > h1')#标题
    price = soup.select('body > div.content > div > div.box_left > div.info_lubotu.clearfix > div.info_massege.left > div.price_li > span > i')#价格
    category = soup.select('#nav > div > span:nth-of-type(4) > a')#类目
    region = soup.select('body > div.content > div > div.box_left > div.info_lubotu.clearfix > div.info_massege.left > div.palce_li > span > i')#区域
    browse = soup.select('body > div.content > div > div.box_left > div.info_lubotu.clearfix > div.box_left_top > p > span.look_time')#浏览次数
    a = {
        'title':title[0].text,
        'price':price[0].text+'元',
        'category':category[0].text.strip(),
        'region':region[0].text,
        '浏览量':browse[0].text,
    }
    return a

for i in get_zz_list(url):
    for a in i:
        if a == 'zz_url':
            print(get_info(i[a]))
