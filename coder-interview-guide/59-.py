#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 14:56:11 2018

@author: longjiemin
"""
#给定数组arr,返回arr的最长递增子序列
#要求：时间复杂度 O（N/log(N))
#难度：3星
#思路：使用动态规划可以实现N^2的方法，使用动态规划与二分查找可以实现NlogN的方法。
#经验：coding过程中一定不能吧dp与arr弄混
def get_dp(arr):
    dp = [1]
    min_value = 1
    for i in range(1,len(arr)):
        if min_value  < arr[i]:
            dp.append(max([dp[j] for j in range(len(dp)) if arr[j] < arr[i]])+1)
        else:
            dp.append(1)
            min_value = arr[i]
    return dp

def get_dp2(arr):
    dp = [1]
    end = [arr[0]]
    right = 0
    for i in range(1,len(arr)):
        for j in range(len(end)):#在此处使用二分查找法
            if end(j) > arr[i]:
				end(j) = arr[i]
				dp.append(dp[-1])
				break
			if j == len(end):
				dp.append(dp[-1]+1)
  				end.append(arr[i])
	return dp
				

def dp_to_seq(dp,arr):
    get_index = lambda arr,value:[i for i,j in enumerate(arr) if j == value]
    max_value = max(dp)
    value_index = get_index(dp,max_value)[-1]
    index_list = [value_index]
    while max_value > 1:
        value_index  = get_index(dp[:value_index],max_value-1)[-1]
        index_list.append(value_index)
        max_value -= 1
    index_list.reverse()
    seq_list = [arr[i] for i in index_list]
    return seq_list
        
        
    
