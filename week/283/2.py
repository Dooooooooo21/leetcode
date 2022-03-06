#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2022/3/6 10:51
# @Author  : dly
# @File    : 2.py
# @Desc    :
import copy


class Solution(object):
    def minimalKSum1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        max_num = max(nums) + k

        nums_copy = []

        count = 0
        for i in range(1, max_num):
            if i in nums:
                continue
            else:
                count += 1
                nums_copy.append(i)
            if count == k:
                break

        return sum(nums_copy)

    # 列表求差集
    def minimalKSum2(self, nums, k):
        max_num = max(nums) + k
        num_list = [i for i in range(1, max_num)]
        nums = sorted(nums)

        list_res = list(set(num_list) - set(nums))[:k]

        return sum(list_res)

    def minimalKSum(self, nums, k):
        nums.append(0)
        nums.append(10 ** 10)
        nums = sorted(list(set(nums)))
        s = 0
        for i in range(1, len(nums)):
            c = nums[i] - nums[i - 1] - 1
            if k >= c:
                s += c * (nums[i - 1] + 1 + nums[i] - 1) // 2
                k -= c
            else:
                s += k * (nums[i - 1] + 1 + nums[i - 1] + k) // 2
                k = 0
        return s


s = Solution()
result = s.minimalKSum([5, 6], 6)
print(result)
