#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 10:36:23 2018

@author: admin
"""

#题目：无序数组，可正，可负，可0，累加和为k,子树组长度
#变体1：可正，可负，可0,求正负数相等的子数组长度
#变体2：只有元素1，0求所有两种元素相等的最长子数组长度 
#思路：分析输入数据和需求，生成s列表，s[i] 表示sum(arr[:i]), 把求k表示成求s[i]-k出线的位置，变体的解答略，转换数字即可
#要点：hashmap中保留的是最早出现的位置，注意hashmap的初始化
#测试： 通过
def maxLength(arr,k):
    s = [0] * len(arr)
    s[0]= arr[0]
    for i in range(1,len(arr)):
        s[i] = s[i-1] + arr[i] #这一步其实可以整合到下面的for循环中
    print(s) #debug
    max_len = 0
    hashmap = {}
    hashmap = {0:0}   #非常重要，初始化
    for i in range(len(s)):
        target = k-s[i]
        if s[i] not in hashmap.keys():
            hashmap[s[i]] = i
        if target in hashmap.keys():
            max_len = max(max_len,i-hashmap[target]+1)
    return max_len

test = [-1,0,3,-3,1,8,1]
k=0
print(maxLength(test,k))
