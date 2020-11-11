#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/11/11 22:34
# @Author  : dly
# @File    : 68_2.py
# @Desc    :

# 二叉树的最近公共祖先
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left:
            return right
        if not right:
            return left

        return root