from datetime import datetime

from pydantic import BaseModel, ValidationError


class User(BaseModel):
    id: int
    name = 'John Doe'
    signup_ts: datetime | None = None
    friends: list[int] = []


external_data = {
    'id': '123',
    'signup_ts': '2019-06-01 12:22',
    'friends': [1, 2, '3'],
}

if __name__ == '__main__':
    user = User(**external_data)
    print(user.id)
    print(repr(user.signup_ts))
    print(user.friends)
    print(user.dict())
    try:
        User(signup_ts='broken', friends=[1, 2, 'not number'])
    except ValidationError as e:
        print('----------------error------------------')
        print(e.json())