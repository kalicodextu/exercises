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


# output:
# Start Polling: at 0.0s seconds
# Start Polling: at 0.0s seconds
# Hey lets do some stuff while the greenlets poll, at 0.0s seconds
# End stuff: at 1.0s seconds
# End Polling: at 2.0s seconds
# End Polling: at 2.0s seconds
#



#   select.select  source code @ module gevent select.py
#   
#   def select(rlist, wlist, xlist, timeout=None): # pylint:disable=unused-argument
#       """An implementation of :meth:`select.select` that blocks only the current greenlet.
#   
#       .. caution:: *xlist* is ignored.
#   
#       .. versionchanged:: 1.2a1
#          Raise a :exc:`ValueError` if timeout is negative. This matches Python 3's
#          behaviour (Python 2 would raise a ``select.error``). Previously gevent had
#          undefined behaviour.
#       .. versionchanged:: 1.2a1
#          Raise an exception if any of the file descriptors are invalid.
#       """
#       if timeout is not None and timeout < 0:
#           # Raise an error like the real implementation; which error
#           # depends on the version. Python 3, where select.error is OSError,
#           # raises a ValueError (which makes sense). Older pythons raise
#           # the error from the select syscall...but we don't actually get there.
#           # We choose to just raise the ValueError as it makes more sense and is
#           # forward compatible
#           raise ValueError("timeout must be non-negative")
#   
#       # First, do a poll with the original select system call. This
#       # is the most efficient way to check to see if any of the file descriptors
#       # have previously been closed and raise the correct corresponding exception.
#       # (Because libev tends to just return them as ready...)
#       # We accept the *xlist* here even though we can't below because this is all about
#       # error handling.
#       sel_results = ((), (), ())
#       try:
#           sel_results = _original_select(rlist, wlist, xlist, 0)
#       except error as e:
#           enumber = getattr(e, 'errno', None) or e.args[0]
#           if enumber != EINTR:
#               # Ignore interrupted syscalls
#               raise
#   
#       if sel_results[0] or sel_results[1] or sel_results[2]:
#           # If we actually had stuff ready, go ahead and return it. No need
#           # to go through the trouble of doing our own stuff.
#           # However, because this is typically a place where scheduling switches
#           # can occur, we need to make sure that's still the case; otherwise a single
#           # consumer could monopolize the thread. (shows up in test_ftplib.)
#           _g_sleep()
#           return sel_results
#   
#       result = SelectResult()
#       return result.select(rlist, wlist, timeout)
#   
