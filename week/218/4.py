#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/12/6 11:18
# @Author  : dly
# @File    : 4.py
# @Desc    :

class Solution(object):
    def minimumIncompatibility(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        nums.sort(reverse=True)
        bucketCount = k
        bucketSize = len(nums) / k
        length = len(nums) - 1
        buckets = [[] for _ in range(bucketCount)]
        for bucket in buckets:
            pass

        print(buckets)


s = Solution()
s.minimumIncompatibility([6, 3, 8, 1, 3, 1, 2, 2], 4)
