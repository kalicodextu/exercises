#!/usr/bin/env python
# -*- coding: utf-8 -*-

import falcon
from pymongo import MongoClient
import json
from pprint import pprint

db = MongoClient().account


class sign_up(object):
    def on_post(self, req, resp):
        post_stream = json.load(req.stream)
        pprint(post_stream)

        # check user exit in db or not
        if db.user_account.find_one({"user": post_stream["user"]}) is not None:
            resp_body = {
                "Signup Status": "Forbiden",
                "message": "The user has been signed!"
            }
            resp.body = json.dumps(resp_body)
            resp.status = falcon.HTTP_403

        else:
            db.user_account.insert_one(post_stream)
            resp_body = {
                "Signup Status": "Success",
                "message": "The account has been signed successful"
            }
            resp.body = json.dumps(resp_body)
            resp.status = falcon.HTTP_200


class sign_in(object):
    def on_post(self, req, resp):
        post_stream = json.load(req.stream)
        pprint(post_stream)

        # check user exit in db or not
        if not db.user_account.find_one({
                "user": post_stream["user"],
                "password": post_stream["password"]
        }):
            resp_body = {
                "Signin Status": "Forbiden",
                "message": "user or password is incorrect!"
            }
            resp.body = json.dumps(resp_body)
            resp.status = falcon.HTTP_403

        else:
            resp_body = {
                "Signin Status": "Success",
                "message": "Sign in successful"
            }
            resp.body = json.dumps(resp_body)
            resp.status = falcon.HTTP_200
