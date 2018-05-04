#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 15:01:13 2017

@author: longjiemin
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1=''
        for i in l1:
            l1=l1.join(str(l1))
        l1 = int(l1.reverse())
        l2=''
        for i in l2:
            l2=l2.join(str(l2))
        l2 = int(l2.reverse())
        
        l3 = l1 +l2
        l3 = list(str(l3))
        l3.reverse()
        
        return ListNode(l3)


s = Solution()
