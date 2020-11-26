#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/11/26 22:37
# @Author  : dly
# @File    : 100.py
# @Desc    :

# 相同的树
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        def dfs(tp, tq):
            if not tp and not tq:
                return True
            if not tp or not tq or tp.val != tq.val:
                return False

            return dfs(tp.left, tq.left) and dfs(tp.right, tq.right)

        return dfs(p, q)
