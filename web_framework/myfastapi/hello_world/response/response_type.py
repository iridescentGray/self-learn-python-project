from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/int")
async def index1():
    return 666

@app.get("/str")
async def index2():
    return "test"

@app.get("/bytes")
async def index3():
    return b"satori"

@app.get("/tuple")
async def index4():
    return ("test", "test2", "test3")

@app.get("/list")
async def index5():
    return [{"name": "test", "age": 17}, {"name": "test2", "age": 16}]


if __name__ == "__main__":
    uvicorn.run("response_type:app", host="127.0.0.1", port=5555)