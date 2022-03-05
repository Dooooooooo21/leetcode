#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2022/3/5 23:22
# @Author  : dly
# @File    : 3.py
# @Desc    :

class Solution(object):
    def getAncestors(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[List[int]]
        """
        parent_node = dict()
        for i in range(n):
            parent_node[i] = []

        for edge in edges:
            parent_node[edge[1]].append(edge[0])

        res = [[] for _ in range(n)]
        for start in range(n):
            stack = [start]
            visited = set()
            while stack:
                cur = stack.pop()
                for nex in parent_node[cur]:
                    if nex in visited:
                        continue
                    visited.add(nex)
                    res[start].append(nex)
                    stack.append(nex)
            res[start].sort()

        return res


n = 8
edges = [[0, 3], [0, 4], [1, 3], [2, 4], [2, 7], [3, 5], [3, 6], [3, 7], [4, 6]]
s = Solution()
result = s.getAncestors(n, edges)
print(result)
