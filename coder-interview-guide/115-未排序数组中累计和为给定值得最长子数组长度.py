#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 10:19:22 2018

@author: admin
"""

#题目
#要求：时间复杂度O(N),空间复杂度为1
#难度：2星
#思路：分析题目要点，正数数组，left,right很可能是从同一个位置出发，如开始点，中点，结束点等
#要点
#测试：测试已通过，使用index和list的时候，一定要考虑是否可能超出索引范围
def getMaxlen(arr,k):
    maxLen=0
    right = 0
    left = 0
    sum_value = arr[0]
    while right < len(arr):
        if sum_value < k:
            right += 1
            if right >= len(arr):
                break
            sum_value += arr[right]
        elif sum_value > k:
            sum_value -= arr[left]
            left += 1
        else:
            maxLen = max(maxLen,right-left+1)
            right += 1
            if right >= len(arr):
                break
            sum_value += arr[right]
            sum_value -= arr[left]
            left += 1
    return maxLen

test = [1,2,1,1,1]
k = 3
print(getMaxlen(test,k))