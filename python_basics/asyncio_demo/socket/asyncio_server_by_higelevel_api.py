import asyncio
import logging
from asyncio import StreamReader, StreamWriter


class ServerState:
    def __init__(self):
        self._writers = []

    async def add_client(self, reader: StreamReader, writer: StreamWriter):
        """添加客户端，并创建回显任务"""
        self._writers.append(writer)
        await self._on_connect(writer)
        asyncio.create_task(self._echo(reader, writer))

    async def _on_connect(self, writer: StreamWriter):
        """当有新连接时，告诉客户端有多少用户在线，并同时其他人有新用户上线"""
        writer.write(f"欢迎, 当前在线人数有 {len(self._writers)} 人\n".encode("utf-8"))
        await writer.drain()
        await self._notify_all("新用户上线\n")

    async def _echo(self, reader: StreamReader, writer: StreamWriter):
        try:
            while (data := await reader.readline()) != b"":
                writer.write(data + b"~")
                await writer.drain()
            # 如果客户端断开连接，那么通知其他用户，有人断开连接
            self._writers.remove(writer)
            await self._notify_all(f"有人断开连接, 当前在线人数为 {len(self._writers)}")
        except ConnectionError:
            logging.info("客户端断开连接")
        except Exception as e:
            logging.error(f"出现异常: {e}")
            self._writers.remove(writer)

    async def _notify_all(self, message: str):
        """向所有其他用户发送消息的辅助方法, 如果发送失败, 将删除该用户"""
        for writer in self._writers:
            try:
                writer.write(message.encode("utf-8"))
                await writer.drain()
            except ConnectionError as e:
                logging.error("无法向客户端写入数据, 连接断开")
                self._writers.remove(writer)


async def start_server():
    server_state = ServerState()

    async def client_connected(reader: StreamReader, writer: StreamWriter):
        await server_state.add_client(reader, writer)

    # 当客户端连接时，会调用 client_connected 协程函数，并自动传入 reader 和 writer
    # 在里面我们执行 await server_state.add_client
    server = await asyncio.start_server(client_connected, "localhost", 12345)
    async with server:
        await server.serve_forever()


asyncio.run(start_server())
