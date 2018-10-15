#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 16:06:56 2018

@author: admin
"""

#题目：
#要求：
#难度：2星
#思路：根据子数组的最大累计和，不断根据行来生成子数组
#要点：见代码注释
#测试：测试通过

def maxSum(arr):
    if arr is None or len(arr) == 0 or arr[0] == 0:
        return None
    max_value = -float('inf')
    cur = 0
    s = [] #累加数组
    for i in range(len(arr)):
        s = [0] * len(arr[0])
        for j in range(1,len(arr[0])):
            cur = 0
            for k in range(len(s)):
                s[k] += arr[j][k] #这里累加了多行的元素
                cur += s[k]
                max_value = max(max,cur)
                if cur < 0:
                    cur = 0
    return max_value

