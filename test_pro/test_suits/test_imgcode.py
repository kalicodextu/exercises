import pytest
import requests

from redis import Redis
from input_base.input_imgcode import *



class TestImgCode(object):
    @pytest.fixture(scope='class')
    def test_imgcode_signup(self):
        r = requests.post(
                IMAGE_CODE_URL,
                json=IMAGE_CODE_DATA)
        assert r.status_code == 201
        db = Redis(host='localhost', port=6379,db=0)   
        signup_key = IMAGE_CODE_DATA.get('uuid') + ':sign_up_verify:'
        assert (signup_key in db.keys()) == True
        return db.get(signup_key) 
