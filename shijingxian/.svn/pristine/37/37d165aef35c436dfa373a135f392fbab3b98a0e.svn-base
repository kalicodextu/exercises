from base import Base
import falcon
import json
from jsonschema import Draft4Validator
import jwt


class Login(Base):
    def __init__(self):
        super(Login,self).__init__()

    def on_post(self,req,resp):
        temp=json.load(req.stream)
        errors=Draft4Validator(Base.schema_login).iter_errors(temp)

        if next(errors,None) is None:
            try:
                temp_cmp=Base.db.user_info.find({"user":temp['user']})[0]
            except IndexError:
                resp_temp={
                        "Login Status":"Failed!",
                        "ErrorType":"Invalid username!"
                        }
                resp.body=json.dumps(resp_temp)
                resp.status=falcon.HTTP_400
            else:
                if temp['user'] == temp_cmp['user'] and temp['password'] == temp_cmp['password']:
                    header_temp={"alg":"HS256","typ":"JWT"}
                    secret='123456'
                    token_temp={
                            '_id':str(temp_cmp['_id'])
                            }
                    print(temp_cmp['_id'])
                    token=jwt.encode(token_temp,secret,algorithm='HS256',headers=header_temp)
                    resp_temp={
                            "Login Status":"Successful",
                            "token":token,
                            "Error Type":"None"
                            }
                    resp.body=json.dumps(resp_temp)
                    resp.status=falcon.HTTP_200
                else:
                    resp_temp={
                            "Login Status":"Failed",
                            "Error Type":"Invalid Password!"
                            }
                    resp.body=json.dumps(resp_temp)
                    resp.status=falcon.HTTP_400
        else:
            resp_temp={
                    "Login Status":"Failed",
                    "Error Type":"The Format is Incorrect!"
                    }
            resp.body=json.dumps(resp_temp)
            resp.status=falcon.HTTP_400

