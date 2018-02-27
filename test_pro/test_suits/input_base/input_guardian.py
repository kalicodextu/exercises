import yaml

from json import load, dump


TOKEN_KEY = None
TOKEN_ALG = None

with open('./data/token/test.conf', 'r') as fp:
    config = yaml.load(fp)

TOKEN_KEY = config.get('encryption').get('key')
TOKEN_ALG = config.get('encryption').get('algorithm')


HOST = 'http://localhost:20001/'
GUARDIANID = '596746f4a97daa4f26fba35d'

### guardian-sms


#url 
GUARDIAN_GUARDIANS_URL = HOST + '/authorization/guardians'

GUARDIAN_SMS_URL = HOST + '/authorization/guardians/sms'

GUARDIAN_SESSIONS_URL = HOST + '/authorization/guardian-sessions'

GUARDIAN_GUARDIANID_SMS_URL = HOST + '/authorization/guardians/' + GUARDIANID + '/sms'

GUARDIAN_GUARDIANID_BINDMOBILE_URL = HOST + '/authorization/' + GUARDIANID + '/bind-mobile'

GUARDIAN_GUARDIANID_CHANGEPASSWORD_URL = HOST + '/authorization/' + GUARDIANID + '/change-password'

GUARDIAN_GUARDIANID_MOBILERELEASE_URL = HOST + '/authorization/' + GUARDIANID + '/mobile-release'

GUARDIAN_GUARDIANID_CHANGENAME_URL = HOST + '/authorization/' + GUARDIANID + '/change-name'

GUARDIAN_RESETPASSWORD_URL = HOST + '/authorization/' + GUARDIANID + '/reset-password'


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

GUARDIAN_GUARDIANID_SMS_MOBILERELEASE_VALID_DATA = load(
        open('./data/guardian/authorization/input/guardians_guardianId_sms/mobile_releasing/valid/sms.json'))
# valid data: change-password
GUARDIAN_GUARDIANID_SMS_CHANGEPASSWORD_VALID_DATA = load(
        open('./data/guardian/authorization/input/guardians_guardianId_sms/change_password/valid/sms.json'))

GUARDIAN_GUARDIANS_WITH_NAME_VALID_DATA = load(
        open('./data/guardian/authorization/input/guardians/name/valid/signup.json'))

GUARDIAN_GUARDIANS_WITH_MOBILE_VALID_DATA = load(
        open('./data/guardian/authorization/input/guardians/mobile/valid/signup.json'))

GUARDIAN_GUARDIANID_BINDINGMOBILE_VALID_DATA = load(
        open('./data/guardian/authorization/input/guardians_guardianId_bindmobile/valid/bindmobile.json'))

GUARDIAN_GUARDIANID_CHANGEPASSWORD_VALID_DATA = load(
        open('./data/guardian/authorization/input/guardians_guardianId_changepassword/valid/changepassword.json'))

GUARDIAN_GUARDIANID_MOBILERELEASE_VALID_DATA = load(
        open('./data/guardian/authorization/input/guardians_guardianId_releasemobile/valid/releasemobile.json'))

GUARDIAN_GUARDIANID_CHANGENAME_VALID_DATA = load(
        open('./data/guardian/authorization/input/guardians_guardianId_changename/valid/changename.json'))

GUARDIAN_RESETPASSWORD_VALID_DATA = load(
        open('./data/guardian/authorization/guardian_resetpassword/valid/resetpassword.json'))
