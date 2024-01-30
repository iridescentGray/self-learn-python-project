import datetime
import typing
from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    first_name: str
    birthdate: typing.Optional[datetime.date]


class UserCreate(schemas.BaseUserCreate):
    first_name: str
    birthdate: typing.Optional[datetime.date]


class UserUpdate(schemas.BaseUserUpdate):
    first_name: typing.Optional[str]
    birthdate: typing.Optional[datetime.date]
