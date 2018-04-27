# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 11:39:49 2018

@author: longjiemin
"""
#斐波拉契序列的递归与动态规划
#补充题目1,，给定一个N,代表台阶数，一次可以跨2个或1个台阶，返回多少种走法
#假设成熟的母牛每年都会生一头小母牛，并且永远不会死，每一只小母牛3年之后成熟又可以生小母牛，假设第一年有一头
#小母牛，问年后牛的数量
#要求：时间复杂度（logN)
#难度：3星
#分析：使用传统的动态规划算法只能达到0(n),可以利用矩阵的特性，通过归并运算加快特性
class f():
    def f1(self,n):
        if n == 1 or n ==2:
            return 1
        else:
            res = self.mul([1,1],self.matrixpower([[1,1],[1,0]],n-2))
            return res[0]
#使用  [0]*len(nums2[0])]*len(nums1) 引发了视图问题        
    def mul(self,nums1,nums2):
        nums3 = [[0]*len(nums2[0])]*len(nums1)
        for i in range(len(nums1)):
            for j in range(len(nums2[0])):
                list1=nums1[i]
                list2 =[k[j] for k in nums2]
                value = sum(map(lambda x,y:x*y,list1,list2))
                print(i,j,list1,list2,value)
                nums3[i][j] = value
                print(nums3[i][j])
                print(nums3)
        return nums3
    
    def matrixpower(self,nums1,n):
        if n==1:
            return nums1
        elif n==2:
            return self.mul(nums1,nums1)
        elif n>=3:
            return self.mul(self.matrixpower(nums1,n//2),self.matrixpower(nums1,n-n//2))
            
        
