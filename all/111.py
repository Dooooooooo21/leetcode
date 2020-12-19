#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/12/19 21:04
# @Author  : dly
# @File    : 111.py
# @Desc    :

# 二叉树的最小深度 bfs
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if not root:
            return 0

        nodes = [root]
        count = 1
        tmp = []
        while nodes:
            node = nodes.pop(0)
            if not node.left and not node.right:
                break
            if node.left:
                tmp.append(node.left)
            if node.right:
                tmp.append(node.right)
            if not nodes:
                nodes = tmp[:]
                tmp = []
                count += 1

        return count
