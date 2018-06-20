#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 14:10:34 2018

@author: longjiemin
"""
#换钱的方法数
#arr时货币的值，每个货币可以使用无数次，aim是需要换的货币值，返回换钱的方法数
#难度：2星
#分析：使用动态规划分析，dp[i,j]表示arr[:i]去换货币j时的方法数
#经验：注意第一行和第一列的初始化，第一列应该全部为0.
import numpy as np
def max_coin_num(arr,aim):
    dp = np.random.rand(len(arr),aim+1) #生成dp表
    dp[:] = 0
    dp[:,0] = 1                         #初始化第一行和第一列，细节要点，第一列为0
    for i in range(aim+1):
        dp[0,i] = 1 if i%arr[0] == 0 else 0
    for i in range(1,len(arr)):         #递归更新dp表
        for j in range(1,aim+1):
            n = 0
            while j-n*arr[i] >= 0:
                dp[i,j] += dp[i-1,j-n*arr[i]]
                n += 1
            #print(dp)

    return dp[len(arr)-1,aim]
