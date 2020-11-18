#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/11/18 22:07
# @Author  : dly
# @File    : 169.py
# @Desc    :

# 多数元素
# 投票
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        global ans
        vote = 0
        for num in nums:
            if vote == 0:
                ans = num
                vote += 1
            elif vote > 0:
                if num == ans:
                    vote += 1
                else:
                    vote -= 1

        return ans
