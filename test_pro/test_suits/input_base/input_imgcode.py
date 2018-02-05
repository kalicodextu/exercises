from json import dump, load

HOST = 'http://localhost:20001'

IMAGE_CODE_URL = HOST + '/authorization/image-code' 

IMAGE_CODE_DATA = load(
        open('./data/imgcode/image_code/sign_up/valid/imgcode.json'))
    
