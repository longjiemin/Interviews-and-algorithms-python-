# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 10:00:03 2017

@author: longjiemin
"""
'''
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.
'''
class Solution(object):
    
    def __init__(self):
        self.dict=
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in nums:
            if i in a.keys():
                a[i] = a[i] +1
            else:
                a[i] = 1
            
        for i in a.keys():
            if a[i] > len(nums)//2:
                break
        return i
                