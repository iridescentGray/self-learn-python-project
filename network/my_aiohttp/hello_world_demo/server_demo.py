import datetime

import orjson
from aiohttp import web
from aiohttp.web_request import Request
from aiohttp.web_response import Response

routes = web.RouteTableDef()


# http://localhost:9999/time
@routes.get("/time")
async def time(request: Request) -> Response:
    now = datetime.datetime.now()
    result = {
        "month": now.month,
        "day": now.day,
        "time": str(now.time())
    }
    return Response(body=orjson.dumps(result), content_type="application/json")


# http://localhost:9999/request_info
@routes.get("/request_info")
async def time(request: Request) -> Response:
    result = {
        "request.scheme（使用的协议）": request.scheme,
        "request.secure（协议是否是 https）": request.secure,
        "request.method（请求方法）": request.method,
        "request.version（HTTP 协议版本）": str(request.version),
        "request.host（客户端请求的主机名）": request.host,
        "request.remote（发起请求的客户端的 IP 地址）": request.remote,
        "request.url（客户端请求的 URL）": str(request.url),
        "request.path（客户端请求的路径，不带查询参数）": request.path,
        "request.path_qs（客户端请求的路径，带查询参数）": request.path_qs,
        "request.query（查询参数，像字典一样操作即可）": str(request.query),
        "request.query（查询参数，一个字符串）": request.query_string,
        "request.headers（请求头，像字典一样操作即可）": str(request.headers.__class__),
        "request.keep_alive（是否开启了长连接）": request.keep_alive,
        "request.cookies（cookie 信息，像字典一样操作即可）": str(request.cookies.__class__),
        "request.content（原始的字节流信息，针对 POST 和 PUT）": (await request.content.read()).decode("utf-8"),

    }
    return Response(body=orjson.dumps(result), content_type="application/json")


app = web.Application()
app.add_routes(routes)
web.run_app(app, port=9999)
