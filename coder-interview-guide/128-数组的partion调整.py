#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 19:51:38 2018

@author: admin
"""
#题目：有序数组调整，左半部分没有重复元素且升序，不保证又半部分，补充：给定一个数组，只有0，1，2三个值，实现排序。
#要求：所有题目时间N，空间1
#难度：1星
#思路：难点在于空间复杂度为1，没有重复元素，给定的是一个有序数组,所以依序遍历，不断的交换即可
#要点：补充问题是原始问题的变体，增加左右变量，不断的交换即可
#测试:测试全部通过，注意变体可以衍生成红蓝黄三色球问题
def leftUnique(arr):
    if len(arr) == 0:
        return None
    u = 0
    i = 1
    while i != len(arr):
        if arr[i] != arr[u]:
            i+= 1
            u+= 1
            arr[u],arr[i-1] = arr[i-1],arr[u]
        else:
            i+= 1
    return arr
test = [1,2,2,2,3,3,4,5,6,6,7,7,8,8,8,9]
print(leftUnique(test))            

#补充题目1：一个数组，给定k值，比k小的值放数组的左边，比k大的放右边
def partition(arr,k):
    right = len(arr)  #注意这里的初始值要和后面的迭代吻合
    left = -1
    cur = 0
    #for i in range(len(arr)):#这里我的逻辑没有理清，条件定义有问题
    while cur < right:
        if arr[cur] == k:
            cur+=1
        elif arr[cur] < k:
            left = left+1
            arr[left],arr[cur] = arr[cur],arr[left]
            cur+= 1
        else:
            right -= 1
            arr[right],arr[cur] = arr[cur],arr[right]
    return arr
print('补充问题:',partition(test,5))
