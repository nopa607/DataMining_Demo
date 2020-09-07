import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns


data=pd.read_csv('cleaned_data.csv')
data=data.set_index(['Unnamed: 0']) 
print(data.shape)


pie_plt=data.groupby(['brand']).sum()['comments'].sort_values(ascending=False)
#扇形图
# fig,axes=plt.subplots(figsize=(12,12))
# comment_sum=pie_plt.values.sum()
# percen=[np.round(each/comment_sum*100,2) for each in pie_plt.values]
# axes.pie(pie_plt.values,labels=pie_plt.index,labeldistance=1.2,autopct = '%3.1f%%')
# axes.legend([pie_plt.index[i]+': '+str(percen[i])+"%" for i in range(len(percen))],loc='upper right',bbox_to_anchor=(1, 0, 1, 1))
# axes.set_title('Estimated Handphone Market Share in China')
# plt.show()

# #data[(data['brand']=='NOKIA')|(data['brand']=='Philips')]['price'].median()#诺基亚和飞利浦手机价格中位数
# # data[(data['brand']=='NOKIA')|(data['brand']=='Philips')]['price'].mean()#诺基亚和飞利浦手机价格平均数

# #HeatMap
# correlation=data[(data['brand']!='Apple')&(data['price']!=9999)].corr() 
# fig,axes=plt.subplots(figsize=(8,8))
# cax=sns.heatmap(correlation,vmin=-0.25, cmap="RdBu",vmax=1,square=True,annot=True)
# axes.set_xticklabels(['RAM', 'ROM', 'battery', 'comments', 'price', 'rear camera',
#        'resolution', 'screen size', 'weight'])
# axes.set_yticklabels(['RAM', 'ROM', 'battery', 'comments', 'price', 'rear camera',
#        'resolution', 'screen size', 'weight'])
# axes.set_title('Heatmap of Correlation Matrix of numerical data')
# plt.show()


#price bar
bar_plt=data.groupby(['brand']).median()['price']

fig,axes=plt.subplots(figsize=(20,8))
axes.bar(bar_plt.index,bar_plt.values)
axes.set_title('Median price of handphones of various brands')



bar_plt2=data.groupby(['screen material']).median()['price']

fig,axes=plt.subplots(figsize=(18,8))
axes.bar(bar_plt2.index,bar_plt2.values)
axes.set_title('Median price of handphones of various screen materials')
plt.show()
