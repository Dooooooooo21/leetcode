#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/9/7 20:54
# @Author  : dly
# @File    : 45.py
# @Desc:

# s1 + s2 > s2 + s1, 将s2放在前面
class Solution(object):
    def minNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """

        def quick_sort(l, r):
            i, j = l, r
            if l >= r:
                return

            while i < j:
                while strs[j] + strs[l] > strs[l] + strs[j] and i < j:
                    j -= 1
                while strs[i] + strs[l] <= strs[l] + strs[i] and i < j:
                    i += 1
                strs[i], strs[j] = strs[j], strs[i]

            strs[i], strs[l] = strs[l], strs[i]
            print(strs)
            quick_sort(l, i - 1)
            quick_sort(i + 1, r)

        strs = [str(num) for num in nums]
        quick_sort(0, len(strs) - 1)
        return ''.join(strs)


s = Solution()
s.minNumber([333, 380, 343, 35, 393])
