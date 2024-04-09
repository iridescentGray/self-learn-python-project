import asyncio

import uvicorn
from fastapi import FastAPI
from fastapi.websockets import WebSocket, WebSocketDisconnect


class UserCounter:
    clients = []

    async def on_connect(self, ws: WebSocket):
        await ws.accept()
        print("连接已成功建立")
        # 当新客户端连接时，将其添加到 clients 中
        self.clients.append(ws)
        # 并通知其它用户新的在线计数
        await self._send_count()

    async def on_disconnect(self, ws: WebSocket):
        # 当客户端断开连接时，将其从 clients 中移除
        self.clients.remove(ws)
        # 并通知其它用户新的在线计数
        await self._send_count()

    async def on_receive(self, ws: WebSocket):
        # 当客户端发消息过来时，执行此方法
        return await ws.receive_text()

    async def on_send(self, ws: WebSocket, message: str):
        # 向客户端发消息时，执行此方法
        await ws.send_text(message)

    async def _send_count(self):
        count = len(self.clients)
        if count == 0:
            return
        message = f"当前在线人数: {count}"
        task_to_client = {
            asyncio.create_task(self.on_send(ws, message)): ws for ws in self.clients
        }
        done, pending = await asyncio.wait(task_to_client)
        # 任务正常结束和出现异常都表示任务完成，如果要是出现异常，那么就将连接移除
        for task in done:
            if task.exception() is not None:
                self.clients.remove(task_to_client[task])

    async def deal_ws_conn(self, ws: WebSocket):
        await self.on_connect(ws)
        while True:
            try:
                data = await self.on_receive(ws)
            except WebSocketDisconnect:
                return await self.on_disconnect(ws)
            await self.on_send(ws, f"收到来自客户端的回复: {data}")


app = FastAPI()
app.add_api_websocket_route("/ws", UserCounter().deal_ws_conn)

if __name__ == "__main__":
    uvicorn.run("ws_user_count_demo:app")
