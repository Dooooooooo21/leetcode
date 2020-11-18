#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/11/18 21:40
# @Author  : dly
# @File    : 101.py
# @Desc    :

# 对称二叉树
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        def dfs(ra, rb):
            if not ra and not rb:
                return True
            if not ra or not rb:
                return False
            if ra.val != rb.val:
                return False

            return dfs(ra.left, rb.right) and dfs(ra.right, rb.left)

        return dfs(root.left, root.right)
