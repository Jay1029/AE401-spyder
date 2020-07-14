# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 19:13:52 2020

@author: User
"""
ch=[]
eng=[]
words={}
answer=[]

print('########################')
print('#Python字典#')
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
        while True:
            w = input("輸入新單字(按0退出)")
            if w =='0':
                break
            if w not in words:
                m = input('中文解釋:') 
                words[w] = m
        else:    
            break
    elif sel=='2': 
        us = sorted(words)
        file = open('tv.txt','w')
        for i in us:
            file.write(print(i,"是",words[i]))
            file.close()
    elif sel=='3': 
        eng = input('填入英文')
        if eng in words:
            print('中文:',words[eng])
    elif sel=='4':
        got=False
        ch = input('輸入要查詢的中文(按0跳出): ')
        if ch == '0':
            break
        for k,v in d.items():
            if ch==v :
                print(ch,'的英文是',k)
                got=True
        if not got:
            print('抱歉，查不到!')    

    elif sel=='5':
        score=0
        print(v,':')
        ans = input()
        if ans == k:
            score +=1
            print('正確')  
        else:
            print('錯誤')
    elif sel=='6':
        break
    else:
        print('wrong input')
































































































