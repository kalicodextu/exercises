#!/usr/bin/env python
# -*- coding: utf-8 -*-

from wsgiref.simple_server import make_server
from app import api


httpd = make_server('', 8000, api)
print "Serving HTTP on port 8000..."
httpd.serve_forever()
