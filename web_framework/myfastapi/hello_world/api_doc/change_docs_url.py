from fastapi import FastAPI
import uvicorn

# doc: http://127.0.0.1:5555/my_docs
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


if __name__ == "__main__":
    uvicorn.run("change_docs_url:app", host="127.0.0.1", port=5555)
