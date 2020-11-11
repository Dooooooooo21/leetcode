#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/11/11 22:09
# @Author  : dly
# @File    : 55_2.py
# @Desc    :

# 平衡二叉树
# 从下往上返回树深度
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def recur(root):
            if not root:
                return 0
            left = recur(root.left)
            if left == -1:
                return -1
            right = recur(root.right)
            if right == -1:
                return -1

            return max(left, right) + 1 if abs(left - right) <= 1 else -1

        return recur(root) != -1
