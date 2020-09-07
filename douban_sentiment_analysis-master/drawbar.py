import matplotlib.pyplot as plt
import numpy as np
from wordcloud import WordCloud
import PIL.Image as image


def draw_from_dict(dicdata,RANGE, heng=0):
    #dicdata：字典的数据。
    #RANGE：截取显示的字典的长度。
    #heng=0，代表条状图的柱子是竖直向上的。heng=1，代表柱子是横向的。考虑到文字是从左到右的，让柱子横向排列更容易观察坐标轴。
    # by_value = sorted(dicdata.items(),key = lambda item:item[1],reverse=True)
    by_value = comment_dict
    x = []
    y = []
    index = len(dicdata) - 30
    while index < len(dicdata) - 15:
        x.append(by_value[index][0])
        y.append(by_value[index][1])
        index += 1
    # for d in by_value:
        # y.append(d[1])
    if heng == 0:
        plt.bar(x, y)
        plt.tick_params(labelsize=26)
        plt.show()
        return 
    elif heng == 1:
        plt.barh(x, y)
        plt.show()
        return 
    else:
        return "heng的值仅为0或1！"

if __name__ == "__main__":
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    comment_dict = np.load('comment_dict.npy', allow_pickle=True)
    draw_from_dict(comment_dict,15)

    # dicty = {}
    # index = len(comment_dict) - 100
    # while index < len(comment_dict):
    #     dicty[str(comment_dict[index][0])] = int(comment_dict[index][1])
    #     index += 1

    # mask = np.array(image.open("douban.jpg"))
    # wordcloud = WordCloud(
    # font_path="C:/Windows/Fonts/simfang.ttf",
    # background_color="white",mask=mask).generate_from_frequencies(dicty)
    # plt.imshow(wordcloud, interpolation="bilinear")
    # plt.axis("off")
    # wordcloud.to_file("new_wordcloud.jpg")
    # plt.show()