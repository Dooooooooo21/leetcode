#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/9/24 21:39
# @Author  : dly
# @File    : 59_1.py
# @Desc    : 滑动窗口的最大值，辅助单调队列

import collections


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums or k == 0:
            return []

        deque = collections.deque()

        for i in range(k):
            while deque and deque[-1] < nums[i]:
                deque.pop()
            deque.append(nums[i])
        res = [deque[0]]

        for i in range(k, len(nums)):
            if deque[0] == nums[i - k]:
                deque.popleft()
            while deque and deque[-1] < nums[i]:
                deque.pop()
            deque.append(nums[i])
            res.append(deque[0])

        return res


s = Solution()
s.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3)
