# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 09:41:25 2017

@author: 705family
"""

class Solution(object):
    def convert(self,s,numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        ar = []
        for i in range(len(s)):
            for j in range(numRows):
                ar.append(s[i])
                i=i+1
                if i < len(s):
                    continue
                else:
                    break
            for j in range(1,numRows-2):
                ar[numRows-1-j] = ar[numRows-1-j]+s[i]
                i=i+1
                if i < len(s):
                    continue
                else:
                    break
        for j in range(len(ar)):
            ar[0] = ar[0]+ar[j]
        return ar[0]
    
sol = Solution
s = "PAYPALISHIRING"
numRows = 3
print(sol.convert(0,s,numRows))