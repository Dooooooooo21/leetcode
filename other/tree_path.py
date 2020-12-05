#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/12/5 18:30
# @Author  : dly
# @File    : tree_path.py
# @Desc    :

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def tree_path(root):
    if not root:
        return []

    def dfs(root, path):
        if not root:
            if list(path) not in res:
                res.append(list(path))
            return
        path.append(root.val)
        dfs(root.left, path)
        dfs(root.right, path)
        path.pop()

    res = []
    tmp = []
    dfs(root, tmp)

    print(res)
    return res


root = TreeNode(0)
root.left = TreeNode(1)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)

tree_path(root)
