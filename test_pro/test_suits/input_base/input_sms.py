from dbdriver import *

HOST = 'http://localhost:20001'

storage = MongoBase()
storage.switchDatabase('TestDB')
storage.conCollection('sms_reset')


# imagecode -- create imagecode
storage.getDocument({'name': 'guardian'})
storage.getData('mobile')
SMS_GUARDIAN_MOBILE = storage.data

storage.getData('uuid')
SMS_GUARDIAN_UUID = storage.data

