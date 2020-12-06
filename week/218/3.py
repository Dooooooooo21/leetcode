#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/12/6 10:39
# @Author  : dly
# @File    : 3.py
# @Desc    :

class Solution(object):
    def concatenatedBinary(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1 or n == 0:
            return n

        store = []
        for i in range(1, n + 1):
            store.append(str(bin(i))[2:])

        return int(''.join(store), 2) % (10 ** 9 + 7)


s = Solution()
res = s.concatenatedBinary(12)
print(res)
