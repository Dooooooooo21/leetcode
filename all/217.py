#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/12/1 22:48
# @Author  : dly
# @File    : 217.py
# @Desc    :

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == len(set(nums)):
            return False
        else:
            return True
