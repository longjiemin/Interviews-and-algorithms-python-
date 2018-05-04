#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 15:16:19 2018

@author: longjiemin
"""
from random import randint

def bubble_sort(nums):
    for i in range(len(nums)-1):
        for j in range(len(nums)-1-i):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
            print(nums)
            
    return nums
                
if __name__== 'mian':
    nums = [randint(1,100) for i in range(15)]
    print('nums_unsorted',nums)
    print('nums_sorted',bubble_sort(nums))
            
nums = [randint(1,100) for i in range(19)]      
bubble_sort(nums)
 