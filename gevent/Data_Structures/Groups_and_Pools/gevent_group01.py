#!/usr/bin/env python
# -*- coding:utf-8 -*-


import gevent
from gevent.pool import Group

def talk(msg):
    for i in xrange(3):
        print(msg)

g1 = gevent.spawn(talk, 'bar')
g2 = gevent.spawn(talk, 'foo')
g3 = gevent.spawn(talk, 'fizz')

group = Group()
group.add(g1)
group.add(g2)
group.add(g3)
group.join()


# source code
# class Group(GroupMappingMixin):
#     """
#     Maintain a group of greenlets that are still running, without
#     limiting their number.
# 
#     Links to each item and removes it upon notification.
# 
#     Groups can be iterated to discover what greenlets they are tracking,
#     they can be tested to see if they contain a greenlet, and they know the
#     number (len) of greenlets they are tracking. If they are not tracking any
#     greenlets, they are False in a boolean context.
#     """
# 
#     #: The type of Greenlet object we will :meth:`spawn`. This can be changed
#     #: on an instance or in a subclass.
#     greenlet_class = Greenlet
# 
#     def __init__(self, *args):
#         assert len(args) <= 1, args
#         self.greenlets = set(*args)
#         if args:
#             for greenlet in args[0]:
#                 greenlet.rawlink(self._discard)
#         # each item we kill we place in dying, to avoid killing the same greenlet twice
#         self.dying = set()
#         self._empty_event = Event()
#         self._empty_event.set()
# 
#     def __repr__(self):
#         return '<%s at 0x%x %s>' % (self.__class__.__name__, id(self), self.greenlets)
# 
#     def __len__(self):
#         """
#         Answer how many greenlets we are tracking. Note that if we are empty,
#         we are False in a boolean context.
#         """
#         return len(self.greenlets)
# 
#     def __contains__(self, item):
#         """
#         Answer if we are tracking the given greenlet.
#         """
#         return item in self.greenlets
# 
#     def __iter__(self):
#         """
#         Iterate across all the greenlets we are tracking, in no particular order.
#         """
#         return iter(self.greenlets)
# 
#     def add(self, greenlet):
#         """
#         Begin tracking the greenlet.
# 
#         If this group is :meth:`full`, then this method may block
#         until it is possible to track the greenlet.
#         """
#         try:
#             rawlink = greenlet.rawlink
#         except AttributeError:
#             pass  # non-Greenlet greenlet, like MAIN
#         else:
#             rawlink(self._discard)
#         self.greenlets.add(greenlet)
#         self._empty_event.clear()


#     def join(self, timeout=None, raise_error=False):
#         """
#         Wait for this group to become empty *at least once*.
# 
#         If there are no greenlets in the group, returns immediately.
# 
#         .. note:: By the time the waiting code (the caller of this
#            method) regains control, a greenlet may have been added to
#            this group, and so this object may no longer be empty. (That
#            is, ``group.join(); assert len(group) == 0`` is not
#            guaranteed to hold.) This method only guarantees that the group
#            reached a ``len`` of 0 at some point.
# 
#         :keyword bool raise_error: If True (*not* the default), if any
#             greenlet that finished while the join was in progress raised
#             an exception, that exception will be raised to the caller of
#             this method. If multiple greenlets raised exceptions, which
#             one gets re-raised is not determined. Only greenlets currently
#             in the group when this method is called are guaranteed to
#             be checked for exceptions.
# 
#         :return bool: A value indicating whether this group became empty.
#            If the timeout is specified and the group did not become empty
#            during that timeout, then this will be a false value. Otherwise
#            it will be a true value.
# 
#         .. versionchanged:: 1.2a1
#            Add the return value.
#         """
#         greenlets = list(self.greenlets) if raise_error else ()
#         result = self._empty_event.wait(timeout=timeout)
# 
#         for greenlet in greenlets:
#             if greenlet.exception is not None:
#                 if hasattr(greenlet, '_raise_exception'):
#                     greenlet._raise_exception()
#                 raise greenlet.exception
# 
#         return result
