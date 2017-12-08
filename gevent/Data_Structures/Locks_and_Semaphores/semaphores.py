#!/usr/bin/env python
# -*- coding:utf-8 -*-


from gevent import sleep
from gevent.pool import Pool
# v1.2.2 remove the module coros
#from gevent.coros import BoundedSemaphore
# v1.0.2 is valid use coros
from gevent.lock import BoundedSemaphore


sem = BoundedSemaphore(2)

def worker1(n):
    sem.acquire()
    print 'Worker %i acquired semaphore' % n
    sleep(0)
    sem.release()
    print 'Worker %i released semaphore' % n


def worker2(n):
    with sem:
        print 'Worker %i acquired semaphore' % n
        sleep(0)
    print 'Worker %i released semaphore' % n


pool = Pool()
pool.map(worker1, xrange(0, 3))
pool.map(worker2, xrange(3, 6))


# Worker 0 acquired semaphore
# Worker 1 acquired semaphore
# Worker 0 released semaphore
# Worker 1 released semaphore
# Worker 2 acquired semaphore
# Worker 2 released semaphore
# Worker 3 acquired semaphore
# Worker 4 acquired semaphore
# Worker 3 released semaphore
# Worker 4 released semaphore
# Worker 5 acquired semaphore
# Worker 5 released semaphore


# remark
# BoundedSemaphore, Queue can set the size
