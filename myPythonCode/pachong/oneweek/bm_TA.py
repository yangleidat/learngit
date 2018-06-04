from bs4 import BeautifulSoup
import requests
headers = {
    'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_2_1 like Mac OS X) AppleWebKit/602.4.6 (KHTML, like Gecko) Version/10.0 Mobile/14D27 Safari/602.1'
}

url = 'https://cn.tripadvisor.com/Attractions-g60763-Activities-oa60-New_York_City_New_York.html#FILTERED_LIST'
wb_data = requests.get(url, headers=headers)
soup = BeautifulSoup(wb_data.text, 'lxml')
imgs = soup.select('img[width="54"]')
for i in imgs:
    print(i.get('src'))