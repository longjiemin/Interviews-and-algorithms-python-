# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 08:36:44 2018

@author: longjiemin
"""

#1
#给定整数N,返回斐波拉契数列的第N项。
#难度： 1星
#完成：
#备注：
def get_N(n):
    if n==1 or n==2:
        return 1
    else:
        return get_N(n-2)+get_N(n-1)
#上图使用的递归，没有使用动态规划，如下是使用动态规划的O(N)解法
dp_dict = {}
def get_N2(n):
    if n==1 or n==2:
        dp_dict[n] = 1
        return dp_dict[n]
    elif n in dp_dict:
        return dp_dict[n]
    else:
        dp_dict[n] = get_N(n-2)+get_N(n-1)
        return dp_dict[n]
    
def get_N3(n):
    '''使用自底向上的递归方法'''
    if n==1 or n==2:
        return 1
    a=1
    b=1
    for i in range(n-2):
        b,a = a+b,b
    return b

    #4
#猫狗队列


 