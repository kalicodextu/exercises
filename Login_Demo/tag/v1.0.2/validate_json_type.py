#!/usr/bin/env python
# -*- coding: utf-8 -*-

import falcon
from jsonschema import validate
import json

schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "title": "json schema",
    "description": "account from user's get ot post request",
    "type": "object",
    "properties": {
        "user": {
            "type": "string"
        },
        "password": {
            "type": "string"
        },
    },
    "required": ["user", "password"]
}

schema_mpswd = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "title": "change password json schema",
    "description": "account from user's change password request",
    "type": "object",
    "properties": {
        "password": {
            "type": "string"
        },
    },
    "required": ["password"]
}

def json_validate_type(req_json, bMpsw):
    if not bMpsw:
       try:
           validate(req_json, schema) 
       except:
           msg = "the json type not valid!"
           raise falcon.HTTPBadRequest('Bad request', msg)
       else:
           pass
    else:
        try:
            validate(req_json, schema_mpswd) 
        except:
            msg = "the json type not valid!"
            raise falcon.HTTPBadRequest('Bad request', msg)
        else:
            pass
