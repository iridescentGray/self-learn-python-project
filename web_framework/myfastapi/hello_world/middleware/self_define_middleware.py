from fastapi import FastAPI, Request, Response
import uvicorn
import orjson

app = FastAPI()


@app.get("/")
async def view_func(request: Request):
    """尝试自定义中间件

    http://127.0.0.1:5555/users/
    """
    return {"name": "11111"}


@app.middleware("http")  # 使用 @app.middleware("http") 装饰的就是中间件
async def middleware(request: Request, call_next):
    # 当请求头中缺少 "ping": "pong"，就直接返回了
    if request.headers.get("ping", "") != "pong":
        response = Response(
            content=orjson.dumps({"error": "请求头中缺少指定字段"}),
            media_type="application/json",
            status_code=404,
        )

        return response
    # 如果该中间件后面还有中间件，那么 call_next 就是下一个中间件；如果没有，那么 call_next 就是对应的视图函数
    response: Response = await call_next(request)
    return response


if __name__ == "__main__":
    uvicorn.run("self_define_middleware:app", host="0.0.0.0", port=5555)
