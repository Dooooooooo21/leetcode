#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/11/14 23:32
# @Author  : dly
# @File    : 94.py
# @Desc    :

# 二叉树的中序遍历
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        ans = []

        def dfs(root):
            if not root:
                return
            dfs(root.left)
            ans.append(root.val)
            dfs(root.right)

        dfs(root)
        return ans
