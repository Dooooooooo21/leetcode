#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/12/8 22:11
# @Author  : dly
# @File    : 0205.py
# @Desc    :

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1

        def get_num(node):
            ans = []
            while node:
                ans.append(str(node.val))
                node = node.next

            return int(''.join(reversed(ans)))

        def num_to_list(num, node):
            chs = reversed(list(str(num)))
            for c in chs:
                node.next = ListNode(int(c))
                node = node.next

        num_1 = get_num(l1)
        num_2 = get_num(l2)
        node = ListNode(0)
        head = node
        num_to_list(num_1 + num_2, node)

        return head.next
