#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/11/11 22:19
# @Author  : dly
# @File    : 68_1.py
# @Desc    :

# 二叉搜索树的最近公共祖先
class Solution(object):
    # 迭代
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root: return None
        while root:
            if root.val < p.val and root.val < q.val:
                root = root.right
            elif root.val > p.val and root.val > q.val:
                root = root.left
            else:
                break

        return root

    # 递归
    def lowestCommonAncestor2(self, root, p, q):
        if not root: return None
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor2(root.right, p, q)
        elif root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor2(root.left, p, q)
        return root
