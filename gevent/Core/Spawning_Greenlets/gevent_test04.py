#!/usr/bin/env python
# -*- coding:utf-8 -*-

#================================================================
#   
#   File Name：gevent_test004.py
#   Author   ：GaoZhiChao
#   Date     ：2017年12月07日
#   Desc     ：spawn' cls parameter must be callable
#
#================================================================


import gevent
from gevent import Greenlet

def foo(message, n):
    """
    Each thread will be passed the message, and n arguments
    in its initialization.
    """
    gevent.sleep(n)
    print(message)

# Initialize a new Greenlet instance running the named function
# foo
thread1 = Greenlet.spawn(foo, "Hello", 1)

# Wrapper for creating and running a new Greenlet from the named
# function foo, with the passed arguments
thread2 = gevent.spawn(foo, "I live!", 2)

# Lambda expressions
thread3 = gevent.spawn(lambda x: (x+1), 2)

threads = [thread1, thread2, thread3]

# Block until all threads complete.
gevent.joinall(threads)



#    source code @file: greenlet.py
#    @classmethod
#    def spawn(cls, *args, **kwargs):
#        """
#        Create a new :class:`Greenlet` object and schedule it to run ``function(*args, **kwargs)``.
#        This can be used as ``gevent.spawn`` or ``Greenlet.spawn``.
#
#        The arguments are passed to :meth:`Greenlet.__init__`.
#
#        .. versionchanged:: 1.1b1
#            If a *function* is given that is not callable, immediately raise a :exc:`TypeError`
#            instead of spawning a greenlet that will raise an uncaught TypeError.
#        """
#        g = cls(*args, **kwargs)
#        g.start()
#        return g
