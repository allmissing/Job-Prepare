# -*- coding: utf-8 -*-
"""
twosum:
    Given an array of integers, return indices of the two numbers
    such that they add up to a specific target. You may assume
    that each input would have exactly one solution, and you may 
    not use the same element twice.

Created on Thu Jul 20 09:39:38 2017

@author: 705family
"""

def twoSum(self,nums, target):
    buff_dict = {}
    if len(nums) <= 1:
        return False
    for i in range(len(nums)):
        buff_dict[nums[i]] = i
        print(buff_dict)
    for i in range(len(nums)):
        if target-nums[i] in buff_dict and buff_dict[target-nums[i]] != i:
            return [i,buff_dict[target-nums[i]]]
                                         
title = twoSum(0,[3,2,4],6)                        
print(title)
