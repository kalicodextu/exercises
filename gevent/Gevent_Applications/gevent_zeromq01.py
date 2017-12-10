#!/usr/bin/venv python
# -*- coding:utf-8 -*-

import gevent
import zmq.green as zmq

# Global Context
context = zmq.Context()


def server():
    server_socket = context.socket(zmq.REQ)
    server_socket.bind("tcp://127.0.0.1:5000")

    for request in range(1, 10):
        server_socket.send("Hello")
        print 'Switched to Server for %s' % request
        # Implicit context switch occurs here
        server_socket.recv()


def client():
    client_socket = context.socket(zmq.REP)
    client_socket.connect("tcp://127.0.0.1:5000")

    for request in range(1, 10):

        client_socket.recv()
        print 'Switched to Client for %s' % request
        # Implicit context switch occurs here
        client_socket.send("World")


publisher = gevent.spawn(server)
client = gevent.spawn(client)

gevent.joinall([publisher, client])

# output：

# Switched to Server for 1
# Switched to Client for 1
# Switched to Server for 2
# Switched to Client for 2
# Switched to Server for 3
# Switched to Client for 3
# Switched to Server for 4
# Switched to Client for 4
# Switched to Server for 5
# Switched to Client for 5
# Switched to Server for 6
# Switched to Client for 6
# Switched to Server for 7
# Switched to Client for 7
# Switched to Server for 8
# Switched to Client for 8
# Switched to Server for 9
# Switched to Client for 9
