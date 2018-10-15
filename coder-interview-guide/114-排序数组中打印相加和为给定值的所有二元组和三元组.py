#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 10:05:09 2018

@author: admin
"""

#题目：
#要求：
#难度：
#思路：审题，排序数组中，不降序，分析输入数据特点,寻找三元组则先固定住一个值，（第一个值），确定固定的含义
#要点：整理清楚解题思路，再写代码
#测试：已通过

def printUniquePair(arr,target):
    left = 0
    right = len(arr) -1
    res = []
    while left < right:
        if arr[left] + arr[right] == target:
            res.append([arr[left],arr[right]])
            left += 1
            right -= 1
        elif arr[left] + arr[right] < target:
            left += 1
        else:
            right -= 1
    return res

test = [-8,-4,-3,0,1,2,4,5,8,9]
print(printUniquePair(test,10))

def printUniqueTriad(arr,target):
    res = []
    for i in range(len(arr)-3):
        left = i+1
        right = len(arr) - 1
        target2 = target -arr[i]
        while left < right:
            if arr[left] + arr[right] == target2:
                res.append([arr[i],arr[left],arr[right]])
                left += 1
                right -= 1
            elif arr[left] + arr[right] < target2:
                left += 1
            else:
                right -= 1
    return res

test = [-8,-4,-3,0,1,2,4,5,8,9]
print(printUniqueTriad(test,10))