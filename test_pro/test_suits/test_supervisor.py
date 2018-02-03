import requests
import pytest
import json

from input_base import *


@pytest.fixture(scope='module')
def test_supervisor_session():
    ''' supervisor log-in
        success: status_code 201
        return : token, supervisorId
    '''
    r = requests.post(URL_SUPERVISOR_SESSION, json=DATA_SUPERVISOR_SESSION)
    assert r.status_code == 201
    content_dict = json.loads(r.content)
    assert content_dict.has_key('token') == True
    assert content_dict.has_key('id') == True
    token = content_dict.get('token')
    supervisor_id = content_dict.get('id')
    return token, supervisor_id


class TestSupervisorSms(object):
    @pytest.fixture(scope='function')
    def test_supervisor_resetpassword_sms(self):
        r = requests.post(
            URL_SUPERVISOR_SMS, json=DATA_SUPERVISOR_SMS.get('RESETPASSWORD'))
        assert r.status_code == 200
        content_dict = json.loads(r.content)
        assert content_dict.haskey('uuid') == True
        uuid = content_dict.get('uuid')
        return uuid

    @pytest.fixture(scope='function')
    def test_supervisor_bindmobile_sms(self):
        r = requests.post(
            URL_SUPERVISOR_SMS, json=DATA_SUPERVISOR_SMS.get('BINDMOBILE'))
        assert r.status_code == 200
        content_dict = json.loads(r.content)
        assert content_dict.haskey('uuid') == True
        uuid = content_dict.get('uuid')
        return uuid


class TestSupervisorSupervisirIdSms():
    @pytest.fixture(scope='function')
    def test_supervisor_supervisorid_changepassword_sms(
            self, test_supervisor_session):
        token, supervisor_id = test_supervisor_session
        headers = {'authorization': 'Authorization Bearer' + token}
        r = requests.post(
            URL_SUPERVISOR_SUPERVISORID_SMS,
            headers=headers,
            json=DATA_SUPERVISOR_SUPERVISORID_SMS.get('CHANGEPASSWORD'))
        content_dict = json.loads(r.content)
        assert content_dict.has_key('id') == True
        uuid = content_dict.get('id')
        return token, uuid

    @pytest.fixture(scope='function')
    def test_supervisor_supervisorid_releasemobile_sms(
            self, test_supervisor_session):
        token, supervisor_id = test_supervisor_session
        headers = {'authorization': 'Authorization Bearer' + token}
        r = requests.post(
            URL_SUPERVISOR_SUPERVISORID_SMS,
            headers=headers,
            json=DATA_SUPERVISOR_SUPERVISORID_SMS.get('RELEASEMOBILE'))
        content_dict = json.loads(r.content)
        assert content_dict.has_key('id') == True
        uuid = content_dict.get('id')
        return token, uuid


class TestSupervisorResetpassword(TestSupervisorSms):
    def test_supervisor_resetpassword(self, test_spuervisor_resetpassword_sms):
        sms_uuid = test_supervisor_resetpassword_sms
        r = requests.poast(
            URL_SUPERVISOR_RESETPASSWORD, json=DATA_SUPERVISOR_RESETPASSWORD)
        assert r.status_code == 201
        content_dict = json.loads(r.content)
        assert content_dict.has_key('id') == True
        supervisor_id = content_dict.get('id')
        return supervisor_id


class TestSupervosorBindmobile(TestSupervisorSupervisirIdSms):
    def test_supervisor_supervisorid_bindmobile(
            self, test_supervisor_session, test_supervisor_bindmobile_sms):
        token, supervisor_id = test_supervisor_session
        uuid = test_supervisor_bindmobile_sms
        headers = {'authorization', 'Authorization Bearer' + token}
        r = requests.post(
            URL_SUPERVISOR_SUPERVISORID_BINDMOBILE,
            headers=headers,
            json=DATA_SUPERVISOR_SUPERVISORID_BINDMOBILE)
        assert r.status_code == 201
        content_dict = json.loads(r.content)
        assert content_dict.has_key('id') == True
        supervisor_id = content_dict.get('id')
        return supervisor_id


class TestSupervisorChangepassword(TestSupervisorSupervisirIdSms):
    def test_supervisor_supervisorid_changepassword(
            self, test_supervisor_supervisorid_changepassword_sms):
        token, uuid = test_supervisor_supervisorid_changepassword_sms
        headers = {'authorization', 'Authorization Bearer' + token}
        r = requests.post(
            URL_SUPERVISOR_SUPERVISORID_CHANGEPASSWORD,
            headers=headers,
            json=DATA_SUPERVISOR_SUPERVISORID_CHANGEPASSWORD)
        assert r.status_code == 201
        content_dict = json.loads(r.content)
        assert content_dict.has_key('id')
        supervisor_id = content_dict.get('id')
        return supervisor_id


class TestSUpervisorReleaseMobile(TestSupervisorSupervisirIdSms):
    def test_supervisor_supervisorid_releasemobile(
            self, test_supervisor_supervisorid_releasemobile_sms):
        token, uuid = test_supervisor_supervisorid_releasemobile_sms
        headers = {'authorization', 'Authorization Bearer' + token}
        r = requests.post(
            URL_SUPERVISOR_SUPERVISORID_RELEASEMOBILE,
            headers=headers,
            json=DATA_SUPERVISOR_SUPERVISORID_RELEASEMOBILE)
        assert r.status_code == 201
        content_dict = json.loads(r.content)
        assert content_dict.has_key('id')
        supervisor_id = content_dict.get('id')
        return supervisor_id


class TestSupervisorMaintainwoker():
    def test_supervisor_supervisorid_createworker(self,
                                                  test_supervisor_session):
        token, supervisor_id = test_supervisor_session
        headers = {'authorization', 'Authorization Bearer' + token}
        r = requests.post(
            URL_SUPERVISOR_SUPERVISORID_CREATEWORKER,
            headers=headers,
            json=DATA_SUPERVISOR_SUPERVISORID_CREATEWORKER)
        assert r.status_code == 201
        content_dict = json.loads(r.content)
        assert content_dict.has_key('id')
        worker_id = content_dict.get('id')
        return worker_id

    def test_supervisor_supervisorid_maintainworker(self,
                                                    test_supervisor_session):
        token, supervisor_id = test_supervisor_session
        headers = {'authorization', 'Authorization Bearer' + token}
        r = requests.delete(
            URL_SUPERVISOR_SUPERVISORID_MAINTAINWORKER, headers=headers)
        assert r.status_code == 201
        content_dict = json.loads(r.content)
        assert content_dict.has_key('id')
        worker_id = content_dict.get('id')
        return worker_id
