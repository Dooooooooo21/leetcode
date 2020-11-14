#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/11/14 23:01
# @Author  : dly
# @File    : 49.py
# @Desc    :

# 字母异位词分组
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if not strs:
            return []
        ans = []

        dic = {}
        for str in strs:
            c = list(str)
            c = sorted(c)
            sc = ''.join(c)
            if sc in dic:
                values = dic.get(sc)
                values.append(str)
                dic[sc] = values
            else:
                dic[sc] = [str]

        for k, v in dic.items():
            ans.append(v)

        return ans


s = Solution()
s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
