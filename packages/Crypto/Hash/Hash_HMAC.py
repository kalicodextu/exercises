from Crypto.Hash import (
        HMAC,
        MD2,
        MD4,
        MD5,
        RIPEMD,
        SHA,
        SHA224,
        SHA256,
        SHA384,
        SHA512
        )

class Hash_cryptor(object):

    def crypto_HMAC(self, secret, text):
        secret = secret
        h = HMAC.new(secret)
        h.update(text)
        return h.hexdigest()

    def crypto_MD2(self, text):
        h = MD2.new()
        h.update(text)
        return h.hexdigest()
    
    def crypto_MD4(self, text):
        h = MD4.new()
        h.update(text)
        return h.hexdigest()

    def crypto_MD5(self, text):
        h = MD5.new()
        h.update(text)
        return h.hexdigest()

    def crypto_RIPEMD(self, text):
        h = RIPEMD.new()
        h.update(text)
        return h.hexdigest()

    def crypto_SHA(self, text):
        h = SHA.new()
        h.update(text)
        return h.hexdigest()
 
    def crypto_SHA224(self, text):
        h = SHA224.new()
        h.update(text)
        return h.hexdigest()

    def crypto_SHA225(self, text):
        h = SHA225.new()
        h.update(text)
        return h.hexdigest()

    def crypto_SHA384(self, text):
        h = SHA384.new()
        h.update(text)
        return h.hexdigest()

    def crypto_SHA512(self, text):
        h = SHA512.new()
        h.update(text)
        return h.hexdigest()


if __name__ == '__main__':
    crypto_inst = Hash_cryptor()
    print crypto_inst.crypto_SHA224('the meaning of life!')
