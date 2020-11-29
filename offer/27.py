#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/9/5 21:59
# @Author  : dly
# @File    : 27.py
# @Desc:

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mirrorTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        if not root:
            return

        tmp = [root]

        while tmp:
            node = tmp.pop()
            if node.left:
                tmp.append(node.left)
            if node.right:
                tmp.append(node.right)
            node.left, node.right = node.right, node.left

        return root

    def mirrorTree2(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return

        tmp = root.left
        root.left = self.mirrorTree2(root.right)
        root.right = self.mirrorTree2(tmp)

        return root
