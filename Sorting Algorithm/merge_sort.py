#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 14:20:37 2018

@author: longjiemin
"""
from random import randint

def merge_sort(nums):
    if len(nums)>1:
        print(nums[:len(nums)//2])
        nums1 = merge_sort(nums[:len(nums)//2])
        print(nums[len(nums)//2:])
        nums2 = merge_sort(nums[len(nums)//2:])
        return insert_merge(nums1,nums2)
    else:
        return nums
        
def insert_merge(nums1,nums2):
    nums = []
    i = 0
    j = 0
    while i<len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            nums.append(nums1[i])
            i += 1
        else:
            nums.append(nums2[j])
            j += 1
    if i == len(nums1):
        nums.extend(nums2[j:])
    else:
        nums.extend(nums1[i:])
    print('nums',':',nums)
    return nums

        
if __name__ == 'main':
    nums = [randint(0,100) for i in range(15)]
    print('nums_unsorted',nums)
    print('nums_sorted',merge_sort(nums))
            
nums = [randint(1,100) for i in range(10)] 
print(nums)     
merge_sort(nums)