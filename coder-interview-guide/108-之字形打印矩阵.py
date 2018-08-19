# -*- coding: utf-8 -*-
"""
Created on Thu May 10 11:05:36 2018

@author: longjiemin
"""

#之字形打印矩阵
#空间复杂度为1
#难度：1星
# 思路：仍然是这是tr,tc，dr,dc,根据题目分别从两个方向移动
import numpy as np
def printMaxZigzag(nums):
    tr,tc,dr,dc = 0,0,0,0
    endR = nums.shape[0]-1
    endC = nums.shape[1]-1
    fromup = False
    while tr != endR-1:
        print('start')
        print(nums,tr,tc,dr,dc,fromup)
        printlevel(nums,tr,tc,dr,dc,fromup)
        if tc == endC:
            tr += 1
            tc = tc
        else:
            tr = tr
            tc = tc+1
        if dr == endR:
            dc += 1
            dr = dr
        else:
            dc = dc 
            dr += 1
        fromup = not fromup

def printlevel(nums,tr,tc,dr,dc,fromup):
    print('print_level')
    if fromup:
        while (tr!=dr+1): #注意细节
            print(nums[tr][tc])
            tr+=1;tc-=1
    else:
        while(dr!=tr-1): #注意细节
            print(nums[dr][dc])
            dr-=1;dc+=1
test = np.array(range(12)).reshape(3,4)
print(test)
printMaxZigzag(test)
            
        