from dbdriver import *

HOST = 'http://localhost:20001'

storage = MongoBase()
storage.switchDatabase('TestDB')
storage.conCollection('test_info')


# guardian
storage.getDocument({'name': 'guardian'})
storage.getData('test_mobile')
INFO_GUARDIAN_MOBILE = storage.data

storage.getData('test_name')
INFO_GUARDIAN_NAME = storage.data

storage.getData('uuid')
INFO_GUARDIAN_UUID = storage.data

# supervisor
storage.getDocument({'name': 'supervisor'})
storage.getData('test_mobile')
INFO_SUPERVISOR_MOBILE = storage.data

storage.getData('test_name')
INFO_SUPERVISOR_NAME = storage.data

storage.getData('uuid')
INFO_SUPERVISOR_UUID = storage.data

