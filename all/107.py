#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/10/25 21:18
# @Author  : dly
# @File    : 107.py
# @Desc    :

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        node_list = []
        if not root:
            return node_list
        node_list.append(root)

        res = []
        while node_list:
            l = len(node_list)
            value_list = []
            for i in range(l):
                node = node_list.pop(0)
                value_list.append(node.val)
                if node.left:
                    node_list.append(node.left)
                if node.right:
                    node_list.append(node.right)
            res.append(value_list)

        return res[::-1]
