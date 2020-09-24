#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/9/24 23:00
# @Author  : dly
# @File    : 63.py
# @Desc    :

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        min = prices[0]
        profit = 0

        for num in prices:
            if num < min:
                min = num
            if num - min > profit:
                profit = num - min

        return profit