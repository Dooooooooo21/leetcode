#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/9/29 21:40
# @Author  : dly
# @File    : 54.py
# @Desc    :
class Solution(object):
    def kthLargest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        def dfs(x):
            if not x:
                return
            dfs(x.right)
            if self.k == 0:
                return
            self.k -= 1
            if self.k == 0:
                self.res = x.val
            dfs(x.left)

        self.k = k
        dfs(root)
        return self.res
