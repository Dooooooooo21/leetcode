#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2022/3/6 10:38
# @Author  : dly
# @File    : 1.py
# @Desc    :

class Solution(object):
    def cellsInRange(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        col = s.split(':')[0]
        row = s.split(':')[1]

        a = col[0]
        num_a = col[1:]
        b = row[0]
        num_b = row[1:]

        res = []
        for i in range(ord(a), ord(b)+1):
            if num_a == num_b:
                res.append(chr(i) + str(num_a))
            else:
                for num in range(int(num_a), int(num_b) + 1):
                    res.append(chr(i) + str(num))
        return res


s = Solution()
result = s.cellsInRange('K1:L2')
print(result)
