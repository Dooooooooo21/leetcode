#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/11/26 22:50
# @Author  : dly
# @File    : 58.py
# @Desc    :

# 最后一个单词的长度
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        length = len(s) - 1
        while length >= 0 and s[length] == ' ':
            length -= 1
        if length == -1:
            return 0

        count = 0
        while length >= 0 and s[length] != ' ':
            count += 1
            length -= 1

        return count


s = Solution()
res = s.lengthOfLastWord('a bbb')
print(res)
