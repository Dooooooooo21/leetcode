#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/11/15 21:29
# @Author  : dly
# @File    : sort.py
# @Desc    :


# 冒泡排序
def bubble_sort(nums):
    if not nums:
        return None
    size = len(nums)
    # 每次在剩下的范围内找到最大的
    for i in range(size):
        for j in range(size - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
        print(nums)

    return nums


# 选择排序
# n + (n - 1) + (n - 2) + ... + 1
# 时间复杂度 n*n
def select_sort(nums):
    size = len(nums)
    for i in range(size):
        mi = i
        # 在未排序中找到最小值，放到排序后
        for j in range(i, size):
            if nums[j] < nums[mi]:
                mi = j
        nums[i], nums[mi] = nums[mi], nums[i]
        print(nums)

    return nums


# 插入排序
# 通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入
def insert_sort(nums):
    size = len(nums)
    for i in range(1, size):
        preIndex = i - 1
        tmp = nums[i]
        while preIndex >= 0 and nums[preIndex] > tmp:
            nums[preIndex + 1] = nums[preIndex]
            preIndex -= 1
        nums[preIndex + 1] = tmp
        print(nums)

    return nums


nums = [5, 3, 1, 7, 2, 6]
# bubble_sort(nums)
insert_sort(nums)
