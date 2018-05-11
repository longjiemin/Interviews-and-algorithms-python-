# -*- coding: utf-8 -*-
"""
Created on Thu May 10 10:20:32 2018

@author: longjiemin
"""
#给定矩阵，按转圈的方式打印它
#要求：额外空间复杂度为1
#难度：1星
#分析：本题的难度主要在于设计一个简单易懂的逻辑来实现，矩阵的大小有左上角和右下角两点来决定的


import numpy as np

def print_arr(arr):
    tr,tc = 0,0
    dr,dc = arr.shape[0]-1,arr.shape[1]-1 #注意这里的shape要减一
    if dr == tr:
        for i in arr[tr]:
            print(i)
        return
    elif dc == tc:
        for i in arr[:,dc]:
            print(i)
        return
    for i in [arr[tr,tc:dc],arr[tr:dr,dc],arr[dr,dc:tc:-1],arr[dr:tr:-1,tc]]: #这里可以现在纸上标好位置
        for j in i:
            print(j)
    tr+=1;tc+=1
    dr-=1;dc-=1
    if tr>dr or tc>dc:
        return
    else:
        print_arr(arr[tr:dr+1,tc:dc+1])
    
#测试用例：
arr = np.array(range(16)).reshape(4,4)