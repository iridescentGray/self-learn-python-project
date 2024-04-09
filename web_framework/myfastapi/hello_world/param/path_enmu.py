from enum import Enum

import uvicorn
from fastapi import FastAPI

app = FastAPI()


class Name(str, Enum):
    satori = "test1"
    koishi = "name2"
    marisa = "fish3"


@app.get("/users/{user_name}")
async def get_user(user_name: Name):
    """枚举参数

    http://127.0.0.1:5555/users/test1 success
    http://127.0.0.1:5555/users/name2 success
    http://127.0.0.1:5555/users/2     error
    """
    return {"user_id": user_name}


if __name__ == "__main__":
    uvicorn.run("path_enmu:app", host="127.0.0.1", port=5555)
