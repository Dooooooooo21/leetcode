#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/11/20 14:56
# @Author  : dly
# @File    : thread_queue.py
# @Desc    :

import time
from datetime import datetime
import queue
import threading

from openpyxl.compat import singleton


# @singleton
class Worker(threading.Thread):
    def __init__(self, name, queue):
        threading.Thread.__init__(self)
        self.queue = queue
        # 执行
        self.start()

    def run(self):
        while True:
            # 队列为空 退出线程
            if self.queue.empty():
                break
            # 获取队列数据
            foo = self.queue.get()
            time.sleep(1)
            print(self.getName() + ' process ' + str(foo))
            # 任务完成
            self.queue.task_done()


startTime = datetime.now()
print(startTime)
# 队列
q = queue.Queue()
# 加入100个任务队列
for i in range(100):
    q.put(i)

# 10个线程
for i in range(10):
    threadName = 'thread' + str(i)
    Worker(threadName, q)

q.join()

endTime = datetime.now()
print('cost : ', endTime - startTime)