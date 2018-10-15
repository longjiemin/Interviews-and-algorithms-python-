#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 09:48:02 2018

@author: admin
"""

#题目
#要求
#难度：一星
#思路：分析输出的特点
#要点，注意是j-i，不是j-i+1
def getlil(arr):
    length = 0
    max_value = 0
    min_value = 0
    hashset = set()
    for i in range(len(arr)):
        max_value = -float('inf')
        min_value = float('inf')
        for j in range(i,len(arr)):
            if arr[j] in hashset:
                break
            hashset.add(arr[j])
            max_value = max(hashset)
            min_value = min(hashset)
            if max_value - min_value == (j-i): #y要点，注意是j-i，不是j-i+1
                length = max(length,j-i+1)
        print(i,j,hashset,length)
        hashset.clear()
    return length

if __name__ == '__main__':
    test = [5,5,3,2,6,4,3]
    ans =5
    print(getlil(test))            