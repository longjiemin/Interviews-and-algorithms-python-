# -*- coding: utf-8 -*-
"""
Created on Mon May  7 14:38:36 2018

@author: longjiemin
"""
#给定一个字符串str,返回一个统计字符串cstr,补充问题：给定一个整数index,返回统计字符串代表的字符串该index的字符
#难度：1星
#要求：
#分析：原问题非常简单，故不实现，补充问题可以设置阶段变量stage（bool型）来判断当前字符。
#经验：stage变量的使用

def getcharat(cstr,index):
    stage = True #stag为字符的时候表示处于字符的阶段，为False时表示处于数字统计的阶段
    count_index = 0
    cur = ''
    cur_num = 0
    for i in cstr:
        if i == '_':
            stage = not stage
            if stage is True:
                count_index += cur_num                
                if count_index >= index:
                    #pass
                    return cur
                cur = ''
                cur_num = 0
#                stage = not stage
#            else:
#                stage = not stage        #错误代码示例
        elif stage is True:
            cur += i
        else:
            cur_num = 10*cur_num + int(i)
    stage = not stage
    count_index += cur_num                
    if count_index >= index:
        return cur
    else:
        raise ValueError('the index is error' )
    
    
                
cstr = 'a_10_b_15_c_13'                 
                
        
