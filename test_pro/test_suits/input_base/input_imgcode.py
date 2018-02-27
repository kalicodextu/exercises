from json import dump, load

HOST = 'http://localhost:20001'

IMAGE_CODE_URL = HOST + '/authorization/image-code'

IMAGE_CODE_DATA = {
    "SIGN_UP":
    load(open('./data/imgcode/image_code/sign_up/valid/imgcode.json')),
    "SIGN_IN":
    load(open('./data/imgcode/image_code/sign_in/valid/imgcode.json')),
    "RELEASE_BLOCK_ADDRESS":
    load(
        open(
            './data/imgcode/image_code/release_block_address/valid/imgcode.json'
        ))
}
