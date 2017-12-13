import json
from pymongo import MongoClient


class Base(object):
    def __init__(self):
        pass
    db=MongoClient('localhost',27017).account

    schema_login={
            "type":"object",
            "properties":{
                "user":{"type":"string"},
                "password":{"type":"string"},
                },
            "minProperties":2,
            "maxProperties":2,
            "required":['user','password']
            }

    schema_sign_up={
            "type":"object",
            "properties":{
                "user":{"type":"string"},
                "password":{"type":"string"},
                },
            "minProperties":2,
            "maxProperties":2,
            "required":['user','password']
            }

    schema_psw_edit={
            "type":"object",
            "properties":{
                "password":{"type":"string"},
                },
            "minProperties":1,
            "maxProperties":1,
            "required":['password']
            }




