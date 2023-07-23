import uvicorn
from fastapi import FastAPI
from fastapi.websockets import WebSocket, WebSocketDisconnect

app = FastAPI()


@app.websocket("/ws")
async def ws(websocket: WebSocket):
    await websocket.accept()
    while True:
        try:
            data = await websocket.receive_text()
        except WebSocketDisconnect:
            return
        await websocket.send_text(f"收到来自客户端的回复: {data}")


if __name__ == "__main__":
    uvicorn.run("ws_simple_demo:app")
