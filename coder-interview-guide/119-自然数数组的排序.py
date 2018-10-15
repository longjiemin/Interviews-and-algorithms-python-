#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 15:23:51 2018

@author: admin
"""

#题目：
#要求：不能通过索引进行排序，时间复杂度N,空间复杂度1
#难度：
#思路:方法2的思路更加清晰
#要点:编程时要小心的点
#测试：
#方法一，行跳过程
import time
def sort1(nums):
    tmp = 0
    tmp_next = 0
    for i in range(len(nums)):
        if nums[i] == i+1:
            continue
        while nums[i] != i+1:
            tmp_next = nums[tmp-1]
            tmp = nums[i]
            nums[tmp-1] = tmp
            tmp  = tmp_next
            
#方法2，交换
def sort2(nums):
    for i in range(len(nums)):
        while nums[i] != i+1:
            time.sleep(2)
            print(i,nums)
            tmp = nums[i]
            nums[i] = nums[nums[i]-1]
            print('tmp1',tmp,nums)
            nums[nums[i]-1] = tmp
            print('tmp2',tmp,nums)#tmp 应该保留nums[nums[i]-1]
            #nums[i],nums[nums[i]-1] = nums[nums[i]-1],nums[i] #报错，涉及索引，慎用
    return nums
    
test=[1,2,5,3,4]
print(sort2(test))