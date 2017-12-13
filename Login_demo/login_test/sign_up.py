import falcon
import json
from pymongo import MongoClient
import pprint
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
            "maxProperties":2,
            "minProperties":2,
            "required":['user','password']
        }
        #insert_temp comes from request
        insert_temp=json.load(req.stream)
        #errors to store format errors
        errors=Draft4Validator(schema).iter_errors(insert_temp)
        if next(errors,None) is None:   #"errors" is empty means format is correct
            #print(insert_temp)
            #check if the username has been used!
            if db.user_info.find_one({"user":insert_temp["user"]}) is not None:
                resp_temp={
                    "Sign Up Status":"Fail",
                    "message":"This username has been used"
                }
                resp.body=json.dumps(resp_temp)
                resp.status=falcon.HTTP_400
            else:
                #the username haven't been used
                db.user_info.insert_one(insert_temp)
                resp_temp={
                        "Sign Up Status":"Success",
                        "message":"The account has been created successfully!"
                        }
                resp.body=json.dumps(resp_temp)
                resp.status=falcon.HTTP_200
        else:
            resp_temp={
                    "Sign Up Status":"Failed!",
                    "ErrorType":"Incorrect Input!"
                    }
            resp.body=json.dumps(resp_temp)
            resp.status = falcon.HTTP_400


