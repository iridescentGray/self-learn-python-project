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
    user = User(**external_data)
    logging.info(f"user id {user.id}")
    logging.info(f"repr {repr(user.signup_ts)}")
    logging.info(f"friends {repr(user.friends)}")
    logging.info(f"user.dict {repr(user.dict())}")
    logging.info(f"user.json {user.json()}")

    try:
        User(signup_ts="broken", friends=[1, 2, "not number"])
    except ValidationError as e:
        logging.error(f"ValidationError {repr(user.json())}")
        logging.error(e)
