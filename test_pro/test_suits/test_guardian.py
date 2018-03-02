import requests
import pytest
import json
import yaml
import jwt

from time import time
from jwt_base import get_token_payload
from input_base.input_guardian import *
from output_base.output_guardian import *
from dbdriver import *


@pytest.fixture(scope='class')
def setUpBeforeClass(query_object):
    try:
        storage = MongoBase()
        storage.conCollection('TestDB')
        storage.delDocument(query_object)
    except:
        print 'The document not exit, cotinue ...'
    finally:
        storage.client.close()

@pytest.fixture(scope='class')
def tearDownAfterClass():
    # TODO
    # teardown func
    pass


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



class TestGuardianSmsBase(object):
    '''
        5 kinds smscode without status of login
            - sign up
            - sign in
            - mobile binding
            - forget password
            - wechat binding
    '''
    @pytest.fixture(scope='class')
    def guardian_sms_signin(self):
        # guardian send smscode request for login with mobile and smscode
        r = requests.post(GUARDIAN_SMS_URL,
                json=GUARDIAN_SMS_VALID_DATA['sign_in'])
        assert r.status_code == 201
        content_dict = json.loads(r.content)
        assert content_dict.has_key('uuid') == True
        uuid = content_dict.get('uuid')
        return uuid

    @pytest.fixture(scope='class')
    def guardian_sms_signup(self):
        # guardian send smscode request for signup
        r = requests.post(GUARDIAN_SMS_URL,
                json=GUARDIAN_SMS_VALID_DATA['sign_up'])
        assert r.status_code == 201
        content_dict = json.loads(r.content)
        assert content_dict.has_key('id') == True
        uuid = content_dict.get('uuid')
        return uuid

    @pytest.fixture(scope='class')
    def guardian_sms_forgetpassword(self):
        # guardian send smscode request for resetpassword
        r = requests.post(GUARDIAN_SMS_URL,
                json=GUARDIAN_SMS_VALID_DATA['forget_password'])
        assert r.status_code == 201
        content_dict = json.loads(r.content)
        assert content_dict.has_key("uuid") == True
        uuid = content_dict.get('uuid')
        return uuid

    @pytest.fixture(scope='class')
    def guardian_sms_mobilebinding(self):
        # guardian send smscode request for resetpassword
        r = requests.post(GUARDIAN_SMS_URL,
                json=GUARDIAN_SMS_VALID_DATA['mobile_binding'])
        assert r.status_code == 201
        content_dict = json.loads(r.content)
        assert content_dict.has_key("uuid") == True
        uuid = content_dict.get('uuid')
        return uuid

    @pytest.fixture(scope='class')
    def guardian_sms_wechatbinding(self):
        # guardian send smscode request for resetpassword
        r = requests.post(GUARDIAN_SMS_URL,
                json=GUARDIAN_SMS_VALID_DATA['wechat_binding'])
        assert r.status_code == 201
        content_dict = json.loads(r.content)
        assert content_dict.has_key("uuid") == True
        uuid = content_dict.get('uuid')
        return uuid


class TestGuardianGuardianIdSmsBase(TestGuardianSessionBase):
    '''
    2 kinds smscode with status of login 
            - change pasword
            - mobile release
    '''
    @pytest.fixture(scope='class')
    def guardian_guardianId_sms_changepassword(
            self, guardian_login_with_mobile_pswd_valid):
        # guardian send smscode request for changepassword after signin
        login_token, guardian_type, guardian_id, guardian_mobile = guardian_login_with_mobile_pswd_valid
        headers = {"authorization": "Bearer " + login_token}
        r = requests.post(
            GUARDIAN_GUARDIANID_SMS_URL,
            headers=headers,
            json=GUARDIAN_GUARDIANID_SMS_VALID_DATA['change_password'])
        assert r.status_code == 201
        content_dict = json.loads(r.content)
        assert content_dict.has_key('uuid') == True
        uuid = content_dict.get('uuid')
        return uuid

    @pytest.fixture(scope='class')
    def guardian_guardianId_sms_mobilereleasing(
            self, guardian_login_with_mobile_pswd_valid):
        # guardian send smscode request for changepassword after signin
        login_token, guardian_type, guardian_id, guardian_mobile = guardian_login_with_mobile_pswd_valid
        headers = {"authorization": "Bearer " + login_token}
        r = requests.post(
            GUARDIAN_GUARDIANID_SMS_URL,
            headers=headers,
            json=GUARDIAN_GUARDIANID_SMS_VALID_DATA['mobile_releasing'])
        assert r.status_code == 201
        content_dict = json.loads(r.content)
        assert content_dict.has_key('uuid') == True
        uuid = content_dict.get('uuid')
        return uuid


class TestAuthorizationGuadianOne(TestGuardianSmsBase, TestGuardianSessionBase):
    ''' guardian sign-up with mobile, then make serial test flow:
            log-in
            change-name
            change-password
            release-mobile
    '''
    def setup_class(query_object):
        try:
            storage = MongoBase()
            storage.conCollection('TestDB')
            storage.delDocument(query_object)
            print 'clear old document .... ok'
        except:
            print 'The document not exit, cotinue ...'
        finally:
            storage.client.close()

    def test_signup_with_mobile(self, guardian_sms_signup):
        r = requests.post(
                GUARDIAN_GUARDIANS_URL,
                json=GUARDIAN_GUARDIANS_VALID_DATA['sign_up'])
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
        '''
        assert guardian_mobile == OUTPUT_GUARDIAN_SESSIONS_MOBILE_PSWD_VALID_DATA.get(
            'mobile')
        assert guardian_type == OUTPUT_GUARDIAN_SESSIONS_MOBILE_PSWD_VALID_DATA.get(
            'type')
        assert guardian_id == OUTPUT_GUARDIAN_SESSIONS_MOBILE_PSWD_VALID_DATA.get(
            'id')
        '''
        payload = get_token_payload(login_token)
        assert payload.get('exp') > time()
        return guardian_id, login_token

    def test_change_name(self, test_login_with_mobile_password):
        guardian_id, login_token = test_login_with_mobile_password
        headers = {"authorization": "Bearer " + login_token}
        r = requests.post(
                GUARDIAN_GUARDIANID_CHANGENAME_URL.replace('guardianId',guardian_id),
                headers=headers,
                json=GUARDIAN_GUARDIANID_CHANGENAME_VALID_DATA['new_name'])
        assert r.status_code == 201
        content_dict = json.loads(r.content)
        assert content_dict.has_key('id') == True
        guardianId = content_dict.get('id')
        assert guardian_id == guardianId
        return guardian_id

    def test_change_password(self, test_login_with_mobile_password):
        guardian_id, login_token = test_login_with_mobile_password
        headers = {"authorization": "Bearer " + login_token}
        r = requests.post(
                GUARDIAN_GUARDIANID_CHANGEPASSWORD_URL.replace('guardianId',guardian_id),
                headers=headers,
                json=GUARDIAN_GUARDIANID_CHANGEPASSWORD_VALID_DATAL['new_name'])
        assert r.status_code == 201
        content_dict = json.loads(r.content)
        assert content_dict.has_key('id') == True
        guardianId = content_dict.get('id')
        return guardianId

    def test_release_mobile(self, test_login_with_mobile_password):
        guardian_id, login_token = test_login_with_mobile_password
        headers = {"authorization": "Bearer " + login_token}
        r = requests.post(
                GUARDIAN_GUARDIANID_CHANGEPASSWORD_URL.replace('guardianId',guardian_id),
                headers=headers,
                json=GUARDIAN_GUARDIANID_CHANGEPASSWORD_VALID_DATAL['new_name'])
        assert r.status_code == 201
        content_dict = json.loads(r.content)
        assert content_dict.has_key('id') == True
        guardianId = content_dict.get('id')
        return guardianId

'''
class TestGuardianSession(TestGuardianSessionBase):
    def test_login_with_name(self, guardian_login_with_name_valid):
        login_token, guardian_type, guardian_id, guardian_name = guardian_login_with_name_valid
        assert guardian_name == OUTPUT_GUARDIAN_SESSIONS_NAME_VALID_DATA.get(
            'name')
        assert guardian_type == OUTPUT_GUARDIAN_SESSIONS_NAME_VALID_DATA.get(
            'type')
        assert guardian_id == OUTPUT_GUARDIAN_SESSIONS_NAME_VALID_DATA.get(
            'id')
        payload = get_token_payload(login_token)
        assert payload.get('exp') > time()

    def test_login_with_mobile_pswd(self,
                                    guardian_login_with_mobile_pswd_valid):
        login_token, guardian_type, guardian_id, guardian_mobile = guardian_login_with_mobile_pswd_valid
        assert guardian_mobile == OUTPUT_GUARDIAN_SESSIONS_MOBILE_PSWD_VALID_DATA.get(
            'mobile')
        assert guardian_type == OUTPUT_GUARDIAN_SESSIONS_MOBILE_PSWD_VALID_DATA.get(
            'type')
        assert guardian_id == OUTPUT_GUARDIAN_SESSIONS_MOBILE_PSWD_VALID_DATA.get(
            'id')
        payload = get_token_payload(login_token)
        assert payload.get('exp') > time()

    def test_login_with_mobile_smscode(
            self, guardian_login_with_mobile_smscode_valid):
        login_token, guardian_type, guardian_id, guardian_mobile = guardian_login_with_mobile_pswd_valid
        assert guardian_mobile == OUTPUT_GUARDIAN_SESSIONS_MOBILE_SMSCODE_VALID_DATA.get(
            'mobile')
        assert guardian_type == OUTPUT_GUARDIAN_SESSIONS_MOBILE_SMSCODE_VALID_DATA.get(
            'type')
        assert guardian_id == OUTPUT_GUARDIAN_SESSIONS_MOBILE_SMSCODE_VALID_DATA.get(
            'id')
        payload = get_token_payload(login_token)
        assert payload.get('exp') > time()

    """
    def test_login_with_wechatid(self,
            guardian_login_with_wechatid_valid):
        login_token, guardian_type, guardian_id, guardian_mobile = guardian_login_with_mobile_pswd_valid
        assert guardian_mobile == OUTPUT_GUARDIAN_SESSIONS_WECHATID_VALID_DATA.get('mobile') 
        assert guardian_type == OUTPUT_GUARDIAN_SESSIONS_WECHATID_VALID_DATA.get('type') 
        assert guardian_id == OUTPUT_GUARDIAN_SESSIONS_WECHATID_VALID_DATA.get('id') 
        payload = get_token_payload(login_token)
        assert payload.get('exp') > time()
    """
'''

class TestGuardianOne(TestGuardianSmsBase, TestGuardianSessionBase,
        TestGuardianGuardianIdSmsBase):
    """ class TestGuardianOne
            guardian function test with sign-up use name and password
    """  
    
        
