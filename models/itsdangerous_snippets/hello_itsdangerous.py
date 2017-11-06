# coding: utf-8
from itsdangerous import Signer, BadSignature


def main():
    k = 'bt6n4k2m'
    signer = Signer(k)
    s = '11878121-b36d-4c38-9f87-682e8986d1f9'
    ss = signer.sign(s)
    print('signed str: {}'.format(ss))
    us = signer.unsign(ss)
    print('unsigned str: {}'.format(us))

    # 做点改动
    try:
        print(signer.unsign('{}a'.format(ss)))
    except BadSignature as e:
        print e

    print('------')
    cid = 110000000000000262
    uid = 105697106
    for i in xrange(10):
        print(signer.sign("{}_{}".format(cid, uid + i)))



if __name__ == '__main__':
    main()
