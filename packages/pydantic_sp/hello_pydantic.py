from datetime import datetime
from typing import List
from pydantic import BaseModel


class User(BaseModel):
    id: int
    name = 'John Doe'
    signup_ts: datetime = None
    friends: List[int] = []


def main():
    external_data = {'id': '123', 'signup_ts': '2017-06-01 12:22', 'friends': [1, '2', b'3']}
    user = User(**external_data)
    print(user)
    print(user.id)


if __name__ == '__main__':
    main()
