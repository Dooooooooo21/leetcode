#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2022/3/5 22:34
# @Author  : dly
# @File    : 1.py
# @Desc    :

class Solution(object):
    def mostFrequent(self, nums, key):
        """
        :type nums: List[int]
        :type key: int
        :rtype: int
        """
        num_dict = dict()

        size = len(nums)

        for i in range(size - 1):
            if nums[i] == key:
                if nums[i + 1] in num_dict.keys():
                    num_dict[nums[i + 1]] += 1
                else:
                    num_dict[nums[i + 1]] = 1
                i += 1
            else:
                continue

        max = 0
        result = 0
        for k, v in num_dict.items():
            if v > max:
                max = v
                result = k

        return result


nums = [1, 1]
key = 1
s = Solution()
result = s.mostFrequent(nums, key)
print(result)
