#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 17:00:04 2018

@author: admin
"""

class Node():
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

def getTestData():
    a = Node(1)
    a.left = Node(2)
    a.left.left = None
    a.left.right = Node(4)
    a.left.right.left = Node(7)
    a.left.right.right = Node(8)
    a.left.right.right.right = Node(8)
    a.right = Node(3)
    a.right.left = Node(5)
    a.right.right = Node(6)
    a.right.left.left = Node(7)
    a.right.left.left.left = Node(12)
    a.right.left.right =Node(10)
    return a
def printEdge(head):
    if head is None:
        return None
    height = getHeight(head)
    edgemap = [[None]*height,[None]*height]
    setEdgeMap(head,0,edgemap) 
    for i in setEdgeMap[0]:
        print(i.value,end=',') #打印左边界
    printLeafNotEdge(head) #打印叶子节点，在左边界，也不再右边界
    
    
def getHeight(head):
    if head is None:
        return 0
    return max(1+getHeight(head.left),1+getHeight(head.right))

def setEdgeMap(head,l,edgemap):
    if head is None:
        return
    edgemap[l][0] = head if edgemap[l][0] is None else edgemap[l][0]
    edgemap[l][1] = head
    setEdgeMap(head.left,l+1,edgemap)
    setEdgeMap(head.right,l+1,edgemap)
    
def printLeafNotEdge(head,l,edgemap):
    if head is None:
        return None
    if head.left is None and head.right is None and head not in edgemap[l]:
        print(h.value,end=',')
    printLeafNotEdge(head.left,l+1,edgemap)
    printLeafNotEege(head,right,l+1,edgemap)
    
    

        
    