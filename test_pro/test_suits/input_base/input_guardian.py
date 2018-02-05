from json import load, dump
import yaml

TOKEN_KEY = None
TOKEN_ALG = None

with open('./data/token/test.conf', 'r') as fp:
    config = yaml.load(fp)

TOKEN_KEY = config.get('encryption').get('key')
TOKEN_ALG = config.get('encryption').get('algorithm')


HOST = 'http://localhost:20001'
GUARDIANID = '596746f4a97daa4f26fba35d'

### guardian-sms
#url 
GUARDIAN_SMS_URL = HOST + '/authorization/guardians/sms'
# valid data
GUARDIAN_SMS_SIGNUP_DATA = load(
        open('./data/guardian/authorization/input/guardians_sms/sign_up/valid/sms.json'))
# 
GUARDIAN_SMS_SIGNIN_DATA = load(
        open('./data/guardian/authorization/input/guardians_sms/sign_in/valid/sms.json'))

GUARDIAN_SMS_FORGETPASSWORD_DATA = load(
        open('./data/guardian/authorization/input/guardians_sms/forget_password/valid/sms.json'))

GUARDIAN_SMS_MOBILE_BINDING = load(
        open('./data/guardian/authorization/input/guardians_sms/mobile_binding/valid/sms.json'))

GUARDIAN_SMS_WECHAT_BINDING_DATA = load(
        open('./data/guardian/authorization/input/guardians_sms/wechat_binding/valid/sms.json'))


### guardian-sessions

# url
GUARDIAN_SESSIONS_URL = HOST + '/authorization/guardian-sessions'

# valid data: name password
GUARDIAN_SESSIONS_NAME_VALID_DATA = load(
        open('./data/guardian/authorization/input/guardian_sessions/name/valid/login.json', 'r'))
# valid data: mobile password
GUARDIAN_SESSIONS_MOBILE_PSWD_VALID_DATA = load(
        open('./data/guardian/authorization/input/guardian_sessions/mobile/password/valid/login.json'))
# valid data: mobile smsCode
GUARDIAN_SESSIONS_MOBILE_SMSCODE_VALID_DATA = load(
        open('./data/guardian/authorization/input/guardian_sessions/mobile/smscode/valid/login.json'))
# valid data: wechatid
GUARDIAN_SESSIONS_WECHATID_VALID_DATA = load(
        open('./data/guardian/authorization/input/guardian_sessions/wechatId/valid/login.json'))


### guardian--guardianId-sms

# url
GUARDIAN_GUARDIANID_SMS_URL = HOST + '/authorization/guardians/' + GUARDIANID + '/sms'

# valid data: mobile-release
GUARDIAN_GUARDIANID_SMS_MOBILERELEASE_VALID_DATA = load(
        open('./data/guardian/authorization/input/guardians_guardianId_sms/mobile_releasing/valid/sms.json'))
# valid data: change-password
GUARDIAN_GUARDIANID_SMS_CHANGEPASSWORD_VALID_DATA = load(
        open('./data/guardian/authorization/input/guardians_guardianId_sms/change_password/valid/sms.json'))
