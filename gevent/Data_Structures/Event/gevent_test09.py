#!/usr/bin/env python
# -*- coding:utf-8 -*-


import gevent
from gevent.event import Event

'''
Illustrates the use of events
'''


evt = Event()

def setter():
    '''After 3 seconds, wake all threads waiting on the value of evt'''
    print('A: Hey wait for me, I have to do something')
    gevent.sleep(10)
    print("Ok, I'm done")
    evt.set()


def waiter():
    '''After 3 seconds the get call will unblock'''
    print("I'll wait for you")
    evt.wait()  # blocking
    print("It's about time")

def main():
    gevent.joinall([
        gevent.spawn(setter),
        gevent.spawn(waiter),
        gevent.spawn(waiter),
        gevent.spawn(waiter),
        gevent.spawn(waiter),
        gevent.spawn(waiter)
    ])

if __name__ == '__main__': 
    main()


# output:

# A: Hey wait for me, I have to do something                                                           
# I'll wait for you                                                                                    
# I'll wait for you                                                                                    
# I'll wait for you                                                                                    
# I'll wait for you                                                                                    
# I'll wait for you                                                                                    
# Ok, I'm done                                                                                         
# It's about time                                                                                      
# It's about time                                                                                      
# It's about time                                                                                      
# It's about time                                                                                      
# It's about time 


# source code
# def set(self):
#         """
#         Set the internal flag to true.
# 
#         All greenlets waiting for it to become true are awakened in
#         some order at some time in the future. Greenlets that call
#         :meth:`wait` once the flag is true will not block at all
#         (until :meth:`clear` is called).
#         """
#         self._flag = True
#         self._check_and_notify()
# 
# def wait(self, timeout=None):
#         """
#         Block until the internal flag is true.
# 
#         If the internal flag is true on entry, return immediately. Otherwise,
#         block until another thread (greenlet) calls :meth:`set` to set the flag to true,
#         or until the optional timeout occurs.
# 
#         When the *timeout* argument is present and not ``None``, it should be a
#         floating point number specifying a timeout for the operation in seconds
#         (or fractions thereof).
# 
#         :return: This method returns true if and only if the internal flag has been set to
#             true, either before the wait call or after the wait starts, so it will
#             always return ``True`` except if a timeout is given and the operation
#             times out.
# 
#         .. versionchanged:: 1.1
#             The return value represents the flag during the elapsed wait, not
#             just after it elapses. This solves a race condition if one greenlet
#             sets and then clears the flag without switching, while other greenlets
#             are waiting. When the waiters wake up, this will return True; previously,
#             they would still wake up, but the return value would be False. This is most
#             noticeable when the *timeout* is present.
#         """
#         return self._wait(timeout)
