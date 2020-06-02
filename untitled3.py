# -*- coding: utf-8 -*-
"""
Created on Tue May 26 19:30:26 2020

@author: User
"""
import random

while True:
    guess = int(input('guess(1~20):'))
    a = random.randint(1,20)
    if guess==a:
        print('bingo!')
        print(a)
        break
    else:
        print('wrong!')
        if guess > a:
            print('大一點')
            a + 1
        else guess < a:
            print('小一點') 
            a + 1
            