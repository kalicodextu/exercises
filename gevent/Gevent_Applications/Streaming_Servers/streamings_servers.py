#!/usr/bin/env python
# -*- coding: utf-8 -*-


from gevent.wsgi import WSGIServer

def application(environ, start_response):
    status = '200 OK'
    body = '<p>Hello World</p>'

    headers = [
        ('Content-Type', 'text/html')
    ]

    start_response(status, headers)
    return [body]

WSGIServer(('', 8000), application).serve_forever()


#  Using pywsgi we can however write our handler as a generator and yield the result chunk by chunk.
#  
#  from gevent.pywsgi import WSGIServer
#  
#  def application(environ, start_response):
#      status = '200 OK'
#  
#      headers = [
#          ('Content-Type', 'text/html')
#      ]
#  
#      start_response(status, headers)
#      yield "<p>Hello"
#      yield "World</p>"
#  
#  WSGIServer(('', 8000), application).serve_forever()
#  
