#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 14:06:23 2018

@author: longjiemin
"""

from random import randint

def selection_sort(nums):
    for i in range(len(nums)):
        min_index = i
        for j in range(i,len(nums)):
            if nums[j] <= nums[min_index]:
                min_index = j
        swap(i, min_index,nums)
        print(nums)
    return nums

def swap(i,min_index,nums):
    nums[i],nums[min_index] = nums[min_index],nums[i]
    return nums

if __name__ == 'main':
    nums = [randint(1,100) for i in range(15)]
    print('nums_unsorted',nums)
    print('nums_sorted',selection_sort(nums))
            
nums = [randint(1,100) for i in range(150)]      
selection_sort(nums)
            