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
        image_code = IMGCODE_VALID_DATA.get('sign_up')
        uuid = image_code.get('uuid')
        r = requests.post(
                IMGCODE_URL,
                json=image_code)
        assert r.status_code == 200
        db = connect_redis_db
        signup_key = uuid + ':sign_up_verify:'
        assert (signup_key in db.keys()) == True
        return uuid, db.get(signup_key)

    @pytest.fixture(scope='class')
    def test_imgcode_signin(self, connect_redis_db):
        image_code = IMGCODE_VALID_DATA.get('sign_in')
        uuid = image_code.get('uuid')
        r = requests.post(
                IMGCODE_URL,
                json=image_code)
        assert r.status_code == 200
        db = connect_redis_db
        signin_key = uuid + ':sign_in_verify:'
        assert (signup_key in db.keys()) == True
        return uuid, db.get(signin_key)

    @pytest.fixture(scope='class')
    def test_imgcode_release_block_address(self, connect_redis_db):
        image_code = IMGCODE_VALID_DATA.get('RELEASE_BLOCK_ADDRESS')
        uuid = image_code.get('uuid')
        r = requests.post(
                IMGCODE_URL,
                json=image_code)
        assert r.status_code == 200
        db = connect_redis_db
        release_block_address_key = uuid + ':release_block_address'
        assert (signup_key in db.keys()) == True
        return uuid, db.get(signin_key)

    @pytest.fixture(scope='class')
    def test_imgae_code_vertify(self, test_imgcode_release_block_address):
        uuid, image_code = test_imgcode_release_block_address
        vertify_data = IMGCODE_UUID_VALID_DATA
        vertify_data['imgCode'] = image_code
        IMGCODE_UUID_URL = IMGCODE_UUID_URL.replace('uuid', uuid)
        r = requests.post(
                IMGCODE_UUID_URL,
                json=vertify_data)
        assert r.status_code == 201
        content_dict = json.loads(r.content)
        assert content_dict.has_key('id') == True
        _id = content_dict.get('id')
        assert uuid == _id

