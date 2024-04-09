import orjson
import uvicorn
from fastapi import FastAPI, Request, Response
from fastapi.responses import HTMLResponse

app = FastAPI()

"""Response

直接返回的字典都会被FastAPI转成一个 Response 对象。

Response 之外还有很多其它类型的响应,比如:
FileResponse、HTMLResponse、PlainTextResponse 等等

"""

"""response参数

. content:返回的数据
. status_code:状态码
. headers:返回的请求头
. media_type:响应类型(就是 HTML 中 Content-Type,只不过这里换了个名字)
. background:接收一个任务,Response 在返回之后会自动异步执行（这里不做介绍,后面会说）
"""


@app.get("/girl")
async def read_girl(request: Request):
    """
    http://127.0.0.1:5555/girl?name=小明&age=17   success

    """
    method = request.method  # 请求方法
    query_params = request.query_params  # 查询参数
    data = {
        "name": query_params.get("name"),
        "age": query_params.get("age"),
        "method": method,
    }
    response = Response(
        orjson.dumps(data),
        status_code=201,
        headers={"Token": "xxx"},
        media_type="application/json",
    )
    return response


@app.get("/html")
async def html_response(request: Request):
    """
    http://127.0.0.1:5555/html   success

    """
    response1 = HTMLResponse("<h1>你好呀</h1>")
    return response1


if __name__ == "__main__":
    uvicorn.run("response_attr:app", host="127.0.0.1", port=5555)
