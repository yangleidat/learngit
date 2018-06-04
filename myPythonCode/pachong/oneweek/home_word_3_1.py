import requests
from bs4 import  BeautifulSoup

url = 'http://bj.xiaozhu.com/search-duanzufang-p1-0/'
hw_url = 'http://bj.xiaozhu.com/fangzi/2581904363.html'

wb_data = requests.get(hw_url)
soup = BeautifulSoup(wb_data.text, 'lxml')

titles = soup.select('div.pho_info > h4 > em')
add = soup.select('.pr5')
rizujin = soup.select('.day_l')
photos = soup.select('#curBigImage')
master_photo = soup.select('.member_pic > a > img')
if 'member_ico1' in soup.select('.member_pic > div'):
    master_nv = '女'
else:
    master_nv = '男'
master_name = soup.select('.lorder_name')
print(titles, add, rizujin, photos, master_photo, master_name, master_nv, sep='\n-------------------------------------\n')