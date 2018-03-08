# coding: utf-8
import qiniu
from config import QiniuConfig
from qiniu_client import QiniuClient


def main():
    qiniu_client = QiniuClient(QiniuConfig.ACCESS_KEY, QiniuConfig.SECRET_KEY,
                               QiniuConfig.BUCKET, QiniuConfig.HOST, QiniuConfig.PREFIX)
    file_name = '../../models/_common_img/google.jpg.png'
    with open(file_name) as f:
        url = qiniu_client.upload_img(f.read())
        print(url)
    url2 = qiniu_client.upload_img_file(file_name)
    print(url2)


if __name__ == '__main__':
    main()
