#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 15:16:07 2018

@author: longjiemin
"""
from random import randint

def count_sort(nums):
    min_num = nums[0]
    max_num = nums[0]
    count_dict = {}
    for i in nums:
        if i<min_num:
            min_num = i
        if i > max_num:
            max_num = i
        if i in count_dict.keys():
            count_dict[i] += 1
        else:
            count_dict[i] = 1
    sorted_num = []
    for i in range(min_num,max_num+1):
        if i in count_dict.keys():
            sorted_num.extend([i]*count_dict[i])
    return sorted_num

if __name__== 'mian':
    nums = [randint(1,100) for i in range(15)]
    print('nums_unsorted',nums)
    print('nums_sorted',count_sort(nums))
            
nums = [randint(1,100) for i in range(100)]      
sorted_nums = count_sort(nums)
        
