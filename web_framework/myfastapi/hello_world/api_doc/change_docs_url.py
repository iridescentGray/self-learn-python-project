import uvicorn
from fastapi import FastAPI, Query

# api-doc: http://127.0.0.1:8000/openapi.json
# defualt-Swagger UI: http://127.0.0.1:8000/docs

# Swagger UI: http://127.0.0.1:5555/my_docs
# api-doc: http://127.0.0.1:5555/my_openapi
app = FastAPI(
    title="测试文档",
    description="这是一个简单的 demo",
    docs_url="/my_docs",
    openapi_url="/my_openapi",
)


@app.get("/apple/{item_id}")
async def get_item(item_id: int):
    return {"item_id": item_id}


@app.get("/user")
async def get_user(password: str = Query("test", min_length=3, max_length=5)):
    """指定参数限制,会显示到api_doc中"""
    return {"password": password}


if __name__ == "__main__":
    uvicorn.run("change_docs_url:app", host="127.0.0.1", port=5555)
