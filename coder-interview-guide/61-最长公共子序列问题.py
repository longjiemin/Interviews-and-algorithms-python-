#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 14:56:11 2018

@author: longjiemin
"""
#给定字符串str1,str2,返回任意一个最长公共子序列
#难度：2星
#分析：问题分两步，找出dp,然后查找路径，返回索引

import numpy as np

#dp[i,j]代表str[:i],str[:j]的最大子序列的长度
def get_dp(str1,str2):
	dp = np.random.randn(len(str1),len(str2))
	dp[:,:]=0
	dp[:,0] = [0 if str1[0] in str2[:i] else 0 for i in range(1,len(str2)+1)]
	dp[0,:] = [0 if str1[0] in str1[:i] else 0 for i in range(1,len(str1)+1)]
	for i in range(1,len(str1)):
		for j in range(1,len(str2)):
			value = dp[i-1][j-1]+1 if str[i]== str[j] else dp[i-1][j-1]
			dp[i][j] = max(dp[i-1][j],dp[i][j-1],value)
	return dp

#从dp表的右下角往左上角移动，寻找最大子序列
def dp_to_sep(dp,arr):
	i = len(str1);j = len(str2)
	index_list =[]
	while i>0 and j > 0:
		if dp[i][j] == dp[i][j-1]: #往上移动
			j -= 1
		elif dp[i][j] == dp[i-1][j]: #往左移动
			i -= 1
		elif dp[i][j] == dp[i-1][j-1]+1: #往左上角移动并记录值
			index_list.append(i)
			i -= 1
			j-=1
	if dp[i][j] ==1:
		index_list.append(i)
	index_list.reverse()
	return index_list
