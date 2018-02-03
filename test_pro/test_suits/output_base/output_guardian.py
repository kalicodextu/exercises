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
