#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 16:37:06 2018

@author: admin
"""

#题目：
#要求：时间N,空间1
#难度：2
#思路，使用动态规划，所有的最大累乘积必然以一个arr[i]结尾，
#要点：建立dp表的时候注意负负得正,并非所有动态规划都需要用到表
#测试：测试通过

def maxProduct(arr):
    if arr is None or len(arr) == 0:
        return None
    if len(arr) == 1:
        return arr[0]
    Max = arr[0]
    Min = arr[0]
    res = arr[0]
    maxEnd = 0
    minEnd = 0
    for i in arr[1:]:#这里是1开头，出了一次bug
        maxEnd = Max *i
        minEnd = Min *i
        Max = max(max(maxEnd,minEnd),i)
        Min = min(min(minEnd,maxEnd),i)
        res = max(res,Max)
        print(res)
                  
    return res
test = [-2.5,4,0,3,0.5,8,-1]
print(maxProduct(test))