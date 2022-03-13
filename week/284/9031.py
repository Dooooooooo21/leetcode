#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2022/3/13 10:33
# @Author  : dly
# @File    : 9031.py
# @Desc    :
class Solution(object):
    def findKDistantIndices(self, nums, key, k):
        """
        :type nums: List[int]
        :type key: int
        :type k: int
        :rtype: List[int]
        """
        indexs = []
        count = 0
        for num in nums:
            if num == key:
                indexs.append(count)
            count += 1

        res = []
        for index in indexs:
            tmp = [i for i in range(index - k, index + k + 1)]
            res.extend(tmp)

        a = []
        for r in res:
            if 0 <= r <= len(nums) - 1:
                a.append(r)
        return sorted(set(a))


s = Solution()
res = s.findKDistantIndices(nums=[3, 4, 9, 1, 3, 9, 5], key=9, k=1)
print(res)
