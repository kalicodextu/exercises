import yaml

from json import load, dump
from dbdriver import *

TOKEN_KEY = None
TOKEN_ALG = None

with open('./data/token/test.conf', 'r') as fp:
    config = yaml.load(fp)

TOKEN_KEY = config.get('encryption').get('key')
TOKEN_ALG = config.get('encryption').get('algorithm')


AUTH_HOST = 'http://localhost:20001'
GATEWAY_HOST = 'http://localhost:10000'


storage = MongoBase()
storage.switchDatabase('TestDB')
storage.conCollection('supervisor')

# Authorization

# supervisor-sessions
storage.getDocument({'name': 'supervisor-sessions'})
storage.getData('url')
SUPERVISOR_SESSIONS_URL = AUTH_HOST + storage.data

storage.getData('input_data')
SUPERVISOR_SESSIONS_VALID_DATA = storage.data['valid']
storage.getData('output_data')
SUPERVISOR_SESSIONS_OUT_DATA = storage.data


# supervisors-sms
storage.getDocument({'name': 'supervisors-sms'})
storage.getData('url')
SUPERVISOR_SMS_URL = AUTH_HOST + storage.data

storage.getData('input_data')
SUPERVISOR_SMS_VALID_DATA = storage.data['valid']
storage.getData('output_data')
SUPERVISOR_SMS_OUT_DATA = storage.data


# supervisor-reset-password
storage.getDocument({'name': 'supervisors-reset-password'})
storage.getData('url')
SUPERVISOR_RESETPASSWORD_URL = AUTH_HOST + storage.data

storage.getData('input_data')
SUPERVISOR_RESETPASSWORD_VALID_DATA = storage.data['valid']
storage.getData('output_data')
SUPERVISOR_RESETPASSWORD_OUT_DATA = storage.data


# supervisor-bind-mobile(supervisorId)
storage.getDocument({'name': 'supervisors-bind-mobile'})
storage.getData('url')
SUPERVISOR_SUPERVISORID_BINDMOBILE_URL = AUTH_HOST + storage.data

storage.getData('input_data')
SUPERVISOR_SUPERVISORID_BINDINGMOBILE_VALID_DATA = storage.data['valid']
storage.getData('output_data')
SUPERVISOR_SUPERVISORID_BINDINGMOBILE_OUT_DATA = storage.data


# supervisor-change-name(supervisorId)
storage.getDocument({'name': 'supervisors-change-name'})
storage.getData('url')
SUPERVISOR_SUPERVISORID_CHANGENAME_URL = AUTH_HOST + storage.data

storage.getData('input_data')
SUPERVISOR_SUPERVISORID_CHANGENAME_VALID_DATA = storage.data['valid']
storage.getData('output_data')
SUPERVISOR_SUPERVISORID_CHANGENAME_OUT_DATA = storage.data


# supervisor-sms(supervisorId)
storage.getDocument({'name': 'supervisors-supervisorId-sms'})
storage.getData('url')
SUPERVISOR_SUPERVISORID_SMS_URL = AUTH_HOST + storage.data

storage.getData('input_data')
SUPERVISOR_SUPERVISORID_SMS_VALID_DATA = storage.data['valid']
storage.getData('output_data')
SUPERVISOR_SUPERVISORID_SMS_OUT_DATA = storage.data


# supervisor-change-password(supervisorId)
storage.getDocument({'name': 'supervisors-change-password'})
storage.getData('url')
SUPERVISOR_SUPERVISORID_CHANGEPASSWORD_URL = AUTH_HOST + storage.data

storage.getData('input_data')
SUPERVISOR_SUPERVISORID_CHANGEPASSWORD_VALID_DATA = storage.data['valid']
storage.getData('output_data')
SUPERVISOR_SUPERVISORID_CHANGEPASSWORD_OUT_DATA = storage.data


# supervisor-release-mobile(supervisorId)
storage.getDocument({'name': 'supervisors-release-mobile'})
storage.getData('url')
SUPERVISOR_SUPERVISORID_MOBILERELEASE_URL = AUTH_HOST + storage.data

storage.getData('input_data')
SUPERVISOR_SUPERVISORID_MOBILERELEASE_VALID_DATA = storage.data['valid']
storage.getData('output_data')
SUPERVISOR_SUPERVISORID_MOBILERELEASE_OUT_DATA = storage.data


# supervisor-create-worker(supervisorId)
storage.getDocument({'name': 'supervisors-create-worker'})
storage.getData('url')
SUPERVISOR_SUPERVISORID_CREATEWORKER_URL = AUTH_HOST + storage.data

storage.getData('input_data')
SUPERVISOR_SUPERVISORID_CREATEWORKER_VALID_DATA = storage.data['valid']
storage.getData('output_data')
SUPERVISOR_SUPERVISORID_CREATEWORKER_OUT_DATA = storage.data


# supervisor-maintian-worker(supervisorId)
storage.getDocument({'name': 'supervisors-maintain-worker'})
storage.getData('url')
SUPERVISOR_SUPERVISORID_MAINTAINWORKER_URL = AUTH_HOST + storage.data

storage.getData('input_data')
SUPERVISOR_SUPERVISORID_MAINTAINWORKER_VALID_DATA = storage.data['valid']
storage.getData('output_data')
SUPERVISOR_SUPERVISORID_MAINTAINWORKER_OUT_DATA = storage.data


# Gateway

# maintain-workers (get workers info)
storage.getDocument({'name': 'gateway-maintain-workers'})
storage.getData('url')
GATEWAY_SUPERVISOR_MAINTAINWORKER_URL = GATEWAY_HOST + storage.data

storage.getData('input_data')
GATEWAY_SUPERVISOR_MAINTAINWORKER_VALID_DATA = storage.data['valid']
storage.getData('output_data')
GATEWAY_SUPERVISOR_MAINTAINWORKER_OUT_DATA = storage.data

# supervisor-worker-permissoion
storage.getDocument({'name': 'geteway-worker-permission'})
storage.getData('url')
GETEWAY_SUPERVISOR_WORKERPERMISSION_URL = GATEWAY_HOST + storage.data

storage.getData('input_data')
GATEWAY_SUPERVISOR_WORKERPERMISSION_VALID_DATA = storage.data['valid']
storage.getData('output_data')
GATEWAY_SUPERVISOR_WORKERPERMISSION_OUT_DATA = storage.data

# worker-permissoion-workerId
supervisor-storage.getDocument({'name': 'geteway-worker-permission'})
storage.getData('url')
GETEWAY_SUPERVISOR_WORKERPERMISSION_WORKERID_URL = GATEWAY_HOST + storage.data
storage.getData('input_data')
GATEWAY_SUPERVISOR_WORKERPERMISSION_WORKERID_VALID_DATA = storage.data['valid']
storage.getData('output_data')
GATEWAY_SUPERVISOR_WORKERPERMISSION_WORKERID_OUT_DATA = storage.data
