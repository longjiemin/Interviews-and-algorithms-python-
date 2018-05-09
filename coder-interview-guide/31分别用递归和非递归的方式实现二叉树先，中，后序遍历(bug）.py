# -*- coding: utf-8 -*-
"""
Created on Fri May  4 15:35:18 2018

@author: longjiemin
"""
#分别用递归方法与非递归方法实现二叉树的先序，中序，后序遍历
#难度：3星
#备注：使用list来模拟堆栈，自己生成node类

class node():
    def __init__(self,value=None,left=None,right=None):
        self.value = value
        self.left  = left
        self.right = right
    def __repr__(self):
        return '(value:%s left:%s right:%s)'%(self.value,self.left,self.right)
        
#生成书上的测试数据
def get_test_data():
    head = node(1)
    head.left  = node(2)
    head.left.left = node(4)
    head.left.right = node(5)
    head.right = node(3)
    head.right.right = node(6)
    head.right.left = node(7)
    return head
    
#使用递归的方法进行,如下分别是先序，中序，后序
#不要把问题想复杂了，理清遍历的逻辑就可以写出来了
def pre_order_recur(head):#先序
    if head is None:
        return
    print(head.value)
    pre_order_recur(head.left)
    pre_order_recur(head.right)

def in_order_recur(head):#中序
    if head is None:
        return
    in_order_recur(head.left)
    print(head.value)
    in_order_recur(head.right)
    
def pos_order_recur(head):#后序
    if head is None:
        return
    pos_order_recur(head.left)
    pos_order_recur(head.right)
    print(head.value)
    
#使用非递归的方式
#首先是先序遍历,使用一个堆栈不断的压如左右子树，并在下一次循环的时候不断弹出
def pre_order_unrecur(head):
    stack = []
    if head is None:
        return 
    stack.append(head)
    while len(stack)>0:
        head = stack.pop()
        print(head.value)
        if head.right is not None:#这个地方的判断语句应该有可以改进的地方
            stack.append(head.right)
        if head.left is not None:
            stack.append(head.left)
            
#中序遍历,中序遍历需要生成一个变量cur来记录当前节点的位置
def in_order_unrecur(head):
    if head is None:
        return
    cur = head
    stack = []
    stack.append(cur)
    cur = cur.left
    while len(stack) > 0:
        if cur is not None:
            stack.append(cur)
            cur = cur.left
        else:
            node_ = stack.pop()
            print (node_.value)
            cur = node_.right
        





















