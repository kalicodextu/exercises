#!/usr/bin/env python
# -*- coding: utf-8 -*-

import falcon
from pymongo import MongoClient
import json


client = MongoClient()
db = client['account']


class sign_up(object):
    def on_post(self, req, resp):
        post_stream = json.load(req.stream)

        # check user exit in db or not
        if db.user_account.find_one({"user": post_stream["user"]}) is not None:
            resp_body = {
                "Signup Status": "Forbiden",
                "message": "The user has been signed!"
            }
            resp.body = json.dumps(resp_body)
            resp.status = falcon.HTTP_403
            print 'The user has been signed.'


        else:
            db.user_account.insert_one(post_stream)
            resp_body = {
                "Signup Status": "Success",
                "message": "The account has been signed successful"
            }
            resp.body = json.dumps(resp_body)
            resp.status = falcon.HTTP_200
            print 'The account has been signed successful.'


class sign_in(object):
    def on_get(self, req, resp):
        get_stream = json.load(req.stream)

        # check user exit in db or not
        if not db.user_account.find_one({
                "user": get_stream["user"],
                "password": get_stream["password"]
        }):
            resp_body = {
                "Signin Status": "Forbiden",
                "message": "user or password is incorrect!"
            }
            resp.body = json.dumps(resp_body)
            resp.status = falcon.HTTP_403
            print "user or password is incorrect!"

        else:
            resp_body = {
                "Signin Status": "Success",
                "message": "Sign in successful"
            }
            resp.body = json.dumps(resp_body)
            resp.status = falcon.HTTP_200
            print "Sign in successful."


class ch_pw(object):
    def on_post(self, req, resp):
        post_stream = json.load(req.stream)

        # check user exit 
        if not db.user_account.find_one({ "user" : post_stream["user"]}):
            resp_body = {
                    "change_password": "Forbidden",
                    "message": "User not exist!"
                    }
            resp.body = json.dumps(resp_body)
            resp.status = falcon.HTTP_403
            print "User not exist!"

        else:
            db.user_account.update_one({"user": post_stream["user"]},
                    {"$set":{"password": post_stream["password"]}})
            resp_body = {
                    "change_password": "Success",
                    "message": "PassWord has been changed."
                    }
            resp.body = json.dumps(resp_body)
            resp.status = falcon.HTTP_200
