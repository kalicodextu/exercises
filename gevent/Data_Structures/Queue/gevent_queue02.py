#!/usr/bin/env python
# -*- coding:utf-8 -*-


import gevent
from gevent.queue import Queue, Empty

tasks = Queue(maxsize=3)

def worker(n):
    try:
        while True:
            task = tasks.get(timeout=1) # decrements queue size by 1
            print('Worker %s got task %s' % (n, task))
            gevent.sleep(0)
    except Empty:
        print('Quitting time!')

def boss():
    """
    Boss will wait to hand out work until a individual worker is
    free since the maxsize of the task queue is 3.
    """

    for i in xrange(1,10):
        tasks.put(i)
    print('Assigned all work in iteration 1')

    for i in xrange(10,20):
        tasks.put(i)
    print('Assigned all work in iteration 2')

gevent.joinall([
    gevent.spawn(boss),
    gevent.spawn(worker, 'steve'),
    gevent.spawn(worker, 'john'),
    gevent.spawn(worker, 'bob'),
    ])


#  output:
#   
#  Worker steve got task 1             
#  Worker john got task 2          
#  Worker bob got task 3           
#  Worker steve got task 4         
#  Worker john got task 5          
#  Worker bob got task 6           
#  Assigned all work in iteration 1        ***** Now, queue  tasks [7, 8, 9]
#  Worker steve got task 7         
#  Worker john got task 8          
#  Worker bob got task 9           
#  Worker steve got task 10        
#  Worker john got task 11         
#  Worker bob got task 12          
#  Worker steve got task 13        
#  Worker john got task 14         
#  Worker bob got task 15          
#  Worker steve got task 16        
#  Worker john got task 17         
#  Worker bob got task 18          
#  Assigned all work in iteration 2      ******  Now, queue tasks [19]
#  Worker steve got task 19        
#  Quitting time!                  
#  Quitting time!                  
#  Quitting time!
   
