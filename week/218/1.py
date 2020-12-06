#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/12/6 10:34
# @Author  : dly
# @File    : 1.py
# @Desc    :


class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        if not command:
            return command

        command = command.replace('()', 'o')
        command = command.replace('(', '')
        command = command.replace(')', '')

        return command
