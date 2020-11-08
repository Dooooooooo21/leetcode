#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/9/5 22:21
# @Author  : dly
# @File    : 39.py
# @Desc:

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)

        return nums[len(nums) // 2]

    def majorityElement2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tmp = nums[0]
        votes = 0

        for num in nums:
            if votes == 0:
                tmp = num
            if num == tmp:
                votes += 1
            else:
                votes -= 1

        count = 0
        for num in nums:
            if num == tmp:
                count += 1

        if count >= len(nums) // 2:
            return tmp
        else:
            return 0


s = Solution()
print(s.majorityElement2([1, 2, 3, 2, 2, 2, 5, 4, 2]))
