#!/usr/bin/env python
# -*- coding: utf-8 -*-

import base64

from Crypto.Util import RFC1751

rfc = RFC1751

res = base64.b64encode(rfc.english_to_key('I LOVE CODE A A A'))
print res

text = rfc.key_to_english(base64.b64decode(res))
print text



# output:
# HPZppAAAAAA=
# I LOVE CODE A A A
# 
