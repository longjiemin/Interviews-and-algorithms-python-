#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 19:31:05 2018

@author: admin
"""
#题目：
#要求：时间 N,空间1，进阶要求：没有时间和空间要求，不可以使用除法
#难度：1星
#思路：使用除法，则考虑数组中出现的0的个数
#要点：方法2的思路可以通过分析输出数据的要求得到
#测试：方法1,方法2测试均通过


#方法1
def product(nums):
    zero_count = 0
    all_res = 1
    for i in nums:
        if i==0:
            zero_count += 1
        all_res *= i
    if zero_count == 1:
        return [all_res/i if i != 0 else 0 for i in nums]
    if zero_count >1:
        return [0]*len(nums)
    return [all_res/i for i in nums]

test = [2,3,1,4]
print(product(test))

def product2(nums):
    right = [i for i in nums]
    for i in range(1,len(right)):
        right[i] = right[i]*right[i-1]
    left = [i for i in nums]
    for i in range(len(left)-2,-1,-1):
        left[i] *= left[i+1]
    print(right,left)
    res = [left[1]]*len(nums)
    for i in range(1,len(nums)-1):
        print(res,i)
        res[i] = right[i-1] * left[i+1]
    res.append(right[1])
    return res
print(product2(test))