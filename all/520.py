#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/11/29 22:43
# @Author  : dly
# @File    : 520.py
# @Desc    :


# 检测大写字母
class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """

        return word.islower() or word.isupper() or word.istitle()
