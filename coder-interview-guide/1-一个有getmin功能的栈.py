# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 14:20:11 2018

@author: longjiemin
"""
#1 设计一个具有getmin的堆栈
class getmin_stack():

    def __init__(self,nums):
        self.stack_data = list([])
        self.stack_min = list([])
        for i in nums:
            self.stack_data = self.push(i)    
    
#    def get(self,nums):
#        for i in nums:
#            self.stack_data = self.push(i)       
            
    def push(self,elem):
        if self.stack_data is not []:
            self.stack_data.append(elem)
            self.stack_min.append(elem)
        elif elem <= self.stack_data[-1]:
            self.stack_data.append(elem)
            self.stack_min.append(elem)
        else:
            self.stack_data.append(elem)
    
    def pop(self):
        value = self.stack_data.pop()
        if value > self.stack_min[-1]:
            pass
        else:
            self.stack_min.pop()
        return value
    
    def get_min(self):
        return self.stack_min[-1]

#2
#由两个堆栈组成的队列，add,poll,peek, 
#问题：__repr__函数无反应
class de_list():
    '''
    dfsdf
    '''
    def __init__(self,nums):
        self.stack1 = list (nums)
        self.stack2 = list([])
        for i in range(len(nums)-1,0-1,-1):
            self.stack2.append(self.stack1[i])
        
    def push(self,num):
        self.stack1.append(num)
        self.stack2 = list([])
        for i in range(len(self.stack1)-1,0-1,-1):
            self.stack2.append(self.stack1[i])
    
    def poll(self):
        self.stack2.pop()
        self.stack1 = list([])
        for i in range(len(self.stack2)-1,0-1,-1):
            self.stack1.append(self.stack2[i])
            
    def peek(self):
        return self.stack2[-1]

    def __repr__(self):
        return self.stack2
        
    def __str__(self):
        return print(self.stack2)
        
        
#3
#仅仅使用递归函数对堆栈进行逆序

#4
#猫狗队列


#5
#用一个堆栈实现另一个堆栈的排序，不允许额外变量
#功能实现，基本没有问题
def sort_another(nums):
    if len(nums)==0:
        return []
    stack2 = [nums.pop()]
    while len(nums)>0:
        cur = nums.pop()
        while len(stack2) != 0 and cur>stack2[-1] :
            nums.append(stack2.pop())
        stack2.append(cur)
    return stack2


#6
#用堆栈解决汉诺塔问题


#7
#生成窗口最大值数组，输入参数数组arr,窗口大小W, 输出一个长度为n-w+1的数组res
#使用O(N)的算法实现
#功能算法基本实现，并满足复杂度要求
def getmax_window(nums,w):
    res = []
    qmax = []
    for i in range(len(nums)):
        while len(qmax) !=0 and nums[i]>nums[qmax[-1]]:
            qmax.pop()
        qmax.append(i)
        if i-qmax[0] == w:
            qmax=qmax[1:]
        if i >= w-1:
            res.append(nums[qmax[0]])
    return res
        

#8
#给定一个定义的二叉树节点类，对一个没有 重复元素的的list生成最大树
#要求时间复杂度为O(N)，空间复杂度为O(N)
#如下为给定二叉树定义：
#逻辑不难，代码实现有点复杂
class Node():
    def __init__(self,data=None,left=None,right=None):
        self.left = left
        self.right = right 
        self.data = data
        
        
#9
#求最大子矩阵的大小，给定矩阵map，其中的值只有0和1，求其中全是1的矩阵的1的数量
#测试数据如下
#hight_size暂时没有实现o(N）的算法
import numpy as np
map = np.array([[1,0,1,1],[1,1,1,1],[1,1,1,0]])

def maxsizefrommap(map):
    max_size = 0         #总的maxsize
    hight_size = [0]*map.shape[1]
    for i in range(map.shape[0]):
        this_row = list(map[i])
        max_size_row = 0    #每一行的maxsize
        for j in range(len(hight_size)):
            if this_row[j] == 0:
                hight_size[j] = 0
            else:
                hight_size[j] += 1
#O(N**2)实现hight_size的面积计算
        for j in range(len(hight_size)):
            width_right = 0
            for h in range(j,len(hight_size)):
                if hight_size[h] >= hight_size[j]:
                    width_right += 1
                else:
                    break
            width_left = 0
            for h in range(j,-1,-1):
                if hight_size[h] >= hight_size[j]:
                    width_left += 1
                else:
                    break
            width = width_left + width_right - 1
            
            max_size_row = max(max_size_row,width*hight_size[j])
        max_size = max(max_size,max_size_row)
    return max_size


#10 
#最大值减去最小值小于或者等于num的子数组的数量
#本题的重点在于根据题干得到一些基本的结论：如果arr[i,j]满足，则其子数组必然满足，如果arr不满足，则包含这个数组的数组必然不满足
def get_Num(arr,num):
    ''' arr is a list
        num is the number of the condition'''
    res = 0
    for i in range(len(arr)):
        qmax = i
        qmin = i
        for j in range(i,len(arr)):
            if arr[j] > arr[qmax]:
                qmax = j
            if arr[j] < arr[qmin]:
                qmin = j
            if arr[qmax]-arr[qmin] <= num:
                continue
            else:
                res += j-i
                break
            if j == len(arr):
                res += j-i
                break
    return res       
        
