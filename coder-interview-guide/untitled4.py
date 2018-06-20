# -*- coding: utf-8 -*-
"""
Created on Thu May 10 11:11:32 2018

@author: longjiemin
"""
#跳跃游戏
#


def jump(arr)：
    if len(arr)==0:
        return 0
    jump_value = 0
    cur = 0
    next = 0
    for i in range(len(arr))
        if cur < i：
            jump_value += 1
            cur = next
        next = max（next,i+arr[i])
    return jump_value
