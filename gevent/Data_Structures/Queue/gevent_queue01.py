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


# Worker test1 got task 1
# Worker test2 got task 2
# Worker test3 got task 3
# Worker test1 got task 4
# Worker test2 got task 5
# Worker test3 got task 6
# Worker test1 got task 7
# Worker test2 got task 8
# Worker test3 got task 9
# Worker test1 got task 10
# Worker test2 got task 11
# Worker test3 got task 12
# Worker test1 got task 13
# Worker test2 got task 14
# Worker test3 got task 15
# Worker test1 got task 16
# Worker test2 got task 17
# Worker test3 got task 18
# Worker test1 got task 19
# Worker test2 got task 20
# Worker test3 got task 21
# Worker test1 got task 22
# Worker test2 got task 23
# Worker test3 got task 24
# Quitting time!          
# Quitting time!          
# Quitting time!  
