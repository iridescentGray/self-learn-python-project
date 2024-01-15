from fastapi import FastAPI

# https://fastapi.tiangolo.com/zh/tutorial/middleware/
app = FastAPI()


# 要求请求协议必须是 https 或者 wss，如果不是，则自动跳转
from starlette.middleware.httpsredirect import HTTPSRedirectMiddleware

app.add_middleware(HTTPSRedirectMiddleware)

# 请求中必须包含 Host 字段，为防止 HTTP 主机报头攻击，并且添加中间件的时候，还可以指定一个 allowed_hosts，那么它是干什么的呢？
# 假设我们有服务 a.example.com, b.example.com, c.example.com
# 但我们不希望用户访问 c.example.com，就可以像下面这么设置，如果指定为 ["*"]，或者不指定 allow_hosts，则表示无限制
from starlette.middleware.trustedhost import TrustedHostMiddleware

app.add_middleware(
    TrustedHostMiddleware, allowed_hosts=["a.example.com", "b.example.com"]
)

# 如果用户的请求头的 Accept-Encoding 字段包含 gzip，那么 FastAPI 会使用 GZip 算法压缩
# minimum_size=1000 表示当大小不超过 1000 字节的时候就不压缩了
from starlette.middleware.gzip import GZipMiddleware

app.add_middleware(GZipMiddleware, minimum_size=1000)
