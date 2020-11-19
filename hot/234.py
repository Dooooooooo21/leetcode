#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/11/19 23:25
# @Author  : dly
# @File    : 234.py
# @Desc    :

# 回文链表
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True

        values = []
        while head:
            values.append(head.val)
            head = head.next

        i, j = 0, len(values) - 1
        while i <= j:
            if values[i] != values[j]:
                return False
            i += 1
            j -= 1

        return True
