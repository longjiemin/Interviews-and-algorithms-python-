#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 19:42:27 2018

@author: admin
"""

#题目：
#要求：
#难度：1星
#思路：要点，仔细分析矩阵的特点即可
#要点：col 可以等于0
def Find(target, array):
    # write code here
    n,m = len(array),len(array[0])
    raw = 0
    col = m-1
    while raw < n and col >=0:
        if array[raw][col] == target:
            return True
        elif array[raw][col]>target:
            col -= 1
        else:
            raw += 1
    return False,raw,col