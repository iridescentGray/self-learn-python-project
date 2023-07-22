import asyncio
import sys
from asyncio import StreamReader

"""
read the stdin(keyboard) not block thread like input()
"""


async def delay(seconds):
    print(f"sleep {seconds} second")
    await asyncio.sleep(seconds)
    print(f"{seconds} second sleep complete")


async def create_stdin_reader() -> StreamReader:
    stream_reader = asyncio.StreamReader()
    protocol = asyncio.StreamReaderProtocol(stream_reader)
    loop = asyncio.get_running_loop()
    await loop.connect_read_pipe(lambda: protocol, sys.stdin)
    return stream_reader


async def main():
    print("please input delay time")
    stdin_reader = await create_stdin_reader()
    while True:
        delay_time = await stdin_reader.readline()
        asyncio.create_task(delay(int(delay_time)))


asyncio.run(main())
