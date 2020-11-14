#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/11/14 10:23
# @Author  : dly
# @File    : 46.py
# @Desc    :

# 全排列
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []

        ans = []
        c = list(nums)
        l = len(c)

        def helper(index):
            if index == l - 1:
                ans.append(list(c))
                return
            for i in range(index, l):
                c[index], c[i] = c[i], c[index]
                print(c)
                helper(index + 1)
                c[index], c[i] = c[i], c[index]

        helper(0)
        return ans


s = Solution()
s.permute([1, 2, 3])
