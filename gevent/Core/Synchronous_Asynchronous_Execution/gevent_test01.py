#!/usr/bin/env python
# -*- coding:utf-8 -*-

#================================================================
#   
#   File Name：gevent_test01.py
#   Author   ：GaoZhiChao
#   Date     ：2017年12月07日
#   Desc     ：bcs gevent‘s asyn make random's property show as print order
#
#================================================================


import gevent
import random

def task(pid):
    """
    Some non-deterministic task
    """
    gevent.sleep(random.randint(0, 2)*0.001)
    print('Task %s done' % pid)

def synchronous():
    for i in range(1,10):
        task(i)

def asynchronous():
    threads = [gevent.spawn(task, i) for i in xrange(10)]
    gevent.joinall(threads)

print('Synchronous:')
synchronous()

print('Asynchronous:')
asynchronous()


# Output
# Synchronous:
# Task 1 done
# Task 2 done
# Task 3 done
# Task 4 done
# Task 5 done
# Task 6 done
# Task 7 done
# Task 8 done
# Task 9 done
# Asynchronous:
# Task 1 done
# Task 2 done
# Task 0 done
# Task 3 done
# Task 5 done
# Task 6 done
# Task 7 done
# Task 9 done
# Task 4 done
# Task 8 done
