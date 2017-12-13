import jwt

encoded = jwt.encode({'some':'payload'},'secret',algorithm='HS256')
print (encoded)
decoded = jwt.decode(encoded,'secret',algorithm='HS256')
print(decoded)
try:
    decoded2=jwt.decode(encoded+'w','secret',algorithm='HS256')
except Exception:
    print("signature verification failed")
else:
    print("let's see if this line will appear!")

print(jwt.decode(encoded,verify=False))
print(jwt.decode(encoded,'secret',algorithms=['HS512','HS256']))
