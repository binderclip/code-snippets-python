# coding: utf-8
from itsdangerous import Signer, BadSignature


def main():
    k = 'sdf823mm.xcl@?'
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


if __name__ == '__main__':
    main()
