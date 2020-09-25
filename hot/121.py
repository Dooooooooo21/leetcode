#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/9/25 22:21
# @Author  : dly
# @File    : 121.py
# @Desc    :

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        min_val = prices[0]
        profit = 0

        for num in prices:
            min_val = min(min_val, num)
            profit = max(profit, num - min_val)

        return profit
