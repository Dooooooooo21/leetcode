#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/11/9 22:21
# @Author  : dly
# @File    : 53_1.py
# @Desc    :

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i, j = 0, len(nums) - 1

        while i <= j:
            m = (i + j) // 2
            if nums[m] <= target:
                i = m + 1
            else:
                j = m - 1
        right = j
        print(right)
        if j >= 0 and nums[j] != target:
            return 0

        i = 0
        while i <= j:
            m = (i + j) // 2
            if nums[m] < target:
                i = m + 1
            else:
                j = m - 1

        left = i
        print(left)
        return right - left + 1


s = Solution()
s.search([5, 7, 7, 8, 8, 10], 8)
