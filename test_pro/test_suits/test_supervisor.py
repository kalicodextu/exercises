import requests
import pytest
import json

from time import time
from jwt_base import get_token_payload
from input_base.input_supervisor import *
from input_base.input_test_info import *
from dbdriver import *
from redis import Redis


class TestSupervisorSmsBase(object):
    ''' 2 kinds smscode without auth
            - supervisor reset password
            - supervisor bind mobile
    '''
    def setup_method(self):
        db_redis = Redis(host='localhost', port=6379,db=0)
        interval_cache_key = 'send_interval:' + INFO_SUPERVISOR_MOBILE
        perday_cache_key = 'phone_send_per_day:' + INFO_SUPERVISOR_MOBILE
        bRet1 = db_redis.delete(interval_cache_key)
        bRet2 = db_redis.delete(perday_cache_key)
        return bRet1, bRet2

    @pytest.fixture(scope='class')
    def supervisor_sms_resetpassword(self):
        # supervisor send smscode request for resetpassword
        r = requests.post(SUPERVISOR_SMS_URL,
                json=SUPERVISOR_SMS_VALID_DATA['reset_password'])
        assert r.status_code == 200
        content_dict = json.loads(r.content)
        assert content_dict.has_key('uuid') == True
        uuid = content_dict.get('uuid')
        return uuid

    @pytest.fixture(scope='class')                                
    def supervisor_sms_bindmobile(self):
        # supervisor send smscode request for resetpassword
        r = requests.post(SUPERVISOR_SMS_URL,
                json=SUPERVISOR_SMS_VALID_DATA['bind_mobile'])
        assert r.status_code == 200
        content_dict = json.loads(r.content)
        assert content_dict.has_key('uuid') == True
        uuid = content_dict.get('uuid')
        return uuid


class TestSupervisorSessionBase(object):
    ''' supervisor login throught 2 ways:
            - name, password
            - mobile, password
    '''
    @pytest.fixture(scope='class')
    def supervisor_login_with_name_valid(self):
        r = requests.post(SUPERVISOR_SESSIONS_URL,
                json=SUPERVISOR_SESSIONS_VALID_DATA['name'])
        assert r.status_code == 201 
        content_dict = json.laods(r.content)
        assert content_dict.has_key('token') == True
        assert content_dict.has_key('type') == True
        assert content_dict.has_key('id') == True
        assert content_dict.has_key('name') == True
        login_token = content_dict.get('token')
        supervisor_type = content_dict.get('type')
        supervisor_id = content_dict.get('id')
        supervisor_name = content_dict.get('name')
        return login_token, supervisor_type, supervisor_id, supervisor_name
 
    @pytest.fixture(scope='class')
    def supervisor_login_with_mobile_valid(self):
        r = requests.post(SUPERVISOR_SESSIONS_URL,
                json=SUPERVISOR_SESSIONS_VALID_DATA['mobile'])
        assert r.status_code == 201 
        content_dict = json.laods(r.content)
        assert content_dict.has_key('token') == True
        assert content_dict.has_key('type') == True
        assert content_dict.has_key('id') == True
        assert content_dict.has_key('mobile') == True
        login_token = content_dict.get('token')
        supervisor_type = content_dict.get('type')
        supervisor_id = content_dict.get('id')
        supervisor_mobile = content_dict.get('mobile')
        return login_token, supervisor_type, supervisor_id, supervisor_mobile


class TestSupervisorSupervisorIdSmsBase(TestSupervisorSessionBase):
    ''' 2 kinds smscode with auth
            - change password
            - mobile release
    '''
    def setup_method(self):
        db_redis = Redis(host='localhost', port=6379,db=0)
        interval_cache_key = 'send_interval:' + INFO_SUPERVISOR_MOBILE
        perday_cache_key = 'phone_send_per_day:' + INFO_SUPERVISOR_MOBILE
        bRet1 = db_redis.delete(interval_cache_key)
        bRet2 = db_redis.delete(perday_cache_key)
        return bRet1, bRet2

    @pytest.fixture(scope='class')
    def supervisor_supervisorId_sms_changepassword(
            self, supervisor_login_with_mobile_valid):
        # supervisor send smscode request for changepassword with auth
        login_token, supervisor_type, supervisor_id, supervisor_mobile = supervisor_login_with_mobile_valid
        SUPERVISOR_SUPERVISORID_SMS_URL_TEMP = SUPERVISOR_SUPERVISORID_SMS_URL
        SUPERVISOR_SUPERVISORID_SMS_URL_TEMP = SUPERVISOR_SUPERVISORID_SMS_URL_TEMP.replace('supervisorId', supervisor_id)
        headers = {"authorization": "Bearer " + login_token}
        r = requests.post(
            SUPERVISOR_SUPERVISORID_SMS_URL_TEMP,
            headers=headers,
            json=SUPERVISOR_SUPERVISORID_SMS_VALID_DATA['change_password'])
        assert r.status_code == 200
        content_dict = json.loads(r.content)
        assert content_dict.has_key('id') == True
        _id = content_dict.get('id')
        return _id

    @pytest.fixture(scope='class')
    def supervisor_supervisorId_sms_mobilereleasing(
            self, supervisor_login_with_mobile_valid):
        # supervisor send smscode request for changepassword with auth
        login_token, supervisor_type, supervisor_id, supervisor_mobile = supervisor_login_with_mobile_valid
        SUPERVISOR_SUPERVISORID_SMS_URL_TEMP = SUPERVISOR_SUPERVISORID_SMS_URL
        SUPERVISOR_SUPERVISORID_SMS_URL_TEMP = SUPERVISOR_SUPERVISORID_SMS_URL_TEMP.replace('supervisorId', supervisor_id)
        headers = {"authorization": "Bearer " + login_token}
        r = requests.post(
            SUPERVISOR_SUPERVISORID_SMS_URL_TEMP,
            headers=headers,
            json=SUPERVISOR_SUPERVISORID_SMS_VALID_DATA['mobile_releasing'])
        assert r.status_code == 200
        content_dict = json.loads(r.content)
        assert content_dict.has_key('id') == True
        _id = content_dict.get('id')
        return _id


class TestAuthorizationSupervisor(TestSupervisorSupervisorIdSmsBase):
    ''' re-set a supervisor account(mobile-password) at TestDB, test as flow:
            - reset password
            - supervisor-sessions with mobile (sign-in)
            - change name
            - supervisor-sessions with name
            - release-mobile
            - bind-mobile
            - create-worker
            - maintian-worker
            - change-password
    '''
    def setup_class(cls):
        try:
            print '\nsetup_class:'
            print 'Unset supervisor name...'
            storage_setup = MongoBase()
            storage_setup.switchDatabase('accountManagement')
            storage_setup.conCollection('supervisors')
            query_object = {'mobile': INFO_SUPERVISOR_MOBILE}
            query_key = INFO_SUPERVISOR_NAME
            storage_setup.delField(query_object, query_key)
            print '... ok'
        except:
            print 'unset suporvisor fail, continue ...'
        finally:
            storage_setup.close()

    def teardown_class(cls):
        try:
            print '\nteardown_class:'
            print 'Unset supervisor name...'
            storage_setup = MongoBase()
            storage_setup.switchDatabase('accountManagement')
            storage_setup.conCollection('supervisors')
            query_object = {'mobile': INFO_SUPERVISOR_MOBILE}
            query_key = INFO_SUPERVISOR_NAME
            storage_setup.delField(query_object, query_key)
            print '... ok'
        except:
            print 'unset suporvisor fail, continue ...'
        finally:
            storage_setup.close()

    def test_reset_password(self, supervisor_sms_resetpassword):
        r = requests.post(
                SUPERVISOR_RESETPASSWORD_URL,
                json=SUPERVISOR_RESETPASSWORD_VALID_DATA)
        assert r.status_code == 201
        content_dict = json.loads(r.content)
        assert content_dict.has_key('id') == True
        supervisorId = content_dict.get('id')
        return supervisorId

    def test_login_with_mobile(self, supervisor_login_with_mobile_valid):
        login_token, supervisor_type, supervisor_id, supervisor_mobile = supervisor_login_with_mobile_valid
        assert supervisor_type == GUARDIAN_SESSIONS_OUT_DATA.get('type')
        assert supervisor_mobile == GUARDIAN_SESSIONS_OUT_DATA.get('mobile')
        payload = get_token_payload(login_token)
        assert payload.get('exp') > time()
    
    def test_change_name(self, supervisor_login_with_mobile_valid):
        login_token, supervisor_type, supervisor_id, supervisor_mobile = supervisor_login_with_mobile_valid
        headers = {'authorization': 'Bearer ' + login_token}
        r = requests.post(
                SUPERVISOR_SUPERVISORID_CHANGENAME_URL.replace('supervisorId',
                    supervisor_id),
                headers=headers,
                json=SUPERVISOR_SUPERVISORID_CHANGENAME_VALID_DATA)
        assert r.status_code == 201
        content_dict = json.laods(r.content)
        assert content_dict.has_key('id') == True
        supervisorId = content_dict.get('id')
        return supervisorId

    def test_login_with_name(self, supervisor_login_with_name_valid):
        login_token, supervisor_type, supervisor_id, supervisor_name = supervisor_login_with_name_valid
        assert supervisor_type == GUARDIAN_SESSIONS_OUT_DATA.get('type')
        assert supervisor_name == GUARDIAN_SESSIONS_OUT_DATA.get('name')
        payload = get_token_payload(login_token)
        assert payload.get('exp') > time()
        

    def test_release_mobile(self, supervisor_login_with_mobile_valid,
            guardian_guardianId_sms_mobilereleasing):
        login_token, supervisor_type, supervisor_id, supervisor_mobile = supervisor_login_with_mobile_valid
        headers = {'authorization': 'Bearer ' + login_token}
        r = requests.post(
                SUPERVISOR_SUPERVISORID_MOBILERELEASE_URL.replace('supervisorId',
                    supervisor_id),
                headers=headers,
                json=SUPERVISOR_SUPERVISORID_MOBILERELEASE_VALID_DATA)
        assert r.status_code == 201
        content_dict = json.laods(r.content)
        assert content_dict.has_key('id') == True
        supervisorId = content_dict.get('id')
        return supervisorId

    def test_bind_mobile(self, supervisor_login_with_name_valid,
            guardian_guardianId_sms_mobilereleasing):
        login_token, supervisor_type, supervisor_id, supervisor_name = supervisor_login_with_name_valid
        headers = {'authorization': 'Bearer ' + login_token}
        r = requests.post(
                SUPERVISOR_SUPERVISORID_BINDMOBILE_URL.replace('supervisorId',
                    supervisor_id),
                headers=headers,
                json=SUPERVISOR_SUPERVISORID_BINDINGMOBILE_VALID_DATA)
        assert r.status_code == 201
        content_dict = json.laods(r.content)
        assert content_dict.has_key('id') == True
        supervisorId = content_dict.get('id')
        return supervisorId

    # TODO
    '''
    test_create_worker
    test_maintian_worker
    '''

    def test_change_password(self, supervisor_login_with_mobile_valid,
            supervisor_supervisorId_sms_changepassword):
        login_token, supervisor_type, supervisor_id, supervisor_name = supervisor_login_with_mobile_valid
        headers = {'authorization': 'Bearer ' + login_token}
        r = requests.post(
                SUPERVISOR_SUPERVISORID_CHANGEPASSWORD_URL.replace('supervisorId',
                    supervisor_id),
                headers=headers,
                json=SUPERVISOR_SUPERVISORID_CHANGEPASSWORD_VALID_DATA)
        assert r.status_code == 201
        content_dict = json.laods(r.content)
        assert content_dict.has_key('id') == True
        supervisorId = content_dict.get('id')
        return supervisorId
