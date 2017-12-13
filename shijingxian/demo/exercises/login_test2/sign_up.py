from base import Base
from jsonschema import Draft4Validator
import json
import falcon


class Sign_up(Base):
    def __init__(self):
        super(Sign_up,self).__init__()

    def on_post(self,req,resp):
        insert_temp=json.load(req.stream)
        errors=Draft4Validator(Base.schema_sign_up).iter_errors(insert_temp)
        if next(errors,None) is None:
            if Base.db.user_info.find_one({'user':insert_temp['user']}) is not None:
                resp_temp={
                        "Sign Up Status":"Failed",
                        "Message":"This Username has been used!"
                        }
                resp.body=json.dumps(resp_temp)
                resp.status=falcon.HTTP_400
            else:
                Base.db.user_info.insert_one(insert_temp)
                resp_temp={
                        "Sign Up Status":"Success",
                        "Message":"The account has been created successfully!"
                        }
                resp.body=json.dumps(resp_temp)
                resp.status=falcon.HTTP_200
        else:
            resp_temp={
                    "Sign Up Status":"Failed",
                    "Error Type":"The Format is Incorrect!"
                    }
            resp.body=json.dumps(resp_temp)
            resp.status=falcon.HTTP_400

