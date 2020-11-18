#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/11/18 22:48
# @Author  : dly
# @File    : 226_1.py
# @Desc    :

# 翻转二叉树
# 迭代
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root

        nodes = [root]
        while nodes:
            node = nodes.pop(0)
            node.left, node.right = node.right, node.left
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)

        return root
