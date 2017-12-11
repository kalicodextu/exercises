# Gevent provides two WSGI servers for serving content over HTTP. Henceforth called wsgi and pywsgi:

> gevent.wsgi.WSGIServer
> gevent.pywsgi.WSGIServer

# In earlier versions of gevent before 1.0.x, gevent used libevent instead of libev. Libevent included a fast HTTP server which was used by gevent's wsgi server.

# In gevent 1.0.x there is no http server included. Instead gevent.wsgi is now an alias for the pure Python server in gevent.pywsgi.


可以从源代码种看出其中的关系

# version： gevent1.0.2

# @file： gevent/wsgi.py

'''
from gevent.pywsgi import *
import gevent.pywsgi as _pywsgi
__all__ = _pywsgi.__all__
del _pywsgi
'''
