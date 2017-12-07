# coding: utf-8
import qiniu
import imghdr
import uuid


def get_image_type_of_file_data(file_data):
    type_ = imghdr.what('', file_data) or ''
    if type_ == 'jpeg':
        type_ = 'jpg'
    return type_


def get_image_type_of_file(file_name):
    type_ = imghdr.what(file_name) or ''
    if type_ == 'jpeg':
        type_ = 'jpg'
    return type_


class QiniuClientError(Exception):
    pass


class QiniuClient(object):

    def __init__(self, access_key, secret_key, bucket, host, prefix='uuimgs/'):
        self.access_key = access_key
        self.secret_key = secret_key
        self.bucket = bucket
        self.host = host
        self.prefix = prefix

    def upload_img(self, img_data):
        type_ = get_image_type_of_file_data(img_data)
        key = '{}{}.{}'.format(self.prefix, str(uuid.uuid4()), type_)
        q = qiniu.Auth(self.access_key, self.secret_key)
        token = q.upload_token(self.bucket, key, 3600)
        ret, info = qiniu.put_data(token, key, img_data)
        if not ret:
            raise QiniuClientError(info)
        return '{}/{}'.format(self.host, key)

    def upload_img_file(self, local_img_file):
        type_ = get_image_type_of_file(local_img_file)
        key = '{}{}.{}'.format(self.prefix, str(uuid.uuid4()), type_)
        q = qiniu.Auth(self.access_key, self.secret_key)
        token = q.upload_token(self.bucket, key, 3600)
        ret, info = qiniu.put_file(token, key, local_img_file)
        if not ret:
            raise QiniuClientError(info)
        return '{}/{}'.format(self.host, key)
