import pandas as pd
import numpy as np
import re

data=pd.read_csv('parsed_phone_info_raw.csv')
data=data.set_index(['Unnamed: 0'])

data=data.replace('以官网信息为准',np.nan).replace(' 以官网信息为准',np.nan).replace('以官网发布为准',np.nan)
data=data.replace('其他',np.nan).replace('无',np.nan).replace('官网信息为准',np.nan).replace('暂无报价',np.nan)
data=data.replace('--',np.nan).replace('以官方信息为准',np.nan).replace('其它',np.nan)
data=data.replace('以官网数据为准',np.nan).replace('以官网发布信息为准',np.nan)
data=data.replace('请以官网数据为准',np.nan).replace('以官方发布信息为准',np.nan).replace('以官方信息为准',np.nan)
data=data.replace('以官网参数为准',np.nan).replace('其它接口',np.nan).replace('-',np.nan)

def clean_comments(x):
    if pd.isnull(x):
        return np.nan
    else:
        x=x.split('+')[0]
        if '万' in x:
            x=float(x.split('万')[0])
            x=x*10000
        else:
            x=float(x)

        return x

def clean_price(x):
    if pd.isnull(x):
        return np.nan
    else:
        return float(x)

#def clean_brand(x):
#    if x=='苹果（Apple）':
#        x='Apple'
#    return x

def clean_ROM(x):

    if pd.isnull(x):
        return np.nan
    else:
        return int(x.split('GB')[0])

def clean_RAM(x):

    if pd.isnull(x):
        return np.nan
    elif x=='512MB':
        return 0.5
    else:
        y=x.split('GB')[0]
        y=float(y)
        return y
def clean_resolution(x):
    if pd.isnull(x):
        return np.nan
    else:
        find_list=re.findall('\d+',x)
        multiplication=1
        for each in find_list:
            multiplication=multiplication*int(each)
        return multiplication
def clean_resolution(x):
    if pd.isnull(x):
        return np.nan
    else:

        find_list=re.findall('\d+',x)[0:2]
        multiplication=1
        for each in find_list:
            multiplication=multiplication*int(each)
        return multiplication
def clean_weight(x):
    if pd.isnull(x):
        return np.nan
    else:
        find_list=re.findall('\d+',x)
        if len(find_list)>0:
            return find_list[0]
        else:
            return np.nan

def clean_rearcamera(x):
    if pd.isnull(x):
        return np.nan
    elif '1' in x:
        return 1
    elif '2' in x:
        return 2
    elif '3' in x:
        return 3
    elif '四' in x:
        return 4
    elif '双' in x:
        return 2
    elif '三' in x:
        return 3
    elif '4' in x:
        return 4
    elif '无' in x:
        return 0
    elif '单' in x:
        return 1
    else:
        return np.nan
def clean_battery(x):
    if pd.isnull(x):
        return np.nan
    else:
        find_list=re.findall('\d{4}',x)
        if len(find_list)>0:
            return int(find_list[0])
        else:
            return np.nan

def clean_CPU_model(x):
    if pd.isnull(x):
        return np.nan
    elif x=='麒麟710F':
        return '麒麟710F'
    elif '麒麟' in x:
         find_list=re.findall('麒麟\d+',x)
         find_list.insert(len(find_list),np.nan)
         return find_list[0]
    elif '骁龙' in x:
        find_list=re.findall('骁龙\d+',x)
        find_list.insert(len(find_list),np.nan)
        return find_list[0]
    elif 'Kirin 710' in x:
        return '麒麟710'
    elif 'Kirin 980' in x:
        return '麒麟980'
    elif 'Kirin 970' in x:
        return '麒麟970'
    else:
        return x

def clean_screen_size(x):
    if pd.isnull(x):
        return np.nan
    else:
        #print('.',end='')
        find_list=re.findall('\d+.\d+',x)
        if len(find_list)>0:

            return float(find_list[0])
        else:
            return np.nan

def clean_brand(x):
    if pd.isnull(x):
        return np.nan
    elif x=='苹果（Apple）':
        return 'Apple'
    elif x=='华为（HUAWEI）':
        return 'HUAWEI'
    elif x=='小米（MI）':
        return 'XIAOMI'
    elif x=='诺基亚（NOKIA）':
        return 'NOKIA'
    elif x=='飞利浦（Philips）':
        return 'Philips'
    elif x=='天语（K-Touch）':
        return 'K-Touch'
    elif x=='魅族（MEIZU）':
        return 'MEIZU'
    elif x=='三星（SAMSUNG）':
        return 'SAMSUNG'
    elif x=='锤子（smartisan）':
        return 'smartisan'
    elif x=='联想（lenovo）':
        return 'lenovo'
    elif x=='美图（Meitu）':
        return 'Meitu'
    elif x=='努比亚（nubia）':
        return 'nubia'
    elif x=='中兴（ZTE）':
        return 'ZTE'
    elif x=='酷派（Coolpad）':
        return 'Coolpad'
    elif x=='其他品牌':
        return np.nan
    elif x=='小辣椒':
        return 'chilli'
    elif x=='黑莓（BlackBerry）':
        return 'BlackBerry'
    else:
        return x
data['comments']=data['comments'].apply(clean_comments)
data['price']=data['price'].apply(clean_price)
data['brand']=data['brand'].apply(clean_brand)
data['RAM']=data['RAM'].apply(clean_RAM)
data['ROM']=data['ROM'].apply(clean_ROM)
data['resolution']=data['resolution'].apply(clean_resolution)
data['weight']=data['weight'].apply(clean_weight)
data['CPU model']=data['CPU model'].apply(clean_CPU_model)
data['rear camera']=data['rear camera'].apply(clean_rearcamera)
data['battery']=data['battery'].apply(clean_battery)
data['CPU model']=data['CPU model'].apply(clean_CPU_model)
data['screen size']=data['screen size'].apply(clean_screen_size)
data['brand']=data['brand'].apply(clean_brand)

data.to_csv('cleaned_data.csv')