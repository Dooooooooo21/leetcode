#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/10/29 21:50
# @Author  : dly
# @File    : 7.py
# @Desc    :

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            ind = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[ind])
            root.left = self.buildTree(preorder, inorder[0:ind])
            root.right = self.buildTree(preorder, inorder[ind + 1:])

            return root
