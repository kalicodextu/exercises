#!/usr/bin/env python
# -*- coding:utf-8 -*-


import gevent
from gevent.event import AsyncResult
a = AsyncResult()

def setter():
    """
    After 3 seconds set the result of a.
    """
    gevent.sleep(3)
    a.set('Hello!')

def waiter():
    """
    After 3 seconds the get call will unblock after the setter
    puts a value into the AsyncResult.
    """
    print a.get()

gevent.joinall([
    gevent.spawn(setter),
    gevent.spawn(waiter),
])


# source code
# def get(self, block=True, timeout=None):
#     """Return the stored value or raise the exception.
# 
#     If this instance already holds a value or an exception, return  or raise it immediatelly.
#     Otherwise, block until another greenlet calls :meth:`set` or :meth:`set_exception` or
#     until the optional timeout occurs.
# 
#     When the *timeout* argument is present and not ``None``, it should be a
#     floating point number specifying a timeout for the operation in seconds
#     (or fractions thereof). If the *timeout* elapses, the *Timeout* exception will
#     be raised.
# 
#     :keyword bool block: If set to ``False`` and this instance is not ready,
#         immediately raise a :class:`Timeout` exception.
#     """
#     if self._value is not _NONE:
#         return self._value
#     if self._exc_info:
#         return self._raise_exception()
# 
#     if not block:
#         # Not ready and not blocking, so immediately timeout
#         raise Timeout()
# 
#     # Wait, raising a timeout that elapses
#     self._wait_core(timeout, ())
# 
#     # by definition we are now ready
#     return self.get(block=False)
