import socket
import select
print socket.socket
print 'After monkey patch'
from gevent import monkey
monkey.patch_socket()
print socket.socket

print select.select
print 'After monkey patch'
monkey.patch_select()
print select.select


# output:
# class 'socket.socket'
# After monkey patch
# class 'gevent.socket.socket'
# 
# built-in function select
# After monkey patch
# function select at 0x1924de8


#  
#  Python's runtime allows for most objects to be modified at runtime including modules, classes, and even functions. This is generally an astoudingly bad idea since it creates an "implicit side-effect" that is most often extremely difficult to debug if problems occur, nevertheless in extreme situations where a library needs to alter the fundamental behavior of Python itself monkey patches can be used. In this case gevent is capable of patching most of the blocking system calls in the standard library including those in socket, ssl, threading and select modules to instead behave cooperatively.
#  
#  For example, the Redis python bindings normally uses regular tcp sockets to communicate with the redis-server instance. Simply by invoking gevent.monkey.patch_all() we can make the redis bindings schedule requests cooperatively and work with the rest of our gevent stack.
#  
#  This lets us integrate libraries that would not normally work with gevent without ever writing a single line of code. While monkey-patching is still evil, in this case it is a "useful evil".
