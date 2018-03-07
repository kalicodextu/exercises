from json import dump, load
from dbdriver import *

HOST = 'http://localhost:20001'

storage = MongoBase()
storage.switchDatabase('TestDB')
storage.conCollection('imgcode')


# imagecode -- create imagecode
storage.getDocument({'name': 'imagecode'})
storage.getData('url')
IMGCODE_URL = HOST + storage.data

storage.getData('input_data')
IMGCODE_VALID_DATA = storage.data['valid']


# imagecode-uuid -- imgcode vertify 
storage.getDocument({'name': 'imgcode-uuid'})
storage.getData('url')
IMGCODE_UUID_URL = HOST + storage.data

storage.getData('input_data')
IMGCODE_UUID_VALID_DATA = storage.data['valid']
