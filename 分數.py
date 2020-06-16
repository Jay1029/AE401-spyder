# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 17:21:54 2020

@author: User
"""


scores = []
num = input('幾個同學')
for i in range(int(num)):
    score = input('分數')
    name = input('名字')
    scores.append(int(score))
    scores.append(int(name))
high = 100
for each_score in scores:
    if score[i]<high:
        high = each_score

print('最高分:,high')

total = 0     
for each_score in scores:
    total= total + each_score

aver = total/int(num)














