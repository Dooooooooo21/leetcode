#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/12/7 15:15
# @Author  : dly
# @File    : num_search.py
# @Desc    :


def num_search(nums, target):
    left = 0
    right = len(nums)

    # 查找左边界
    while left < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            right = mid
        elif nums[mid] < target:
            left += 1
        elif nums[mid] > target:
            right = mid
    tmpleft = left

    left = 0
    right = len(nums)
    # 查找右边界
    while left < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            left = mid + 1
        elif nums[mid] < target:
            left = mid
        elif nums[mid] > target:
            right -= 1
    tmpright = left - 1

    return [tmpleft, tmpright]


nums = [5, 7, 7, 8, 8, 8, 8, 10]
target = 8
print(num_search(nums, target))
