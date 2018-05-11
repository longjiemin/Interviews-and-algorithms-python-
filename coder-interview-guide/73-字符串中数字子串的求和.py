# -*- coding: utf-8 -*-
"""
Created on Fri May  4 17:08:43 2018

@author: longjiemin
"""
#字符串数字的求和（忽略小数点）
#难度：1星
#思路：要点在于设置合适的变量存储数字运算的重要字符，整形变量res,num,布尔变量posi
#备注：ord（）返回ascii,不要忘了res每次迭代完了之后将num,posi重置
def numSum(str1):
    res = 0
    num = 0
    posi = True
    for i in str1:
        if ord(i) in range(48,58):
            num = num*10 + int(i)
        elif i =='-':
            posi = False if posi else True #用异或是错误的
        else:
            res = res+num if posi else res-num
            num = 0
            posi = True
    res = res+num if posi else res-num #这里还需要进行一次迭代
    return res

