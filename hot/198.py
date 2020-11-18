#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/11/18 22:00
# @Author  : dly
# @File    : 198.py
# @Desc    :

# 打家劫舍
# dp
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pre, cur = 0, 0
        for num in nums:
            cur, pre = max(pre + num, cur), cur

        return cur
