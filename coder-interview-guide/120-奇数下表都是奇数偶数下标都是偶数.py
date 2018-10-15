#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 15:51:02 2018

@author: admin
"""

#题目：
#要求：
#难度：
#思路：设置odd,even两个变量
#要点 不断交换列表的最后一个值
#测试：成功
def sort_odd_even(nums):
    odd = 1
    even = 0
    while odd < len(nums) and even < len(nums):
        print('tmp',nums)
        if nums[-1] %2 == 0:
            swap(nums,-1,even)
            even+=2
        else:
            swap(nums,-1,odd)
            odd+=2
    return nums
        
def swap(nums,i,j):
    tmp = nums[i]
    nums[i] = nums[j]
    nums[j] = tmp

test = [1,2,1,3,6,7,3,6,7]
print(sort_odd_even(test))