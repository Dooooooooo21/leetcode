#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/11/20 14:08
# @Author  : dly
# @File    : thread_2.py
# @Desc    :


import threading
import time


class MyThread(threading.Thread):
    def __init__(self, threadId, name, counter):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
        self.counter = counter

    def run(self):
        print('start ' + self.name)
        # 获得锁后返回 True
        threadLock.acquire()
        print_time(self.name, self.counter, 5)
        print('end ' + self.name)
        # 释放锁
        threadLock.release()


def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print('%s process at: %s ' % (threadName, time.ctime(time.time())))
        counter -= 1


threadLock = threading.Lock()
thread1 = MyThread(1, 'Thread-1', 1)
thread2 = MyThread(2, 'Thread-2', 2)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
print('end')
