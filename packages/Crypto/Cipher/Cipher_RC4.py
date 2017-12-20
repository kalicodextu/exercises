from Crypto.Cipher import ARC4
from Crypto import Random
from Crypto.Hash import SHA
from binascii import b2a_hex, a2b_hex


class MyCrypt():
    def __init__(self, key):
        self.key = key
        self.nonce = Random.new().read(16)

    def myencrypt(self, text):
        length = 16
        count = len(text)
        add = (length - (count % length))
        text = text + ('\0' * add)
        tempkey = SHA.new(self.key + self.nonce).digest()
        cryptor = ARC4.new(tempkey)
        self.ciphertext = cryptor.encrypt(text)
        return b2a_hex(self.ciphertext)

    def mydecrypt(self, text):
        tempkey = SHA.new(self.key + self.nonce).digest()
        cryptor = ARC4.new(tempkey)
        plain_text = cryptor.decrypt(a2b_hex(text))
        return plain_text.rstrip('\0')


if __name__ == '__main__':
    mycrypt = MyCrypt('0123456789123456')
    e = mycrypt.myencrypt('hello')
    d = mycrypt.mydecrypt(e)
    print e
    print d
