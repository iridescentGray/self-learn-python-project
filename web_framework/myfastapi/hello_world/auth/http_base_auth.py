from fastapi import FastAPI, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import uvicorn

app = FastAPI()

security = HTTPBasic()


@app.get("/index")
async def index(credentials: HTTPBasicCredentials = Depends(security)):
    """http bas _auth

    http://127.0.0.1:5555/index
    """
    return {"username": credentials.username, "password": credentials.password}


if __name__ == "__main__":
    uvicorn.run("http_base_auth:app", host="0.0.0.0", port=5555)
