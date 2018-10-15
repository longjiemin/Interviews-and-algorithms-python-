#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 16:25:07 2018

@author: admin
"""

#题目
#要求：
#思路：二分查找法的变体
#要点：二分法要定义left,right
#测试：测试通过
def getLocalMin(nums):
    if len(nums) == 0:
        return None
    if len(nums) ==1:
        return nums[0]
    if nums[0]<nums[1]:
        return nums[0]
    if nums[-1]<nums[-2]:
        return nums[-1]
    #使用二分查找法（变体）
    left = 0
    right = len(nums)
    median = 0
    while right>left:
        median = (left+right)//2
        if nums[median] > nums[median-1]:
            right = median-1
        elif nums[median]>nums[median+1]:
            left = median +1
        else:
            return nums[median]
test = [9, 7, 12, 5, 10, 19, 3, 6, 8]
print(getLocalMin(test))