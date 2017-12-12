#!/usr/bin/env python
# -*- coding: utf -8 -*-

import falcon
import msgpack
import os
import time
import uuid

ALLOWED_IMAGE_TYPES = (
    'image/gif',
    'image/jpeg',
    'image/png',
)


def extract_project_id(req, resp, params):
    """Adds `project_id` to the list of params for all responders.

    Meant to be used as a `before` hook.
    """
    params['project_id'] = req.get_header('X-PROJECT-ID')


# @falcon.before(extract_project_id)
def validate_image_type(req, resp, params):
    if req.content_type not in ALLOWED_IMAGE_TYPES:
        msg = 'Image type not allowed. Must be PNG, JPEG or GIF'
        raise falcon.HTTPBadRequest('Bad request', msg)


def _media_type_to_ext(media_type):
    # strip the 'image/' prefix
    return media_type[6:]


def _ext_to_media_type(ext):
    return 'image/' + ext


def _generate_id():
    return str(uuid.uuid4())


class Collection(object):
    def __init__(self, storage_path):
        self.storage_path = storage_path

    def on_get(self, req, resp):
        resp.body = '{"message": "hello world!"}'
        resp.content_type = 'application/msgpack'
        resp.status = falcon.HTTP_200

    # add image type validate
    @falcon.before(validate_image_type)
    def on_post(self, req, resp):
        # 读取指定的本地pic到流中，写入到服务器中
        #filename由uuid生成，文件扩展o名保持一致

        image_id = _generate_id()
        ext = _media_type_to_ext(req.content_type)
        filename = image_id + '.' + ext
        image_path = os.path.join(self.storage_path, filename)
        with open(image_path, 'wb') as image_file:
            while True:
                chunk = req.stream.read(4096)
                if not chunk:
                    break
                image_file.write(chunk)

        resp.status = falcon.HTTP_201  # 201 Created
        resp.location = '/images/' + image_id


class Item(object):
    # 根据请求的文件名，将服务器上指定的path下的pic 重定向到流中

    def __init__(self, storage_path):
        self.storage_path = storage_path

    def on_get(self, req, resp, name):
        ext = os.path.splitext(name)[1][1:]
        resp.content_type = _ext_to_media_type(ext)

        image_path = os.path.join(self.storage_path, name)
        try:
            resp.stream = open(image_path, 'rb')
        except IOError:
            raise falcon.HTTPNotFound()
        resp.stream_len = os.path.getsize(image_path)
