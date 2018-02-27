import pytest
import requests

from redis import Redis
from input_base.input_imgcode import *



class TestImgCode(object):
    @pytest.fixture(scope='class')
    def connect_redis_db(self):
        db = Redis(host='localhost', port=6379,db=0)   
        return db 

    @pytest.fixture(scope='class')
    def test_imgcode_signup(self, connect_redis_db):
        image_code = IMAGE_CODE_DATA.get('SIGN_UP')
        r = requests.post(
                IMAGE_CODE_URL,
                json=image_code)
        assert r.status_code == 201
        db = connect_redis_db
        signup_key = image_code.get('uuid') + ':sign_up_verify:'
        assert (signup_key in db.keys()) == True
        return db.get(signup_key) 
    
    @pytest.fixture(scope='class')
    def test_imgcode_signin(self, connect_redis_db):
        image_code = IMAGE_CODE_DATA.get('SIGN_IN')
        r = requests.post(
                IMAGE_CODE_URL,
                json=image_code)
        assert r.status_code == 201
        db = connect_redis_db
        signin_key = image_code.get('uuid') + ':sign_in_verify:'
        assert (signup_key in db.keys()) == True
        return db.get(signin_key) 
    
    @pytest.fixture(scope='class')
    def test_imgcode_release_block_address(self, connect_redis_db):
        image_code = IMAGE_CODE_DATA.get('RELEASE_BLOCK_ADDRESS')
        r = requests.post(
                IMAGE_CODE_URL,
                json=image_code)
        assert r.status_code == 201
        db = connect_redis_db
        release_block_address_key = image_code.get('uuid') + ':release_block_address'
        assert (signup_key in db.keys()) == True
        return db.get(signin_key) 
    
    @pytest.fixture(scope='class')
    def test_imgae_code_vertify(self):
        
