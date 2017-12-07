#!/usr/bin/env python
# -*- coding:utf-8 -*-

#================================================================
#   
#   File Name：gevent_test06.py
#   Author   ：GaoZhiChao
#   Date     ：2017年12月07日
#   Desc     ：
#
#================================================================


import gevent
from gevent import Timeout


seconds = 10


timeout = Timeout(seconds)
timeout.start()

def wait():
    gevent.sleep(10)


try:
    gevent.spawn(wait).join()
except Timeout:
    print 'Could\'t complete'
##import gevent
##from gevent import Timeout
##
##time_to_wait = 5 # seconds
##
##class TooLong(Exception):
##    pass
##
##with Timeout(time_to_wait, TooLong):
##    gevent.sleep(10)
##
