#!/usr/bin/venv python
# -*- coding:utf-8 -*-

# telnet_server.py
# On Unix: Access with ``$ nc 127.0.0.1 5000``
# On Window: Access with ``$ telnet 127.0.0.1 5000``

from gevent.server import StreamServer


def handle(socket, address):
    socket.send("Hello from a telnet!\n")
    for i in range(5):
        socket.send(str(i) + '\n')
    socket.close()


server = StreamServer(('0.0.0.0', 5000), handle)
server.serve_forever()

# nc 127.0.0.1 5000

# Hello from a telnet!
# 0
# 1
# 2
# 3
# 4