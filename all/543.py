#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/12/13 23:18
# @Author  : dly
# @File    : 543.py
# @Desc    :

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.max = 0

        def dfs(root):
            if not root:
                return 0
            l = dfs(root.left)
            r = dfs(root.right)
            self.max = max(self.max, l + r)

            return max(l, r) + 1

        dfs(root)
        return self.max
