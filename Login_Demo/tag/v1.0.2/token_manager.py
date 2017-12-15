#!/usr/bin/env python
# -*- coding: utf-8 -*-

import jwt

SECRET = "DAYANGDATA"


class Token(object):
    def __init__(self):
        self.header = {"alg": "HS256", "typ": "JWT"}
        self.alg = "HS256"
        self.secret = SECRET

    def encode_token(self, payload):
        token = jwt.encode(
            payload, self.secret, algorithm=self.alg, headers=self.header)
        return token

    def decode_token(self, token):
        payload = jwt.decode(token, self.secret, self.alg)
        return payload
