#!/usr/bin/env python
# -*- coding: utf-8 -*-

import falcon
import manager

api = application = falcon.API()


api.add_route('/signin', manager.sign_in())
api.add_route('/signup', manager.sign_up())
api.add_route('/chpw', manager.ch_pw())
api.add_route('/signout', manager.sign_out())
