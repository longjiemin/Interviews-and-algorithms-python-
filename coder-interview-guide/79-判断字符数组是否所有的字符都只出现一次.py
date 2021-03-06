# -*- coding: utf-8 -*-
"""
Created on Mon May  7 15:12:56 2018

@author: longjiemin
"""
#判断数组是否所有的字符串都只出现1次
#要求1：实现时间复杂度为N的方法
#难度：1星
#要求2：实现空间复杂度为1的算法
#分析：要求1可以使用哈希表，不做实现
#***分析：要求2,整体思路是进行数组排序，首先任何复杂度为N的算法空间复杂度都非常高，NlogN的排序算法中，
#归并排序需要辅助数组（k可以通过手摇算法解决，但是会提高实践复杂度），快速排序的空间复杂度为logN,
#希尔排序的复杂度不稳，因此上述的算法中只有堆排序符合要求。
 