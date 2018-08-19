#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 20:18:35 2018

@author: admin
"""
#
#
#
#
#检测通过
def maxSum(nums):
    max_sum = -float('inf')
    cur = 0
    if len(nums) == 0:
        return None
    for i in nums:
        cur += i
        max_sum = max(max_sum,cur)
        cur = cur if cur>0 else 0
    return max_sum