import uvicorn
from fastapi import FastAPI, Path

app = FastAPI()


@app.get("/user/{pass_word}")
async def get_user(password: str = Path(max_length=2, alias="pass_word")):
    """url参数校验/限制

    1.默认值为 'satori'
    2.传递的时候必须要以 'satori' 结尾
    3.具有长度限制

    request:
    http://127.0.0.1:5555/user/1       success
    http://127.0.0.1:5555/user/333     error

    """

    return {"password": password}


if __name__ == "__main__":
    uvicorn.run("path_param_check:app", host="127.0.0.1", port=5555)
