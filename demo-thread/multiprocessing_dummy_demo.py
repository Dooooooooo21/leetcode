#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/11/21 17:40
# @Author  : dly
# @File    : multiprocessing_dummy_demo.py
# @Desc    :


from multiprocessing.dummy import Pool as ThreadPool
import time


def fun(n):
    time.sleep(2)


start = time.time()
for i in range(5):
    fun(i)
print("单线程顺序执行耗时:", time.time() - start)

start2 = time.time()
pool = ThreadPool(processes=5)
results2 = pool.map(fun, range(5))
pool.close()
pool.join()
print("线程池（5）并发执行耗时:", time.time() - start2)
