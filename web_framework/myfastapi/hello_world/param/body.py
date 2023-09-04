from fastapi import FastAPI
import uvicorn

app = FastAPI()

# 普通路径参数
# http://127.0.0.1:5555/items/1

if __name__ == "__main__":
    uvicorn.run("body:app", host="127.0.0.1", port=5555)
