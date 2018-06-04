'''
2018年5月10日
爬取王者荣耀英雄皮肤
'''
from bs4 import BeautifulSoup
import requests, time, re

headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    'Cookie':'LW_uid=M1a5t2t1A9k7V9W7B708l5T7f4; eas_sid=v1Y542K1P9G7p9H797a8y5h852; pgv_pvid=1023401668; pgv_pvi=7337104384; pgv_pvid_new=_367758da4a; pgv_si=s8804880384; pgv_info=pgvReferrer=http://qt.qq.com/zhibo/index.html&ssid=s2793128968; LW_sid=71G5d2z5E9C6c2w8e6C7f7T5s9; PTTcookiesFrom=seo_baidu; PTTuserFirstTime=1525962867784; ts_refer=www.baidu.com/link; ts_uid=8061401328; PTTosav=osav; PTTweekStartTime=1525962867791; PTTweekPerSession=1525962889996; PTTperWeekNum=2; ieg_ingame_userid=GAmPMshb54FgAqJ8Y6RxEeupdTy6TsEb; PTTrouteLine=index_herolist_herodetail_herodetail_herodetail_herodetail_herodetail',
    'Host':'pvp.qq.com',
    'If-Modified-Since':'Thu, 10 May 2018 14:40:00 GMT',
    'Referer':'http://pvp.qq.com/web201605/herolist.shtml',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36',
}
# pf_url = 'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/{0}/{0}-bigskin-{1}.jpg'.format(hero_id, pf_num)
herolist_url = 'http://pvp.qq.com/web201605/herolist.shtml'
hero_url = 'http://pvp.qq.com/web201605/herodetail/111.shtml'
hero_url_befor = 'http://pvp.qq.com/web201605/'
def hero_data_all(herolist_url):
    '''
    :param herolist_url:全英雄列表网址
    :return: 英雄名字与英雄ID和网址对应的一个字典
    '''
    wb_data = requests.get(herolist_url)
    soup = BeautifulSoup(wb_data.content, 'lxml')
    heros = soup.select('.herolist > li > a > img')
    heros_url = soup.select('.herolist > li > a')
    hero_data_all = {}
    hero_data_all1 = []
    for i,j in zip(heros, heros_url):
        hero_name = i.get('alt')
        hero_url = j.get('href')
        hero_id = re.search(r'/\d+', hero_url).group(0).replace(r'/', '')
        hero_data_all.update({hero_name:[hero_id,hero_url]})
        hero_data_all1.append([hero_name, hero_id, hero_url])
    return hero_data_all1

# print(hero_data_all(herolist_url))
def get_pf_data(hero_name, hero_id, hero_url):
    wb_data = requests.get('http://pvp.qq.com/web201605/herodetail/{}.shtml'.format(hero_id))
    soup = BeautifulSoup(wb_data.content, 'lxml')
    hero_pf_all = soup.select('body > div.wrapper > div.zk-con1.zk-con > div > div > div.pic-pf > ul')
    pf_names = hero_pf_all[0].get('data-imgname')
    if '|' in pf_names:
        pf_names_list = pf_names.split('|')
        pf_count = len(pf_names_list)
    else:
        pf_count = 1
        pf_names_list = [pf_names]
    pf_data = {
        '英雄':hero_name,
        '英雄ID':hero_id,
        '皮肤数量':pf_count,
        '皮肤名字':pf_names_list
    }
    return pf_data

a = hero_data_all(herolist_url)
for i in a:
    pf_data = get_pf_data(i[0], i[1], i[2])
    for pf_num, pf_name in zip(range(1,pf_data['皮肤数量']+1), pf_data['皮肤名字']):
        print('开始下载英雄-'+pf_data['英雄']+'-的皮肤-'+pf_name+'-...')
        time.sleep(3)
        respnse_pf_data = requests.get('http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/{0}/{0}-mobileskin-{1}.jpg'.format(pf_data['英雄ID'], pf_num))
        imgdata = respnse_pf_data.content
        with open('./img/'+pf_data['英雄']+'-'+pf_name+'.jpg', 'wb') as f:
            f.write(imgdata)
        f.close()
        print('英雄-'+pf_data['英雄']+'-的皮肤-'+pf_name+'-下载完毕')