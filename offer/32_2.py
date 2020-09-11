#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/9/4 20:32
# @Author  : dly
# @File    : 32_2.py
# @Desc:

import collections

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        result = []
        node_list = collections.deque()

        node_list.append(root)
        while len(node_list) > 0:
            tmp = []
            for _ in range(len(node_list)):
                tmp_node = node_list.popleft()
                tmp.append(tmp_node.val)
                if tmp_node.left:
                    node_list.append(tmp_node.left)
                if tmp_node.right:
                    node_list.append(tmp_node.right)
            result.append(tmp)

        return result
