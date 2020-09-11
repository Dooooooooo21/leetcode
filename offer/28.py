#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/9/5 22:14
# @Author  : dly
# @File    : 28.py
# @Desc:


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        def recur(A, B):
            if not A and not B:
                return True
            if not A or not B or A.val != B.val:
                return False

            return recur(A.left, B.right) and recur(A.right, B.left)

        return recur(root.left, root.right)
