from typing import Optional, Union
from fastapi import FastAPI
import uvicorn

app = FastAPI()


# 普通路径参数
# http://127.0.0.1:5555/user?name=古明地觉&age=17   success
# http://127.0.0.1:5555/user?name=古明地觉  error: filed required
@app.get("/user")
async def get_user(name: str, age: int):
    return {"name": name, "age": age}


# 普通路径参数-带默认值
# http://127.0.0.1:5555/get_user_with_default_param?name=古明地觉&age=17   success
# http://127.0.0.1:5555/get_user_with_default_param?name=古明地觉  success
@app.get("/get_user_with_default_param")
async def get_user_with_default_param(name: str, age: int = 0):
    return {"name": name, "age": age}

# 普通路径参数-混合类型
# http://127.0.0.1:5555/get_user_mix_type/1?name=古明地觉   success
# http://127.0.0.1:5555/get_user_mix_type/测试 success
# http://127.0.0.1:5555/get_user_mix_type/001   success
@app.get("/get_user_mix_type/{user_id}")
async def get_user_mix_type(user_id: Union[int, str], name: Optional[str] = None):
    return {"user_id": user_id, "name": name}


if __name__ == "__main__":
    uvicorn.run("url_param:app", host="127.0.0.1", port=5555)
