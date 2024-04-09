import asyncio
from asyncio import StreamReader
from typing import AsyncGenerator


async def read_until_empty(stream_reader: StreamReader) -> AsyncGenerator[bytes, None]:
    # 读取一行，直到没有任何剩余数据
    while response := await stream_reader.readline():
        yield response


async def main():
    host = "www.baidu.com"
    request = "GET / HTTP/1.1\r\n" "Connection: close\r\n" f"Host: {host}\r\n\r\n"

    stream_reader, stream_write = await asyncio.open_connection(host, 80)
    try:
        stream_write.write(request.encode("utf-8"))
        # Block the coroutine until all queued data is sent to the socket
        await stream_write.drain()
        response = b"".join(
            [response_byte async for response_byte in read_until_empty(stream_reader)]
        )
        print(response)
    finally:
        # 关闭 writer
        stream_write.close()
        # 并等待它完成关闭
        await stream_write.wait_closed()


asyncio.run(main())
