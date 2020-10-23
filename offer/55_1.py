#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/10/23 21:53
# @Author  : dly
# @File    : 55_1.py
# @Desc    :

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        queue = [root]

        depth = 0

        while queue:
            tmp = []
            for node in queue:
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)

            queue = tmp
            depth += 1

        return depth
