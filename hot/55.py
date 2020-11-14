#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/11/14 23:26
# @Author  : dly
# @File    : 55.py
# @Desc    :

# 跳跃游戏
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        k = 0

        for i in range(len(nums)):
            if i > k:
                return False
            k = max(i + nums[i], k)

        return True
