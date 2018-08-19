#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 22:14:38 2018

@author: admin
"""

#进阶问题,注意，这里只能求得大于，不能求得大于或等于
def get_minKB(nums,k):
    cand = {}
    for i in nums:
        if i in cand.keys():
            cand[i] += 1
        else:
            if len(cand.keys()) < k-1:
                cand[i] =1
            else:
                for i in cand.keys():
                    cand[i] -= 1
                cand = {k:v for k,v in cand.items() if v>0}
        print('cand',cand,'i',i)
    print(cand)

    for i in cand.keys():
        count_number = 0
        for j in nums:
            if i == j:
                count_number += 1
        if count_number >= k:
            print(i)