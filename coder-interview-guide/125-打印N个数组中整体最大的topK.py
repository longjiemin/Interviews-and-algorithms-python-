#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 16:55:58 2018

@author: admin
"""

#题目
#要求:时间复杂度klogN,空间
#难度：2星
#思路：注意数组是有序的，建立一个为N的最大堆
#要点：每一次取每一个有序数组的最后一个插入堆
#测试：通过

    
    
    
class HeapNode(): #这只堆里面保存的是什么元素
    def __init__(self,value,arrNum,index):
        self.value = value
        self.arrNum = arrNum
        self.index = index
    def __repr__(self):
        return str(self.value)

def heapinsert(heap,index):#插入堆时的操作
    while (index!=0):
        parent = (index-1)//2
        if heap[parent].value < heap[index].value:
            swap(heap,parent,index)
        else:
            break
        
def swap(heap,index1,index2):
    tmp = heap[index1]
    #print(heap,index1,index2)
    heap[index1] = heap[index2]
    heap[index2] = tmp
    
def heapify(heap,index,heapsize): #对堆的某一部分结构堆化时的操作
    left = index*2 +1
    right  = index*2 + 2 #注意这里是否可能出错
    largest = index
    while left<heapsize:
        if heap[left].value > heap[index].value:
            largest = left #注意largest保存的是索引
        if heap[right].value > heap[left].value and right < heapsize:
            largest = right
        if largest  != index:
            swap(heap,largest,index)
        else:
            break
        index = largest
        left = index*2+1
        right = index*2+2
        
def printTopK(arr,k): #主程序
    heapsize = len(arr)
    heap = [0] * heapsize
    for i in range(len(heap)):
        index = len(arr[i]) -1
        heap[i] = HeapNode(arr[i][index],i,index)
        heapinsert(heap,i) #每插入一个元素要保证最大堆得规则
        print('top',':','topK'+':')
    for i in range(k):
        print(heap,k)
        if heapsize == 0:
            break
        print(heap[0].value,' ')
        if heap[0].index != 0:
            heap[0].index -= 1
            heap[0].value = arr[heap[0].arrNum][heap[0].index]
        else:
            swap(heap,0,heapsize-1)
            heapsize -= 1
        heapify(heap,0,heapsize)
            
            
test =[[1,2,3],
       [1,4,7],
       [1,3,8]]
k = 3
printTopK(test,k)
        
        
        
        
        
        
        
        
        
        
        