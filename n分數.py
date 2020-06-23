# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 18:35:42 2020

@author: User
"""


scores = []
names = []
num = input('幾個同學')
for i in range(int(num)):
    score = input('分數')
    name = input('名字')
    scores.append(int(score))
    names.append(name)

high = 0
for each_name in names:
    if each_name[1]>high:
        high = each_name[1]
lo = 100
for each_name in names:
    if each_name[1]<lo:
        lo = each_name[1]

print('最高分:',high)
print('最低分:',lo)
total = 0     
for each_name in names :
    total= total + each_name[1]
    

aver = total//int(3)
print('平均',aver)