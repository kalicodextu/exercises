import falcon
import json
from pymongo import MongoClient
import jwt
from jsonschema import Draft4Validator


db=MongoClient('localhost',27017).account

class Resource(object):
    def on_post(self,req,resp):
        #schema for format judgement
        schema={
                "type":"object",
                "properties":{
                    "user":{"type":"string"},
                    "password":{"type":"string"},
                    },
                "required":['password'],
                "minProperties":2,
                "maxProperties":2,
        }
        #get token from header
        autho_temp = req.auth.split(' ')
        token=autho_temp[1]
        #edit_temp comes from request
        edit_temp=json.load(req.stream)
        #errors to store the format errors
        errors=Draft4Validator(schema).iter_errors(edit_temp)
        if next(errors,None) is None:  #if the "errors" is empty
            try:
                #fetch the item from database
                temp_cmp=db.user_info.find({'user':edit_temp['user']})[0]
                #payload validate
                payload=jwt.decode(token,'123456',algorithm='HS256')
                #check validation
                if payload['user']==edit_temp['user']==temp_cmp['user']\
                        and payload['password']==temp_cmp['password']:
                    #validation passed and update the password
                    db.user_info.find_one_and_update(
                        {"user":edit_temp["user"]},
                        {'$set':{'password':edit_temp['password']}}
                    )
                    resp_temp={
                        "Edit Status":"Success",
                        "Error Type":"None"
                    }
                    resp.body=json.dumps(resp_temp)
                    resp.status=falcon.HTTP_200
                else:
                    #wrong token details
                    resp_temp={
                        "Edit Status":"Failed",
                        "Error Type":"Signature verification failed"
                    }
                    resp.body=json.dumps(resp_temp)
                    resp.status=falcon.HTTP_400
            #can't find that username in database
            except IndexError:
                    resp_temp={
                        "Edit Status":"Failed",
                        "Error Type":"Invalid Username!"
                    }
                    resp.body=json.dumps(resp_temp)
                    resp.status=falcon.HTTP_400
            #token signature verification failed
            except jwt.DecodeError:
                resp_temp={
                    "Edit Status":"Failed",
                    "Error Type":"Signature verification failed!"
                }
                resp.body=json.dumps(resp_temp)
                resp.status=falcon.HTTP_400

        else:
            resp_temp={
                "Password Edit Status":"Failed!",
                "ErrorType":"The Format is Incorrect!"
            }
            resp.body=json.dumps(resp_temp)
            resp.status = falcon.HTTP_400
