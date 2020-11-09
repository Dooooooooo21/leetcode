#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/11/9 22:56
# @Author  : dly
# @File    : 55.py
# @Desc    :
# 平衡二叉树
# dfs
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
