#!/usr/bin/env python
# -*- coding: utf -8 -*-

import falcon
import msgpack

class Resource(object):
    
    def on_get(self, req, resp):
        resp.body = '{"message": "hello world!"}'
        resp.content_type = 'application/msgpack'
        resp.status = falcon.HTTP_200
 
