import os
import shutil

import requests


def make_dir_if_not_exists(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)


class OW365Downloader:

    def __init__(self):
        self.get_next_page_url = 'http://ow365.cn/pdf/GetNextPage/'
        self.get_img_url = 'http://ow365.cn/img/'

    def _get_next_page(self, f, vid, img_id):
        params = {
            'f': f,
            'vid': vid,
            'img': img_id,
            'isMobile': 'false',
            'isNet': 'True',
        }
        return requests.get(self.get_next_page_url, params=params).json()

    def _download_img_by_id(self, img_id, index, doc_id):
        params = {
            'img': img_id,
        }
        headers = {"Accept": "image/webp,image/apng,image/*,*/*;q=0.8",
                   "Accept-Encoding": "gzip, deflate",
                   "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7",
                   "Referer": "http://ow365.cn/",
                   "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"
                   }
        r = requests.get(self.get_img_url, params=params, stream=True, headers=headers)
        make_dir_if_not_exists('out/{:02d}'.format(doc_id))
        with open('out/{:02d}/{:02d}.png'.format(doc_id, index), 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)

    def download_imgs_by_ids(self, img_ids, doc_id):
        for i, img_id in enumerate(img_ids):
            # fix 第一张的问题
            if i == 0:
                continue
            self._download_img_by_id(img_id, i, doc_id)

    def _test_download_img(self):
        headers = {"Accept": "image/webp,image/apng,image/*,*/*;q=0.8",
                   "Accept-Encoding": "gzip, deflate",
                   "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7",
                   "Referer": "http://ow365.cn/",
                   "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"
                   }
        r = requests.get('http://ow365.cn/img/?img=IDcMbrrMGOVAPZN4V59hSow0sY_Fm0wPUAAnUToqtHAbs_Q5e5OydARuuADviAYPcsHxcF5aMdI=', stream=True,
                         headers=headers)
        with open('out/{:02d}.png'.format(100000), 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)

    def get_all_img_id(self, f, vid, first_img_id):
        img_ids = [first_img_id]
        next_img_id = first_img_id
        page_count = 0
        while True:
            ret = self._get_next_page(f, vid, next_img_id)
            # 设置 page_count
            if ret['PageCount']:
                page_count = ret['PageCount']
            img_ids.append(ret['NextPage'])
            next_img_id = ret['NextPage']
            # 最后一张则结束
            if ret['PageIndex'] == page_count:
                break
        return img_ids


def main():
    owd = OW365Downloader()
    img_ids = owd.get_all_img_id(
        f='Y2RuMTEuYm9va2xuLmNuLjgwXDUxMDkzNF9kYmI4YTQxZTYxOTI3NzdkOWJiODgzZDNlNjllNWZiYzBkMjU4NjIwLnBkZg',
        vid='EkCBzpCokdJQBcvXk_ykLQ==',
        first_img_id='IDcMbrrMGOVAPZN4V59hSow0sY_Fm0wPUAAnUToqtHAbs_Q5e5OydOg7QJWgsV_2',
    )
    owd.download_imgs_by_ids(img_ids, 8)


if __name__ == '__main__':
    main()
