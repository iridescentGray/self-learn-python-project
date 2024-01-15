from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()


@app.get("/girl")
async def read_girl(request: Request):
    """
    http://127.0.0.1:5555/girl?name=小明&age=17   success

    """
    header = request.headers  # 请求头
    method = request.method  # 请求方法
    cookies = request.cookies  # cookies
    query_params = request.query_params  # 查询参数
    return {
        "name": query_params.get("name"),
        "age": query_params.get("age"),
        "header": header,
        "method": method,
        "cookies": cookies,
    }


if __name__ == "__main__":
    uvicorn.run("request_attr:app", host="127.0.0.1", port=5555)
