#!/usr/bin/env python
# -*- coding:utf-8 -*-


import gevent
from gevent import getcurrent
from gevent.pool import Group

group = Group()

def hello_from(n):
    print('Size of group %s' % len(group))
    print('Hello from Greenlet %s' % id(getcurrent()))

group.map(hello_from, xrange(3))


def intensive(n):
    gevent.sleep(3 - n)
    return 'task', n

print('Ordered')

ogroup = Group()
for i in ogroup.imap(intensive, xrange(3)):
    print(i)

print('Unordered')

igroup = Group()
for i in igroup.imap_unordered(intensive, xrange(3)):
    print(i)


# output:
#  Size of group 3
#  Hello from Greenlet 4340152592
#  Size of group 3
#  Hello from Greenlet 4340928912
#  Size of group 3
#  Hello from Greenlet 4340928592
#  Ordered
#  ('task', 0)
#  ('task', 1)
#  ('task', 2)
#  Unordered
#  ('task', 2)
#  ('task', 1)
#  ('task', 0)


# source code
# def map(self, func, iterable):
#         """Return a list made by applying the *func* to each element of
#         the iterable.
# 
#         .. seealso:: :meth:`imap`
#         """
#         return list(self.imap(func, iterable))
# 
#     def map_cb(self, func, iterable, callback=None):
#         result = self.map(func, iterable)
#         if callback is not None:
#             callback(result)
#         return result
# 
#     def map_async(self, func, iterable, callback=None):
#         """
#         A variant of the map() method which returns a Greenlet object that is executing
#         the map function.
# 
#         If callback is specified then it should be a callable which accepts a
#         single argument.
#         """
#         return Greenlet.spawn(self.map_cb, func, iterable, callback)
# 
#     def __imap(self, cls, func, *iterables, **kwargs):
#         # Python 2 doesn't support the syntax that lets us mix varargs and
#         # a named kwarg, so we have to unpack manually
#         maxsize = kwargs.pop('maxsize', None)
#         if kwargs:
#             raise TypeError("Unsupported keyword arguments")
#         return cls.spawn(func, izip(*iterables), spawn=self.spawn,
#                          _zipped=True, maxsize=maxsize)
# 
#     def imap(self, func, *iterables, **kwargs):
#         """
#         imap(func, *iterables, maxsize=None) -> iterable
# 
#         An equivalent of :func:`itertools.imap`, operating in parallel.
#         The *func* is applied to each element yielded from each
#         iterable in *iterables* in turn, collecting the result.
# 
#         If this object has a bound on the number of active greenlets it can
#         contain (such as :class:`Pool`), then at most that number of tasks will operate
#         in parallel.
# 
#         :keyword int maxsize: If given and not-None, specifies the maximum number of
#             finished results that will be allowed to accumulate awaiting the reader;
#             more than that number of results will cause map function greenlets to begin
#             to block. This is most useful if there is a great disparity in the speed of
#             the mapping code and the consumer and the results consume a great deal of resources.
# 
#             .. note:: This is separate from any bound on the number of active parallel
#                tasks, though they may have some interaction (for example, limiting the
#                number of parallel tasks to the smallest bound).
# 
#             .. note:: Using a bound is slightly more computationally expensive than not using a bound.
# 
#             .. tip:: The :meth:`imap_unordered` method makes much better
#                 use of this parameter. Some additional, unspecified,
#                 number of objects may be required to be kept in memory
#                 to maintain order by this function.
# 
#         :return: An iterable object.
# 
#         .. versionchanged:: 1.1b3
#             Added the *maxsize* keyword parameter.
#         .. versionchanged:: 1.1a1
#             Accept multiple *iterables* to iterate in parallel.
#         """
#         return self.__imap(IMap, func, *iterables, **kwargs)
# 
#     def imap_unordered(self, func, *iterables, **kwargs):
#         """
#         imap_unordered(func, *iterables, maxsize=None) -> iterable
# 
#         The same as :meth:`imap` except that the ordering of the results
#         from the returned iterator should be considered in arbitrary
#         order.
# 
#         This is lighter weight than :meth:`imap` and should be preferred if order
#         doesn't matter.
# 
#         .. seealso:: :meth:`imap` for more details.
#         """
#         return self.__imap(IMapUnordered, func, *iterables, **kwargs)
# 
