import requests
import pytest
import json
import yaml
import jwt

from time import time
from jwt_base import get_token_payload
from input_base.input_guardian import *
from input_base.input_sms import *
from output_base.output_guardian import *
from dbdriver import *
from test_imgcode import TestImgCode
from redis import Redis


class TestGuardianSmsBase(object):
    '''
        5 kinds smscode without status of login
            - sign up
            - sign in
            - mobile binding
            - forget password
            - wechat binding
    '''
    def setup_method(self):
        db_redis = Redis(host='localhost', port=6379,db=0)
        interval_cache_key = 'send_interval:' + SMS_GUARDIAN_MOBILE
        perday_cache_key = 'phone_send_per_day:' + SMS_GUARDIAN_MOBILE
        bRet1 = db_redis.delete(interval_cache_key)
        bRet2 = db_redis.delete(perday_cache_key)
        return bRet1, bRet2

    @pytest.fixture(scope='class')
    def guardian_sms_signin(self):
        # guardian send smscode request for login with mobile and smscode
        r = requests.post(GUARDIAN_SMS_URL,
                json=GUARDIAN_SMS_VALID_DATA['sign_in'])
        assert r.status_code == 200
        content_dict = json.loads(r.content)
        assert content_dict.has_key('uuid') == True
        uuid = content_dict.get('uuid')
        return uuid

    @pytest.fixture(scope='class')
    def guardian_sms_signup(self):
        # guardian send smscode request for signup
        r = requests.post(GUARDIAN_SMS_URL,
                json=GUARDIAN_SMS_VALID_DATA['sign_up'])
        assert r.status_code == 200
        print r.content
        content_dict = json.loads(r.content)
        assert content_dict.has_key('uuid') == True
        uuid = content_dict.get('uuid')
        return uuid

    @pytest.fixture(scope='class')
    def guardian_sms_forgetpassword(self):
        # guardian send smscode request for resetpassword
        r = requests.post(GUARDIAN_SMS_URL,
                json=GUARDIAN_SMS_VALID_DATA['forget_password'])
        assert r.status_code == 200
        content_dict = json.loads(r.content)
        assert content_dict.has_key("uuid") == True
        uuid = content_dict.get('uuid')
        return uuid

    @pytest.fixture(scope='class')
    def guardian_sms_mobilebinding(self):
        # guardian send smscode request for resetpassword
        r = requests.post(GUARDIAN_SMS_URL,
                json=GUARDIAN_SMS_VALID_DATA['mobile_binding'])
        assert r.status_code == 200
        content_dict = json.loads(r.content)
        assert content_dict.has_key("uuid") == True
        uuid = content_dict.get('uuid')
        return uuid

    @pytest.fixture(scope='class')
    def guardian_sms_wechatbinding(self):
        # guardian send smscode request for resetpassword
        r = requests.post(GUARDIAN_SMS_URL,
                json=GUARDIAN_SMS_VALID_DATA['wechat_binding'])
        assert r.status_code == 200
        content_dict = json.loads(r.content)
        assert content_dict.has_key("uuid") == True
        uuid = content_dict.get('uuid')
        return uuid


class TestGuardianSessionBase(TestGuardianSmsBase):
    ''' guardian login can throught 4 ways:
            - name, password
            - mobile, smsCode
            - mobile, password
            - wechatId
    '''

    @pytest.fixture(scope='class')
    def guardian_login_with_name_valid(self):
        # login with name vliad fixtured method
        r = requests.post(
            GUARDIAN_SESSIONS_URL, json=GUARDIAN_SESSIONS_VALID_DATA['name'])
        assert r.status_code == 201
        content_dict = json.loads(r.content)
        assert content_dict.has_key('token') == True
        assert content_dict.has_key('type') == True
        assert content_dict.has_key('id') == True
        assert content_dict.has_key('name') == True
        login_token = content_dict.get('token')
        guardian_type = content_dict.get('type')
        guardian_id = content_dict.get('id')
        guardian_name = content_dict.get('name')
        return login_token, guardian_type, guardian_id, guardian_name

    @pytest.fixture(scope='class')
    def guardian_login_with_mobile_pswd_valid(self):
        # login with mobile-password vliad fixtured method
        r = requests.post(
            GUARDIAN_SESSIONS_URL,
            json=GUARDIAN_SESSIONS_VALID_DATA['mobile_password'])
        assert r.status_code == 201
        content_dict = json.loads(r.content)
        assert content_dict.has_key('token') == True
        assert content_dict.has_key('type') == True
        assert content_dict.has_key('id') == True
        assert content_dict.has_key('mobile') == True
        login_token = content_dict.get('token')
        guardian_type = content_dict.get('type')
        guardian_id = content_dict.get('id')
        guardian_mobile = content_dict.get('mobile')
        return login_token, guardian_type, guardian_id, guardian_mobile

    @pytest.fixture(scope='class')
    def guardian_login_with_mobile_smscode_valid(self, guardian_sms_signin):
        # login with mobile-smscode vliad fixtured method
        r = requests.post(
            GUARDIAN_SESSIONS_URL,
            json=GUARDIAN_SESSIONS_VALID_DATA['mobile_smscode'])
        assert r.status_code == 201
        content_dict = json.loads(r.content)
        assert content_dict.has_key('token') == True
        assert content_dict.has_key('type') == True
        assert content_dict.has_key('id') == True
        assert content_dict.has_key('mobile') == True
        login_token = content_dict.get('token')
        guardian_type = content_dict.get('type')
        guardian_id = content_dict.get('id')
        guardian_mobile = content_dict.get('mobile')
        return login_token, guardian_type, guardian_id, guardian_mobile

    @pytest.fixture(scope='class')
    def guardian_login_with_wechatid_valid(self):
        #  with wechatid vliad fixtured method
        r = requests.post(
            GUARDIAN_SESSIONS_URL, json=GUARDIAN_SESSIONS_VALID_DATA['wechatId'])
        assert r.status_code == 201
        content_dict = json.loads(r.content)
        assert content_dict.has_key('token') == True
        assert content_dict.has_key('type') == True
        assert content_dict.has_key('id') == True
        assert content_dict.has_key('mobile') == True
        login_token = content_dict.get('token')
        guardian_type = content_dict.get('type')
        guardian_id = content_dict.get('id')
        guardian_mobile = content_dict.get('mobile')
        return login_token, guardian_type, guardian_id, guardian_mobile


    # TODO
    # guardian login test with invalid input data




class TestGuardianGuardianIdSmsBase(TestGuardianSessionBase):
    '''
    2 kinds smscode with status of login
            - change pasword
            - mobile release
    '''
    def setup_method(self):
        db_redis = Redis(host='localhost', port=6379,db=0)
        interval_cache_key = 'send_interval:' + SMS_GUARDIAN_MOBILE
        perday_cache_key = 'phone_send_per_day:' + SMS_GUARDIAN_MOBILE
        bRet1 = db_redis.delete(interval_cache_key)
        bRet2 = db_redis.delete(perday_cache_key)
        return bRet1, bRet2

    @pytest.fixture(scope='class')
    def guardian_guardianId_sms_changepassword(
            self, guardian_login_with_mobile_pswd_valid):
        # guardian send smscode request for changepassword after signin
        login_token, guardian_type, guardian_id, guardian_mobile = guardian_login_with_mobile_pswd_valid
        GUARDIAN_GUARDIANID_SMS_URL_TEMP = GUARDIAN_GUARDIANID_SMS_URL
        GUARDIAN_GUARDIANID_SMS_URL_TEMP = GUARDIAN_GUARDIANID_SMS_URL_TEMP.replace('guardianId', guardian_id)
        headers = {"authorization": "Bearer " + login_token}
        r = requests.post(
            GUARDIAN_GUARDIANID_SMS_URL_TEMP,
            headers=headers,
            json=GUARDIAN_GUARDIANID_SMS_VALID_DATA['change_password'])
        assert r.status_code == 200
        content_dict = json.loads(r.content)
        assert content_dict.has_key('id') == True
        _id = content_dict.get('id')
        return _id

    @pytest.fixture(scope='class')
    def guardian_guardianId_sms_mobilereleasing(
            self, guardian_login_with_mobile_pswd_valid):
        # guardian send smscode request for changepassword after signin
        login_token, guardian_type, guardian_id, guardian_mobile = guardian_login_with_mobile_pswd_valid
        GUARDIAN_GUARDIANID_SMS_URL_TEMP = GUARDIAN_GUARDIANID_SMS_URL
        GUARDIAN_GUARDIANID_SMS_URL_TEMP = GUARDIAN_GUARDIANID_SMS_URL_TEMP.replace('guardianId', guardian_id)
        headers = {"authorization": "Bearer " + login_token}
        r = requests.post(
            GUARDIAN_GUARDIANID_SMS_URL_TEMP,
            headers=headers,
            json=GUARDIAN_GUARDIANID_SMS_VALID_DATA['mobile_releasing'])
        assert r.status_code == 200
        content_dict = json.loads(r.content)
        assert content_dict.has_key('id') == True
        _id = content_dict.get('id')
        return _id


class TestAuthorizationGuadianOne(TestGuardianGuardianIdSmsBase):
    ''' guardian sign-up with mobile, then make serial test flow:
            log-in
            change-name
            change-password
            release-mobile
    '''
    def setup_class(cls):
        try:
            storage_setup = MongoBase()
            storage_setup.switchDatabase('TestDB')
            storage_setup.conCollection('guardian')
            storage_setup.getDocument({'name': 'guardians'})
            storage_setup.getData('input_data')
            signup_data = storage_setup.data['valid'].get('mobile')
            mobile = signup_data.get('mobile')
            query_object = {'mobile': mobile}
            storage_setup.switchDatabase('accountManagement')
            storage_setup.conCollection('guardians')
            storage_setup.delDocument(query_object)
        except:
            print 'The document not exit, cotinue ...'
        finally:
            storage.client.close()

    def teardown_class(cls):
        try:
            storage_setup = MongoBase()
            storage_setup.switchDatabase('TestDB')
            storage_setup.conCollection('guardian')
            storage_setup.getDocument({'name': 'guardians'})
            storage_setup.getData('input_data')
            signup_data = storage_setup.data['valid'].get('mobile')
            mobile = signup_data.get('mobile')
            query_object = {'mobile': mobile}
            storage_setup.switchDatabase('accountManagement')
            storage_setup.conCollection('guardians')
            storage_setup.delDocument(query_object)
        except:
            print 'The document not exit, cotinue ...'
        finally:
            storage.client.close()

    def test_signup_with_mobile(self, guardian_sms_signup):
        r = requests.post(
                GUARDIAN_GUARDIANS_URL,
                json=GUARDIAN_GUARDIANS_VALID_DATA['mobile'])
        assert r.status_code == 201
        content_dict = json.loads(r.content)
        assert content_dict.has_key('id') == True
        guardianId = content_dict.get('id')

    @pytest.fixture(scope='class')
    def test_login_with_mobile_password(self,
            guardian_login_with_mobile_pswd_valid):
        login_token, guardian_type, guardian_id, guardian_mobile = guardian_login_with_mobile_pswd_valid
        # TODO
        # assert return and out
        #
        assert guardian_type == GUARDIAN_SESSIONS_OUT_DATA.get('type')
        assert guardian_mobile == GUARDIAN_SESSIONS_OUT_DATA.get('mobile')
        payload = get_token_payload(login_token)
        assert payload.get('exp') > time()
        return guardian_id, login_token

    def test_change_name(self, test_login_with_mobile_password):
        guardian_id, login_token = test_login_with_mobile_password
        headers = {"authorization": "Bearer " + login_token}
        r = requests.post(
                GUARDIAN_GUARDIANID_CHANGENAME_URL.replace('guardianId',guardian_id),
                headers=headers,
                json=GUARDIAN_GUARDIANID_CHANGENAME_VALID_DATA)
        print r.content
        assert r.status_code == 200
        content_dict = json.loads(r.content)
        assert content_dict.has_key('id') == True
        guardianId = content_dict.get('id')
        assert guardian_id == guardianId
        return guardian_id

    def test_change_password(self, test_login_with_mobile_password,
            guardian_guardianId_sms_changepassword):
        guardian_id, login_token = test_login_with_mobile_password
        headers = {"authorization": "Bearer " + login_token}
        r = requests.post(
                GUARDIAN_GUARDIANID_CHANGEPASSWORD_URL.replace('guardianId',guardian_id),
                headers=headers,
                json=GUARDIAN_GUARDIANID_CHANGEPASSWORD_VALID_DATA['new'])
        print r.content
        assert r.status_code == 200
        content_dict = json.loads(r.content)
        assert content_dict.has_key('id') == True
        guardianId = content_dict.get('id')
        return guardianId


class TestAuthorizationGuadianTwo(TestImgCode, TestGuardianGuardianIdSmsBase):
    ''' guardian sign-up with name, then make serial test flow:
            log-in with name&password
            bind-mobile
            log-in with mobile&password
            log-in with mobile&smscode
            mobile-release
    '''
    def setup_class(cls):
        try:
            storage_setup = MongoBase()
            storage_setup.switchDatabase('TestDB')
            storage_setup.conCollection('guardian')
            storage_setup.getDocument({'name': 'guardians'})
            storage_setup.getData('input_data')
            signup_data = storage_setup.data['valid'].get('name')
            name = signup_data.get('name')
            query_object = {'name': name}
            storage_setup.switchDatabase('accountManagement')
            storage_setup.conCollection('guardians')
            storage_setup.delDocument(query_object)
        except Exception as e:
            print 'The document not exit, cotinue ...'
        finally:
            storage.client.close()

    def teardown_class(cls):
        try:
            storage_setup = MongoBase()
            storage_setup.switchDatabase('TestDB')
            storage_setup.conCollection('guardian')
            storage_setup.getDocument({'name': 'guardians'})
            storage_setup.getData('input_data')
            signup_data = storage_setup.data['valid'].get('name')
            name = signup_data.get('name')
            query_object = {'name': name}
            storage_setup.switchDatabase('accountManagement')
            storage_setup.conCollection('guardians')
            storage_setup.delDocument(query_object)
        except Exception as e:
            print 'The document not exit, cotinue ...'
        finally:
            storage.client.close()

    def test_signup_with_name(self, test_imgcode_signup):
        uuid, imgcode = test_imgcode_signup
        SIGN_UP_DATA = GUARDIAN_GUARDIANS_VALID_DATA['name']
        SIGN_UP_DATA['imgCode'] = imgcode
        r = requests.post(
                GUARDIAN_GUARDIANS_URL,
                json=SIGN_UP_DATA)
        assert r.status_code == 201
        content_dict = json.loads(r.content)
        assert content_dict.has_key('id') == True
        guardianId = content_dict.get('id')

    @pytest.fixture(scope='class')
    def test_login_with_name_password(self,
            guardian_login_with_name_valid):
        login_token, guardian_type, guardian_id, guardian_name = guardian_login_with_name_valid
        # TODO
        # assert return and out
        #
        assert guardian_type == GUARDIAN_SESSIONS_OUT_DATA.get('type')
        assert guardian_name == GUARDIAN_SESSIONS_OUT_DATA.get('name')
        payload = get_token_payload(login_token)
        assert payload.get('exp') > time()
        return guardian_id, login_token

    def test_bind_mobile(self,
            test_login_with_name_password, guardian_sms_mobilebinding):
        guardian_id, login_token = test_login_with_name_password
        headers = {"authorization": "Bearer " + login_token}
        r = requests.post(
                GUARDIAN_GUARDIANID_BINDMOBILE_URL.replace('guardianId',guardian_id),
                headers=headers,
                json=GUARDIAN_GUARDIANID_BINDINGMOBILE_VALID_DATA)
        print r.content
        assert r.status_code == 200
        content_dict = json.loads(r.content)
        assert content_dict.has_key('id') == True
        guardianId = content_dict.get('id')
        assert guardian_id == guardianId
        return guardian_id

    def test_login_with_mobile_password(self,
            guardian_login_with_mobile_pswd_valid):
        login_token, guardian_type, guardian_id, guardian_mobile = guardian_login_with_mobile_pswd_valid
        # TODO
        # assert return and out
        #
        assert guardian_type == GUARDIAN_SESSIONS_OUT_DATA.get('type')
        assert guardian_mobile == GUARDIAN_SESSIONS_OUT_DATA.get('mobile')
        payload = get_token_payload(login_token)
        assert payload.get('exp') > time()
        return guardian_id, login_token

    def test_login_with_mobile_smscode(self, guardian_login_with_mobile_smscode_valid):
        login_token, guardian_type, guardian_id, guardian_mobile = guardian_login_with_mobile_smscode_valid

        # TODO
        # assert return and out
        #
        assert guardian_type == GUARDIAN_SESSIONS_OUT_DATA.get('type')
        assert guardian_mobile == GUARDIAN_SESSIONS_OUT_DATA.get('mobile')
        payload = get_token_payload(login_token)
        assert payload.get('exp') > time()
        return guardian_id, login_token

    def test_release_mobile(self, test_login_with_name_password, guardian_guardianId_sms_mobilereleasing):
        guardian_id, login_token = test_login_with_name_password
        headers = {"authorization": "Bearer " + login_token}
        r = requests.post(
                GUARDIAN_GUARDIANID_MOBILERELEASE_URL.replace('guardianId',guardian_id),
                headers=headers,
                json=GUARDIAN_GUARDIANID_MOBILERELEASE_VALID_DATA)
        assert r.status_code == 200
        content_dict = json.loads(r.content)
        assert content_dict.has_key('id') == True
        guardianId = content_dict.get('id')
        return guardianId

