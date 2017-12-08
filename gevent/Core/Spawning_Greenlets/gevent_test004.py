#!/usr/bin/env python
# -*- coding:utf-8 -*-


import gevent
from gevent import Greenlet
import time


class MyGreenlet(Greenlet):
    def __init__(self, message, n):
        Greenlet.__init__(self)
        self.message = message
        self.n = n

    def _run(self):
        start_time = time.time()
        print self.message
        gevent.sleep(self.n)
        times = round(time.time() - start_time)
        print 'After %s, get recv "hi"' % times

g = MyGreenlet('hi, darren!', 3)

g.start()
g.join()



#  Output
#  hi, darren!
#  After 3.0, get recv "hi"
