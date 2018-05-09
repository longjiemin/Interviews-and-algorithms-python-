# -*- coding: utf-8 -*-
"""
Created on Fri May  4 16:55:04 2018

@author: longjiemin
"""

#判断两个字符串是否为变形词
#难度：1星
#备注：应该有更简单的方法
#思路：使用哈希表即可实现n的算法
def isDeformation(str1,str2):
    if len(str1) != len(str2):
        return False
    def str_dict(str1):
        dict1 ={}
        for i in str1:
            if i in dict1.keys():
                dict1[i]+=1 
            else:
                dict1[i] = 1
        return dict1
    dict1 = str_dict(str1)
    dict2 = str_dict(str2)
    if dict1 == dict2:
        return True
    else: 
        return False