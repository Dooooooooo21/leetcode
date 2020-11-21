#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/11/21 15:32
# @Author  : dly
# @File    : threaad_pool.py
# @Desc    :

import queue
import threading
import time


class WorkManger(object):
    def __init__(self, work_num=1000, thread_num=2):
        self.work_queue = queue.Queue()
        self.threads = []
        self.__init_work_queue(work_num)
        self.__init_thread_pool(thread_num)

    # 初始化线程池
    def __init_thread_pool(self, thread_num):
        for i in range(thread_num):
            self.threads.append(Work(self.work_queue))

    # 初始化工作队列
    def __init_work_queue(self, jobs_num):
        for i in range(jobs_num):
            self.add_job(do_job, i)

    # 添加工作入队
    def add_job(self, func, *args):
        self.work_queue.put((func, list(args)))

    # 等待所有线程运行完
    def wait_allcomplete(self):
        for item in self.threads:
            if item.isAlive():
                item.join()


class Work(threading.Thread):
    def __init__(self, work_queue):
        threading.Thread.__init__(self)
        self.work_queue = work_queue
        self.start()

    def run(self) -> None:
        while True:
            try:
                do, args = self.work_queue.get(block=False)
                do(args)
                self.work_queue.task_done()
            except:
                break


def do_job(args):
    time.sleep(0.1)
    print(threading.current_thread())
    print(list(args))


start = time.time()
work_manager = WorkManger(100, 10)
work_manager.wait_allcomplete()
end = time.time()
print('cost %s' % (end - start))
