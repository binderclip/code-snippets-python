# coding: utf-8
import uuid


def main():
    print('uuid: {}'.format(str(uuid.uuid4())))
    print('uuid: {}'.format(str(uuid.uuid4()).split('-')[0]))



if __name__ == '__main__':
    main()
