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
    logging.info(f"-----------------------------------------create instance------------------------------------------")
    create_user_with_default_value = User(id=1, friends=[1, 2])
    logging.info(f"create_user_with_default_value:  {create_user_with_default_value}")
    create_user_by_dict = User(**external_data)
    logging.info(f"create_user_by_dict:  {create_user_by_dict}")

    logging.info(f"-----------------------------------------base operation------------------------------------------")
    logging.info(f"user object type {type(create_user_by_dict)}")
    logging.info(f"get user id field {create_user_by_dict.id}")
    logging.info(f"user repr {repr(create_user_by_dict.signup_ts)}")
    logging.info(f"get friends field {repr(create_user_by_dict.friends)}")
    logging.info(f"user.dict {repr(create_user_by_dict.dict())}")
    logging.info(f"dict(user) {dict(create_user_by_dict)}")
    logging.info(f"repr {repr(create_user_by_dict.signup_ts)}")

    logging.info(f"------------------------------------------handle json-----------------------------------------------")
    user_json = create_user_by_dict.json()
    logging.info(f"user_json  {user_json}")
    logging.info(f"user_json object type {type(user_json)}")

    # parse json to Object
    user_from_json = User.parse_raw(user_json)
    logging.info(f"user_from_json object type  {type(user_from_json)}")
    logging.info(f"user_from_json   {user_from_json}")

    # 'is' return False, '==' return True, it means '== ' is overrider by pydantic
    logging.info(f"user is user_from_json  {create_user_by_dict is user_from_json}")
    logging.info(f"user==user_from_json  {create_user_by_dict == user_from_json}")

    logging.info(f"------------------------------------------error_test-----------------------------------------------")
    try:
        User(signup_ts="broken", friends=[1, 2, "not number"])
    except ValidationError as e:
        logging.error(e)
