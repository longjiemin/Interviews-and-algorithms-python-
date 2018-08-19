#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 21:39:48 2018

@author: admin
"""

class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        cur1 = pHead1
        cur2 = pHead2
        if cur1 is None: return cur2
        if cur2 is None: return cur1
        if cur1.val < cur2.val:
            res = cur1
            cur1 = cur1.next
        else:
            res = cur2
            cur2 = cur2.next
        res_head = res
        while cur1 and cur2:
            if cur1.val < cur2.val:
                res.next = cur1
                cur1 = cur1.next
                res = res.next
            else:
                res.next = cur2
                cur2 = cur2.next
                res = res.next
        if cur1:
            res.next = cur1
        else:
            res.next = cur2
        return res_head
#已通过验证，注意cur1，cur2为空的时候