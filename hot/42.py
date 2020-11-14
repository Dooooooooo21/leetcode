#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/11/14 9:45
# @Author  : dly
# @File    : 42.py
# @Desc    :


# 接雨水
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0

        ans = 0
        stack = []
        n = len(height)

        for i in range(n):
            while len(stack) > 0 and height[stack[-1]] < height[i]:
                # 保存当前柱体的高度索引
                curIndex = stack.pop(-1)
                while len(stack) > 0 and height[stack[-1]] == height[curIndex]:
                    stack.pop(-1)
                if len(stack) > 0:
                    # index 指向的是此次接住雨水的左边界位置，右边界为 i
                    index = stack[-1]
                    # 取出左边界和右边界中最低的，减去之前柱体的高度，就是接住雨水的高度，
                    # i - index - 1 是雨水的宽
                    ans += (min(height[index], height[i]) - height[curIndex]) * (i - index - 1)
            stack.append(i)

        return ans


s = Solution()
s.trap([4, 2, 0, 3, 2, 5])
