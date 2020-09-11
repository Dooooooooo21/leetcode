#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/9/6 21:21
# @Author  : dly
# @File    : 40.py
# @Desc:


class Solution(object):
    def getLeastNumbers(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        if k > len(arr) or k <= 0:
            return []

        start = 0
        end = len(arr) - 1
        index = self.quick_sort(arr, start, end)

        while index != k - 1:
            if index > k - 1:
                end = index - 1
                index = self.quick_sort(arr, start, end)
            elif index < k - 1:
                start = index + 1
                index = self.quick_sort(arr, start, end)

        return arr[:k]

    def quick_sort(self, arr, start, end):
        low = start
        high = end
        tmp = arr[low]
        while low < high:
            while low < high and arr[high] >= tmp:
                high -= 1
            arr[low] = arr[high]

            while low < high and arr[low] < tmp:
                low += 1
            arr[high] = arr[low]
        arr[low] = tmp
        return low
