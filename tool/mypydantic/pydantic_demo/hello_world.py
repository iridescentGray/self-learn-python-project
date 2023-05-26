import logging
from datetime import datetime

from pydantic import BaseModel, ValidationError

logging.basicConfig(level=logging.INFO)


class User(BaseModel):
    id: int
    name = "John Doe"
    signup_ts: datetime | None = None
    friends: list[int] = []


external_data = {
    "id": "123",
    "signup_ts": "2019-06-01 12:22",
    "friends": [1, 2, "3"],
}

if __name__ == "__main__":
    logging.info(f"-----------------------------------------base operation------------------------------------------")
    user = User(**external_data)
    logging.info(f"user id {type(user)}")
    logging.info(f"user id {user.id}")
    logging.info(f"repr {repr(user.signup_ts)}")
    logging.info(f"get friends {repr(user.friends)}")
    logging.info(f"user.dict {repr(user.dict())}")

    logging.info(f"------------------------------------------deal json-----------------------------------------------")
    user_json = user.json()
    logging.info(f"user.json {user_json}")
    logging.info(f"user.type {type(user_json)}")

    # parse json to Object
    user_from_json = User.parse_raw(user_json)
    logging.info(f"User.parse_obj type  {type(user_from_json)}")
    logging.info(f"User.parse_obj   {user_from_json}")
    # 'is' return False, '==' return True, it means == is overrider by pydantic
    logging.info(f"user is user_from_json  {user is user_from_json}")
    logging.info(f"user==user_from_json  {user == user_from_json}")

    logging.info(f"------------------------------------------error_test-----------------------------------------------")
    try:
        User(signup_ts="broken", friends=[1, 2, "not number"])
    except ValidationError as e:
        logging.error(f"ValidationError {repr(user.json())}")
        logging.error(e)
