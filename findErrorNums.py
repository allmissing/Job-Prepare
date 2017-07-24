# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 14:41:59 2017

@author: 705family
"""

class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        L = [0,0]
        nums2 = sorted(nums)
        for i in range(len(nums2)-1):
            if nums2[i] == nums2[i+1]:
                L[0] = nums2[i]
                del nums2[i]
                break
        for i in range(len(nums2)):
            k = i+1
            if nums2[i] != k:
                L[1] = i+1
                break
        if L[1] < 1:
            L[1] = len(nums2)+1
        return L
                        
m = Solution
"s = m.findErrorNums(0,[3,2,3,4,6,5])"
s = m.findErrorNums(0,[1,2,2,4])
print(s)