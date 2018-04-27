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
 

#2
#在单链表和双链表中删除倒数第K个节点
#一星
#说明：时间复杂度O(N)，空间复杂度O(1)
#完成
#备注：单链表类为LList，双链表类为

class double_node(object):
    def __init__(self,data=None,last=None,next=None):
        self.data = data
        self.last = last
        self.next = next
    
class double_List(object):
    def __init__(self,nums):
        self.head = None
        if nums is not None:
            for i in nums:
                self.append(i)

    def append(self,elem):
        if self.head is None:
            self.head = double_node(elem)
            return
        p = self.head
        while p.next is not None:
            p = p.next
        p.next = double_node(elem)
        p.next.last = p
        
    def __repr__(self):
        nums_all = 'doubelList: '
        p = self.head 
        while p is not None:
            nums_all += str(p.data)
            if p.next is not None:
                nums_all +=  '<->'
            p = p.next
        return nums_all

def remove_lathKthnode(nums,k):
    p = nums.head
    while p is not None:
        p = p.next
        k -= 1
    if k > 0:
        return nums
    elif k ==0:
        nums.head = nums.head.next
        return nums
    else:
        p = nums.head
        while k<0:
            p = p.next
            k += 1
        p.last.next = p.next
        return nums
        
            

        
        