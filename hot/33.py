#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/11/13 23:11
# @Author  : dly
# @File    : 33.py
# @Desc    :

# 搜索旋转排序数组
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            # mid 在前半部分
            if nums[mid] >= nums[l]:
                if nums[mid] > target >= nums[l]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[r] >= target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1


s = Solution()
print(s.search([1, 3], 3))
