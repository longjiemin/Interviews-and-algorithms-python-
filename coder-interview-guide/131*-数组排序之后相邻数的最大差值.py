#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 20:45:50 2018

@author: admin
"""
#题目：排序之后，最大差值
#要求：排序法实现，时间复杂度NlogN，桶排序思想可以做到N.
#难度：2星，做到时间复杂度N
#思路：找到最大值与最小值，根据其来分桶
#要点：看注释。
#测试：代码通过
def maxGap(nums):
    if len(nums)==0 or len(nums) == 1:
        return None
    max_value = max(nums)
    min_value = min(nums)
    res = [0] * (max_value-min_value)
    for i in range(len(nums)):
        res[i-min_value] += 1
    print(res)
    max_gap = 0
    temp_gap = 0
    for i in res:
        if i == 0:
            temp_gap += 1
        else:
            max_gap = max(temp_gap,max_gap)
            temp_gap = 0
    return max_gap+1#注意这里要加一
test = [9,3,1,10]
print(maxGap(test))