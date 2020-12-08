#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/10/7 12:39
# @Author  : dly
# @File    : 8.py
# @Desc    :

def myAtoi(s: str) -> int:
    i, n = 0, len(s)

    ans, res = [], 0

    while i < n and s[i] == ' ':  # 找到第一个非空白字符
        i += 1

        # 若第一个字符既不是数字也不是正负号，不需要转换
    if not s[i].isdigit() and (s[i] not in ['+', '-']):
        return res
    else:
        ans.append(s[i])
        i += 1

    while i < n:
        if not s[i].isdigit():
            return int(res)
        ans.append(s[i])
        res = "".join(ans)
        if int(res) > 2147483647:
            return 2147483647
        if int(res) < -2147483648:
            return -2147483648

        i += 1
    return int(res)


print(myAtoi('3.14'))
