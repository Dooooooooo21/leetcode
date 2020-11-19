#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/11/19 22:59
# @Author  : dly
# @File    : 239.py
# @Desc    :

import collections


# 滑动窗口最大值
# 降序最大栈
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return nums
        queue = collections.deque()

        for i in range(k):
            while queue and queue[-1] < nums[i]:
                queue.pop()
            queue.append(nums[i])

        res = [queue[0]]

        for j in range(k, len(nums)):
            if queue[0] == nums[j - k]:
                queue.popleft()
            while queue and queue[-1] < nums[j]:
                queue.pop()

            queue.append(nums[j])
            res.append(queue[0])

        return res
