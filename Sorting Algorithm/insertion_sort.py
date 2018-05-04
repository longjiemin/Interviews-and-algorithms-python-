#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 17:40:32 2018

@author: longjiemin
"""

#
from random import randint
def insertion_sort(nums):
    for i in range(1,len(nums)):
        for j in range(i-1,-1,-1):
            if nums[i] < nums[j]:
                if j ==  0:
                    swap(0,i,nums)
                continue
            else:
                swap(j+1,i,nums)
                break
        print(nums)
    return nums

def swap(index1,index2,nums):
    num = nums[index2]
    nums[index1+1:index2+1] = nums[index1:index2]
    nums[index1] = num
    return nums

if __name__ == 'main':
    nums = [randint(1,100) for i in range(15)]
    print('nums_unsorted',nums)
    print('nums_sorted',insertion_sort(nums))
            
nums = [randint(1,100) for i in range(1000)]      
insertion_sort(nums)