#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 10:51:54 2018
换钱的最小货币数
进阶问题换钱的货币仅为一张
难度：2星
经验：注意whilez终止条件，if,else的逻辑，
@author: longjiemin
"""
import numpy as np
        
def min_coin_num(arr,aim):
    dp = np.random.rand(len(arr),aim+1)
    dp[:] = 0
    dp[:,0] = 0
    for i in range(aim+1):
        if i%arr[0] == 0:
            dp[0,i] = i/arr[0]
        else:
            dp[0,i] = 10000
    for i in range(1,len(arr)):
        for j in range(1,aim+1):
            if j%arr[i]==0:
                dp[i,j] = j/arr[i]
            else:
                dp[i,j] = dp[i-1,j]
            n = 0
            while j-n*arr[i] >= 0:
                if dp[i,j] > dp[i-1,j-n*arr[i]]+n:
                    dp[i,j] = dp[i-1,j-n*arr[i]]+n
                n += 1
            #print(dp)
                
    return dp[len(arr)-1,aim]
    

def min_coin_num2(arr,aim):
    dp = np.random.rand(len(arr),aim+1)
    dp[:] = 0
    dp[:,0] = 0
    for i in range(aim+1):
        if i%arr[0] == 0:
            dp[0,i] = i/arr[0]
        else:
            dp[0,i] = 10000
    for i in range(1,len(arr)):
        for j in range(1,aim+1):
            if j%arr[i]==0:
                dp[i,j] = j/arr[i]
            else:
                dp[i,j] = dp[i-1,j]
            if j-arr[i] >= 0:
                if dp[i,j] > dp[i-1,j-arr[i]]+1:
                    dp[i,j] = dp[i-1,j-arr[i]]+1
            #print(dp)
                
    return dp[len(arr)-1,aim]
               
