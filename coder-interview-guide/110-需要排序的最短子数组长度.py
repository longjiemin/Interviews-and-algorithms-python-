# -*- coding: utf-8 -*-
"""
Created on Thu May 10 11:35:25 2018

@author: longjiemin
"""

#给定一个无序数组，求出需要排序的最短子数组长度
#难度：1星
#思路:进行两次遍历，一次从左至右，一次从右至左。每一次记录遍历书中的最小值，当arr[i]>min时，意味着min值必然要一到min值的位置，记录i的位置。
#但会两个索引位置，则其切片就只需要排列的部分。

def getminlen(arr):
    min_index_left = -1
    min_value_left = arr[0]
    for i in range(len(arr)):
        if min_value_left > arr[i]:
            break
        else:
            if min_value_left < arr[i]:
                min_value_left = arr[i]
                min_index_left = i
                
    if min_index_left == -1:
        print('its sorted')
        return
        
    min_index_right = -1
    min_value_right = arr[len(arr)-1]       
    for i in range(len(arr)-1,-1,-1):
        if min_value_right < arr[i]:
            break
        else:
            if min_value_right > arr[i]:
                min_value_right = arr[i]
                min_index_right = i
            
    return arr[min_index_left:min_index_right+1] 

arr = [1,5,3,4,2,6,7]