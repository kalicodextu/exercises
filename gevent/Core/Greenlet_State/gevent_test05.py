#!/usr/bin/env python
# -*- coding:utf-8 -*-

#================================================================
#   
#   File Name：gevent_test05.py
#   Author   ：GaoZhiChao
#   Date     ：2017年12月07日
#   Desc     ：
#
#================================================================


import gevent
def win():
    return 'you win!'


def fail():
    return 'you fail!'


winner = gevent.spawn(win)
loser = gevent.spawn(fail)

print winner.started
print loser.started


try:
    gevent.joinall([
        winner,
        loser,
        ])

except Exception as e:
    print 'This will never be reached!'


print winner.ready(), loser.ready(), winner.value, loser.value, winner.exception, loser.exception


# Output:

# True
# True
# True True you win! you fail! None None
