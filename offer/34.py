#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/11/5 23:35
# @Author  : dly
# @File    : 34.py
# @Desc    :

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        path = []

        def recur(node, tar):
            if not node:
                return
            path.append(node.val)
            tar -= node.val
            if tar == 0 and not node.left and not node.right:
                res.append(list(path))
            recur(node.left, tar)
            recur(node.right, tar)
            path.pop()

        recur(root, sum)
        return res
