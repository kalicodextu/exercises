#!/usr/bin/env python
# -*- coding:utf-8 -*-

#================================================================
#   
#   File Name：gevent_test.py
#   Author   ：GaoZhiChao
#   Date     ：2017年12月07日
#   Desc     ：
#
#================================================================


import gevent 
import time
from gevent import select


start = time.time()
tic = lambda: 'at %1.1fs seconds' % (time.time() - start)

def gr1():
    print 'Start Polling: %s' % tic()
    select.select([], [], [], 2)
    print 'End Polling: %s' % tic()


def gr2():
    print 'Start Polling: %s' % tic()
    select.select([], [], [], 2)
    print 'End Polling: %s' % tic()
    

def gr3():
    print 'Hey lets do some stuff while the greenlets poll, %s' % tic()
    gevent.sleep(1)
    print 'End stuff: %s' % tic() # add end timepoint


gevent.joinall([
    gevent.spawn(gr1),
    gevent.spawn(gr2),
    gevent.spawn(gr3),
    ])


# output
#
#
#
