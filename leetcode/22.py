# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 10:31:24 2018

@author: longjiemin
"""

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        if n == 1:
            res.append('()')
            return res
        elif n==2:
            res.extend(['()()','(())'])
            return res
        else:
            res2=self.generateParenthesis(n-1)
            res = set(res)
            for i in res2:
                res.add('()'+i)
                res.add('('+i+')')
                res.add(i+'()')
            return list(res)
            
class Solution2(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        dp={}
        if n == 1:
            res.append('()')
            return res
        elif n==2:
            res.extend(['()()','(())'])
            return res
        else:
            res2=self.generateParenthesis(n-1)
            res = set(res)
            for i in res2:
                res.add('()'+i)
                res.add('('+i+')')
                res.add(i+'()')
            return list(res)