#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Gevent also allows you to specify data which is local to the greenlet context. 
Internally, this is implemented as a global lookup which addresses a private namespace keyed by the greenlet's getcurrent() value.
"""
import gevent
from gevent.local import local


stash = local()

def f1():
    stash.x = 1
    print stash.x

def f2():
    stash.y = 2
    print stash.y

    try:
        stash.x
    except AttributeError:
        print 'x is not local to f2?'

g1 = gevent.spawn(f1)
g2 = gevent.spawn(f2)

gevent.joinall([g1, g2])

print type(stash)


# output:
# 1
# 2
# x is not local to f2
# <class 'gevent.local.local'>
