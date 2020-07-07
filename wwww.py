# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 19:13:52 2020

@author: User
"""
w=[]
ch=[]
eng=[]
words=[]
answer=[]

print('########################')
print('#Python蘋果店進出貨系統#')
print('########################')

while True:
    
    print('功能=>')
    print('1. 字彙表')
    print('2. 全部單字')
    print('3. 英翻中')
    print('4. 中翻英')
    print('5. 測驗學習成果')
    print('6. 離開系統')
    
    sel = input('請輸入欲執行選項: ')

    if sel=='1': 
        w = input('輸入單字:')
    elif sel=='2': 
        print(w)
    elif sel=='3': 
        ch = input('填入中文')
    elif sel=='4':
        eng = input('填入英文')
    elif sel=='5': 
        answer=('w','填入中文'
              'ch,填入英文')
        if answer =('ch''eng')
        break
    else:
        print('wrong input')
































































































