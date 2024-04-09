from typing import Optional, Union

import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/user")
async def get_user(name: str, age: int):
    """普通url参数

    http://127.0.0.1:5555/user?name=小明&age=17   success
    http://127.0.0.1:5555/user?name=小明  error: field required
    """
    return {"name": name, "age": age}


@app.get("/get_user_with_default_param")
async def get_user_with_default_param(name: str, age: int = 0):
    """普通url参数-带默认值

    http://127.0.0.1:5555/get_user_with_default_param?name=小明&age=17   success
    http://127.0.0.1:5555/get_user_with_default_param?name=小明  success
    """
    return {"name": name, "age": age}


@app.get("/get_user_mix_type/{user_id}")
async def get_user_mix_type(user_id: Union[int, str], name: Optional[str] = None):
    """普通url参数-混合类型
    混合 路径参数 与 url参数
    http://127.0.0.1:5555/get_user_mix_type/1?name=小明   success
    http://127.0.0.1:5555/get_user_mix_type/测试 success
    http://127.0.0.1:5555/get_user_mix_type/001   success
    """
    return {"user_id": user_id, "name": name}


if __name__ == "__main__":
    uvicorn.run("url_param:app", host="127.0.0.1", port=5555)
