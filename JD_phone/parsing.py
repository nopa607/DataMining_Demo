import requests
from lxml import html
import pandas as pd
import time
import numpy as np

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

browser = webdriver.Chrome()
phone_list=[]
for i in range(2):
    browser.get("https://list.jd.com/list.html?cat=9987%2C653%2C655&page={}&click=0".format(i+1))
    wait = WebDriverWait(browser, 4)
    page=html.fromstring(browser.page_source)
    for each in page.xpath("//div[@class='gl-i-wrap']"):
        print('.',end='')
        phone_id=each.xpath("../@data-sku")[-1]
        price=each.xpath(".//div[@class='p-price']/strong[1]/i/text()")[-1]
        comments=each.xpath(".//div[@class='p-commit']/strong/a/text()")[-1]
        phone_list.append(list((phone_id,price,comments)))
        to_save=pd.DataFrame(phone_list)
        to_save.to_csv('phone_list.csv',encoding='UTF-8')


browser.close()


df=pd.read_csv('phone_list.csv')
phone_list=[]
df=df.set_index(['Unnamed: 0'])
for i in range(df.shape[0]):
    phone_list.append(df.iloc[i,:].values)


dic={}
whether_to_pause=0
for each in phone_list[0:]:
        url='https://item.jd.com/{}.html'.format(each[0])
        r=requests.get(url)
        if r.ok==False:
            print('Access denied!')
            break
        page=html.fromstring(r.text)
        dic_temp={}
        
        print(r.text)

        list_temp=page.xpath(".//dl[@class='clearfix']/dt[text()='电池容量（mAh）']/dd/text()")
        list_temp.insert(0,np.nan)
        dic_temp['battery']=list_temp[-1]

        list_temp=page.xpath(".//dl[@class='clearfix']/dt[text()='上市年份']/dd/text()")
        list_temp.insert(0,np.nan)
        dic_temp['year']=list_temp[-1]

        list_temp=page.xpath("//dl[@class='clearfix'][./dt[text()='上市月份']]/dd/text()")
        list_temp.insert(0,np.nan)
        dic_temp['month']=list_temp[-1]

        list_temp=page.xpath("//dl[@class='clearfix'][./dt[text()='品牌']]/dd/text()")
        list_temp.insert(0,np.nan)
        dic_temp['brand']=list_temp[-1]

        list_temp=page.xpath("//dl[@class='clearfix'][./dt[text()='型号']]/dd/text()")
        list_temp.insert(0,np.nan)
        dic_temp['model']=list_temp[-1]

        list_temp=page.xpath("//dl[@class='clearfix'][./dt[text()='机身重量（g）']]/dd/text()")
        list_temp.insert(0,np.nan)
        dic_temp['weight']=list_temp[-1]

        list_temp=page.xpath("//dl[@class='clearfix'][./dt[text()='CPU型号']]/dd/text()")
        list_temp.insert(0,np.nan)
        dic_temp['CPU model']=list_temp[-1]

        list_temp=page.xpath("//dl[@class='clearfix'][./dt[text()='CPU频率']]/dd/text()")
        list_temp.insert(0,np.nan)
        dic_temp['CPU freq']=list_temp[-1]

        list_temp=page.xpath("//dl[@class='clearfix'][./dt[text()='CPU核数']]/dd/text()")
        list_temp.insert(0,np.nan)
        dic_temp['CPU cores']=list_temp[-1]

        list_temp=page.xpath("//dl[@class='clearfix'][./dt[text()='最大支持SIM卡数量']]/dd/text()")
        list_temp.insert(0,np.nan)
        dic_temp['SIM cards']=list_temp[-1]

        list_temp=page.xpath("//dl[@class='clearfix'][./dt[text()='ROM']]/dd/text()")
        list_temp.insert(0,np.nan)
        dic_temp['ROM']=list_temp[-1]

        list_temp=page.xpath("//dl[@class='clearfix'][./dt[text()='RAM']]/dd/text()")
        list_temp.insert(0,np.nan)
        dic_temp['RAM']=list_temp[-1]

        list_temp=page.xpath("//dl[@class='clearfix'][./dt[text()='主屏幕尺寸（英寸）']]/dd/text()")
        list_temp.insert(0,np.nan)
        dic_temp['screen size']=list_temp[-1]

        list_temp=page.xpath("//dl[@class='clearfix'][./dt[text()='分辨率']]/dd/text()")
        list_temp.insert(0,np.nan)
        dic_temp['resolution']=list_temp[-1]

        list_temp=page.xpath("//dl[@class='clearfix'][./dt[text()='屏幕材质类型']]/dd/text()")
        list_temp.insert(0,np.nan)
        dic_temp['screen material']=list_temp[-1]

        list_temp=page.xpath("//dl[@class='clearfix'][./dt[text()='前置摄像头']]/dd/text()")
        list_temp.insert(0,np.nan)
        dic_temp['front camera']=list_temp[-1]

        list_temp=page.xpath("//dl[@class='clearfix'][./dt[text()='摄像头数量']]/dd/text()")
        list_temp.insert(0,np.nan)
        dic_temp['rear camera']=list_temp[-1]


        list_temp=page.xpath("//dl[@class='clearfix'][./dt[text()='后置摄像头']]/dd/text()")
        list_temp.insert(0,np.nan)
        dic_temp['rear camera specs']=list_temp[-1]


        list_temp=page.xpath("//dl[@class='clearfix'][./dt[text()='充电接口类型']]/dd/text()")
        list_temp.insert(0,np.nan)
        dic_temp['charging port']=list_temp[-1]

        dic_temp['price']=each[1]
        dic_temp['comments']=each[2]

        dic[each[0]]=dic_temp

        print('.',end='')

        whether_to_pause+=1
        if whether_to_pause%50==0:
            print(whether_to_pause,end='')
            print(' pages parsed.Suspending for 10 seconds.')
            time.sleep(10)
            print('Parsing resumed: ',end='')
        time.sleep(0.5)


finaldf=pd.DataFrame(dic).T
finaldf.to_csv('parsed_phones.csv')