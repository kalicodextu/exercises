#!/usr/bin/env python
# -*- coding: utf -8 -*-

# 2017/12/12 v1.0.1
# 1. run_server in the app's path: gunicorn app
# 2. POST: http localhost:8000/images Content-Type:image/jpeg < xxx.jepg
# 3. GET : http localhost:8000/images/{uuid}.jepg
# Note: 3st step will show that in terminal:
"""
+-----------------------------------------+
| NOTE: binary data not shown in terminal |
+-----------------------------------------+
"""

# 2017/12/12 v1.0.2
# output:
#
"""
{
    "title": "Bad request",
    "description": "Image type not allowed. Must be PNG, JPEG or GIF"
}
"""


import falcon
from images import Collection, Item

api = application = falcon.API()

storage_path = './'

image_collection = Collection(storage_path)
image = Item(storage_path)

api.add_route('/images', image_collection)
api.add_route('/images/{name}', image)
