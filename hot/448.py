#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/11/19 23:37
# @Author  : dly
# @File    : 448.py
# @Desc    :


# 找到所有数组中消失的数字
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []

        for num in nums:
            index = abs(num) - 1
            nums[index] = -abs(nums[index])

        return [i + 1 for i, num in enumerate(nums) if num > 0]


s = Solution()
print(s.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))
