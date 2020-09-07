# -*- coding: utf-8 -*-
from native_bayes_sentiment_analyzer import SentimentAnalyzer
import numpy as np
import csv
import torch
import math

model_path = './data/bayes.pkl'
userdict_path = './data/userdict.txt'
stopword_path = './data/stopwords.txt'
corpus_path = './data/review.csv'


analyzer = SentimentAnalyzer(model_path=model_path, stopword_path=stopword_path, userdict_path=userdict_path)

with open(corpus_path, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    rows = []
    i = 0
    for row in reader:
        if 450<i<550:
            rows.append(row)
        i += 1
        if i >= 550:break
    review_data = np.array(rows).tolist()
    review_list = []
    label_list = []
    for words in review_data:
        review_list.append(words[1])
        label_list.append(words[0])

index = 0
count = 0
tp = 0
tn = 0
FP = 0
FN = 0
for test in review_list:
    pre = analyzer.analyze(text=test)
    if float(pre) > 0.5:
        if label_list[index] == '1':
            tp += 1
        else:
            FP += 1
    if float(pre) < 0.5:
        if label_list[index] == '0':
            tn += 1
        else:
            FN += 1
    index += 1
print(tp/(tp+FN))
print(tn/(tn+FP))
print((tp*tn-FP*FN)/math.sqrt((tp+FP)*(tn+FN)*(tp+FN)*(tn+FP)))

