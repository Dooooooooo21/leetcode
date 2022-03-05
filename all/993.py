#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/5/17 19:48
# @Author  : dly
# @File    : 993.py
# @Desc    :


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        if not root:
            return False

        nodeList = [root]

        while nodeList:
            size = len(nodeList)

            tmp = []
            valList = []
            for _ in range(size):
                node = nodeList.pop(0)
                valList.append(node.val)
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)

            if x in valList and y in valList:
                return True
            nodeList = tmp[:]

        return False
