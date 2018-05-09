from bs4 import BeautifulSoup
import requests
import time

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0',
    'Cookie':'TASession=%1%V2ID.4368E3DC212514F2E9C66F472B0976C0*SQ.40*PR.427%7C*LS.ActionRecord*GR.5*TCPAR.84*TBR.1*EXEX.94*ABTR.82*PHTB.51*FS.45*CPU.98*HS.recommended*ES.popularity*AS.popularity*DS.5*SAS.popularity*FPS.oldFirst*TS.5E87C284F1DFC94D31DC2DC377B63D23*FA.1*DF.0*IR.1*OD.null*FLO.60763*TRA.true*LD.60763; ServerPool=C; TAPD=cn.tripadvisor.com; TATravelInfo=V2*AY.2018*AM.5*AD.20*DY.2018*DM.5*DD.21*A.2*MG.-1*HP.2*FL.3*DSM.1525875093988*RS.1; TAUD=LA-1525872422099-1*RDD-1-2018_05_09*HDD-151474-2018_05_20.2018_05_21*LD-2671878-2018.5.20.2018.5.21*LG-2671880-2.1.F.; TART=%1%enc%3ATJRYq41NmC%2BmbXLr54JP3x1Tl7iLBN0ZrJ%2B0KZiU5BJOIS2gslhbe2FzobVlI00G%2FTVcplEacYY%3D; TAUnique=%1%enc%3ApkjiQZB7WO1MlFirjU2YL7VzUa%2B%2FFiqGN7beEyh0tj2uFlGyP%2FmmLQ%3D%3D; CM=%1%HanaPersist%2C%2C-1%7Cpu_vr2%2C%2C-1%7CPremiumMobSess%2C%2C-1%7Ct4b-pc%2C%2C-1%7CSPHRSess%2C%2C-1%7CHanaSession%2C%2C-1%7CRestAds%2FRPers%2C%2C-1%7CRCPers%2C%2C-1%7CWShadeSeen%2C%2C-1%7Cpv%2C2%2C-1%7Cpu_vr1%2C%2C-1%7CFtrPers%2C%2C-1%7CTheForkMCCPers%2C%2C-1%7CHomeASess%2C2%2C-1%7CPremiumSURPers%2C%2C-1%7Ctvsess%2C-1%2C-1%7CPremiumMCSess%2C%2C-1%7CRestPartSess%2C%2C-1%7Ccatchsess%2C5%2C-1%7Cbrandsess%2C%2C-1%7CRestPremRSess%2C%2C-1%7CCpmPopunder_1%2C1%2C1525959065%7CCCSess%2C%2C-1%7CCpmPopunder_2%2C1%2C-1%7CPremRetPers%2C%2C-1%7CViatorMCPers%2C%2C-1%7Csesssticker%2C%2C-1%7C%24%2C%2C-1%7Ct4b-sc%2C%2C-1%7CRestAdsPers%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS2%2C%2C-1%7Cb2bmcpers%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS%2C%2C-1%7CPremMCBtmSess%2C%2C-1%7CPremiumSURSess%2C%2C-1%7CLaFourchette+Banners%2C%2C-1%7Csess_rev%2C%2C-1%7Csessamex%2C%2C-1%7CPremiumRRSess%2C%2C-1%7CSaveFtrPers%2C%2C-1%7CSPMCSess%2C%2C-1%7CTheForkORSess%2C%2C-1%7CTheForkRRSess%2C%2C-1%7Cpers_rev%2C%2C-1%7CMetaFtrSess%2C%2C-1%7CRBAPers%2C%2C-1%7CWAR_RESTAURANT_FOOTER_PERSISTANT%2C%2C-1%7CFtrSess%2C%2C-1%7CRestAds%2FRSess%2C%2C-1%7CHomeAPers%2C%2C-1%7C+r_lf_1%2C%2C-1%7CPremiumMobPers%2C%2C-1%7CSPHRPers%2C%2C-1%7CRCSess%2C%2C-1%7C+r_lf_2%2C%2C-1%7Ccatchpers%2C3%2C1526477286%7CLaFourchette+MC+Banners%2C%2C-1%7CRestAdsCCSess%2C%2C-1%7CRestPartPers%2C%2C-1%7CRestPremRPers%2C%2C-1%7Cvr_npu2%2C%2C-1%7Csh%2CRuleBasedPopup%2C1525958948%7CLastPopunderId%2C137-1859-null%2C-1%7Cpssamex%2C%2C-1%7CTheForkMCCSess%2C%2C-1%7Cvr_npu1%2C%2C-1%7CCCPers%2C%2C-1%7Ctvpers%2C1%2C1526477348%7CWAR_RESTAURANT_FOOTER_SESSION%2C%2C-1%7Cbrandpers%2C%2C-1%7Cb2bmcsess%2C%2C-1%7CSPMCPers%2C%2C-1%7CPremRetSess%2C%2C-1%7CViatorMCSess%2C%2C-1%7CPremiumMCPers%2C%2C-1%7CWarPopunder_Session%2C%2C-1%7CPremiumRRPers%2C%2C-1%7CRestAdsCCPers%2C%2C-1%7CWarPopunder_Persist%2C%2C-1%7CTheForkORPers%2C%2C-1%7Cr_ta_2%2C%2C-1%7CPremMCBtmPers%2C%2C-1%7CTheForkRRPers%2C%2C-1%7Cr_ta_1%2C%2C-1%7CSaveFtrSess%2C%2C-1%7CRestAdsSess%2C%2C-1%7CRBASess%2C%2C-1%7CSPORPers%2C%2C-1%7Cperssticker%2C%2C-1%7CCPNC%2C%2C-1%7CMetaFtrPers%2C%2C-1%7C; TAReturnTo=%1%%2FAttractions-g60763-Activities-New_York_City_New_York.html; TASSK=enc%3AAP5bVsl19sTqhxgescaKU%2B%2FuLFu7Vd9XqT5XyAGA17ftrAjYHQP4F%2FF%2FmPdNpTF7fJwxa3LAZ0cEtHySRfbOFhQhyubosnRHZK0MS2EN3xqr3VwYYnp9%2FRtaCBr43MD1Nw%3D%3D; PAC=AOdEWrmDaQk_a-YMASvnsr5U9lt2OauY2j70g1bwzUmAWpB22ItdSBvDVFyYmp1c_8CIeSfbn8QqHhPfsRVx_MrJXvWhKM0-xwav76h2C_4RSvFoWhmGbzI-atTbYEeKZ73OaPuU7vDoTtnh-CTN5wgGPYUEt6BNbfoBFKzHJj48; PMC=V2*MS.27*MD.20180509*LD.20180509; roybatty=TNI1625!ACvOrcaOkGoPy7kxgCeYnLRintk7EXC4%2BXEFySqTyo3hS3yC13eesvBs8n0Byin8TkarftRt2r9szJzOs7qpuuC0IzCsUEVw%2F%2FfKQIngSndehqqkWZvs3lWCOQZ7qkVVgj0V7GbLiesTneO1AuKsrD2YQxBIuHTo1ibDPm6G3928%2C1; __gads=ID=6486d1627dc8eb21:T=1525872922:S=ALNI_MaG8wXfxMiJalUNlcu89j9qodoaXQ; SecureLogin2=3.4%3AAHtNY%2B5zxjX7awT84AcH7xY26h6T%2FF9LlSTG8G4hbw2cdrhfkJo%2FHUzSEQVrXCAoXCMCWcDwkFmXtSGMUfDuFtjuvlJh3U%2FSETwDf7rM0G5Qp8JIQoiVz9fsj77%2FjsNcQw488ydfBhpyNmUd17jS7fDBMjducub0X07P%2Bu8%2F7pjOICDqnHfMiDcxRl2RKlsP8KrqFNnz4uO0m46p%2FJr7v48%3D; TAAuth3=3%3A528f0325bc7acbe70c94620356f68c91%3AAJmjqEcsUsOGRpXCEPpIr3vVjDO%2B%2FqSHcGk%2FYJcZJfYzb6OOrMUWub%2BAxSc5xbhrEDHnLbDkjhAnSS3XT%2Fw1wUFrud5bfxX3d1CSN%2B0BveFYDXLg0NLGuk4xOuuvZpqdxJyP2FaBXipfnZ1hPDK5h7uMJZfinKXHkJL2WEkpEISvwSfBOEOUaSZ91hgEngm8SnArZu6RqKgt5EwxscMnwfI%3D'
}

url = 'https://cn.tripadvisor.com/Attractions-g60763-Activities-New_York_City_New_York.html'
urls = ['https://cn.tripadvisor.com/Attractions-g60763-Activities-oa{}-New_York_City_New_York.html#FILTERED_LIST'.format(str(i)) for i in range(30,1170,30)]
def get_img(url,data=None):
    wb_data = requests.get(url)
    # time.sleep(4)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    titles = soup.select('div.attraction_element > div > div > div > div > div > a')
    imgs = soup.select('img[width="180"]')
    cates = soup.select('div.p13n_reasoning_v2 ')
    b = []
    for i in cates:
        catea = list(i.stripped_strings)
        if ',' in catea:
            catea.remove(',')
        b.append(catea)
        if [] in b:
            b.remove([])

    a = []
    for title, img, cate in zip(titles, imgs, b):
        # catea = []
        # catea = list(cate.stripped_strings)
        # if ',' in catea:
        #     catea.remove(',')
        data = {
            'title':title.get_text(),
            'img':img.get('src'),
            'cate':cate,
        }
        a.append(data)
        print(data)



'''
url_saves = 'https://cn.tripadvisor.com/Saves/75435128'
wb_data = requests.get(url_saves, headers=headers)
soup = BeautifulSoup(wb_data.text,'lxml')
titles = soup.select('div.saves-single-item.location > a.title')

print(titles)
'''
# get_img('https://cn.tripadvisor.com/Attractions-g60763-Activities-oa30-New_York_City_New_York.html#FILTERED_LIST')
for i in urls:
    get_img(i)