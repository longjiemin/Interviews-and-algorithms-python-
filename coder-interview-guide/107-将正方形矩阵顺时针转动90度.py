# -*- coding: utf-8 -*-
"""
Created on Thu May 10 10:42:32 2018

@author: longjiemin
"""
#给定N*N的矩阵，将整个矩阵调整成转动90°
#要求：额外空间复杂度为1
#思路：使用分圈处理，然后分组转动的思路

import numpy as np

def rotate_arr(arr):
    tr,tc = 0,0
    dr,dc = arr.shape[0]-1,arr.shape[1]-1 #注意这里的shape要减一
    if dr == tr:
        arr[tr] == arr[tr,::-1]
        return
    elif dc == tc:
        arr[tc] == arr[tc,::-1]
        return
#    arr[tr,tc:dc],arr[tr:dr,dc],arr[dr,dc:tc:-1],arr[dr:tr:-1,tc] = \#即便使用列表保存起来，但列表包含的是引用，所以也没有用。
#    [arr[dr:tr:-1,tc],arr[tr,tc:dc],arr[tr:dr,dc],arr[dr,dc:tc:-1]]  #错误代码，在第二次赋值的时候会因此第一次赋值的结果发生变化
#我们还是根据原始思路里的分组循环好了（因为限定了是正方形矩阵）
    for i in range(len(arr[tr,tc:dc])):
        temp_value = arr[dr:tr:-1,tc][i]
        arr[tr:dr,dc][i],arr[dr,dc:tc:-1][i],arr[dr:tr:-1,tc][i],arr[tr,tc:dc][i] = \
        arr[tr,tc:dc][i],arr[tr:dr,dc][i],arr[dr,dc:tc:-1][i],temp_value
    tr+=1;tc+=1
    dr-=1;dc-=1
    if tr>dr or tc>dc:
        return
    else:
        rotate_arr(arr[tr:dr+1,tc:dc+1])

#测试样例，测试通过
arr = np.array(range(1,17)).reshape(4,4)