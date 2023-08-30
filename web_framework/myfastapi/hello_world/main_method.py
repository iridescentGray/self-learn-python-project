from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def index():
    return {"name": "main_method"}


if __name__ == "__main__":
    uvicorn.run("main_method:app", host="0.0.0.0", port=5555)