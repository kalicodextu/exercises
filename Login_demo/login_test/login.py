import falcon
import json
from pymongo import MongoClient
import pprint
import jwt
from jsonschema import Draft4Validator

db=MongoClient().account

class Resource(object):
    def on_post(self, req, resp):
        #schema to check the json format
        schema={
            "type":"object",
            "properties":{
                "user":{"type":"string"},
                "password":{"type":"string"},
                },
            "minProperties":2,
            "maxProperties":2,
            "required":['user','password']
        }

        #temp comes from the request
        temp=json.load(req.stream)
        #check json format and store errors in variable:"errors"
        errors=Draft4Validator(schema).iter_errors(temp)

        if next(errors,None) is None:  #"errors" is empty means the format is correct
            #jwt header
            header_temp={"alg":"HS256","typ":"JWT"}
            #jwt secret
            secret='123456'
            try:
                #temp_cmp comes from the database
                temp_cmp=db.user_info.find({"user":temp["user"]})[0]
            except Exception:
                response_temp={
                    "Login Status":"Failed!",
                    "ErrorType":"Invalid username!"
                }
                resp.body=json.dumps(response_temp)
                resp.status = falcon.HTTP_400
            else:
                if temp['user']==temp_cmp['user']\
                        and temp['password']==temp_cmp['password']:
                    token=jwt.encode(temp, secret, algorithm='HS256', headers=header_temp)
                    #print(token)
                    response_temp={
                        "Login Status":"Successful",
                        "Token":token,
                        "ErrorType":"None"
                    }
                    resp.body=json.dumps(response_temp)
                    resp.status = falcon.HTTP_200
                elif temp['user']==temp_cmp['user']\
                        and temp['password']!=temp_cmp['password']:
                    response_temp={
                        "Login Status":"Failed!",
                        "ErrorType":"Invalid password!"
                    }
                    resp.body=json.dumps(response_temp)
                    resp.status = falcon.HTTP_400


        else:
            response_temp={
                "Login Status":"Failed!",
                "ErrorType":"Incorrect Input!"
            }
            resp.body=json.dumps(response_temp)
            resp.status = falcon.HTTP_400
