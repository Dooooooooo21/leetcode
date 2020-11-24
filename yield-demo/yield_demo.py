#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/11/24 16:34
# @Author  : dly
# @File    : yield_demo.py
# @Desc    :

import sys


# yield 生成器
def fab(n):
    a, b, counter = 0, 1, 0
    while True:
        if n < counter:
            return
        yield a
        a, b = b, a + b
        counter += 1


f = fab(10)

while True:
    try:
        print(next(f))
    except StopIteration:
        sys.exit()
