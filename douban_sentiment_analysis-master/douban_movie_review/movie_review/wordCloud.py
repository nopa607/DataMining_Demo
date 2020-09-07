from wordcloud import WordCloud
import matplotlib.pyplot as plt  #绘制图像的模块
import jieba                    #jieba分词
import csv
import numpy as np
import re

negetive_words = ['电影','没有','觉得','就是','一个','什么','片子','这么','这部','这个','感觉','不是','知道','还是','真的','这种','一部','那么','自己','但是','实在','怎么','一般','完全'
,'时候','可以','这样','有点','可能','看到','豆瓣','以为','评分','只是','不过','一样','一点','一直','不能','为了','其实','那个','哪里','虽然','小时','所以','1','你们','而且'
,'看过','非常','很多','如此','还有','这是','一次','已经','主人','不会','最好','不要']
reg = "[^0-9A-Za-z\u4e00-\u9fa5]"
def removePunctuation(text):
    text = re.sub(reg,'',text)
    return text

path_txt=r'C:\Users\钛\Desktop\bonus\douban_sentiment_analysis-master\data\review.csv'
with open(path_txt,'r',encoding='UTF-8')as f:
    reader = csv.reader(f)
    rows = []
    i = 0
    for row in reader:
        # if 0<i<400:
        rows.append(row)
        i += 1
        # if i >= 5000:break
    review_data = np.array(rows).tolist()
    true_review_list = []
    false_review_list = []
    for words in review_data:
        if words[0] == '1':
            true_review_list.append(words[1])
        else:
            false_review_list.append(words[1])

# 结巴分词，生成字符串，wordcloud无法直接生成正确的中文词云

cut_text = [" ".join(jieba.cut(review)) for review in true_review_list]
final = ""
for test in cut_text:
    for item in negetive_words:
        test = test.replace(item,'')
    test_list = test.split()
    index = 0
    while index < len(test_list):
        test_list[index] = removePunctuation(test_list[index])
        if  test_list[index].__sizeof__() == 76 or test_list[index]=='':
            test_list.remove(test_list[index])
            continue
        final += test_list[index] + ' '
        index += 1
    # test = test_list.__str__()
    # final += test

# ================================================
# wordcloud = WordCloud(
#    #设置字体，不然会出现口字乱码，文字的路径是电脑的字体一般路径，可以换成别的
#    font_path="C:/Windows/Fonts/simfang.ttf",
#    #设置了背景，宽高
#    background_color="white",width=1000,height=880).generate(final)

# plt.imshow(wordcloud, interpolation="bilinear")
# plt.axis("off")
# plt.show()
# ================================================
final = final.split()
comment_dict = dict()
for item in final:
    if item in comment_dict.keys():
        comment_dict[item] += 1
    else:
        comment_dict[item] = 1
# comment_dict = sorted(comment_dict.items(),key = lambda x:x[1],reverse = True)
comment_dict = sorted(comment_dict.items(),key = lambda x:x[1])
# print(comment_dict)
comment_dict = np.save('comment_dict.npy', comment_dict)


