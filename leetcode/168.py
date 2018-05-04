# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 11:02:26 2017

@author: longjiemin
"""

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        '''def int26(x,base = 26):
            return int(x,base=26)'''
#        n2 = int (str(n),base=26)
#        return (''.join([chr(int(i,)+64) for i in str(n2)]))
        m = []
        while n>0:
            if n%26==0:
                m.append(n % 26)
                n = n +1
            else:
                m.append(n % 26)
            n = n//26
            
        m.reverse()
        a = dict(zip(list(range(1,27)),[chr(65+i) for i in range(26)]))
        s = ''
        s = s.join(a[i] for i in m)
        return (s)
s = Solution()
for i in range(120):
    print(s.convertToTitle(i))