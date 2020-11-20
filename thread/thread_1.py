#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/11/20 14:01
# @Author  : dly
# @File    : thread.py
# @Desc    :


import threading
import time


def target():
    print('thread %s is running.' % (threading.current_thread().name))
    time.sleep(1)
    print('thread %s is end.' % (threading.current_thread().name))


print('thread %s is running.' % (threading.current_thread().name))

t = threading.Thread(target=target)
t.start()

# join 阻塞当前进程
t.join()

print('thread %s is ended.' % (threading.current_thread().name))