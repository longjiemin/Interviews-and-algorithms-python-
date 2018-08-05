# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 16:22:11 2018

@author: longjiemin
"""
#1
#打印两个有序列表的公共部分
#难度：一星
#说明：
#完成：
class list_node():
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

        
class LList(object):
    def __init__(self,nums):
        self.head = None
        if nums is not None:
            for i in nums:
                self.append(i)

    def append(self,elem):
        if self.head is None:
            self.head = list_node(elem)
            return
        p = self.head
        while p.next is not None:
            p = p.next
        p.next = list_node(elem)
        
    def __repr__(self):
        nums_all = 'LList:'
        p = self.head 
        while p is not None:
            nums_all += str(p.data)
            if p.next is not None:
                nums_all +=  '->'
            p = p.next
        return nums_all

        
def get_public(LList1,LList2):
    cur1 = LList1.head
    cur2 = LList2.head
    while None not in (cur1,cur2):
        if cur1.data== cur2.data:
            print(cur1.data)
            cur1 = cur1.next
            cur2 = cur2.next
        elif cur1.data < cur2.data:
            cur1 = cur1.next
        else:
            cur2 = cur2.next
    return
 


        
            

        
        