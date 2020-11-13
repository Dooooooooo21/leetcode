#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/11/13 23:54
# @Author  : dly
# @File    : 34.py
# @Desc    :

# 在排序数组中查找元素的第一个和最后一个位置
# 二分
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        i, j = 0, len(nums) - 1

        while i <= j:
            m = (i + j) // 2
            if nums[m] <= target:
                i = m + 1
            else:
                j = m - 1
        right = j
        if nums[right] != target:
            return [-1, -1]

        i = 0
        while i <= j:
            m = (i + j) // 2
            if nums[m] < target:
                i = m + 1
            else:
                j = m - 1
        return [i, right]


s = Solution()
print(s.searchRange([5, 7, 7, 8, 8, 10], 6))
