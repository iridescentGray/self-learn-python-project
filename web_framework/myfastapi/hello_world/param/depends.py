from typing import Optional

import uvicorn
from fastapi import Depends, FastAPI

app = FastAPI()

"""Depends抽象公共参数


"""


async def common_parameters(q: Optional[str] = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}


@app.get("/items/")
async def read_items(commons: dict = Depends(common_parameters)):
    """
    request:
     http://127.0.0.1:5555/users?q=items_id

    response:
        {
            "q": "items_id",
            "skip": 0,
            "limit": 100
        }
    """
    return commons


@app.get("/users/")
async def read_users(commons: dict = Depends(common_parameters)):
    """
    request:
     http://127.0.0.1:5555/users?q=users_id

    response:
        {
            "q": "users_id",
            "skip": 0,
            "limit": 100
        }
    """
    return commons


if __name__ == "__main__":
    uvicorn.run("depends:app", host="127.0.0.1", port=5555)
