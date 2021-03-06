#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Crypto.Cipher import AES
from Crypto.Util import Counter


pt = b' '*1000000
ctr = Counter.new(128)
cipher = AES.new(b' '*16, AES.MODE_CTR, counter=ctr)
ct = cipher.encrypt(pt)
