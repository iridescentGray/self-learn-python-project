from fastapi import FastAPI
import uvicorn

app = FastAPI()


# 普通路径参数
# http://127.0.0.1:5555/items/1
@app.get("/items/{item_id}")
async def get_item(item_id):
    return {"item_id": item_id}


# 普通路径参数-限定参数类型
# http://127.0.0.1:5555/limit_type/2  success
# http://127.0.0.1:5555/limit_type/abc  error
@app.get("/limit_type/{item_id}")
async def get_item_limit_type(item_id: int):
    return {"item_id": item_id}


# 带/的特殊路径处理
# http://127.0.0.1:5555/files//root/test.py  success
@app.get("/files/{file_path:path}")
async def path_contain_(file_path: str):
    return {"file_path": file_path}


if __name__ == "__main__":
    uvicorn.run("path:app", host="127.0.0.1", port=5555)
