#!/usr/bin/env python
# -*- coding:utf-8 -*-

#================================================================
#   
#   File Name：gevent_test03.py
#   Author   ：GaoZhiChao
#   Date     ：2017年12月07日
#   Desc     ：greenlets are deterministic
#
#================================================================


import time

def echo(i):
    time.sleep(0.001)
    return i

# Non Deterministic Process Pool

from multiprocessing.pool import Pool

p = Pool(10)
run1 = [a for a in p.imap_unordered(echo, xrange(10))]
run2 = [a for a in p.imap_unordered(echo, xrange(10))]
run3 = [a for a in p.imap_unordered(echo, xrange(10))]
run4 = [a for a in p.imap_unordered(echo, xrange(10))]

print run1, run2, run3
print( run1 == run2 == run3 == run4 )

# Deterministic Gevent Pool

from gevent.pool import Pool

p = Pool(10)
run1 = [a for a in p.imap_unordered(echo, xrange(10))]
run2 = [a for a in p.imap_unordered(echo, xrange(10))]
run3 = [a for a in p.imap_unordered(echo, xrange(10))]
run4 = [a for a in p.imap_unordered(echo, xrange(10))]

print run1, run2, run3
print( run1 == run2 == run3 == run4 )


# OutPut:
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] [0, 1, 3, 4, 2, 5, 6, 7, 8, 9] [0, 3, 1, 2, 4, 5, 6, 7, 8, 9]
# False
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# True
