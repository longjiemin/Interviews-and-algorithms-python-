# -*- coding: utf-8 -*-
"""
Created on Fri May  4 17:36:41 2018

@author: longjiemin
"""
#去掉字符串中连续出现的k个0的子串
#难度：1星
#思路：设置空字符串res，设置变量count对0计数
def removekzeros(str1,k):
    res = ''
    count = 0
    for i in str1:
        res+=i
        if i =='0':
            count+=1
        elif count == k:
            print (res)
            res = res[:-k-1]+res[-1] #小心这里的赋值即可
            count = 0          
    if count == k:
        res = res[:-k]
    return res
    
a = 'A00B'
b='A000B000'