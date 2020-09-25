#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/9/25 22:50
# @Author  : dly
# @File    : 88.py
# @Desc    :

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        tmp = []
        i = 0
        j = 0

        while i < m and j < n:
            if nums1[i] < nums2[j]:
                tmp.append(nums1[i])
                i += 1
            elif nums1[i] > nums2[j]:
                tmp.append(nums2[j])
                j += 1
            else:
                tmp.append(nums1[i])
                tmp.append(nums2[j])
                i += 1
                j += 1

        if i == m:
            while j < n:
                tmp.append(nums2[j])
                j += 1
        if j == n:
            while i < m:
                tmp.append(nums1[i])
                i += 1

        nums1[:] = tmp[:]
