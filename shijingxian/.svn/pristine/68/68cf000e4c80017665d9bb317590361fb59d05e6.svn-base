import hashlib


def create_md5_key(content):
    md5 = hashlib.md5()
    md5.update(content)
    md5_content = md5.hexdigest()

    return md5_content

print create_md5_key('secret')

