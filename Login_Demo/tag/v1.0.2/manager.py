#!/usr/bin/env python
# -*- coding: utf-8 -*-

import falcon
from pymongo import MongoClient
import json
from token_manager import Token
from validate_json_type import json_validate_type
from bson.objectid import ObjectId

client = MongoClient()
db = client['account']
JW_token = Token()


class sign_up(object):
    def on_post(self, req, resp):
        post_stream = json.load(req.stream)
        try:
            json_validate_type(post_stream, False)
        except:
            resp_body = {
                "Signup Status": "Bad Request",
                "message": "The request type is invalid!"
            }
            resp.body = json.dumps(resp_body)
            resp.status = falcon.HTTP_400
            print 'The request type is invalid!'

        else:
            # check user exit in db or not
            if db.user_account.find_one({
                    "user": post_stream["user"]
            }) is not None:
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
    def on_post(self, req, resp):
        post_stream = json.load(req.stream)

        try:
            json_validate_type(post_stream, False)
        except:
            resp_body = {
                "Signup Status": "Bad Request",
                "message": "The request type is invalid!"
            }
            resp.body = json.dumps(resp_body)
            resp.status = falcon.HTTP_400
            print 'The request type is invalid!'

        else:
            # check user exit in db or not
            user_info = db.user_account.find_one({
                "user":
                post_stream["user"],
                "password":
                post_stream["password"]
            })
            if not user_info:
                resp_body = {
                    "Signin Status": "Forbiden",
                    "message": "user or password is incorrect!"
                }
                resp.body = json.dumps(resp_body)
                resp.status = falcon.HTTP_403
                print "user or password is incorrect!"

            else:
                # create jwt, the payload not use the user and password, just use
                # _id created by MongoDB!
                payload = {"_id": str(user_info["_id"]), "valid": True}
                c_token = JW_token.encode_token(payload)
                resp_body = {
                    "Signin Status": "Success",
                    "token": c_token,
                    "message": "Sign in successful."
                }
                resp.body = json.dumps(resp_body)
                resp.status = falcon.HTTP_200
                print "Sign in successful."


class ch_pw(object):
    def on_post(self, req, resp):
        token = req.auth
        post_stream = json.load(req.stream)
        try:
            json_validate_type(post_stream, True)
        except:
            resp_body = {
                "Change Password": "Bad Request",
                "message": "The request type is invalid!"
            }
            resp.body = json.dumps(resp_body)
            resp.status = falcon.HTTP_400
            print 'The request type is invalid!'
        else:
            # check user exit
            try:
                c_payload = JW_token.decode_token(token)
                if not c_payload["valid"]:
                    resp_body = {
                        "Change Password": "Forbidden",
                        "message": "You should sign in first!"
                    }
                    resp.body = json.dumps(resp_body)
                    resp.status = falcon.HTTP_403
                    print "Not sign in, you should sign in first!"
                else:
                    item = db.user_account.find_one({
                        "_id":
                        ObjectId(c_payload['_id'])
                    })
                    if item is None:
                        resp_body = {
                            "Change Password": "Forbidden",
                            "message": "User's Token invalid, try re-login."
                        }
                        resp.body = json.dumps(resp_body)
                        resp.status = falcon.HTTP_403
                        print "User's token invalid, you can try re-login !"
                    else:
                        db.user_account.update_one(
                            {
                                "_id": ObjectId(c_payload['_id'])
                            }, {
                                "$set": {
                                    "password": post_stream["password"]
                                }
                            })
                        resp_body = {
                        "Change Password": "Success",
                        "message": "Change Password success!",
                        }
                        resp.body = json.dumps(resp_body)
                        resp.status = falcon.HTTP_200
                        print "Change Password success."
            except:
                resp_body = {
                    "Change Password": "Bad Request",
                    "message": "Change Password!"
                }
                resp.body = json.dumps(resp_body)
                resp.status = falcon.HTTP_400
                print "Change Password Fail!"


class sign_out(object):
    def on_get(self, req, resp):
        token = req.auth
        try:
            c_payload = JW_token.decode_token(token)
            if not c_payload["valid"]:
                resp_body = {
                    "Sign out": "Forbidden",
                    "message": "You should sign in first!"
                }
                resp.body = json.dumps(resp_body)
                resp.status = falcon.HTTP_403
                print "Not sign in, you should sign in first!"
            else:
                item = db.user_account.find_one({
                    "_id":
                    ObjectId(c_payload['_id'])
                })
                if item is None:
                    resp_body = {
                        "Sign out": "Forbidden",
                        "message": "User's Token invalid, try re-login."
                    }
                    resp.body = json.dumps(resp_body)
                    resp.status = falcon.HTTP_403
                    print "User's token invalid, you can try re-login !"
                else:
                    # after sign-out, should make the JWT invalid.
                    new_paload = {"_id": c_payload['_id'], "valid": False}
                    print 'encode new token'
                    new_token = JW_token.encode_token(new_paload)
                    print new_token
                    resp_body = {
                        "Sign out": "Success",
                        "message": "Sign out success, update sign out JWT!",
                        "Sign-out_Invalid_Toekn": new_token
                    }
                    resp.body = json.dumps(resp_body)
                    resp.status = falcon.HTTP_200
                    print "Sign out success and update sign out token."

        except:
            resp_body = {
                "Sign out": "Bad Request",
                "message": "Sign out fail!"
            }
            resp.body = json.dumps(resp_body)
            resp.status = falcon.HTTP_400
            print "Sign out fail!"
