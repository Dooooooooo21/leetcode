#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2022/3/5 22:52
# @Author  : dly
# @File    : 2.py
# @Desc    :


class Solution(object):
    def numTrans(self, mapping, num):
        num_str = str(num)
        num_res = ''
        for n in num_str:
            num_res += str(mapping[int(n)])

        return int(num_res)

    def sortJumbled(self, mapping, nums):
        """
        :type mapping: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        nums_trans = {}
        count = 0
        for num in nums:
            nums_trans[count] = self.numTrans(mapping, num)
            count += 1

        sort_nums = sorted(nums_trans.items(), key=lambda d: d[1])
        print(sort_nums)
        result = []
        for t in sort_nums:
            result.append(nums[t[0]])
        return result


s = Solution()
result = s.sortJumbled([8, 2, 9, 5, 3, 7, 1, 0, 6, 4],
                       [418, 4191, 916, 948, 629641556, 574, 111171937, 28250, 42775632, 6086, 85796326, 696292542, 186,
                        67559, 2167, 366, 854, 2441, 78176, 621, 4257, 2250097, 509847, 7506, 77, 50, 4135258, 4036,
                        59934, 59474, 3646243, 9049356, 85852, 90298188, 2448206, 30401413, 33190382, 968234660, 7973,
                        668786, 992777977, 77, 355766, 221, 246409664, 216290476, 45, 87, 836414, 40952])
print(result)
