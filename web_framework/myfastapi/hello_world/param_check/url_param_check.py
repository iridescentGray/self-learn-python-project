import uvicorn
from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/user")
async def get_user(
    password: str = Query(min_length=3, max_length=10, regex=r"^satori")
):
    """url参数校验/限制

    1.默认值为 'satori'
    2.传递的时候必须要以 'satori' 结尾
    3.具有长度限制

    request:
    http://127.0.0.1:5555/user?password=1       Error
    http://127.0.0.1:5555/user?password=123     Error
    http://127.0.0.1:5555/user?password=satori1 Succeed
    """

    return {"password": password}


if __name__ == "__main__":
    uvicorn.run("url_param_check:app", host="127.0.0.1", port=5555)
