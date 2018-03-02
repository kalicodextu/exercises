import yaml

from json import load, dump
from dbdriver import *

TOKEN_KEY = None
TOKEN_ALG = None

with open('./data/token/test.conf', 'r') as fp:
    config = yaml.load(fp)

TOKEN_KEY = config.get('encryption').get('key')
TOKEN_ALG = config.get('encryption').get('algorithm')


HOST = 'http://localhost:20001'
GUARDIANID = '596746f4a97daa4f26fba35d'


storage = MongoBase()
storage.conCollection('guardian')


# create-guardian
storage.getDocument({'name': 'guardians'})
storage.getData('url')
GUARDIAN_GUARDIANS_URL = HOST + storage.data

storage.getData('input_data')
GUARDIAN_GUARDIANS_VALID_DATA = storage.data['valid']


# guardian-login
storage.getDocument({'name': 'guardian-session'})
storage.getData('url')
GUARDIAN_SESSIONS_URL = HOST + storage.data

storage.getData('input_data')
GUARDIAN_SESSIONS_VALID_DATA = storage.data['valid']


# guardian-patch-wechat
storage.getDocument({'name': 'guardians-patch-wechat-id'})
storage.getData('url')
GUARDIAN_PATCH_WECHAT_URL = HOST + storage.data

storage.getData('input_data')
GUARDIAN_PATCH_WECHAT_VALID_DATA = storage.data['valid']


# guardian-sms
storage.getDocument({'name': 'guardians-sms'})
storage.getData('url')
GUARDIAN_SMS_URL = HOST + storage.data

storage.getData('input_data')
GUARDIAN_SMS_VALID_DATA = storage.data['valid']

# guardian-reset-password
storage.getDocument({'name': 'guardians-reset-password'})
storage.getData('url')
GUARDIAN_RESETPASSWORD_URL = HOST + storage.data

storage.getData('input_data')
GUARDIAN_RESETPASSWORD_VALID_DATA = storage.data['valid']


# guardian-bind-mobile(guardianId)
storage.getDocument({'name': 'guardians-bind-mobile'})
storage.getData('url')
GUARDIAN_GUARDIANID_BINDMOBILE_URL = HOST + storage.data

storage.getData('input_data')
GUARDIAN_GUARDIANID_BINDINGMOBILE_VALID_DATA = storage.data['valid']


# guardian-change-name(guardianId)
storage.getDocument({'name': 'guardians-change-name'})
storage.getData('url')
GUARDIAN_GUARDIANID_CHANGENAME_URL = HOST + storage.data

storage.getData('input_data')
GUARDIAN_GUARDIANID_CHANGENAME_VALID_DATA = storage.data['valid']


# guardian-sms(guardianId)
storage.getDocument({'name': 'guardians-guardianId-sms'})
storage.getData('url')
GUARDIAN_GUARDIANID_SMS_URL = HOST + storage.data

storage.getData('input_data')
GUARDIAN_GUARDIANID_SMS_VALID_DATA = storage.data['valid']


# guardian-change-password(guardianId)
storage.getDocument({'name': 'guardians-change-password'})
storage.getData('url')
GUARDIAN_GUARDIANID_CHANGEPASSWORD_URL = HOST + storage.data

storage.getData('input_data')
GUARDIAN_GUARDIANID_CHANGEPASSWORD_VALID_DATAL = storage.data['valid']


# guardian-release-mobile(guardianId)
storage.getDocument({'name': 'guardians-release-mobile'})
storage.getData('url')
GUARDIAN_GUARDIANID_MOBILERELEASE_URL = HOST + storage.data

storage.getData('input_data')
GUARDIAN_GUARDIANID_MOBILERELEASE_VALID_DATA = storage.data['valid']

