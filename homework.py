# -*- coding: utf-8 -*-
"""
Created on Tue May 26 17:57:36 2020

@author: User
"""


math = input ('數學成績:')  
English = input ('英文成績:')

if 0<int(math and English)<=100:
    if int(math and English)>=90:
        print("有獎勵")
    elif int(math and English)>=60:
        print("處罰")
else:
    print('error')
    