# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 20:52:02 2017
最小的矩阵路径和
@author: longjiemin
"""
#shape的赋值问题
#注意nums的切片
import numpy as np
class project():
    def minpathsum(self,nums):
        if nums.shape[0] ==1:
            return sum(nums[:,0])
        elif nums.shape[1] == 1:
            return sum(nums[1,:])
        dp = [0]*nums.shape[1]
        for i in range(nums.shape[0]):
            if i == 0:
                for j in range(len(dp)):
                    dp[j] = sum(nums[0,:j+1])
                print(dp)
            else:
                for j in range(len(dp)):
                    if j ==0:
                        dp[j] = dp[j]+nums[i,j]
                    else:
                        dp[j] = min(dp[j]+nums[i,j],dp[j-1]+nums[i,j])
                print(dp)
        return dp.pop()
        
f = project()
                