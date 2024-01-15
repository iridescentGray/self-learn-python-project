from typing import Optional, List
from fastapi import FastAPI, Request, Response
from pydantic import BaseModel
import uvicorn

app = FastAPI()


class Girl(BaseModel):
    """数据验证是通过 pydantic 实现的，我们需要从中导入 BaseModel，然后继承它"""

    name: str
    age: Optional[str] = None
    length: float
    hobby: List[str]


@app.post("/girl")
async def read_girl(girl: Girl):
    """发送请求

        curl --location --request POST 'http://0.0.0.0:5555/girl' \
        --header 'Content-Type: application/json' \
        --header 'Accept: */*' \
        --header 'Host: 0.0.0.0:5555' \
        --data-raw '{
            "name": 123,
            "age": 123,
            "length": 123,
            "hobby": [1,2,3,4]
        }'
    """
    print(girl)
    return dict(girl)


@app.post("/girl_from_reques")
async def read_girl_from_request(request: Request):
    """发送请求

        curl --location --request POST 'http://0.0.0.0:5555/girl_from_reques' \
        --header 'Content-Type: application/json' \
        --header 'Accept: */*' \
        --header 'Host: 0.0.0.0:5555' \
        --data-raw '{
            "name": 123,
            "age": 123,
            "length": 123,
            "hobby": [1,2,3,4]
        }'
    """
    data = await request.body()
    json_data = await request.json()

    print(data)
    print(json_data)

    return data


if __name__ == "__main__":
    uvicorn.run("body:app", host="0.0.0.0", port=5555)
