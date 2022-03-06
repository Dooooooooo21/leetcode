#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2022/3/6 11:08
# @Author  : dly
# @File    : 3.py
# @Desc    :
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def createBinaryTree1(self, descriptions):
        """
        :type descriptions: List[List[int]]
        :rtype: Optional[TreeNode]
        """

        parent_node_dict = dict()
        node_list = []
        for val in descriptions:
            if val[1] in parent_node_dict.keys():
                parent_node_dict[val[1]].append(val[0])
            else:
                parent_node_dict[val[1]] = [val[0]]
            node_list.append(val[1])
            node_list.append(val[0])

        start_node = list(set(node_list) - set(parent_node_dict.keys()))[0]

        root = TreeNode()
        root.val = start_node
        stack = [root]
        add = [False for _ in range(len(descriptions))]
        while stack:
            count = 0
            cur = stack.pop(0)
            for desc in descriptions:
                if add[count]:
                    count += 1
                    continue

                if desc[0] == cur.val:
                    node = TreeNode(desc[1])
                    stack.append(node)
                    add[count] = True
                    if desc[2] == 0:
                        cur.right = node
                    else:
                        cur.left = node
                count += 1
        return root

    def createBinaryTree2(self, descriptions):
        """
        :type descriptions: List[List[int]]
        :rtype: Optional[TreeNode]
        """

        parent_node_dict = dict()
        node_list = []
        for val in descriptions:
            if val[1] in parent_node_dict.keys():
                parent_node_dict[val[1]].append(val[0])
            else:
                parent_node_dict[val[1]] = [val[0]]
            node_list.append(val[1])
            node_list.append(val[0])

        child_node = dict()
        for val in descriptions:
            if val[0] in child_node.keys():
                child_node[val[0]].append([val[1], val[2]])
            else:
                child_node[val[0]] = [[val[1], val[2]]]

        start_node = list(set(node_list) - set(parent_node_dict.keys()))[0]

        root = TreeNode()
        root.val = start_node
        stack = [root]
        while stack:
            cur = stack.pop(0)
            if cur.val not in child_node.keys():
                continue
            node_list_tmp = child_node[cur.val]
            for node in node_list_tmp:
                tmp = TreeNode(node[0])
                stack.append(tmp)
                if node[1] == 0:
                    cur.right = tmp
                else:
                    cur.left = tmp
        return root

    def createBinaryTree(self, descriptions):
        node_dict = {}
        parend_dict = {}

        for a, b, c in descriptions:
            if a not in node_dict:
                node_dict[a] = TreeNode(a)
            if b not in node_dict:
                node_dict[b] = TreeNode(b)
            parend_dict[b] = a
            if c:
                node_dict[a].left = node_dict[b]
            else:
                node_dict[a].right = node_dict[b]

        for node in node_dict:
            if node not in parend_dict:
                return node_dict[node]


s = Solution()
s.createBinaryTree([[20, 15, 1], [20, 17, 0], [50, 20, 1], [50, 80, 0], [80, 19, 1]])
