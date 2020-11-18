#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/11/18 22:37
# @Author  : dly
# @File    : 226.py
# @Desc    :

# 翻转二叉树
# 递归
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root

        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
