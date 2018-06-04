import requests
from bs4 import  BeautifulSoup
import time

url = 'http://bj.xiaozhu.com/search-duanzufang-p1-0/'
hw_url = 'http://bj.xiaozhu.com/fangzi/2581904363.html'
urls = ['http://bj.xiaozhu.com/search-duanzufang-p{}-0/'.format(str(i)) for i in range(1,300//8)]

def get_data(url,data=None):
    '''
    :param url: 房源的URL
    :param data:
    :return: 房源信息
    '''
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    titles = soup.select('div.pho_info > h4 > em')#标题
    add = soup.select('.pr5')#地址
    rizujin = soup.select('.day_l')#日租金
    photos = soup.select('#curBigImage')#房子第一张照片
    master_photo = soup.select('.member_pic > a > img')#房东照片
    if 'member_ico1' in soup.select('.member_pic > div'):#判断房东性别
        master_nv = '女'
    else:
        master_nv = '男'
    master_name = soup.select('.lorder_name')#房东名字
    print(titles, add, rizujin, photos, master_photo, master_name, master_nv, sep='\n-------------------------------------\n')
    time.sleep(5)

def get_url_list(url,data=None):
    '''
    :param url:房源列表页的URL
    :param data:
    :return:每页所有房源连接的list
    '''
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    links = soup.select('.pic_list > li > a ')
    link_list = []
    for i in links:
        # print(i.get('href'))
        link_list.append(i.get('href'))
    return link_list

for i in urls:
    for j in get_url_list(i):
        get_data(j)
