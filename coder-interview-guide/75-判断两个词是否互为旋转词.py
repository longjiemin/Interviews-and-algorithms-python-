# -*- coding: utf-8 -*-
"""
Created on Mon May  7 14:19:01 2018

@author: longjiemin
"""
#判断两个字符串是否为旋转词
#要求：时间复杂度为N
#难度：1星
#思路：将b+b拼接起来，看是否有字符串a,实现过程的重点是kmp匹配算法
#分析：本题的难度主要在于溢出的判断
#设置布尔量posi,整形res,整型常量minq = min_balue/10用于判断阈值