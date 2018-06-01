import jwt
from jwt import DecodeError


def main():
    encoded_jwt = jwt.encode({'some': 'word'}, 'secret', algorithm='HS256')
    print(encoded_jwt)

    decoded_jwt = jwt.decode(encoded_jwt, 'secret', algorithms=['HS256'])
    print(decoded_jwt)

    decoded_jwt_not_verify = jwt.decode(encoded_jwt, verify=False)
    print(decoded_jwt_not_verify)

    try:
        decoded_jwt = jwt.decode('xxxxxxxxxx', 'secret', algorithms=['HS256'])
        print(decoded_jwt)
    except DecodeError as e:
        print(type(e), e)


if __name__ == '__main__':
    main()
