#!/usr/bin/env python
# -*- coding:utf-8 -*-


import gevent
from gevent.queue import Queue

tasks = Queue()

def worker(name):
    while not tasks.empty():
        task = tasks.get()
        print 'Worker %s got task %s' % (name, task)
        gevent.sleep(0)

    print 'Quitting time!'


def boss():
    for i in xrange(1, 25):
        tasks.put_nowait(i)


# gevent.spawn(boss).join()


gevent.joinall([
    gevent.spawn(boss),
    gevent.spawn(worker, 'test1'),
    gevent.spawn(worker, 'test2'),
    gevent.spawn(worker, 'test3'),
    ])
