#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 11:24:48 2018

@author: admin
"""
#题目：
#要求：时间NlogN,空间N
#难度：3星
#思路：
#要点：左侧最大值辅助数组
#测试：暂时没通过
def maxLength(arr,k):
    sum_arr = len(arr) * [0]
    sum_arr = arr[0]
    help_arr = len(arr)* 10
    help_arr[0] = sum_arr[0]
    for i in range(1,len(arr)):
        sum_arr[i] = sum[i-1] + arr[i]
        help_arr[i] = max(sum_arr[i-1],sum_arr[i])
    