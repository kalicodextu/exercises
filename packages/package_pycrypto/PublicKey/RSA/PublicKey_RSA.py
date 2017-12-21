#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Crypto import Random
from Crypto.Hash import SHA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5
from Crypto.PublicKey import RSA
import base64

# PRNG
random_generator = Random.new().read
# rsa instance
rsa = RSA.generate(1024, random_generator)

# Alice 的秘钥对的生成
private_pem = rsa.exportKey()

with open('Alice-private.pem', 'w') as f:
    f.write(private_pem)
f.close()
public_pem = rsa.publickey().exportKey()
with open('Alice-public.pem', 'w') as f:
    f.write(public_pem)
f.close()
# Bob 的秘钥对的生成
private_pem = rsa.exportKey()
with open('Bob-private.pem', 'w') as f:
    f.write(private_pem)
f.close()
public_pem = rsa.publickey().exportKey()
with open('Bob-public.pem', 'w') as f:
    f.write(public_pem)
f.close()


def get_msg(filename):
    with open(filename, 'r') as f:
        text = f.read()
        f.close()
        return text


def rsa_encrypto(pub_pem, msg):
    with open(pub_pem, 'r') as f_pub:
        pub_key = f_pub.read()
        f_pub.close()
        rsa_pub_key = RSA.importKey(pub_key)
        cipher = Cipher_pkcs1_v1_5.new(rsa_pub_key)
        cipher_msg = base64.b64encode(cipher.encrypt(msg))
        return cipher_msg


def rsa_decrypto(pri_pem, cipher_msg):
    with open(pri_pem, 'r') as f_pri:
        pri_key = f_pri.read()
        f_pri.close()
        rsa_pri_key = RSA.importKey(pri_key)
        cipher = Cipher_pkcs1_v1_5.new(rsa_pri_key)
        msg = cipher.decrypt(base64.b64decode(cipher_msg), random_generator)
        return msg


def rsa_signature(pri_pem, msg):
    with open(pri_pem, 'r') as f_pri:
        key = f_pri.read()
        rsakey = RSA.importKey(key)
        signer = Signature_pkcs1_v1_5.new(rsakey)
        digest = SHA.new()
        digest.update(msg)
        sign = signer.sign(digest)
        signature = base64.b64encode(sign)
        return signature


def rsa_signature_verify(pub_pem, msg, signature):
    with open(pub_pem, 'r') as f_pub:
        key = f_pub.read()
        rsakey = RSA.importKey(key)
        verifier = Signature_pkcs1_v1_5.new(rsakey)
        digest = SHA.new()
        # Assumes the data is base64 encoded to begin with
        digest.update(msg)
        is_verify = verifier.verify(digest, base64.b64decode(signature))
        return is_verify


if __name__ == '__main__':
    # original text
    print 'msg:'
    msg = get_msg('text.txt')
    print msg
    # signature
    print 'Signature msg:'
    sign = rsa_signature('Bob-private.pem', msg)
    print sign
    # verify signature
    print 'Signature verify:'
    is_verify = rsa_signature_verify('Bob-public.pem', msg, sign)
    print is_verify
    # encrypt
    print 'encrypto msg:'
    cipher_msg = rsa_encrypto('Alice-public.pem', msg)
    print cipher_msg
    # decrypt
    print 'after decrypto msg:'
    msg_decrypt = rsa_decrypto('Alice-private.pem', cipher_msg)
    print msg_decrypt

# output:
# msg:
# This is a message from Alice.
#
# Signature msg:
# AE0cx0gr1gp3c8jyZ3ymkp7te3/HH9T5JxOkiouCrpw1iUyii/2xIDTI1cfwdrdPxVjWPTk7Hel83QsT6MD0sux8ejKH5UN0TF/asUnSSvgQUJNAjo5TK5HNws2aicSjmCvYjK6dTT5XMEv1Ghaze1vS8U3KK5Q02O7e/T4dTlU=
# Signature verify:
# True
# encrypto msg:
# bJd4U37ZsZbY9WqPbG+mF6uCOJxCQjS9E1zwX7z5C3yuQFqhXeiZ7PMJR+9P1IWZFUP+jFapBigilaK/ol7Zknndx4pFrmpXlQztWk4j4/NOLkm91v3K7Nfe6vGnGPL9tN689Zmo7FimwP0e9RtKwiSjGzxqncpiAMVYOkCYxlI=
# after decrypto msg:
# This is a message from Alice.
