import asyncio
import socket
from asyncio import AbstractEventLoop


async def echo(conn: socket.socket,
               loop: AbstractEventLoop):
    # 无限循环等待来自客户端连接的数据
    while data := await loop.sock_recv(conn, 1024):
        # 收到数据之后再将其发送给客户端,在结尾加一个 b"~"
        await loop.sock_sendall(conn, data + b"~")


async def listen_for_conn(server: socket.socket):
    running_loop = asyncio.get_running_loop()

    while True:
        conn, addr = await running_loop.sock_accept(server)
        conn.setblocking(False)
        print(f"收到客户端 {addr} 的连接")
        # 每当获得连接时，创建一个任务来监听客户端的数据
        asyncio.create_task(echo(conn, running_loop))


async def start_server():
    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    server.setblocking(False)
    server.bind(("localhost", 12345))
    server.listen()
    await listen_for_conn(server)


asyncio.run(start_server())
