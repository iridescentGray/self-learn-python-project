from fastapi import FastAPI
import uvicorn

app = FastAPI()


# 普通路径参数
@app.get("/items/{item_id}")
async def get_item(item_id):
    return {"item_id": item_id}


@app.get("/limit_type/{item_id}")
async def get_item_limit_type(item_id: int):
    """普通路径参数-限定参数类型

    http://127.0.0.1:5555/limit_type/2  success
    http://127.0.0.1:5555/limit_type/abc  error
    """
    return {"item_id": item_id}


@app.get("/files/{file_path:path}")
async def path_contain_(file_path: str):
    """带/的特殊路径处理

    声明 file_path 的类型:file_path:path
    http://127.0.0.1:5555/files//root/test.py  success
    """
    return {"file_path": file_path}


@app.get("/bool/{flag}")
async def get_flag(flag: bool):
    """带bool的路径参数

    http://127.0.0.1:5555/bool/1  success
    http://127.0.0.1:5555/bool/true  success
    http://127.0.0.1:5555/bool/no  success
    http://127.0.0.1:5555/bool/True  success
    """
    return {"flag": flag}


if __name__ == "__main__":
    uvicorn.run("path:app", host="127.0.0.1", port=5555)
