#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 19:34:53 2018

@author: admin
"""

#给定一个无序的数组arr,找到其最小的K个数
#要求：排序算法，则时间复杂度与空间复杂度相同，均为NlogN，因此要求实现NlogK的和N的算法
#难度：NLogk 2星，N4星
#思路：本题的思路与找到第K小的数的目的是一样的


#先实现Nlogk的算法，根据思路，就是一直维护一个k个数的最大堆即可，接下来遍历数组，查找k个比根节点小的数





#另一种N的解法，是经典的BEFRT算法
def get_minKnumsByHeap(nums,k):
    
    if k<1 or k> len(nums):
        return None
    kheap = [0]*k
    for i in range(k):
        heapinsert(kheap,nums[i],i)
    print('kheap',kheap)
    for i in nums[k:]:
        if i <=kheap[0]:
            kheap[0] = i
            heapify(kheap,0,k)
        print(i,kheap)
    return kheap

def heapinsert(arr,value,index):
    arr[index] = value
    while index != 0:
        parent = (index-1)//2  #注意细节
        if arr[parent] < arr[index]:
            arr[parent],arr[index] = arr[index],arr[parent]
            index = parent
        else:
            break
        
def heapify(arr,index,heapSize):
    left = index *2 +1
    right = index * 2 + 2
    largest = index
    while left <  heapSize:
        if arr[left] > arr[index]:
            largest = left
        if  right < heapSize and arr[right] > arr[largest]:
            largest = right
        if largest != index :
            arr[largest],arr[index]  = arr[index],arr[largest]
        else:
            break
        index = largest
        left = index*2 + 1
        right = index *2 + 2
            
get_minKnumsByHeap([4,5,1,6,2,7,3,8],4)



    
                