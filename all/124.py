#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/12/6 21:35
# @Author  : dly
# @File    : 124.py
# @Desc    :
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root.left and not root.right:
            return root.val

        self.res = float('-inf')

        def dfs(root):
            if not root:
                return 0
            left = max(0, dfs(root.left))
            right = max(0, dfs(root.right))
            tmp = left + right + root.val
            self.res = max(self.res, tmp)

            return max(left, right) + root.val

        dfs(root)
        return self.res
