from bson.objectid import ObjectId
from base import Base
import json
import falcon
import jwt
from jsonschema import Draft4Validator


class Psw_edit(Base):
    def __init__(self):
        super(Psw_edit,self).__init__()

    def on_post(self,req,resp):
        autho_temp=req.auth.split(' ')
        token=autho_temp[1]
        edit_temp=json.load(req.stream)
        errors=Draft4Validator(Base.schema_psw_edit).iter_errors(edit_temp)

        if next(errors,None) is None:
            try:
                payload=jwt.decode(token,'123456',algorithm='HS256')
                print(payload['_id'])
                temp_cmp=Base.db.user_info.find({'_id':ObjectId(payload['_id'])})[0]
                print(payload)
                Base.db.user_info.find_one_and_update(
                        {'_id':ObjectId(payload['_id'])},
                        {'$set':{'password':edit_temp['password']}}
                        )
                resp_temp={
                        "Edit Status":"Success",
                        "Error Type":"None"
                        }
                resp.body=json.dumps(resp_temp)
                resp.status=falcon.HTTP_200
            except jwt.DecodeError:
                resp_temp={
                        "Edit Status":"Failed",
                        "Error Type":"Signature verification failed!"
                        }
                resp.body=json.dumps(resp_temp)
                resp.status=falcon.HTTP_400
        else:
            resp_temp={
                    "Edit Status":"Failed",
                    "Error Type":"The Format is Incorrect!"
                    }
            resp.body=json.dumps(resp_temp)
            resp.status=falcon.HTTP_400
