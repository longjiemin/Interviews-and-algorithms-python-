# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 17:35:50 2018

@author: longjiemin
"""

#龙与地下城
#给定二维数组map,返回初始血量至少为多少
#难度：2星
#

class solution():
    def minph(self,nums):
        dp = [0]*nums.shape[1]
        for i in range(nums.shape[0]-1,-1,-1):
            if i == nums.shape[0]-1:
                for j in range(nums.shape[1]-1,-1,-1):
                    if j == nums.shape[1]-1:
                        dp[j] = -nums[i,j]
                    else:
                        dp[j] = max(dp[j+1]+nums[i,j],1)
            else:
                for j in range(nums.shape[1]-1,-1,-1):
                    if j == nums.shape[1]-1:
                        dp[j] = max(dp[j]-nums[i,j],1)
                    else:
                        dp[j] = max(dp[j+1]-nums[i,j],1,dp[j+1]-nums[i,j])
            print(dp)
        return dp[0]
f = solution()
                
                    
                 
             
