from json import load, dump
import yaml

# guardian-sessions


# valid data: name password
OUTPUT_GUARDIAN_SESSIONS_NAME_VALID_DATA = load(
        open('./data/guardian/authorization/output/guardian_sessions/name/valid/login.json'))
# valid data: mobile password
OUTPUT_GUARDIAN_SESSIONS_MOBILE_PSWD_VALID_DATA = load(
        open('./data/guardian/authorization/output/guardian_sessions/mobile/password/valid/login.json'))
# valid data: mobile smsCode
OUTPUT_GUARDIAN_SESSIONS_MOBILE_SMSCODE_VALID_DATA = load(
        open('./data/guardian/authorization/output/guardian_sessions/mobile/smscode/valid/login.json'))
# valid data: wechatid
OUTPUT_GUARDIAN_SESSIONS_WECHATID_VALID_DATA = load(
        open('./data/guardian/authorization/output/guardian_sessions/wechatId/valid/login.json'))

# guardians-sms
OUTPUT_GUARDIANS_SMS_SIGNIN_DATA = load(
        open('./data/guardian/authorization/output/guardians_sms/sign_in/valid/sms.json'))

OUTPUT_GUARDIANS_SMS_SIGNUP_DATA = load(
        open('./data/guardian/authorization/output/guardians_sms/sign_up/valid/sms.json'))

OUTPUT_GUARDIANS_SMS_MOBILEBINDING_DATA = load(
        open('./data/guardian/authorization/output/guardians_sms/mobile_binding/valid/sms.json'))

OUTPUT_GUARDIANS_SMS_FORGETPSWD_DATA = load(
        open('./data/guardian/authorization/output/guardians_sms/forget_password/valid/sms.json'))

OUTPUT_GUARDIANS_SMS_WECHATBINDING_DATA = load(
        open('./data/guardian/authorization/output/guardians_sms/wechat_binding/valid/sms.json'))
