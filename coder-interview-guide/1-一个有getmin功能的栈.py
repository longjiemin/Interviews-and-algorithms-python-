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
            self.push(i)    
    
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


        
